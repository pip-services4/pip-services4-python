# <img src="https://uploads-ssl.webflow.com/5ea5d3315186cf5ec60c3ee4/5edf1c94ce4c859f2b188094_logo.svg" alt="Pip.Services Logo" width="200"> <br/> Redis components for Pip.Services for Python

This module is a part of the [Pip.Services](http://pipservices.org) polyglot microservices toolkit.

The module for working with a Redis database of type key-value contains components for working with cache and locks: RedisCache and RedisLock.

The module contains the following packages:

- **Build** - factory default
- **Cache** - Redis Cache Components
- **Lock** - components of working with locks in Redis

<a name="links"></a> Quick links:

* [Configuration](https://www.pipservices.org/recipies/configuration)
* [API Reference](https://pip-services4-python.github.io/pip-services4-redis-python/index.html)
* [Change Log](CHANGELOG.md)
* [Get Help](https://www.pipservices.org/community/help)
* [Contribute](https://www.pipservices.org/community/contribute)

## Use

Install the Python package as
```bash
pip install pip-services4-redis
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

The Python version of Pip.Services is created and maintained by
- **Sergey Seroukhov**
- **Danil Prisiazhnyi**
