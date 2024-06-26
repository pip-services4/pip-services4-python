# -*- coding: utf-8 -*-
"""
    pip_services4_commons.refer.__init__
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Inversion of control design pattern. There exist various implementations,
    a popular one being "inversion of dependency". Requires introspection and
    is implemented differently in different languages. In PipServices, the "location
    design pattern” is used, which is much simpler than dependency injection and is
    a simple implementation, that is portable between languages. Used for building
    various containers, as well as testing objects.

    :copyright: Conceptual Vision Consulting LLC 2018-2019, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

__all__ = [
    'Descriptor',
    'IReferenceable', 'IUnreferenceable', 'IReferences',
    'ReferenceException', 'Referencer', 'Reference',
    'References', 'DependencyResolver'
]

from .DependencyResolver import DependencyResolver
from .Descriptor import Descriptor
from .IReferenceable import IReferenceable
from .IReferences import IReferences
from .IUnreferenceable import IUnreferenceable
from .Reference import Reference
from .ReferenceException import ReferenceException
from .Referencer import Referencer
from .References import References
