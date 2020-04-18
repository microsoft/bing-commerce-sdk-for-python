subscription_key = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjRmZGI5N2ZhLWQyYWItNDY1Mi1iMWE0LWM3Y2E3YTBhNDJmNSJ9.eyJhdWQiOiIxZTE0MmJhOC1kNzU1LTQ0ZDAtOGFlYS03YjJiNTI0NjZhMTMiLCJub25jZSI6IjYyM2Q1OWQzLTMxZDMtMDZlYy0xZGVkLTNkYjc4OGYyMGQxYyIsImhhc0FjY2Vzc1RvQWxsSW5zdGFuY2VzIjp0cnVlLCJpbnN0YW5jZXMiOiIiLCJzY3AiOiJBZG1pbi5FbnZpcm9ubWVudC5SZWFkV3JpdGUgQWRtaW4uUm9sZU1hbmFnZW1lbnQuUmVhZFdyaXRlIEFkbWluLlRva2VuLkNyZWF0ZSBTZWFyY2guQXV0b3N1Z2dlc3QuUmVhZFdyaXRlIFNlYXJjaC5JbmRleC5SZWFkV3JpdGUgU2VhcmNoLkN1c3RvbWl6YXRpb24uUmVhZFdyaXRlIiwidGlkcyI6WyI5MjQ0OTQxMi03MzFjLTQ5OGQtZDRhZi0wOGQ3NjY3MzczZjIiXSwiYXBwaWQiOiJjNzM4YWUwYTFhNGQxMDM2MjIxMzBjZGY1MjU4MTFkNzBhMDMyOWRlIiwiaWF0IjoxNTg2Mjg3NTI5LCJleHAiOjE1OTM1NzU5MDksInZlciI6IjEuMCJ9.pqptNx_3d3RbXMu4LKSiNelJd9tBWPAVFcL5iGLWgqTVAo21NAoNYQ_zelxz9sCYtkVoy97rl--nooxvXHDdcWKVmz_jqwOF2Ekmtbjk2oZBK_P8l-GlcQ2W5hZ7wBUiBtfcB22zGPQnTgrkxiWL5COz86I7tME_VhepJP3BXYXIV8AFpTL51J-mxec2dOJEa5s88ZrrCPG4PXCYkgs6OSJ2JGkWN80BWWqD6z7iKDe8jTAyhlebc0bhPISqSICb27SUu9rmlrWmVr49VWMMFPiJ1mUR2VPN13SLl112trcOKW2G-VZkH2pLQ8xVX8yaLVP7Jlh1bb52kr980J0rnQ'
tenantId='92449412-731c-498d-d4af-08d7667373f2'
indexId='12744db4-994e-4676-ab56-79565c8c050f'
instanceId='BlackFridaySettings'
ruleId='ruleId'
synonymId='synonymsId'
redirectId='redirectID'

import requests
import json

def GetSearchInstance():
    search_url = 'https://commerce.bing.com/api/customization/v1/searchinstance/{0}/indexes/{1}'
    url=search_url.format(tenantId,indexId)
    headers = {'Authorization':'Bearer '+ subscription_key}
    response = requests.get(url,headers=headers)
    response.raise_for_status()
    search_results = response.json()

def CreateSearchInstance():
    request={'searchinstanceId':'BlackFridaySettings'}
    json_data = json.dumps(request)
    search_url = 'https://commerce.bing.com/api/customization/v1/searchinstance/{0}/indexes/{1}'
    url=search_url.format(tenantId,indexId)
    headers = {'Authorization':'Bearer '+ subscription_key,'Content-type':'application/json'}
    response=requests.post(url,data=json_data,headers=headers)
    response.raise_for_status()

def DeleteSearchInstance():
    search_url = 'https://commerce.bing.com/api/customization/v1/searchinstance/{0}/indexes/{1}?searchinstanceid={2}'
    url=search_url.format(tenantId,indexId,instanceId)
    headers = {'Authorization':'Bearer '+ subscription_key}
    response = requests.delete(url, headers=headers)
    response.raise_for_status()


def GetAllRule():
    search_url = 'https://commerce.bing.com/api/customization/v1/businessrules/rules/{0}/indexes/{1}?searchinstanceid={2}'
    url=search_url.format(tenantId,indexId,instanceId)
    headers = {'Authorization':'Bearer '+ subscription_key}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    search_results = response.json()

def GetRule():
    search_url = 'https://commerce.bing.com/api/customization/v1/businessrules/rules/{0}/indexes/{1}?rule={2}&searchinstanceid={3}'
    url=search_url.format(tenantId,indexId,ruleId,instanceId)
    headers = {'Authorization':'Bearer '+ subscription_key}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    search_results = response.json()

