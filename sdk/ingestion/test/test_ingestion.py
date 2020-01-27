# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

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
    from msrest.authentication import BasicTokenAuthentication
    from msrest.exceptions import HttpOperationError
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
        creds = BasicTokenAuthentication({ 'access_token': os.environ['INGEST_TOKEN'] })
        client = BingCommerceIngestion(creds)

        query_parameters = {}
        query_parameters['traffictype'] = 'test'

        all_indexes = client.get_all_indexes(self.TENANT_ID, query_parameters=query_parameters)

        for index in all_indexes.indexes:
            if index.name == 'testIndex01234':
                client.delete_index(self.TENANT_ID, index.id, query_parameters=query_parameters)
                return

    def test_Index(self):
        creds = BasicTokenAuthentication({ 'access_token': os.environ['INGEST_TOKEN'] })
        client = BingCommerceIngestion(creds)

        query_parameters = {}
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
        creds = BasicTokenAuthentication({ 'access_token': os.environ['INGEST_TOKEN'] })
        client = BingCommerceIngestion(creds)

        query_parameters = {}
        query_parameters['traffictype'] = 'test'

        index_id = ensure_index(client, self.TENANT_ID, query_parameters)

        push_response = client.push_data_update('Test Content', self.TENANT_ID, index_id, notransform=False, query_parameters=query_parameters)
        assert push_response is not None
        assert push_response.update_id is not None

        push_status = client.push_data_status(self.TENANT_ID, index_id, push_response.update_id, query_parameters=query_parameters)
        assert push_status is not None
        assert push_status.status is not None

    def test_tryout_transformation(self):
        creds = BasicTokenAuthentication({ 'access_token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjRmZGI5N2ZhLWQyYWItNDY1Mi1iMWE0LWM3Y2E3YTBhNDJmNSJ9.eyJhdWQiOiIxZTE0MmJhOC1kNzU1LTQ0ZDAtOGFlYS03YjJiNTI0NjZhMTMiLCJhcHBpZCI6ImM3MzhhZTBhMWE0ZDEwMzYyMjEzMGNkZjUyNTgxMWQ3MGEwMzI5ZGUiLCJub25jZSI6ImYzMTc2NGY2LWEzNGItZjMxOC05MDAzLWJjY2FlNzE0Yjg0MCIsInNjcCI6IkFkbWluLkVudmlyb25tZW50LlJlYWRXcml0ZSBBZG1pbi5Sb2xlTWFuYWdlbWVudC5SZWFkV3JpdGUgQWRtaW4uVG9rZW4uQ3JlYXRlIEFkbWluLlRva2VuLlJldm9rZSBTZWFyY2guQXV0b3N1Z2dlc3QuUmVhZFdyaXRlIFNlYXJjaC5JbmRleC5SZWFkV3JpdGUgU2VhcmNoLkN1c3RvbWl6YXRpb24uUmVhZFdyaXRlIiwiaW5zdGFuY2VzIjoiIiwiaGFzQWNjZXNzVG9BbGxJbnN0YW5jZXMiOnRydWUsImlhdCI6MTU3ODk1NjM4MywiZXhwIjoxOTI1MTA3MTIzLCJ0aWRzIjpbImY5OGQ3OWI4LTY0MzItNDhjZC1iNTg4LWZiMjIwZWRjYjgxNiJdLCJ2ZXIiOiIxLjAifQ.XybtgWMilIAyoOw4k8Lc7k5tQ2ztthEbo1VJfs7rX0JT4Crj6PU9_AyIBRYVZMvJfriBWy_M8M5c9nQaHV3vcWM5pZkPCrKF1yaTYy2C76ffZjZBILoQkR_chG4rZECvv8x0U28WnbiW5Z9FZEfRR-8feD46oo2XmXvLH6SaJr2JbNItEPlqPBZ1kO-Z5ie34h-fdZergk-WjE3n8yD4ZUJXys-_B4vWXDqFMOGENS-VAuJkVED0QJdI6937LIiFm_mhITl26ZXr2beGv0Pn9z25O477nGvv4vqT07LzZ3eS7Bh7TAnPuzdzSKgG2IJqEHFmGk-y9bL4dwFbOLPeAQ'})#os.environ['INGEST_TOKEN'] })
        client = BingCommerceIngestion(creds)

        query_parameters = {}
        query_parameters['traffictype'] = 'test'

        index_id = ensure_index(client, self.TENANT_ID, query_parameters)

        script = ('retailSearchInput({\n'
            '    format: \"TSV\"\n' 
            '});\n' 
            '\n'
            'transform((product, rawProduct) => {\n'
            '    \n'
            '});\n'
            'retailSearchOutput({});')

        data = ("id\ttitle\n"
                "1\tSample Product")

        create_script_response = client.upload_try_out_config(script)
        execute_response = client.execute_try_out_config(data, create_script_response.try_out_id)

        assert 'Succeeded' == execute_response.status

    def test_transformation_api(self):
        creds = BasicTokenAuthentication({ 'access_token': os.environ['INGEST_TOKEN'] })
        client = BingCommerceIngestion(creds)

        query_parameters = {}
        query_parameters['traffictype'] = 'test'

        index_id = ensure_index(client, self.TENANT_ID, query_parameters)

        script = ("retailSearchInput({\n"
            "    format: 'TSV'\n" 
            "});\n" 
            "\n"
            "transform((product, rawProduct) => {\n"
            "    \n"
            "});\n"
            "retailSearchOutput({});")

        create_script_response = client.create_or_update_transformation_config(script, self.TENANT_ID, index_id)
        read_script_response = client.get_transformation_config(self.TENANT_ID, index_id)
        delete_script_response = client.delete_transformation_config(self.TENANT_ID, index_id)

        assert script == delete_script_response.value

        try:
            client.get_transformation_config(self.TENANT_ID, index_id)
            assert False
        except HttpOperationError as e:
            assert e.response.status_code == 400


if __name__ == '__main__':
    unittest.main()
