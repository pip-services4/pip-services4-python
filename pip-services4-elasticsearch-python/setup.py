"""
Pip.Services Elasticsearch
------------------

Pip.Services is an open-source library of basic microservices.
pip_services4_elasticsearch  contains logging components with data storage on the Elasticsearch server.

Links
`````

* `website <http://github.com/pip-services/pip-services>`_
* `development version <http://github.com/pip-services4/pip-services4-python/tree/main/pip-services4-elasticsearch-python>`

"""

from setuptools import find_packages
from setuptools import setup

readme = ''

try:
    readme = open('readme.md').read()
except:
    readme = __doc__

setup(
    name='pip_services4_elasticsearch',
    version='3.1.6',
    url='http://github.com/pip-services4/pip-services4-python/tree/main/pip-services4-elasticsearch-python',
    license='MIT',
    author='Conceptual Vision Consulting LLC',
    author_email='seroukhov@gmail.com',
    description='ElasticSearch components for Pip.Services in Python',
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=['config', 'data', 'test']),
    include_package_data=True,
    zip_safe=True,
    platforms='any',
    install_requires=[
        'moment',
        'elasticsearch >= 7.17.2, < 8.0.0',

        'pip-services4-commons >= 0.0.1, < 1.0',
        'pip-services4-components >= 0.0.1, < 1.0',
        'pip-services4-rpc >= 0.0.1, < 1.0',
        'pip-services4-config >= 0.0.1, < 1.0',
        'pip-services4-data >= 0.0.1, < 1.0',
        'pip-services4-rpc >= 0.0.1, < 1.0',
        'pip-services4-http >= 0.0.1, < 1.0',
        'pip-services4-observability >= 0.0.5, < 1.0',
        'pip_services4_container >= 0.0.1, < 1.0'

    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
