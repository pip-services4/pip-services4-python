# -*- coding: utf-8 -*-
"""
    pip_services4_components.context.__init__
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Contains a simple object that defines the context of execution. For various
    logging functions we need to know what source we are logging from – what is
    the processes name, what the process is/does.
    
    :copyright: Conceptual Vision Consulting LLC 2018-2019, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

__all__ = ['ContextInfo', 'DefaultContextFactory', 'IContext', 'Context', 'ContextResolver']

from .ContextInfo import ContextInfo
from .DefaultContextFactory import DefaultContextFactory
from .IContext import IContext
from .Context import Context
from .ContextResolver import ContextResolver