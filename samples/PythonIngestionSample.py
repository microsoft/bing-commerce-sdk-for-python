import os
import json
import microsoft.bing.commerce.ingestion
from microsoft.bing.commerce.ingestion import BingCommerceIngestion
from microsoft.bing.commerce.ingestion.models import IndexField, Index,Region
from msrest.authentication import BasicTokenAuthentication
from msrest.exceptions import HttpOperationError

#Creates a definition of the tenant's index. 
def CreateIndex(self):
    creds = BasicTokenAuthentication({ 'access_token': os.environ['INGEST_TOKEN'] })
    client = BingCommerceIngestion(creds)
    
    # Create Index (First, make sure we don't have an index with the same name.)
    field = IndexField(name = 'productId',
                       type = 'ProductId',
                       facetable=False,
                       filterable=False,
                       retrievable=True,
                       searchable=True,
                       sortable=False)
    
    new_index = Index(name = 'Contoso',
                      description = 'Index definition for Contoso.com',
                      search_scenario='Retail',
                      regions=[Region.west_us,Region.east_us,Region.north_central_us],
                      fields = [field])

    create_response = client.create_index(self.TENANT_ID, body=new_index)

#Updates an index's definition.
#The updated Index object. Because this is an overwrite operation, 
#the index must specify all information that you want to retain; partial updates are not supported.      
def UpdateIndex(self):
    creds = BasicTokenAuthentication({ 'access_token': os.environ['INGEST_TOKEN'] })
    client = BingCommerceIngestion(creds)
    
    # Create Index
    field = IndexField(name = 'productId',
                       type = 'ProductId',
                       facetable=False,
                       filterable=False,
                       retrievable=True,
                       searchable=True,
                       sortable=False)
    
    new_index = Index(name = 'Contoso',
                      description = 'Index definition for Contoso.com',
                      search_scenario='Retail',
                      regions=[Region.west_us,Region.east_us,Region.north_central_us],
                      fields = [field])
    
    create_response = client.create_index(self.TENANT_ID, body=new_index)
    
    new_index.fields=IndexField(name = 'productId',
                                type = 'ProductId',
                                facetable=False,
                                filterable=False,
                                retrievable=True,
                                searchable=True,
                                sortable=False)
    
    updateResponse=client.update_index(self.TENANT_ID, create_response.indexes[0].id, body=new_index)

 #Deletes an index definition
def DeleteIndex(self):
    creds = BasicTokenAuthentication({ 'access_token': os.environ['INGEST_TOKEN'] })
    client = BingCommerceIngestion(creds)
    
    # Create Index
    field = IndexField(name = 'productId',
                       type = 'ProductId',
                       facetable=False,
                       filterable=False,
                       retrievable=True,
                       searchable=True,
                       sortable=False)
    
    new_index = Index(name = 'Contoso',
                      description = 'Index definition for Contoso.com',
                      search_scenario='Retail',
                      regions=[Region.west_us,Region.east_us,Region.north_central_us],
                      fields = [field])
    create_response = client.create_index(self.TENANT_ID, body=new_index)
    
    delete_Response=client.delete_index(self.TENANT_ID, create_response.indexes[0].id)

#Get a specific index definition for a tenant.
#The response contains an IndexResponse object. 
#The indexes field is an array with the single Index object you requested. 
def GetIndexDefinitionById(self):
    creds = BasicTokenAuthentication({ 'access_token': os.environ['INGEST_TOKEN'] })
    client = BingCommerceIngestion(creds)
    
    # Create Index
    field = IndexField(name = 'productId',
                       type = 'ProductId',
                       facetable=False,
                       filterable=False,
                       retrievable=True,
                       searchable=True,
                       sortable=False)
    
    new_index = Index(name = 'testIndex01234',
                      description = 'Created with the Python sdk unit testing',
                      search_scenario='Retail',
                      regions=[Region.west_us,Region.east_us,Region.north_central_us],
                      fields = [field])
    create_response = client.create_index(self.TENANT_ID, body=new_index, query_parameters=query_parameters)
    
    get_index_response = client.get_index(self.TENANT_ID, create_response.indexes[0].id)
  
#Get list of index definitions that you defined for a tenant.
#The response contains an IndexResponse object. 
#The indexes field is an array with the single Index object you requested.     
def GetListOfIndexDefinition(self):
    creds = BasicTokenAuthentication({ 'access_token': os.environ['INGEST_TOKEN'] })
    client = BingCommerceIngestion(creds)
    
    # Create Index
    field = IndexField(name = 'productId',
                       type = 'ProductId',
                       facetable=False,
                       filterable=False,
                       retrievable=True,
                       searchable=True,
                       sortable=False)
    
    new_index = Index(name = 'testIndex01234',
                      description = 'Created with the Python sdk unit testing',
                      search_scenario='Retail',
                      regions=[Region.west_us,Region.east_us,Region.north_central_us],
                      fields = [field])
    
    create_response = client.create_index(self.TENANT_ID, body=new_index)
    
    all_indexes = client.get_all_indexes(self.TENANT_ID)

#This method pushes your index data to Bing. This is an asynchronous process. To upload your index data to Bing, 
#you'll send a push request that contains your index data.     
def PushCatalogData(self):
    creds = BasicTokenAuthentication({ 'access_token': os.environ['INGEST_TOKEN'] })
    client = BingCommerceIngestion(creds)
    index_id = ensure_index(client, self.TENANT_ID, query_parameters)
    push_response = client.push_data_update('Test Content', self.TENANT_ID, index_id,
                                           notransform=False)

    push_status = client.push_data_status(self.TENANT_ID, index_id, push_response.update_id)


def GetIngestionStatus(self):
    creds = BasicTokenAuthentication({ 'access_token': os.environ['INGEST_TOKEN'] })
    client = BingCommerceIngestion(creds)
    index_id = ensure_index(client, self.TENANT_ID, query_parameters)
    push_response = client.push_data_update('Test Content', self.TENANT_ID, index_id,
                                           notransform=False)

    push_status = client.push_data_status(self.TENANT_ID, index_id, push_response.update_id)
