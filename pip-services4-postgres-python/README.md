# <img src="https://uploads-ssl.webflow.com/5ea5d3315186cf5ec60c3ee4/5edf1c94ce4c859f2b188094_logo.svg" alt="Pip.Services Logo" width="200"> <br/> PostgreSQL components for Python

This module is a part of the [Pip.Services](http://pipservices.org) polyglot microservices toolkit. It provides a set of components to implement PostgreSQL persistence.

The module contains the following packages:
- **Build** - Factory to create PostreSQL persistence components.
- **Connect** - Connection component to configure PostgreSQL connection to database.
- **Persistence** - abstract persistence components to perform basic CRUD operations.

<a name="links"></a> Quick links:

* [Configuration](http://docs.pipservices.org/v4/tutorials/beginner_tutorials/configuration/)
* [API Reference](https://pip-services4-python.github.io/pip-services4-postgres-python/)
* [Change Log](CHANGELOG.md)
* [Get Help](http://docs.pipservices.org/v4/get_help/)
* [Contribute](http://docs.pipservices.org/v4/contribute/)

## Use

Install the Python package as
```bash
pip install pip-services4-postgres
```

As an example, lets create persistence for the following data object.

```python

class MyObject(IStringIdentifiable):
    def __init__(self, id=None, key=None, content=None):
        self.id = id
        self.key = key
        self.content = content
```

The persistence component shall implement the following interface with a basic set of CRUD operations.

```python
class IMyPersistence(ABC):
    def get_page_by_filter(self, context: Optional[IContext], filter: Union[FilterParams, None],
                           paging: Union[PagingParams, None]) -> DataPage:
        raise NotImplemented()

    def get_one_by_id(self, context: Optional[IContext], id: str) -> MyObject:
        raise NotImplemented()

    def get_one_by_key(self, context: Optional[IContext], key: List[str]) -> MyObject:
        raise NotImplemented()

    def create(self, context: Optional[IContext], item: MyObject) -> MyObject:
        raise NotImplemented()

    def update(self, context: Optional[IContext], item: MyObject) -> MyObject:
        raise NotImplemented()

    def delete_by_id(self, context: Optional[IContext], id: str):
        raise NotImplemented()
```

To implement postgresql persistence component you shall inherit `IdentifiablePostgresPersistence`. 
Most CRUD operations will come from the base class. You only need to override `get_page_by_filter` method with a custom filter function.
And implement a `get_one_by_key` custom persistence method that doesn't exist in the base class.

```python
class MyPostgresPersistence(IdentifablePostgresPersistence):
    def __init__(self):
        super(MyPostgresPersistence, self).__init__('myobjects')
        self._auto_create_object("CREATE TABLE myobjects (id VARCHAR(32) PRIMARY KEY, key VARCHAR(50), value VARCH(255)")
        self._ensure_index("myobjects_key", { 'key': 1 }, { 'unique': True })

    def __compose_filter(self, filter):
        filter = filter or FilterParams()

        criteria = []

        id = filter.get_as_nullable_string('id')
        if id is not None:
            criteria.append("id='" + id + "'")

        temp_ids = filter.get_as_nullable_string('ids')
        if temp_ids is not None:
            ids = temp_ids.split(',')
            criteria.append("id IN ('" + "','".join(ids) + "')")

        key = filter.get_as_nullable_string('key')
        if key is not None:
            criteria.append("key='" + key + "'")

        return " AND ".join(criteria) if len(criteria) > 0 else None

    def get_page_by_filter(self, context, filter, paging, sort, select):
        return super().get_page_by_filter(context, self.__compose_filter(filter), paging, 'id', None)

    def get_one_by_key(self, context, key):
        query = "SELECT * FROM " + self._quoted_table_name() + " WHERE \"key\"=%s"
        params = [key]

        result = self._request(query, params)
        item = result[0] or None if result and result[0] else None

        if item is None:
            self._logger.trace(context, "Nothing found from %s with key = %s", self._table_name, key)
        else:
            self._logger.trace(context, "Retrieved from %s with key = %s", self._table_name, key)

        item = self._convert_to_public(item)

        return item
```

Alternatively you can store data in non-relational format using `IdentificableJsonPostgresPersistence`.
It stores data in tables with two columns - `id` with unique object id and `data` with object data serialized as JSON.
To access data fields you shall use `data->'field'` expression or `data->>'field'` expression for string values.

```python
from pip_services4_postgres.persistence.IdentifiableJsonPostgresPersistence import IdentifiableJsonPostgresPersistence


class MyPostgresPersistence(IdentifableJsonPostgresPersistence):
    def __init__(self):
        super(MyPostgresPersistence, self).__init__('myobjects')
        self._ensure_table("VARCHAR(32)", "JSONB")
        self._ensure_index("myobjects_key", { "data->>'key'": 1 }, { 'unique': True })

    def __compose_filter(self, filter):
        filter = filter or FilterParams()

        criteria = []

        id = filter.get_as_nullable_string('id')
        if id is not None:
            criteria.append("data->>'id'='" + id + "'")

        temp_ids = filter.get_as_nullable_string('ids')
        if temp_ids is not None:
            ids = temp_ids.split(',')
            criteria.append("data->>'id' IN ('" + "','".join(ids) + "')")

        key = filter.get_as_nullable_string('key')
        if key is not None:
            criteria.append("data->>'key'='" + key + "'")

        return " AND ".join(criteria) if len(criteria) > 0 else None

    def get_page_by_filter(self, context, filter, paging, sort, select):
        return super().get_page_by_filter(context, self.__compose_filter(filter), paging, 'id', None)

    def get_one_by_key(self, context, key):
        query = "SELECT * FROM " + self._quoted_table_name() + " WHERE data->>'key'=%s"
        params = [key]

        result = self._request(query, params)
        item = result[0] or None if result and result[0] else None

        if item is None:
            self._logger.trace(context, "Nothing found from %s with key = %s", self._table_name, key)
        else:
            self._logger.trace(context, "Retrieved from %s with key = %s", self._table_name, key)

        item = self._convert_to_public(item)

        return item
```

Configuration for your microservice that includes postgresql persistence may look the following way.

```yaml
...
{{#if POSTGRES_ENABLED}}
- descriptor: pip-services:connection:postgres:con1:1.0
  connection:
    uri: {{{POSTGRES_SERVICE_URI}}}
    host: {{{POSTGRES_SERVICE_HOST}}}{{#unless POSTGRES_SERVICE_HOST}}localhost{{/unless}}
    port: {{POSTGRES_SERVICE_PORT}}{{#unless POSTGRES_SERVICE_PORT}}5432{{/unless}}
    database: {{POSTGRES_DB}}{{#unless POSTGRES_DB}}app{{/unless}}
  credential:
    username: {{POSTGRES_USER}}
    password: {{POSTGRES_PASS}}
    
- descriptor: myservice:persistence:postgres:default:1.0
  dependencies:
    connection: pip-services:connection:postgres:con1:1.0
  table: {{POSTGRES_TABLE}}{{#unless POSTGRES_TABLE}}myobjects{{/unless}}
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

The library is created and maintained by:
- **Sergey Seroukhov**
- **Danil Prisiazhnyi**

The documentation is written by **Mark Makarychev**.