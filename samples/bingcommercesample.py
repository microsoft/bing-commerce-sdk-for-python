
# This is a temporary hack until the packages are installed in pip
import sys
sys.path.append("..\\src\\search")
sys.path.append("..\\src\\ingestion")
#end hack

from microsoft.bing.commerce.ingestion import BingCommerceIngestion
from microsoft.bing.commerce.ingestion.models import IndexField, Index, IndexFieldType
from msrest.authentication import Authentication

from microsoft.bing.commerce.search import BingCommerceSearch
from microsoft.bing.commerce.search.models import CommerceSearchPostRequest, RequestQuery, RequestItems, StringSetCondition, RequestDiscoverFacets
import microsoft.bing.commerce.search.operations


import json
import os

sample_index_name = 'SampleIndex'
tenant_id = os.environ['SAMPLE_TENANT']
app_id = os.environ['SAMPLE_APPID']

def ensure_index(client):

    print('Trying to find the index with name : {0:s}.'.format(sample_index_name))

    all_indexes = client.get_all_indexes(tenant_id, query_parameters={'appid' : app_id})

    for index in all_indexes.indexes:
        if index.name == sample_index_name:
            return index.id

    print('Index not found, not creating one.')

    id_field = IndexField(
            name = 'ProductId',
            type = IndexFieldType.product_id,
            filterable = True,
            retrievable = True)
    title_field = IndexField(
            name = 'ProductTitle',
            type = IndexFieldType.title,
            filterable = True,
            retrievable = True)
    desc_field = IndexField(
            name = 'ProductDescription',
            type = IndexFieldType.description,
            filterable = True,
            retrievable = True)
    price_field = IndexField(
            name = 'ProductPrice',
            type = IndexFieldType.price,
            filterable = True,
            sortable = True)
    url_field = IndexField(
            name = 'ProductDetailsUrl',
            type = IndexFieldType.url,
            Retrievable = True)
    arbitrary_text_field = IndexField(
            name = 'ArbitraryText',
            type = IndexFieldType.string,
            searchable = True)
    arbitrary_number_field = IndexField(
            name = 'ArbitraryNumber',
            type = IndexFieldType.number,
            facetable = True)

    new_index = Index(
            name = sample_index_name,
            description = 'Created with the Python sdk samples',
            fields = [id_field, title_field, desc_field, price_field, url_field, arbitrary_number_field, arbitrary_number_field])

    create_response = client.create_index(tenant_id, body=new_index, query_parameters=query_parameters)
    return create_response.indexes[0].id

def push_data(client, index_id, data):
    push_response = client.push_data_update(data, tenant_id, index_id, notransform=True, query_parameters={'appid' : app_id})

    return push_response.update_id

def get_search(client, index_id):

    response = client.search.get(tenant_id, index_id, q='Product', query_parameters={'appid' : app_id})

    return response.items.total_estimated_matches

def post_search(client, index_id):

    query = RequestQuery(
        filter = StringSetCondition(
            values = [ '1', '2'],
            field = 'ProductId'
        )
    )

    request = CommerceSearchPostRequest(
        query = query,
        items = RequestItems(
            select = [ '*' ]
        ),
        aggregations = [ RequestDiscoverFacets( name = "discovered facets" ) ]
    )

    response = client.search.post(tenant_id, index_id, request, query_parameters={'appid' : app_id})

    return response.items.total_estimated_matches

def to_csv(products):
    result = []
    for p in products:
        result.append(p['ProductId'] + ',' + p['ProductTitle'] + ',' + p['ProductDescription'] + ',' + str(p['ProductPrice']) + ',' + p['ArbitraryText'] + ',' + str(p['ArbitraryNumber']))

    return '\n'.join(result)


if __name__ == '__main__':

    print( 'Starting the sample, with app id: {0:s}'.format(app_id))

    creds = Authentication()

    print( 'Creating the ingestion client.')
    ingest_client = BingCommerceIngestion(creds)

    print( 'Creating the search client.')
    search_client = BingCommerceSearch(creds)

    index_id = ensure_index(ingest_client)
    print('working with index: {0:s}'.format(index_id))

    # push some data
    print('Pushing JSONArray data.')
    products = [
        { 'ProductId' : '1', 'ProductTitle': 'My First Product', 'ProductDescription' : 'the first product I have', 'ProductPrice': 100.0, 'ArbitraryText': 'random text', 'ArbitraryNumber' : 52.4},
        { 'ProductId' : '2', 'ProductTitle': 'My Second Product', 'ProductDescription' : 'the second product I have', 'ProductPrice': 10.0, 'ArbitraryText': ' another random text', 'ArbitraryNumber' : 88.8}
    ]
    push_data(ingest_client, index_id, json.dumps(products))

    print('Pushing ND-JSON data.')
    push_data(ingest_client, index_id, '\n'.join([ json.dumps(products[0]), json.dumps(products[1]) ]))

    print('Pushing CSV data.')
    push_data(ingest_client, index_id, to_csv(products))

    get_matches = get_search(search_client, index_id)
    print('found [{0:d}] matches with get search.'.format(get_matches))

    post_matches = post_search(search_client, index_id)
    print('found [{0:d}] matches with post search.'.format(post_matches))
