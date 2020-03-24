import os
from microsoft.bing.commerce.search import BingCommerceSearch
from microsoft.bing.commerce.search.models import CommerceSearchPostRequest, RequestQuery, RequestItems,RequestBingMatchStreams
from  microsoft.bing.commerce.search.models import ConditionBase,EquivalenceConditionBase,EquivalenceOperator
from microsoft.bing.commerce.search.models import ConditionBlock,LogicalOperator,StringCondition, RequestAggregationBase,RequestFacet,RequestRangeFacet,RequestDiscoverFacets
import microsoft.bing.commerce.search.operations
from msrest.authentication import BasicTokenAuthentication

def MatchAll():
    creds = BasicTokenAuthentication({ 'access_token': os.environ['SEARCH_TOKEN'] })
    client = BingCommerceSearch(creds)
    tenant_id = os.environ['SEARCH_TENANT']
    index_id = os.environ['SEARCH_INDEX']

    creds = BasicTokenAuthentication({ 'access_token': os.environ[SEARCH_TOKEN] })
    client = BingCommerceSearch(creds)
    tenant_id = os.environ[SEARCH_TENANT]
    index_id = os.environ[SEARCH_INDEX]

    request = CommerceSearchPostRequest(
        query = RequestQuery(match_all = 'diamond'),
        items = RequestItems(select = ['_itemId', 'name']))

    query_parameters = {}

    response = client.search.post(request, tenant_id, index_id, query_parameters)

    if response.items.total_estimated_matches > 0:
            for item in response.items.value:
                print(item.item_id)
                print(item.fields['name'])
                # Iterate Through Items to retrive selected Items

def MatchingSpecificFields():
        creds = BasicTokenAuthentication({ 'access_token': os.environ['SEARCH_TOKEN'] })
        client = BingCommerceSearch(creds)
        tenant_id = os.environ['SEARCH_TENANT']
        index_id = os.environ['SEARCH_INDEX']

        creds = BasicTokenAuthentication({ 'access_token': os.environ[SEARCH_TOKEN] })
        client = BingCommerceSearch(creds)
        tenant_id = os.environ[SEARCH_TENANT]
        index_id = os.environ[SEARCH_INDEX]

        request = CommerceSearchPostRequest(
            query = RequestQuery(Value=RequestBingMatchStreams(include=['Material'],value='suede')),
            items = RequestItems(select = ['title', 'description']))

        query_parameters = {}
        query_parameters['traffictype'] = 'test'

        response = client.search.post(request, tenant_id, index_id, query_parameters)

        if response.items.total_estimated_matches > 0:
            for item in response.items.value:
                print(item.fields['title'])
                # Iterate Through Items to retrive selected Items


def Filter():
        creds = BasicTokenAuthentication({ 'access_token': os.environ['SEARCH_TOKEN'] })
        client = BingCommerceSearch(creds)
        tenant_id = os.environ['SEARCH_TENANT']
        index_id = os.environ['SEARCH_INDEX']

        creds = BasicTokenAuthentication({ 'access_token': os.environ[SEARCH_TOKEN] })
        client = BingCommerceSearch(creds)
        tenant_id = os.environ[SEARCH_TENANT]
        index_id = os.environ[SEARCH_INDEX]

        request = CommerceSearchPostRequest(
            query = RequestQuery(match_all = 'laptop',filter=ConditionBase(field='brand',value='Microsoft',OperatorProperty=EquivalenceOperator.ne)),
            items = RequestItems(select = ['_itemId', 'brand','title']))

        query_parameters = {}

        response = client.search.post(request, tenant_id, index_id, query_parameters)
        
        if response.items.total_estimated_matches > 0:
            for item in response.items.value:
                print(item.item_id)
                print(item.fields['title'])
                # Iterate Through Items to retrive selected Items


