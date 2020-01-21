# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

#test_search.py
import unittest
try:
    from microsoft.bing.commerce.search import BingCommerceSearch
except ImportError:
    pass
try:
    from microsoft.bing.commerce.search.models import CommerceSearchPostRequest, RequestQuery, RequestItems
except ImportError:
    pass
import microsoft.bing.commerce.search.operations
try:
    from msrest.authentication import BasicTokenAuthentication
except ImportError:
    pass

import os

class Test_Search(unittest.TestCase):
    def test_MatchAll(self):
        creds = BasicTokenAuthentication({ 'access_token': os.environ['SEARCH_TOKEN'] })
        client = BingCommerceSearch(creds)
        tenant_id = os.environ['SEARCH_TENANT']
        index_id = os.environ['SEARCH_INDEX']

        request = CommerceSearchPostRequest(
            query = RequestQuery(match_all = 'diamond'), 
            items = RequestItems(select = ['_itemId', 'name']))

        query_parameters = {}
        query_parameters['traffictype'] = 'test'

        response = client.search.post(request, tenant_id, index_id, query_parameters)

        assert response is not None
        assert response.items is not None
        assert response.items.total_estimated_matches is not None
        assert response.items.value is not None

        assert response.items.total_estimated_matches > 0
        assert len(response.items.value) > 0

        for item in response.items.value:
            assert item is not None
            assert item.item_id is not None
            assert item.fields is not None
            assert item.fields['name'] is not None

if __name__ == '__main__':
    unittest.main()