def DeleteRule():
    search_url = 'https://commerce.bing.com/api/customization/v1/businessrules/rules/{0}/indexes/{1}?rule={2}&searchinstanceid={3}'
    url=search_url.format(tenantId,indexId,ruleId,instanceId)
    headers = {'Authorization':'Bearer '+ subscription_key}
    response = requests.delete(url, headers=headers)
    response.raise_for_status()
    search_results = response.json()

def GetSynonyms():
    search_url = 'https://commerce.bing.com/api/customization/v1/synonym/{0}/indexes/{1}?searchinstanceid={2}'
    url=search_url.format(tenantId,indexId,instanceId)
    headers = {'Authorization':'Bearer '+ subscription_key}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    search_results = response.json()

def UpdateSynonyms():
    search_url = 'https://commerce.bing.com/api/customization/v1/synonym/{0}/indexes/{1}'
    url=search_url.format(tenantId,indexId)
    headers = {'Authorization':'Bearer '+ subscription_key,'Content-type':'application/json'}
    request = {'searchinstanceId': instanceId,
              'synonymId': 'outerwear',
              'synonyms': ['coat', 'jacket', 'suit']}
    json_data = json.dumps(request)
    response=requests.post(url, data=json_data, headers= headers)
    response.raise_for_status()

def DeleteSynonyms():
    search_url = 'https://commerce.bing.com/api/customization/v1/synonym/{0}/indexes/{1}?synonymid={2}&searchinstanceid={3}'
    url=search_url.format(tenantId,indexId,synonymId,instanceId)
    headers = {'Authorization':'Bearer '+ subscription_key}
    response = requests.delete(url, headers=headers)
    response.raise_for_status()
    search_results = response.json()

def GetCondition(type,field,value,op=None):
      dict={'_type':type,
            'field':field,
            'value':value}
      if op!=None:
          dict.update({'operator':op})
      return dict

def UpdateRedirects():
    search_url = 'https://commerce.bing.com/api/customization/v1/redirect/{0}/indexes/{1}'
    url=search_url.format(tenantId,indexId)
    headers = {'Authorization':'Bearer '+ subscription_key,'Content-type':'application/json'}
    request = {'searchinstanceId': instanceId,
              'RedirectId': 'ClothingRedirect',
              'SearchRequestCondition':GetCondition('StringCondition','query','men shirts'),
              'RedirectUrl':'https://www.contoso.com/menshirts'}
    json_data=json.dumps(request)
    response=requests.post(url, data=json_data, headers=headers)
    response.raise_for_status()

def GetRedirect():
    search_url = 'https://commerce.bing.com/api/customization/v1/redirect/{0}/indexes/{1}?searchinstanceid={2}'
    url=search_url.format(tenantId,indexId,instanceId)
    headers = {'Authorization':'Bearer '+ subscription_key}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    search_results = response.json()

def DeleteRedirect():
    search_url = 'https://commerce.bing.com/api/customization/v1/redirect/{0}/indexes/{1}?redirectId={2}&searchinstanceid={3}'
    url=search_url.format(tenantId,indexId,redirectId,instanceId)
    headers = {'Authorization':'Bearer '+ subscription_key}
    response = requests.delete(url, headers=headers)
    response.raise_for_status()
    search_results = response.json()

def CreateUpdateARulePost():
    search_url = 'https://commerce.bing.com/api/customization/v1/businessrules/rule/{0}/indexes/{1}'
    url = search_url.format(tenantId,indexId)
    headers = {'Authorization':'Bearer '+ subscription_key,'Content-type':'application/json'}
    request = {'searchinstanceId': instanceId,
              'Rule': 'ruleclothing',
              'Enabled':True,
              'Description':'Black Friday clothing rule',
              'SearchRequestCondition':GetCondition('StringSetCondition','query',['shirts','coats','*']),
              'Banner':{'type':'PlainText','value':'Get 15% off Black Friday deals'},
              'boosts':[{'boost':500,'condition':GetCondition('StringCondition','brand','Fabrikam')}],
              'filter':{'_type':'ConditionBlock','conditions':[GetCondition('StringCondition','brand','Contoso','Ne')]},
              'StartTimeUtc':'20200101040000',
              'EndTimeUtc':'20201231180000'}
    json_data=json.dumps(request)
    response=requests.post(url,data=json_data,headers=headers, verify=False)
    response.raise_for_status()