def FilterConditionBlock():
        creds = BasicTokenAuthentication({ 'access_token': os.environ['SEARCH_TOKEN'] })
        client = BingCommerceSearch(creds)
        tenant_id = os.environ['SEARCH_TENANT']
        index_id = os.environ['SEARCH_INDEX']

        creds = BasicTokenAuthentication({ 'access_token': os.environ[SEARCH_TOKEN] })
        client = BingCommerceSearch(creds)
        tenant_id = os.environ[SEARCH_TENANT]
        index_id = os.environ[SEARCH_INDEX]
    
        request = CommerceSearchPostRequest(
            query = RequestQuery(match_all = 'laptop',
                                 filter=ConditionBlock(OperatorProperty=LogicalOperator.or_enum,
                                                       ConditionBase=StringCondition[StringCondition(Field='brand',value='HP'),
                                                                                     StringCondition(field='brand',value='HP')])),
            items = RequestItems(select = ['title','shortDescription']))
        
        query_parameters = {}

        response = client.search.post(request, tenant_id, index_id, query_parameters)

        if response.items.total_estimated_matches > 0:
            for item in response.items.value:
                print(item.fields['title'])
                # Iterate Through Items to retrive selected Items

def FacetingWithRangeInterval():
    creds = BasicTokenAuthentication({ 'access_token': os.environ['SEARCH_TOKEN'] })
    client = BingCommerceSearch(creds)
    tenant_id = os.environ['SEARCH_TENANT']
    index_id = os.environ['SEARCH_INDEX']

    creds = BasicTokenAuthentication({ 'access_token': os.environ[SEARCH_TOKEN] })
    client = BingCommerceSearch(creds)
    tenant_id = os.environ[SEARCH_TENANT]
    index_id = os.environ[SEARCH_INDEX]

    request = CommerceSearchPostRequest(
        query = RequestQuery(match_all = 'laptop'),
        items = RequestItems(select = ['_itemId', 'name'],top=5),
        aggregations=RequestAggregationBase[RequestRangeFacet(name='Name of Facet',field='Name of field on which faceting will be perormend',interval=500)])

    query_parameters = {}

    response = client.search.post(request, tenant_id, index_id, query_parameters)
    
    if response.items.total_estimated_matches > 0:
        for item in response.items.value:
            print(item.fields['name'])
                # Iterate Through Items to retrive selected Items

def DiscoverFacetsExclude():
    creds = BasicTokenAuthentication({ 'access_token': os.environ['SEARCH_TOKEN'] })
    client = BingCommerceSearch(creds)
    tenant_id = os.environ['SEARCH_TENANT']
    index_id = os.environ['SEARCH_INDEX']

    creds = BasicTokenAuthentication({ 'access_token': os.environ[SEARCH_TOKEN] })
    client = BingCommerceSearch(creds)
    tenant_id = os.environ[SEARCH_TENANT]
    index_id = os.environ[SEARCH_INDEX]

    request = CommerceSearchPostRequest(
        query = RequestQuery(match_all = 'laptop'),
        items = RequestItems(select = ['_itemId', 'name'],top=5),
        aggregations=RequestAggregationBase[RequestDiscoverFacets(include=[RequestFacet(field='productType')],exclude=['madeIn'])])

    query_parameters = {}

    response = client.search.post(request, tenant_id, index_id, query_parameters)

    if response.items.total_estimated_matches > 0:
        for item in response.items.value:
            print(item.item_id)
                # Iterate Through Items to retrive selected Items

def Faceting():
    creds = BasicTokenAuthentication({ 'access_token': os.environ['SEARCH_TOKEN'] })
    client = BingCommerceSearch(creds)
    tenant_id = os.environ['SEARCH_TENANT']
    index_id = os.environ['SEARCH_INDEX']

    creds = BasicTokenAuthentication({ 'access_token': os.environ[SEARCH_TOKEN] })
    client = BingCommerceSearch(creds)
    tenant_id = os.environ[SEARCH_TENANT]
    index_id = os.environ[SEARCH_INDEX]
    
    request = CommerceSearchPostRequest(
        query = RequestQuery(match_all = 'Your Search Item'),
        items = RequestItems(select = ['A comma - separated list of fields to return, Default is itemId'],top=5),
        aggregations=RequestAggregationBase[RequestDiscoverFacets(pin=[RequestFacet(field='Field Name')])])

    query_parameters = {}

    response = client.search.post(request, tenant_id, index_id, query_parameters)

    if response.items.total_estimated_matches > 0:
        for item in response.items.value:
            print(item.item_id)
                # Iterate Through Items to retrive selected Items


