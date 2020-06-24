indexId='Index ID'
tenantId='Tenant Id'
subscription_key = 'Bearer Token'

import requests
import json

def GetCommits():
    search_url = 'https://commerce.bing.com/api/devops/v1/{0}/indexes/{1}/scm'
    url=search_url.format(tenantId,indexId)
    headers = {'Authorization':'Bearer '+ subscription_key}
    response = requests.get(url,headers=headers,verify=False)
    response.raise_for_status()
    search_results = response.json()
    print('Completed')

def CompareCommits():
    search_url = 'https://commerce.bing.com/api/devops/v1/{0}/indexes/{1}/scm/{2}/diff/{3}'
    url=search_url.format(tenantId,indexId,commitId1,commitId2)
    headers = {'Authorization':'Bearer '+ subscription_key}
    response = requests.get(url,headers=headers,verify=False)
    response.raise_for_status()
    search_results = response.json()
    print('Completed')

def GetDeployments():
    search_url = 'https://commerce.bing.com/api/devops/v1/{0}/indexes/{1}/deployments'
    url=search_url.format(tenantId,indexId)
    headers = {'Authorization':'Bearer '+ subscription_key}
    response = requests.get(url,headers=headers,verify=False)
    response.raise_for_status()
    search_results = response.json()
    print('Completed')

def GetDeploymentbyID():
    search_url = 'https://commerce.bing.com/api/devops/v1/{0}/indexes/{1}/deployments/{2}'
    url=search_url.format(tenantId,indexId,deploymentId)
    headers = {'Authorization':'Bearer '+ subscription_key}
    response = requests.get(url,headers=headers,verify=False)
    response.raise_for_status()
    search_results = response.json()


def CreateCommit():
    search_url = "https://commerce.bing.com/api/devops/v1/{0}/indexes/{1}/scm"
    url=search_url.format(tenantId,indexId)
    f = open("ransformation.zip", "rb")
    payload = f.read()
    headers = {
        'x-ms-author': 'Sergey V',
        'x-ms-author-message': 'New index',
        'Authorization': 'Bearer '+ subscription_key,
        'Content-Type': 'application/zip',
        'Cookie': 'MUIDB=05EB1B523F3063030EFE15843E9C62E7'
        }
    response = requests.request("POST", url, headers=headers, data = payload)
    print(response.text.encode('utf8'))

def DeployCommit():
    search_url = "https://commerce.bing.com/api/devops/v1/{0}/indexes/{1}/deployments/{2}"
    url=search_url.format(tenantId,indexId,commitId)
    payload = {}
    headers = {
        'Authorization':'Bearer '+ subscription_key,
        'Cookie': 'MUIDB=05EB1B523F3063030EFE15843E9C62E7',
        'x-ms-author': 'Sergey V'
        }
    response = requests.request("POST", url, headers=headers, data = payload)
    print(response.text.encode('utf8'))

def RedeployCommit():
    search_url = "https://commerce.bing.com/api/devops/v1/{0}/indexes/{1}/deployments/{2}"
    url=search_url.format(tenantId,indexId,deploymentId)
    payload = {}
    headers = {
        'Authorization':'Bearer '+ subscription_key,
        'Cookie': 'MUIDB=05EB1B523F3063030EFE15843E9C62E7',
        'x-ms-author': 'Sergey V'
        }
    response = requests.request("PUT", url, headers=headers, data = payload)
    print(response.text.encode('utf8'))

def ExportIndexVersion():
    search_url = "https://commerce.bing.com/api/devops/v1/{0}/indexes/{1}/scm/{2}/zip?testhooks=1"
    url=search_url.format(tenantId,indexId,commitId)
    payload = "<file contents here>"
    headers = {
        'Authorization': 'Bearer '+ subscription_key,
        'Content-Type': 'application/zip',
        'Cookie': 'MUIDB=05EB1B523F3063030EFE15843E9C62E7'
        }
    response = requests.request("GET", url, headers=headers, data = payload)
    print(response.text.encode('utf8'))


ExportIndexVersion()