
subscription_key = 'YOUR-SUBSCRIPTION-KEY'
tenantId='tenantID'
indexId='indexId'
import requests
import json
from microsoft.bing.commerce.ingestion import BingCommerceIngestion
from microsoft.bing.commerce.ingestion.models import IndexField, Index,Region
import microsoft.bing.commerce.ingestion
from msrest.authentication import BasicTokenAuthentication
from msrest.exceptions import HttpOperationError

        
def RetrievsScript():
    search_url = 'https://commerce.bing.com/api/ingestion/v1/{0}/indexes/{1}/transformation'
    url=search_url.format(tenantId,indexId)
    headers = {'Authorization':'Bearer '+ subscription_key}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    search_results = response.json()

def DeleteScript():
    search_url = 'https://commerce.bing.com/api/ingestion/v1/{0}/indexes/{1}/transformation'
    url=search_url.format(tenantId,indexId)
    headers = {'Authorization':'Bearer '+ subscription_key}
    response = requests.delete(url, headers=headers)
    response.raise_for_status()

def CreateAScript(self): 
    creds = BasicTokenAuthentication({ 'access_token': os.environ['INGEST_TOKEN'] })
    client = BingCommerceIngestion(creds)
    f=open("Defines a path to the content index on your local file system.", "r")
    script =f.read()
    create_response = client.create_or_update_transformation_config(script,tenantId,indexId,subscription_key)

def TestTryoutTransfromationApi(self): 
    creds = BasicTokenAuthentication({ 'access_token': os.environ['INGEST_TOKEN'] })
    client = BingCommerceIngestion(creds)
    f=open("Defines a path to the content index on your local file system.", "r")
    script =f.read()
    createScriptResponse= client.upload_try_out_config(script)
    reponse=client.execute_try_out_config(scrip,createScriptResponse.TryOutId)

