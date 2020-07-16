import requests
import json

def GetAlertOption():
    search_url = 'https://commerce.bing.com/api/devops/v1/{0}/alerts/options'
    url=search_url.format(tenantId)
    headers = {'Authorization':'Bearer '+ subscription_key}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    search_results = response.json()

def GetAlertGroup():
    search_url = 'https://commerce.bing.com/api/devops/v1/{0}/alerts/group'
    url=search_url.format(tenantId)
    headers = {'Authorization':'Bearer '+ subscription_key}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    search_results = response.json()

def CreateOrUpdateAlertGroup():
    search_url = 'https://commerce.bing.com/api/devops/v1/{0}/alerts/group'
    url=search_url.format(tenantId)
    headers = {'Authorization':'Bearer '+ subscription_key,'Content-type':'application/json'}
    request = {'enabled': True,
              'emailaddress': 'user@domain.com'}
    json_data = json.dumps(request)
    response=requests.put(url, data=json_data, headers= headers)
    response.raise_for_status()

def DeleteAlertGroup():
    search_url = 'https://commerce.bing.com/api/devops/v1/{0}/alerts/group'
    url=search_url.format(tenantId)
    headers = {'Authorization':'Bearer '+ subscription_key}
    response = requests.delete(url, headers=headers)
    response.raise_for_status()
    search_results = response.json()

def GetAllAlert():
    search_url = 'https://commerce.bing.com/api/devops/v1/{0}/indexes/{1}/alerts'
    url=search_url.format(tenantId,indexId)
    headers = {'Authorization':'Bearer '+ subscription_key}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    search_results = response.json()

def GetAlert():
    search_url = 'https://commerce.bing.com/api/devops/v1/{0}/indexes/{1}/alerts/{2}'
    url=search_url.format(tenantId,indexId,alertId)
    headers = {'Authorization':'Bearer '+ subscription_key}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    search_results = response.json()

def CreateOrUpdateAlert():
    search_url = 'https://commerce.bing.com/api/devops/v1/{0}/indexes/{1}/alerts/{2}'
    url=search_url.format(tenantId,indexId,alertId)
    headers = {'Authorization':'Bearer '+ subscription_key,'Content-type':'application/json'}
    request = {'Enabled': True,
              'AggregationDurationInMinutes': 5,
              'FrequencyInMinutes':5,
              'TimeWindowInMinutes':5,
              'SeverityLevel':'Sev3',
              'AlertOperator':'GreaterThan',
              'AlertThreshold':0,
              'TriggerBasis':'Total',
              'TriggerOperator':'GreaterThan',
              'TriggerThreshold':0}
    json_data = json.dumps(request)
    response=requests.put(url, data=json_data, headers= headers)
    response.raise_for_status()

def DeleteAlertGroup():
    search_url = 'https://commerce.bing.com/api/devops/v1/{0}/indexes/{1}/alerts/{2}'
    url=search_url.format(tenantId,indexId,alertId)
    headers = {'Authorization':'Bearer '+ subscription_key}
    response = requests.delete(url, headers=headers)
    response.raise_for_status()
    search_results = response.json()
