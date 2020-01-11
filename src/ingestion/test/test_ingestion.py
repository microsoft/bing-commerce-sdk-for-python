#test_ingestion.py
import unittest
try:
    from microsoft.bing.commerce.ingestion import BingCommerceIngestion
except ImportError:
    pass
try:
    from microsoft.bing.commerce.ingestion.models import IndexField, Index
except ImportError:
    pass
import microsoft.bing.commerce.ingestion
try:
    from msrest.authentication import Authentication
except ImportError:
    pass

import os

def ensure_index(client, tenant_id, query_parameters):
    all_indexes = client.get_all_indexes(tenant_id, query_parameters=query_parameters)

    for index in all_indexes.indexes:
        if index.name == 'testIndex01234':
            return index.id

    field = IndexField(
            name = 'testField01234',
            type = 'ProductId')
    new_index = Index(
            name = 'testIndex01234',
            description = 'Created with the Python sdk unit testing',
            fields = [field])

    create_response = client.create_index(tenant_id, body=new_index, query_parameters=query_parameters)
    return create_response.indexes[0].id

class Test_Ingestion(unittest.TestCase):

    def setUp(self):
        self.TENANT_ID = os.environ['INGEST_TENANT']

    def tearDown(self):
        creds = Authentication()
        client = BingCommerceIngestion(creds)

        query_parameters = {}
        query_parameters['appid'] = os.environ['INGEST_APPID']
        query_parameters['traffictype'] = 'test'

        all_indexes = client.get_all_indexes(self.TENANT_ID, query_parameters=query_parameters)

        for index in all_indexes.indexes:
            if index.name == 'testIndex01234':
                client.delete_index(self.TENANT_ID, index.id, query_parameters=query_parameters)
                return

    def test_Index(self):
        creds = Authentication()
        client = BingCommerceIngestion(creds)

        query_parameters = {}
        query_parameters['appid'] = os.environ['INGEST_APPID']
        query_parameters['traffictype'] = 'test'

        # Create Index
        field = IndexField(
            name = 'testField01234',
            type = 'ProductId')
        new_index = Index(
            name = 'testIndex01234',
            description = 'Created with the Python sdk unit testing',
            fields = [field])

        create_response = client.create_index(self.TENANT_ID, body=new_index, query_parameters=query_parameters)
        assert create_response is not None
        assert create_response.indexes is not None
        assert len(create_response.indexes) > 0

        # Get All Indexes
        all_indexes = client.get_all_indexes(self.TENANT_ID, query_parameters=query_parameters)

        assert all_indexes is not None
        assert all_indexes.indexes is not None
        assert len(all_indexes.indexes) > 0

        # Get Specific Index
        get_index_response = client.get_index(self.TENANT_ID, create_response.indexes[0].id, query_parameters=query_parameters)
        assert get_index_response is not None
        assert get_index_response.indexes is not None
        assert len(get_index_response.indexes) > 0

        # Update Index
        extra_field = IndexField(
            name = 'extraTestField01234',
            type = 'Number')
        new_index.fields.append(extra_field)
        update_response = client.update_index(self.TENANT_ID, create_response.indexes[0].id, body=new_index, query_parameters=query_parameters)
        assert update_response is not None
        assert update_response.indexes is not None
        assert len(update_response.indexes) > 0
        assert len(update_response.indexes[0].fields) == 2

        # Get Index Status
        index_status = client.get_index_status(self.TENANT_ID, create_response.indexes[0].id, query_parameters=query_parameters)
        assert index_status is not None
        assert index_status.index_statuses is not None
        assert len(index_status.index_statuses) > 0

        # Delete Index
        delete_response = client.delete_index(self.TENANT_ID, create_response.indexes[0].id, query_parameters=query_parameters)
        assert delete_response is not None
        assert delete_response.indexes is not None
        assert len(delete_response.indexes) > 0


    def test_Push(self):
        creds = Authentication()
        client = BingCommerceIngestion(creds)

        query_parameters = {}
        query_parameters['appid'] = os.environ['INGEST_APPID']
        query_parameters['traffictype'] = 'test'

        index_id = ensure_index(client, self.TENANT_ID, query_parameters)

        push_response = client.push_data_update('Test Content', self.TENANT_ID, index_id, notransform=False, query_parameters=query_parameters)
        assert push_response is not None
        assert push_response.update_id is not None

        push_status = client.push_data_status(self.TENANT_ID, index_id, push_response.update_id, query_parameters=query_parameters)
        assert push_status is not None
        assert push_status.status is not None

if __name__ == '__main__':
    unittest.main()
