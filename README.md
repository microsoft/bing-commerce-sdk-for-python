
# Bing for Commerce Python SDK

## Overview

This contains the generated SDKs that can help developers integrate with Bing for Commerce platform, both on the Search and Ingestion sides. The repository also contains unit tests and samples that can show you quick examples for how to use the SDKs.

For more details about the project, please refer to the [Bing for Commerce main repository](https://github.com/microsoft/bing-commerce), or [Bing for Commerce API Documentation](https://commerce.bing.com/docs/product-search/).

## Getting Started

### Prerequisites

* Python 2.7, or 3.5 or later is required to use this package.
* [Bing for Commerce Account](https://commerce.bing.com/).

### Install the package

Coming soon.

### Authenticate the client

Bing for Commerce APIs use Bearer Tokens for authentication. You can use the [Bing for Commerce Portal Documentation](https://commerce.bing.com/docs/Portal%20Documentation/#manage-keys-and-tokens) for help creating one.

## Usage

### Imports

You will need to add imports for the required implementation as part of the sdk, besides any other dependencies needed.

#### Ingestion imports:
~~~python
from microsoft.bing.commerce.ingestion import BingCommerceIngestion
import microsoft.bing.commerce.ingestion.models
~~~

#### Search imports:
~~~python
from microsoft.bing.commerce.search import BingCommerceSearch
import microsoft.bing.commerce.search.models
import microsoft.bing.commerce.search.operations
~~~

### Create the SDK client object

Creating the SDK client object SDK are the first step you need to do in order to call the Bing for Commerce services APis. You will need first to get an access token with the proper access scope as described [here](https://commerce.bing.com/docs/Portal%20Documentation/#manage-keys-and-tokens).

#### Create the Ingestion SDK Client
~~~python
def create_ingestion_client():
    creds = BasicTokenAuthentication({ 'access_token': access_token })
    ingest_client = BingCommerceIngestion(creds)
    return ingest_client
~~~

#### Create the Search SDK Client
~~~python
def create_search_client():
    creds = BasicTokenAuthentication({ 'access_token': access_token })
    search_client = BingCommerceSearch(creds)
    return search_client
~~~
### Manage your Index

You can create and manage you index using the Bing for Commerce portal. However, you could also use the SDK to manage your indexes.

#### Create an index
~~~python
def ensure_index(ingestion_client, tenant_id, index_name):

    id_field = IndexField(
            name = 'ProductId',
            type = IndexFieldType.product_id, # Exactly one Product Id field is required while creating an index.
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

    new_index = Index(
            name = index_name,
            description = 'my sample index',
            fields = [id_field, title_field, desc_field])

    create_response = ingestion_client.create_index(tenant_id, body=new_index)
    return create_response.indexes[0]
~~~

#### Get all indexes
~~~python
all_indexes =  ingestion_client.get_all_indexes(tenant_id);
~~~

#### Get an index by Id
~~~python
var myIndex = ingestion_client.get_index(tenant_i_d, index_id);
~~~

### Pushing data

The APIs to push data to Bing for Commerce are asynchronous, where the service / SDK contains two separate APIs to serve this, one for the push itself, and another to track down the status.

The content that you will be pushing to your index catalog needs to match the index configuration that you have the index created with, and it can be in any of the following formats:
* JSon Array.
* ND-JSon (New-Line Delimited JSon).
* CSV.
* TSV.

Please note however that if you have a transformation config added to your index, the format of the pushed data needs to match that of what your transformation script is expecting.

#### Push Data
~~~python
def push_data(ingestion_client, tenant_id, index_id, content):
    push_response = ingestion_client.push_data_update(content, tenant_id, index_id)
    return push_response.update_id
~~~

#### Push Data Status
~~~python
def push_data_status(ingestion_client, tenant_id, index_id, push_data_update_id):
    push_response = ingestion_client.push_data_status(tenant_id, index_id, push_data_update_id)

    # returns the overall status for the push call.
    #
    # You can get the status for each record being updated by accessing status.records list.
    return push_response.status
~~~

### Search Query

You can use the Search SDK to do queries on your Bing for Commerce indexes given that you have an access token with the proper scope. 

#### Simple Search Query
There are few cusomizations that you can still apply to the simple search query api by providing different values for different API arguments (like: market, language, field select, order configuration, pagination, facet discovery and query alteration toggle).
~~~python
def simple_search(search_client, tenant_id, index_id, query_term):
    response = search_client.search.get(query_term, tenant_id, index_id)
    return response.items
~~~

#### Advanced Search Query
You can do a lot more customization (like filering, boosting, ...etc) to your advanced search query by providing a detailed search query description for how you want your results to be.
~~~python
def advanced_search(search_client, tenant_id, index_id):
    
    # Prepare the Search request.
    request = CommerceSearchPostRequest(
        query = RequestQuery(
            filter = StringSetCondition(
                values = [ '1', '2'],
                field = 'ProductId'
            )
        ),
        items = RequestItems(
            select = [ '*' ]
        ),
        aggregations = [ RequestDiscoverFacets( name = "discovered facets" ) ]
    )

    # Send the search request
    response = search_client.search.post(request, tenant_id, index_id)

    return response.items
~~~

### Transformation Script Management
You can upload a custom configuration that you might need applied to the data you push to your index automatically. Please refer to the [Bing for Commerce docs](https://commerce.bing.com/docs/product-search/#transformation-script-management-api) for more details about how to create a valid transformation config.

#### Create or Update the transformation config
~~~python
my_script = get_my_transformation_script()
create_script_response = ingestion_client.create_or_update_transformation_config(my_script, tenant_id, index_id)
~~~

#### Get the existing tranformation config
~~~python
# Note that the getTransformationConfig will throw a 400 Bad Request if your index doesn't have a transformation config.
read_script_response = ingestion_client.get_transformation_config(tenant_id, index_id)
myScript = read_script_response.value
~~~

#### Delete the transformation config
~~~python
delete_script_response = ingestion_client.delete_transformation_config(tenant_id, index_id);
~~~

### Transformation Script Tryout
Before you associate a transformation script to your index, you can use the transformation tryout apis to make sure that your index works with your data and the SDK before actually associating it to your index.

#### Upload a tranformation config tryout
~~~python
def upload_transformation_tryout(ingestion_client, script):
    create_script_response = ingestion_client.upload_try_out_config(script)
    return create_script_response.try_out_id
~~~

#### Test the transformation config tryout
~~~python
def execute_transformation_tryout(ingestion_client, data, try_out_id):
    execute_response = ingestion_client.execute_try_out_config(data, try_out_id)
    return execute_response.status == 'Succeeded'
~~~

## Samples

Please take a look at the [sample](./samples/) for a quick example for how to use the SDK in order to manage your indexes, push data to your index catalog and perform search queries on your data.


## Contributing

For details on contributing to this repository, see the [contributing guide](./CONTRIBUTING.md).

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
