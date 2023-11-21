# <img src="https://uploads-ssl.webflow.com/5ea5d3315186cf5ec60c3ee4/5edf1c94ce4c859f2b188094_logo.svg" alt="Pip.Services Logo" width="200"> <br/> MySQL components for Python

This module is a part of the [Pip.Services](http://pipservices.org) polyglot microservices toolkit.

The module contains the following packages:
 
- **Build** - a standard factory for constructing components
- **Connect** - instruments for configuring connections to the database.
- **Persistence** - abstract classes for working with the database that can be used for connecting to collections and performing basic CRUD operations

<a name="links"></a> Quick links:

* [Configuration](http://docs.pipservices.org/v4/tutorials/beginner_tutorials/configuration/)
* [API Reference](https://pip-services4-python.github.io/pip-services4-mysql-python/)
* [Change Log](CHANGELOG.md)
* [Get Help](http://docs.pipservices.org/v4/get_help/)
* [Contribute](http://docs.pipservices.org/v4/contribute/)

## Use

Install the Python package as
```bash
pip install pip-services4-mysql
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
