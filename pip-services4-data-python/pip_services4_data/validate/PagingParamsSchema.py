# -*- coding: utf-8 -*-
"""
    pip_services4_commons.validate.PagingParamsSchema
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    PagingParams schema implementation
    
    :copyright: Conceptual Vision Consulting LLC 2018-2019, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from pip_services4_commons.convert import TypeCode

from .ObjectSchema import ObjectSchema


class PagingParamsSchema(ObjectSchema):
    """
    Schema to validate :class:`PagingParams <pip_services4_data.query.PagingParams.PagingParams>`.
    """

    def __init__(self):
        """
        Creates a new instance of validation schema.
        """
        super(PagingParamsSchema, self).__init__()
        self.with_optional_property('skip', TypeCode.Long)
        self.with_optional_property('take', TypeCode.Long)
        self.with_optional_property('total', TypeCode.Boolean)
