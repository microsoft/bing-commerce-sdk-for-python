import os
from microsoft.bing.commerce.search import BingCommerceSearch
from microsoft.bing.commerce.search.models import CommerceSearchPostRequest, RequestQuery, RequestItems,RequestBingMatchStreams
from  microsoft.bing.commerce.search.models import ConditionBase,EquivalenceConditionBase,EquivalenceOperator
from microsoft.bing.commerce.search.models import ConditionBlock,LogicalOperator,StringCondition, RequestAggregationBase,RequestFacet,RequestRangeFacet,RequestDiscoverFacets
from microsoft.bing.commerce.search.models import BoostExpression
import microsoft.bing.commerce.search.operations
from msrest.authentication import BasicTokenAuthentication

def MatchAll():
    creds = BasicTokenAuthentication({ 'access_token': os.environ['SEARCH_TOKEN'] })
    client = BingCommerceSearch(creds)
    tenant_id = os.environ['SEARCH_TENANT']
    index_id = os.environ['SEARCH_INDEX']
    
    #Constructs the Request Query.
    #Specify list of fields to return
    request = CommerceSearchPostRequest(
        query = RequestQuery(match_all = 'diamond'),
        items = RequestItems(select = ['_itemId', 'name']))
    
    response = client.search.post(request, tenant_id, index_id)

    if response.items.total_estimated_matches > 0:
        for item in response.items.value:
            print(item.item_id)
            print(item.fields['name'])

#During the ingestion process of your catalog, you defined specific fields to make searchable.
#Bing exposes these fields for matching operations. 
#For more information, see the Bing Retail Search Ingestion API guide.
#Matching enables you to define specific fields to query. 
#The default matchAll or Match type matches against all searchable fields
def MatchingSpecificFields():
    creds = BasicTokenAuthentication({ 'access_token': os.environ['SEARCH_TOKEN'] })
    client = BingCommerceSearch(creds)
    tenant_id = os.environ['SEARCH_TENANT']
    index_id = os.environ['SEARCH_INDEX']
    
    request = CommerceSearchPostRequest(
        query = RequestQuery(
            Value=RequestBingMatchStreams(
                include=['Material'],value='suede')),
        items = RequestItems(select = ['title', 'description']))
    
    response = client.search.post(request, tenant_id, index_id)
    
    if response.items.total_estimated_matches > 0:
        for item in response.items.value:
            print(item.fields['title'])

#Filtering is a non-ranking type of query with the single purpose of excluding items from query results.
#It answers the question of exclusion with various operators such as lesser than, greater than, equality etc
def Filter():
    creds = BasicTokenAuthentication({ 'access_token': os.environ['SEARCH_TOKEN'] })
    client = BingCommerceSearch(creds)
    tenant_id = os.environ['SEARCH_TENANT']
    index_id = os.environ['SEARCH_INDEX']
    
    request = CommerceSearchPostRequest(
        query = RequestQuery(
            match_all = 'laptop',
            filter=ConditionBase(
                field='brand',
                value='Microsoft',
                OperatorProperty=EquivalenceOperator.ne)),
        items = RequestItems(select = ['_itemId', 'brand','title']))
    
    response = client.search.post(request, tenant_id, index_id)
    
    if response.items.total_estimated_matches > 0:
        for item in response.items.value:
            print(item.item_id)
            print(item.fields['title'])

#Filtering is a non-ranking type of query with the single purpose of excluding items from query results.
#The following example shows a filter condition block.
#It answers the question of exclusion with various operators such as lesser than, greater than, equality etc
def FilterConditionBlock():
    creds = BasicTokenAuthentication({ 'access_token': os.environ['SEARCH_TOKEN'] })
    client = BingCommerceSearch(creds)
    tenant_id = os.environ['SEARCH_TENANT']
    index_id = os.environ['SEARCH_INDEX']
    request = CommerceSearchPostRequest(
        query = RequestQuery(
            match_all = 'laptop',
            filter=ConditionBlock(
                OperatorProperty=LogicalOperator.or_enum,
                ConditionBase=StringCondition
                [
                    StringCondition(field='brand',value='HP'),
                    StringCondition(field='brand',value='HP')
                ])),
        items = RequestItems(select = ['title','shortDescription']))
    
    response = client.search.post(request, tenant_id, index_id, query_parameters)
    if response.items.total_estimated_matches > 0:
        for item in response.items.value:
            print(item.fields['title'])

#Faceting is a search technique that breaks up search results into multiple categories,
#often showing the counts of each one. 
#Faceting with Range interval allows faceting on a user defined interval
def FacetingWithRangeInterval():
    creds = BasicTokenAuthentication({ 'access_token': os.environ['SEARCH_TOKEN'] })
    client = BingCommerceSearch(creds)
    tenant_id = os.environ['SEARCH_TENANT']
    index_id = os.environ['SEARCH_INDEX']

    request = CommerceSearchPostRequest(
        query = RequestQuery(match_all = 'laptop'),
        items = RequestItems(
            select = ['_itemId', 'name'],
            top=5),
        aggregations=RequestAggregationBase[
            RequestRangeFacet(
                name='Name of Facet',
                field='Name of field on which faceting will be perormend',
                interval=500)])
    
    response = client.search.post(request, tenant_id, index_id)
    
    if response.items.total_estimated_matches > 0:
        for item in response.items.value:
            print(item.fields['name'])

