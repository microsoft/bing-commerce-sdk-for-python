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
    query_parameters['traffictype'] = 'test'

    response = client.search.post(request, tenant_id, index_id, query_parameters)

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
        query = RequestQuery(match_all = 'laptop',filter=ConditionBase(Field='brand',value='Microsoft',OperatorProperty=EquivalenceOperator.ne)), 
        items = RequestItems(select = ['_itemId', 'brand','title']))

        query_parameters = {}
        query_parameters['traffictype'] = 'test'

        response = client.search.post(request, tenant_id, index_id, query_parameters)

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
        query = RequestQuery(match_all = 'laptop',filter=ConditionBlock(OperatorProperty=LogicalOperator.or_enum, ConditionBase=StringCondition[StringCondition(Field='brand',value='HP'),StringCondition(Field='brand',value='HP')])), 
        items = RequestItems(select = ['title','shortDescription']))
        
        query_parameters = {}
        query_parameters['traffictype'] = 'test'

        response = client.search.post(request, tenant_id, index_id, query_parameters)

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
        query = RequestQuery(match_all = 'laptop'), 
        items = RequestItems(select = ['_itemId', 'name'],top=5),
        aggregations=RequestAggregationBase[RequestFacet(name='Name of Facet',field='Name of field on which faceting will be perormend')])

        query_parameters = {}
        query_parameters['traffictype'] = 'test'

        response = client.search.post(request, tenant_id, index_id, query_parameters)

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
    query_parameters['traffictype'] = 'test'

    response = client.search.post(request, tenant_id, index_id, query_parameters)

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
    query_parameters['traffictype'] = 'test'

    response = client.search.post(request, tenant_id, index_id, query_parameters)

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
    query_parameters['traffictype'] = 'test'

    response = client.search.post(request, tenant_id, index_id, query_parameters)


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
    query_parameters['traffictype'] = 'test'

    response = client.search.post(request, tenant_id, index_id, query_parameters)

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
    query_parameters['traffictype'] = 'test'

    response = client.search.post(request, tenant_id, index_id, query_parameters)


def GetPaging():
    creds = BasicTokenAuthentication({ 'access_token': os.environ['SEARCH_TOKEN'] })
    client = BingCommerceSearch(creds)
    tenant_id = os.environ['SEARCH_TENANT']
    index_id = os.environ['SEARCH_INDEX']

    creds = BasicTokenAuthentication({ 'access_token': os.environ[SEARCH_TOKEN] })
    client = BingCommerceSearch(creds)
    tenant_id = os.environ[SEARCH_TENANT]
    index_id = os.environ[SEARCH_INDEX]
    
    response = client.search.get('headphones', tenant_id,index_id, null, null, 'title,brand', null, 2, 10)

def GetSearch():
    creds = BasicTokenAuthentication({ 'access_token': os.environ['SEARCH_TOKEN'] })
    client = BingCommerceSearch(creds)
    tenant_id = os.environ['SEARCH_TENANT']
    index_id = os.environ['SEARCH_INDEX']

    creds = BasicTokenAuthentication({ 'access_token': os.environ[SEARCH_TOKEN] })
    client = BingCommerceSearch(creds)
    tenant_id = os.environ[SEARCH_TENANT]
    index_id = os.environ[SEARCH_INDEX]

    response = client.search.get('rugs', tenant_id,index_id, null, null, 'title,brand', null, 20, 10)
