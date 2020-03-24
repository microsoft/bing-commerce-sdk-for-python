import os
import json
from microsoft.bing.commerce.ingestion import BingCommerceIngestion
from microsoft.bing.commerce.ingestion.models import IndexField, Index,Region
import microsoft.bing.commerce.ingestion
from msrest.authentication import BasicTokenAuthentication
from msrest.exceptions import HttpOperationError


def test_CreateIndex(self):
        creds = BasicTokenAuthentication({ 'access_token': os.environ['INGEST_TOKEN'] })
        client = BingCommerceIngestion(creds)

        query_parameters = {}

        # Create Index
        field = IndexField(name = 'testField01234',
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

def test_UpdateIndex(self):
        creds = BasicTokenAuthentication({ 'access_token': os.environ['INGEST_TOKEN'] })
        client = BingCommerceIngestion(creds)

        query_parameters = {}

        # Create Index
        field = IndexField(name = 'testField01234',
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

        new_index.fields=IndexField(name = 'testIndex01234',
                                    type = 'ProductId',
                                    facetable=False,
                                    filterable=False,
                                    retrievable=True,
                                    searchable=True,
                                    sortable=False)

        updateResponse=client.update_index(self.TENANT_ID, create_response.indexes[0].id, body=new_index, query_parameters=query_parameters)

def test_DeleteIndex(self):
        creds = BasicTokenAuthentication({ 'access_token': os.environ['INGEST_TOKEN'] })
        client = BingCommerceIngestion(creds)

        query_parameters = {}

        # Create Index
        field = IndexField(name = 'testField01234',
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
        
        delete_Response=client.delete_index(self.TENANT_ID, create_response.indexes[0].id, query_parameters=query_parameters)

def test_GetIndexDefinitionById(self):
        creds = BasicTokenAuthentication({ 'access_token': os.environ['INGEST_TOKEN'] })
        client = BingCommerceIngestion(creds)

        query_parameters = {}

        # Create Index
        field = IndexField(name = 'testField01234',
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

        get_index_response = client.get_index(self.TENANT_ID, create_response.indexes[0].id, query_parameters=query_parameters)
  
def test_GetListOfIndexDefinition(self):
        creds = BasicTokenAuthentication({ 'access_token': os.environ['INGEST_TOKEN'] })
        client = BingCommerceIngestion(creds)

        query_parameters = {}

        # Create Index
        field = IndexField(name = 'testField01234',
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

        all_indexes = client.get_all_indexes(self.TENANT_ID, query_parameters=query_parameters)

def test_Push(self):

        creds = BasicTokenAuthentication({ 'access_token': os.environ['INGEST_TOKEN'] })
        client = BingCommerceIngestion(creds)

        query_parameters = {}

        index_id = ensure_index(client, self.TENANT_ID, query_parameters)

        push_response = client.push_data_update('Test Content', self.TENANT_ID, index_id, notransform=False, query_parameters=query_parameters)
     
        push_status = client.push_data_status(self.TENANT_ID, index_id, push_response.update_id, query_parameters=query_parameters)
        