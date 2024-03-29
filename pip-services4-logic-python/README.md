# <img src="https://uploads-ssl.webflow.com/5ea5d3315186cf5ec60c3ee4/5edf1c94ce4c859f2b188094_logo.svg" alt="Pip.Services Logo" width="200"> <br/> Business Logic Components for Python

This module is a part of the [Pip.Services](http://pipservices.org) polyglot microservices toolkit.

The Logic module contains standard component definitions to handle complex business transactions.

The module contains the following packages:
- **Cache** - distributed cache
- **Lock** -  distributed lock components
- **State** -  distributed state management components

<a name="links"></a> Quick links:

* [Logging](http://docs.pipservices.org/v4/tutorials/beginner_tutorials/observability/logging/)
* [Configuration](http://docs.pipservices.org/v4/tutorials/beginner_tutorials/configuration/) 
* [API Reference](https://pip-services4-python.github.io/pip-services4-logic-python/index.html)
* [Change Log](CHANGELOG.md)
* [Get Help](http://docs.pipservices.org/v4/get_help/)
* [Contribute](http://docs.pipservices.org/v4/contribute/)

## Use

Install the Python package as
```bash
pip install pip_services4_logic
```

Example how to use caching and locking.
Here we assume that references are passed externally.

```python
from pip_services4_commons.refer import Descriptor, References, IReferences, IReferenceable
from pip_services4_logic.cache import ICache, MemoryCache
from pip_services4_logic.lock.ILock import ILock
from pip_services4_logic.lock.MemoryLock import MemoryLock


class MyComponent(IReferenceable):
    __cache: ICache
    __lock: ILock

    def set_references(self, references: IReferences):
        self.__cache = references.get_one_required(Descriptor("*", "cache", "*", "*", "1.0"))
        self.__lock = references.get_one_required(Descriptor("*", "lock", "*", "*", "1.0"))

    def my_method(self, context, param1):
        # First check cache for result
        result = self.__cache.retrieve(context, 'mykey')

        # Lock..
        self.__lock.acquire_lock(context, "mykey", 1000, 1000, )

        # Do processing
        # ...

        # Store result to cache async
        self.__cache.store(context, 'mykey', result, 3600000)

        # Release lock async
        self.__lock.release_lock(context, 'mykey')

        return result


# Use the component
my_component = MyComponent()
my_component.set_references(References.from_tuples(
    Descriptor("pip-services", "cache", "memory", "default", "1.0"), MemoryCache(),
    Descriptor("pip-services", "lock", "memory", "default", "1.0"), MemoryLock(),
))

result = my_component.my_method(None, param1)
```

If you need to create components using their locators (descriptors) implement 
component factories similar to the example below.

```python
from pip_services4_commons.refer import Descriptor
from pip_services4_components.build import Factory


class MyFactory(Factory):
    my_component_descriptor = Descriptor("myservice", "mycomponent", "default", "*", "1.0")

    def __init__(self):
        super(MyFactory, self).__init__()

        self.register_as_type(MyFactory.my_component_descriptor, MyFactory)


# Using the factory
my_factory = MyFactory()
my_component1 = my_factory.create(Descriptor("myservice", "mycomponent", "default", "myComponent1", "1.0"))
my_component2 = my_factory.create(Descriptor("myservice", "mycomponent", "default", "myComponent2", "1.0"))

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

The initial implementation is done by **Sergey Seroukhov**. Pip.Services team is looking for volunteers to 
take ownership over Python implementation in the project.
