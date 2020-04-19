subscription_key = 'YOUR-SUBSCRIPTION-KEY'
tenantId='tenantID'
indexId='indexId'
instanceId='BlackFridaySettings'

def RequestAsync():
    search_url = 'https://commerce.bing.com/api/autosuggest/v1/{0}/indexes/{1}/?q=Contoso&count=2&source=logs'
    url=search_url.format(tenantId,indexId)
    headers = {'Authorization':'Bearer '+ subscription_key}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    search_results = response.json()

def RequestIndexAsync():
    search_url = 'https://commerce.bing.com/api/autosuggestauthoring/v1/{0}/indexes/{1}'
    url=search_url.format(tenantId,indexId)
    headers = {'Authorization':'Bearer '+ subscription_key}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    search_results = response.json()

def GetIndexAsync():
    search_url = 'https://commerce.bing.com/api/autosuggestauthoring/v1/{0}/indexes/{1}'
    url=search_url.format(tenantId,indexId)
    headers = {'Authorization':'Bearer '+ subscription_key}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    search_results = response.json()

def Add_UpdateIndex():
    search_url = 'https://commerce.bing.com/api/autosuggestauthoring/v1/{0}/indexes/{1}'
    url=search_url.format(tenantId,indexId)
    headers = {'Authorization':'Bearer '+ subscription_key,'Content-type':'application/json'}
    body={'Enabled':False}
    json_data = json.dumps(body)
    response=requests.put(url,body,headers=headers)
    response.raise_for_status()

def DeleteIndex():
    search_url = 'https://commerce.bing.com/api/autosuggestauthoring/v1/{0}/indexes/{1}'
    url=search_url.format(tenantId,indexId)
    headers = {'Authorization':'Bearer '+ subscription_key}
    response = requests.delete(url, headers=headers)
    response.raise_for_status()
    search_results = response.json()

def GetBlockedSuggestions():
    search_url = 'https://commerce.bing.com/api/autosuggestauthoring/v1/{0}/indexes/{1}/blocking'
    url=search_url.format(tenantId,indexId)
    headers = {'Authorization':'Bearer '+ subscription_key}
    response = requests.get(url, headers=headers)
    response.raise_for_status()

 
def CreateBlockedSuggestionsAsync():
    suggs=[]
    p1={'query':'example','matchingType':'Exact'}
    p2={'query':'blocked suggestion','matchingType':'Contains'}
    suggs.append(p1)
    suggs.append(p2)
    search_url = 'https://commerce.bing.com/api/autosuggestauthoring/v1/{0}/indexes/{1}/blocking'
    url=search_url.format(tenantId,indexId)
    headers = {'Authorization':'Bearer '+ subscription_key,'Content-type':'application/json'}
    body={'BlockedSuggestions':suggs}
    json_data = json.dumps(body)
    addBlockedSuggestionsResponse = requests.post(url, json_data, headers=headers)
    addBlockedSuggestionsResponse.raise_for_status()

def UpdateBlockdSuggestionsAsync():
    suggs=[]
    p1={'id':'85e1d36d-c044-408e-9bc4-1696c3460f57','query':'blocked suggestion','matchingType':'Contains'}
    suggs.append(p1)
    search_url = 'https://commerce.bing.com/api/autosuggestauthoring/v1/{0}/indexes/{1}/blocking'
    url=search_url.format(tenantId,indexId)
    headers = {'Authorization':'Bearer '+ subscription_key,'Content-type':'application/json'}
    body={'BlockedSuggestions':suggs}
    json_data = json.dumps(body)
    addBlockedSuggestionsResponse = requests.put(search_url, data=json_data, headers= headers)
    addBlockedSuggestionsResponse.raise_for_status()

