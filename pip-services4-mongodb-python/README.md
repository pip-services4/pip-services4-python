# <img src="https://uploads-ssl.webflow.com/5ea5d3315186cf5ec60c3ee4/5edf1c94ce4c859f2b188094_logo.svg" alt="Pip.Services Logo" width="200"> <br/> MongoDB components for Python

This module is a part of the [Pip.Services](http://pipservices.org) polyglot microservices toolkit.

The MongoDB module simplifies how we work with Mongo databases and contains everything you need to start working with MongoDB.

The module contains the following packages:
- **Build** - contains a factory for creating MongoDB persistence components.
- **Connect** - instruments for configuring connections to the database. The component receives a set of configuration parameters and uses them to generate all necessary database connection parameters.
- **Persistence** - abstract classes for working with the database that can be used for connecting to collections and performing basic CRUD operations.

<a name="links"></a> Quick links:

* [MongoDB persistence](https://www.pipservices.org/recipies/mongodb-persistence)
* [Configuration](http://docs.pipservices.org/v4/tutorials/beginner_tutorials/configuration/)
* [API Reference](https://pip-services4-python.github.io/pip-services4-mongodb-python/index.html)
* [Change Log](CHANGELOG.md)
* [Get Help](http://docs.pipservices.org/v4/get_help/)
* [Contribute](http://docs.pipservices.org/v4/contribute/)

## Use

Install the Python package as
```bash
pip install pip-services4-mongodb
```

As an example, lets create persistence for the following data object.

```python
class Dummy(IStringIdentifiable):
    def __init__(self, id: str = None, key: str = None, content: str = None):
        self.id = id
        self.key = key
        self.content = content


```

The persistence component shall implement the following interface with a basic set of CRUD operations.

```python
class IMyPersistence:

    def get_page_by_filter(self, context: Optional[IContext], filter: FilterParams, paging: PagingParams) -> DataPage:
        pass

    def get_one_by_id(self, context: Optional[IContext], id: str) -> T:
        pass

    def get_one_by_key(self, context: Optional[IContext], key: str) -> T:
        pass

    def create(self, context: Optional[IContext], item: T)-> T:
        pass

    def update(self, context: Optional[IContext], item: T)-> T:
        pass

    def delete_by_id(self, context: Optional[IContext], id: str) -> T:
        pass
```

To implement mongodb persistence component you shall inherit `IdentifiableMongoDbPersistence`. 
Most CRUD operations will come from the base class. You only need to override `get_page_by_filter` method with a custom filter function.
And implement a `get_one_by_key` custom persistence method that doesn't exist in the base class.

```python
class MyMongoDbPersistence(IdentifiableMongoDbPersistence):
    def __init__(self):
        super(MyMongoDbPersistence, self).__init__('myobjects')

    def __composeFilter(self, filterr):
        filterr = filterr or FilterParams()
        id = filterr.get_as_nullable_string("id")
        if id:
            filterr.update({'_id': id})
        temp_ids = filterr.get_as_nullable_string("ids")
        if temp_ids:
            ids = temp_ids.split(",")
            filterr.update({'_id': {'$in': ids}})
        ids = temp_ids.split(",") if temp_ids is not None else None
        if ids:
            filterr.update({'_id': {'$in': ids}})
        key = filterr.get_as_nullable_string("key")

        if key:
            filterr.update({'key': key})

        if len(filterr) > 0:
            return {'$and': filterr}
        else:
            return None

    def get_page_by_filter(self, context, filter, paging, sort=None, select=None):
        return super().get_page_by_filter(context, filter, paging, '_id', select)

    def get_one_by_key(self, context, key):

        filterr = {'key': key}
        item = self._collection.find_one(filterr)
        if item:
            self._logger.trace(context, "Retrieved from {} with key = {}", self._collection_name, key)
            item = self._convert_to_public(item)
            return item
        else:
            self._logger.trace(context, "Nothing found from {} with key = {}", self._collection_name, key)
```

Configuration for your microservice that includes mongodb persistence may look the following way.

```yaml
...
{{#if MONGODB_ENABLED}}
- descriptor: pip-services:connection:mongodb:con1:1.0
  collection: {{MONGO_COLLECTION}}{{#unless MONGO_COLLECTION}}myobjects{{/unless}}
  connection:
    uri: {{{MONGO_SERVICE_URI}}}
    host: {{{MONGO_SERVICE_HOST}}}{{#unless MONGO_SERVICE_HOST}}localhost{{/unless}}
    port: {{MONGO_SERVICE_PORT}}{{#unless MONGO_SERVICE_PORT}}27017{{/unless}}
    database: {{MONGO_DB}}{{#unless MONGO_DB}}app{{/unless}}
  credential:
    username: {{MONGO_USER}}
    password: {{MONGO_PASS}}
    
- descriptor: myservice:persistence:mongodb:default:1.0
  dependencies:
    connection: pip-services:connection:mongodb:con1:1.0
{{/if}}
...
```

## Develop

For development you shall install the following prerequisites:
* Python 3.7+
* Visual Studio Code or another IDE of your choice
* Docker

Install dependencies:
```bash
pip install -r requirements.txt
```

Run automated tests:
```bash
python test.py
```

Generate API documentation:
```bash
./docgen.ps1
```

Before committing changes run dockerized build and test as:
```bash
./build.ps1
./test.ps1
./clear.ps1
```

## Contacts

The Python version of Pip.Services is created and maintained by **Sergey Seroukhov**