import requests
import re
import subprocess
import sys
import time

## Helper functions
def check_container(containerName):
    dockerPsOutput = subprocess.run(['docker','ps', '-af', 'name=' +containerName ], capture_output=True, universal_newlines=True, text=True).stdout
    if containerName in dockerPsOutput:
        return True
    else:
        return False

def print_and_sleep(message, numberOfSeconds):
    print(message)
    time.sleep(numberOfSeconds)

## Start script
subprocess.check_call(['docker-compose','-p','nopcommercetest', '-f', './nop_commerce/docker-compose.yml', 'up', '-d'])
print_and_sleep('Docker started, waiting 15 secs to give containers some time to start up....', 15)

print('Getting cookie required to start installation')
url = 'http://localhost:90/install'
res = requests.get(url)
if res.status_code != 200:
    sys.exit('Error getting cookie!')

regexSearch = re.findall(re.escape('Cookie ') + '(.*)' + re.escape(' for'), str(res.cookies))
if len(regexSearch) == 1:
    requiredCookie = regexSearch[0]
else:
    sys.exit('Error parsing cookie!')

print('Starting installation process')
installHeaders ={
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Origin': 'http://localhost:90',
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'http://localhost:90/install',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Cookie': requiredCookie,
    'sec-gpc': '1'
        }
installData = 'AdminEmail=admin%40yourStore.com&AdminPassword=123&ConfirmPassword=123&Country=GB-en-US&InstallSampleData=true&DataProvider=1&ConnectionStringRaw=true&ServerName=&DatabaseName=&Username=&Password=&ConnectionString=Data+Source%3Dnopcommerce_database%3BInitial+Catalog%3DnopCommerce%3BPersist+Security+Info%3DTrue%3BUser+ID%3Dsa%3BPassword%3DnopCommerce_db_password&Collation=&__RequestVerificationToken=CfDJ8HwM9cCm3UhEg4bV5AKWlwRHr5_tFZr3Cn5W87kMYLh3llFCO0lZC7BYIk3ku4LzSp4DLLLNKKfefxyHAnbW29cvR4V_lk9gxO_PDD387iGDrNpQfZXjNSDOEa2vjnFENDLmJKlaToXWdrj_OueTYUY&InstallSampleData=false&CreateDatabaseIfNotExists=true&ConnectionStringRaw=false&IntegratedSecurity=false&UseCustomCollation=false'
installRequest = requests.post('http://localhost:90/install', headers = installHeaders, data=installData)
if installRequest.status_code != 200:
    sys.exit('Error sending installation request')

print_and_sleep('Sleeping 15 secs to give installation process a bit of time...', 15)

print('Restarting main container')
subprocess.check_call(['docker', 'restart', 'nopcommerce_web'])

print_and_sleep('Sleeping 15 secs to give app time to startup', 15)
print('NopCommerce should now be reachable through http://localhost:90/')