def Sorting():
    creds = BasicTokenAuthentication({ 'access_token': os.environ['SEARCH_TOKEN'] })
    client = BingCommerceSearch(creds)
    tenant_id = os.environ['SEARCH_TENANT']
    index_id = os.environ['SEARCH_INDEX']

    creds = BasicTokenAuthentication({ 'access_token': os.environ[SEARCH_TOKEN] })
    client = BingCommerceSearch(creds)
    tenant_id = os.environ[SEARCH_TENANT]
    index_id = os.environ[SEARCH_INDEX]

    request = CommerceSearchPostRequest(
        query = RequestQuery(match_all = 'headphones'),
        items = RequestItems(order_by='rating desc,baseRate',select = ['title', 'shortDescription']))

    query_parameters = {}

    response = client.search.post(request, tenant_id, index_id, query_parameters)
    
    if response.items.total_estimated_matches > 0:
        for item in response.items.value:
            print(item.fields['title'])
            # Iterate Through Items to retrive selected Items

def Paging():
    creds = BasicTokenAuthentication({ 'access_token': os.environ['SEARCH_TOKEN'] })
    client = BingCommerceSearch(creds)
    tenant_id = os.environ['SEARCH_TENANT']
    index_id = os.environ['SEARCH_INDEX']

    creds = BasicTokenAuthentication({ 'access_token': os.environ[SEARCH_TOKEN] })
    client = BingCommerceSearch(creds)
    tenant_id = os.environ[SEARCH_TENANT]
    index_id = os.environ[SEARCH_INDEX]

    request = CommerceSearchPostRequest(
        query = RequestQuery(match_all = 'headphones'),
        items = RequestItems(select = ['title', 'shortDescription'],top=10,skip=10))

    query_parameters = {}

    response = client.search.post(request, tenant_id, index_id, query_parameters)

    if response.items.total_estimated_matches > 0:
        for item in response.items.value:
            print(item.fields['title'])
                # Iterate Through Items to retrive selected Items


def GetPaging():
    creds = BasicTokenAuthentication({ 'access_token': os.environ['SEARCH_TOKEN'] })
    client = BingCommerceSearch(creds)
    tenant_id = os.environ['SEARCH_TENANT']
    index_id = os.environ['SEARCH_INDEX']

    creds = BasicTokenAuthentication({ 'access_token': os.environ[SEARCH_TOKEN] })
    client = BingCommerceSearch(creds)
    tenant_id = os.environ[SEARCH_TENANT]
    index_id = os.environ[SEARCH_INDEX]


    response = client.search.get('headphones', tenant_id, index_id, mkt=None, setlang=None,select='title,brand', orderby= None, top=2, skip= 10)
 
    if response.items.total_estimated_matches > 0:
        for item in response.items.value:
            print(item.fields['title'])
                # Iterate Through Items to retrive selected Items

def GetSearch():
    creds = BasicTokenAuthentication({ 'access_token': os.environ['SEARCH_TOKEN'] })
    client = BingCommerceSearch(creds)
    tenant_id = os.environ['SEARCH_TENANT']
    index_id = os.environ['SEARCH_INDEX']

    creds = BasicTokenAuthentication({ 'access_token': os.environ[SEARCH_TOKEN] })
    client = BingCommerceSearch(creds)
    tenant_id = os.environ[SEARCH_TENANT]
    index_id = os.environ[SEARCH_INDEX]

    response = client.search.get('rugs', tenant_id,index_id, mkt= None,setlang=None, select= 'title,brand', orderby=None, top= 20, skip= 10)
    if response.items.total_estimated_matches > 0:
        for item in response.items.value:
            print(item.fields['title'])
            # Iterate Through Items to retrive selected Items
