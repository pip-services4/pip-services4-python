# <img src="https://uploads-ssl.webflow.com/5ea5d3315186cf5ec60c3ee4/5edf1c94ce4c859f2b188094_logo.svg" alt="Pip.Services Logo" width="200"> <br/> Prometheus components for Python

This module is a part of the [Pip.Services](http://pipservices.org) polyglot microservices toolkit.

The module contains components for working with meters in the Prometheus service. The PrometheusCounters and PrometheusMetricsController components allow you to work both in client mode through PushGateway, and as a service.

The module contains the following packages:
- **Build** - the default factories for constructing components.
- **Count** - components of counters (metrics) with sending data to Prometheus via PushGateway
- **Services** - components of the service for reading counters (metrics) by the Prometheus service

<a name="links"></a> Quick links:

* [Configuration](http://docs.pipservices.org/v4/tutorials/beginner_tutorials/configuration/)
* [API Reference](https://pip-services4-python.github.io/pip-services4-prometheus-python/)
* [Change Log](CHANGELOG.md)
* [Get Help](http://docs.pipservices.org/v4/get_help/)
* [Contribute](http://docs.pipservices.org/v4/contribute/)

## Use

Install the Python package as
```bash
pip install pip_services4_prometheus
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

The module is created and maintained by:
- **Sergey Seroukhov**
- **Danil Prisiazhnyi**