#Faceting is a search technique that breaks up search results into multiple categories,
#often showing the counts of each one. 
#Faceting with Range interval allows faceting on a user defined interval
def DiscoverFacetsExclude():
    creds = BasicTokenAuthentication({ 'access_token': os.environ['SEARCH_TOKEN'] })
    client = BingCommerceSearch(creds)
    tenant_id = os.environ['SEARCH_TENANT']
    index_id = os.environ['SEARCH_INDEX']
    
    request = CommerceSearchPostRequest(
        query = RequestQuery(match_all = 'laptop'),
        items = RequestItems(select = ['_itemId', 'name'],top=5),
        aggregations=RequestAggregationBase[
            RequestDiscoverFacets(
                include=[
                    RequestFacet(field='productType')
                    ],
                exclude=['madeIn'])])
    
    response = client.search.post(request, tenant_id, index_id)
    
    if response.items.total_estimated_matches > 0:
        for item in response.items.value:
            print(item.item_id)

#Faceting is a search technique that breaks up search results into multiple categories,
#often showing the counts of each one. 
#The following example shows a request for discover facets with the category facet pinned to the top position
#of the list of discovered facets.
def DiscoverFacetsPin():
    creds = BasicTokenAuthentication({ 'access_token': os.environ['SEARCH_TOKEN'] })
    client = BingCommerceSearch(creds)
    tenant_id = os.environ['SEARCH_TENANT']
    index_id = os.environ['SEARCH_INDEX']
    
    request = CommerceSearchPostRequest(
        query = RequestQuery(match_all = 'Your Search Item'),
        items = RequestItems(
            select = ['A comma - separated list of fields to return, Default is itemId'],
            top=5),
        aggregations=RequestAggregationBase[
            RequestDiscoverFacets(
                pin=[RequestFacet(
                    field='Field Name')
                     ]
                )])
    
    response = client.search.post(request, tenant_id, index_id)
    
    if response.items.total_estimated_matches > 0:
        for item in response.items.value:
            print(item.item_id)

#By default, Bing sorts the list of items by best match.
#As an alternative, you can include the sortBy query parameter in a GET request to sort by a specific item field.
#Possible values are asc (ascending) and desc (descending).
def Sorting():
    creds = BasicTokenAuthentication({ 'access_token': os.environ['SEARCH_TOKEN'] })
    client = BingCommerceSearch(creds)
    tenant_id = os.environ['SEARCH_TENANT']
    index_id = os.environ['SEARCH_INDEX']
    
    request = CommerceSearchPostRequest(
        query = RequestQuery(match_all = 'headphones'),
        items = RequestItems(
            order_by='rating desc,baseRate',
            select = ['title', 'shortDescription']
            ))
    
    response = client.search.post(request, tenant_id, index_id)
    
    if response.items.total_estimated_matches > 0:
        for item in response.items.value:
            print(item.fields['title'])

#By default, Bing returns 24 items per request. 
#To change this number, use the top query parameter to specify a number result of results per request.
# There is no limit on the page size, but maximum of 1000 results can be obtained.       
def Paging():
    creds = BasicTokenAuthentication({ 'access_token': os.environ['SEARCH_TOKEN'] })
    client = BingCommerceSearch(creds)
    tenant_id = os.environ['SEARCH_TENANT']
    index_id = os.environ['SEARCH_INDEX']
    
    request = CommerceSearchPostRequest(
        query = RequestQuery(match_all = 'headphones'),
        items = RequestItems(
            select = ['title', 'shortDescription'],
            top=10,
            skip=10))
    
    response = client.search.post(request, tenant_id, index_id)
    
    if response.items.total_estimated_matches > 0:
        for item in response.items.value:
            print(item.fields['title'])

#By default, Bing returns 24 items per request.
# To change this number, use the top query parameter to s
#specify a number resul of results per request. 
#There is no limit on the page size, but maximum of 1000 results can be obtained.      
def GetPaging():
    creds = BasicTokenAuthentication({ 'access_token': os.environ['SEARCH_TOKEN'] })
    client = BingCommerceSearch(creds)
    tenant_id = os.environ['SEARCH_TENANT']
    index_id = os.environ['SEARCH_INDEX']
    
    response = client.search.get('headphones', tenant_id, index_id,
                                 mkt=None, 
                                 setlang=None,
                                 select='title,brand',
                                 orderby= None,
                                 top=2,
                                 skip= 10)
    
    if response.items.total_estimated_matches > 0:
        for item in response.items.value:
            print(item.fields['title'])

#GET requests can search an index using only URL parameters.
#Only limited request options are available. 
#GET requests will always do simple item search and support
#only a default facet discovery aggregation.
def GetSearch():
    creds = BasicTokenAuthentication({ 'access_token': os.environ['SEARCH_TOKEN'] })
    client = BingCommerceSearch(creds)
    tenant_id = os.environ['SEARCH_TENANT']
    index_id = os.environ['SEARCH_INDEX']
    
    response = client.search.get('rugs', tenant_id,index_id,
                                mkt= None,
                                setlang=None,
                                select= 'title,brand',
                                orderby=None,
                                top= 20,
                                skip= 10)
    if response.items.total_estimated_matches > 0:
        for item in response.items.value:
            print(item.fields['title'])

def BoostingAndBurrying():
    creds = BasicTokenAuthentication({ 'access_token': os.environ['SEARCH_TOKEN'] })
    client = BingCommerceSearch(creds)
    tenant_id = os.environ['SEARCH_TENANT']
    index_id = os.environ['SEARCH_INDEX']
    request = CommerceSearchPostRequest(
        query = RequestQuery(
            MatchAll='laptop',
            boosts=[BoostExpression(boost=100,condition=StringCondition(field='brand',value='Microsoft')),
                    BoostExpression(boost=-5,condition=StringCondition(field='brand',value='Northwind'))],
            items = RequestItems(select = ['_score', 'brand', 'title'],top=10)))

    response = client.search.post(request, tenant_id, index_id)
    if response.items.total_estimated_matches > 0:
        for item in response.items.value:
            print(item.fields['title'])
