import requests
import json

subscription_key = 'YOUR-SUBSCRIPTION-KEY'
tenantId='tenantID'
indexId='indexId'
instanceId='BlackFridaySettings'

def Request():
    search_url = 'https://commerce.bing.com/api/autosuggest/v1/{0}/indexes/{1}/?q=Contoso&count=2&source=logs'
    url=search_url.format(tenantId,indexId)
    headers = {'Authorization':'Bearer '+ subscription_key}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    search_results = response.json()

def RequestIndex():
    search_url = 'https://commerce.bing.com/api/autosuggestauthoring/v1/{0}/indexes/{1}'
    url=search_url.format(tenantId,indexId)
    headers = {'Authorization':'Bearer '+ subscription_key}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    search_results = response.json()

#Sending a GET request to the mentioned URL should retrieve the main fields of the index if it exists,
#otherwise it returns a Bad Request error.      
def GetIndexAsync():
    search_url = 'https://commerce.bing.com/api/autosuggestauthoring/v1/{0}/indexes/{1}'
    url=search_url.format(tenantId,indexId)
    headers = {'Authorization':'Bearer '+ subscription_key}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    search_results = response.json()

#PUT requests are used for both adding a new index and updating an existing one. 
#The indexId and tenantId are specified in the URL,
#whereas the body must be of JSON type with two optional fields specifying 
#whether the autosuggest service is enabled for this index, 
#and what fields can be used as custom filters.    
def Add_UpdateIndex():
    search_url = 'https://commerce.bing.com/api/autosuggestauthoring/v1/{0}/indexes/{1}'
    url=search_url.format(tenantId,indexId)
    headers = {'Authorization':'Bearer '+ subscription_key,'Content-type':'application/json'}
    body={'Enabled':True,
          'customFilters':['Locale','AverageRatingCountOverall','BasePrice'],
          'customPostFilters':['Locale','AverageRatingCountOverall','BasePrice','IsMasterProduct','ProductReleaseDate']}
    json_data = json.dumps(body)
    response=requests.put(url,body,headers=headers)
    response.raise_for_status()

#An index can be deleted by sending a DELETE request to the same URL specifying the tenantId and indexId.      
def DeleteIndex():
    search_url = 'https://commerce.bing.com/api/autosuggestauthoring/v1/{0}/indexes/{1}'
    url=search_url.format(tenantId,indexId)
    headers = {'Authorization':'Bearer '+ subscription_key}
    response = requests.delete(url, headers=headers)
    response.raise_for_status()
    search_results = response.json()

#A GET request is used to retrieve all the blocked suggestions for the indexId given in the URL.       
def GetBlockedSuggestions():
    search_url = 'https://commerce.bing.com/api/autosuggestauthoring/v1/{0}/indexes/{1}/blocking'
    url=search_url.format(tenantId,indexId)
    headers = {'Authorization':'Bearer '+ subscription_key}
    response = requests.get(url, headers=headers)
    response.raise_for_status()

#POST requests are used to add blocked suggestions for the specified index.
#Multiple blocked suggestions can be added on request. Once they are added,
#each blocked suggestion gets a unique id that can be used for updating or deleting.     
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

#A PUT request is used to update possibly multiple blocked suggestions for the indexId specified in the URL. 
#The body of the request is of JSON type and contains a list of blocked suggestions 
#similar to the body of adding new blocked suggestions,
#with one additional field in each item, which is the id of the blocked suggestion.
def UpdateBlockdSuggestionsAsync():
    suggs=[]
    p1={'id':'85e1d36d-c044-408e-9bc4-1696c3460f57','query':'blocked suggestion','matchingType':'Contains'}
    suggs.append(p1)
    search_url = 'https://commerce.bing.com/api/autosuggestauthoring/v1/{0}/indexes/{1}/blocking'
    url=search_url.format(tenantId,indexId)
    headers = {'Authorization':'Bearer '+ subscription_key,'Content-type':'application/json'}
    body={'BlockedSuggestions':suggs}
    json_data = json.dumps(body)
    addBlockedSuggestionsResponse = requests.put(url, data=json_data, headers= headers)
    addBlockedSuggestionsResponse.raise_for_status()

def DeleteBlockdSuggestions():
    search_url = 'https://commerce.bing.com/api/autosuggestauthoring/v1/{0}/indexes/{1}/blocking'
    url=search_url.format(tenantId,indexId)
    headers = {'Authorization':'Bearer '+ subscription_key}
    body={'ids':'Ids to be deleted'}
    json_data = json.dumps(body)
    response = requests.delete(url,data=json_data, headers=headers)
    response.raise_for_status()
    search_results = response.json()

