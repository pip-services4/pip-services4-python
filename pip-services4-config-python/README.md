# <img src="https://uploads-ssl.webflow.com/5ea5d3315186cf5ec60c3ee4/5edf1c94ce4c859f2b188094_logo.svg" alt="Pip.Services Logo" width="200"> <br/>  Config Components for Python

This module is a part of the [Pip.Services](http://pipservices.org) polyglot microservices toolkit.

The Config module contains configuration component definitions that can be used to build applications and services.

The module contains the following packages:
- **Auth** - authentication credential stores
- **Config** - configuration readers and managers, whose main task is to deliver configuration parameters to the application from wherever they are being stored
- **Connect** - connection discovery and configuration services

<a name="links"></a> Quick links:

* [API Reference](https://pip-services4-python.github.io/pip-services4-config-python/index.html)
* [Change Log](CHANGELOG.md)
* [Get Help](http://docs.pipservices.org/v4/get_help/)
* [Contribute](http://docs.pipservices.org/v4/contribute/)

## Use

Install the Python package as
```bash
pip install pip_services4_config
```

Example how to get connection parameters and credentials using resolvers.
The resolvers support "discovery_key" and "store_key" configuration parameters
to retrieve configuration from discovery services and credential stores respectively.

```python
from pip_services4_commons.config import ConfigParams, IConfigurable
from pip_services4_commons.refer import IReferences, IReferenceable
from pip_services4_commons.run import IOpenable
from pip_services4_components.auth import CredentialParams, CredentialResolver
from pip_services4_components.connect import ConnectionParams, ConnectionResolver


class MyComponent(IConfigurable, IReferenceable, IOpenable):
    __connection_resolver = ConnectionResolver()
    __credential_resolver = CredentialResolver()

    def configure(self, config):
        self.__connection_resolver.configure(config)
        self.__credential_resolver.configure(config)

    def set_references(self, references):
        self.__connection_resolver.set_references(references)
        self.__credential_resolver.set_references(references)

    # ...

    def open(self, context):
        connection = self.__connection_resolver.resolve(context)
        credential = self.__credential_resolver.lookup(context)

        host = connection.get_post()
        port = connection.get_port()
        user = credential.get_username()
        pas = credential.get_password()

    # ...


# Using the component
my_component = MyComponent()

my_component.configure(ConfigParams.from_tuples(
    'connection.host', 'localhost',
    'connection.port', 1234,
    'credential.username', 'anonymous',
    'credential.password', 'pass123'
))

my_component.open(None)
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
