# -*- coding: utf-8 -*-
"""
    tests.refer.test_Descriptor
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest
from pip_services4_commons.errors import ConfigException

from pip_services4_components.refer import Descriptor


class TestDescriptor:

    def test_match(self):
        descriptor = Descriptor("pip-services-dummies", "controller", "default", "default", "1.0")

        # Check match by individual fields
        assert descriptor.match(Descriptor("pip-services-dummies", None, None, None, None))
        assert descriptor.match(Descriptor(None, "controller", None, None, None))
        assert descriptor.match(Descriptor(None, None, "default", None, None))
        assert descriptor.match(Descriptor(None, None, None, "default", None))
        assert descriptor.match(Descriptor(None, None, None, None, "1.0"))

        # Check match by individual "*" fields
        assert descriptor.match(Descriptor("pip-services-dummies", "*", "*", "*", "*"))
        assert descriptor.match(Descriptor("*", "controller", "*", "*", "*"))
        assert descriptor.match(Descriptor("*", "*", "default", "*", "*"))
        assert descriptor.match(Descriptor("*", "*", "*", "default", "*"))
        assert descriptor.match(Descriptor("*", "*", "*", "*", "1.0"))

        # Check match by all values
        assert descriptor.match(Descriptor("pip-services-dummies", "controller", "default", "default", None))
        assert descriptor.match(Descriptor(None, "controller", "default", "default", "1.0"))
        assert descriptor.match(Descriptor("pip-services-dummies", "controller", "default", "default", "1.0"))

        # Check mismatch by individual fields
        assert not descriptor.match(Descriptor("pip-services-runtime", None, None, None, None))
        assert not descriptor.match(Descriptor(None, "cache", None, None, None))
        assert not descriptor.match(Descriptor(None, None, "special", None, None))
        assert not descriptor.match(Descriptor(None, None, None, "special", None))
        assert not descriptor.match(Descriptor(None, None, None, None, "2.0"))

    def test_to_string(self):
        descriptor1 = Descriptor("pip-services-dummies", "controller", "default", "default", "1.0")
        assert "pip-services-dummies:controller:default:default:1.0" == str(descriptor1)

        descriptor2 = Descriptor(None, None, None, None, None)
        assert "*:*:*:*:*" == str(descriptor2)

    def test_from_string(self):
        descriptor = Descriptor.from_string(None)
        assert descriptor is None

        descriptor = Descriptor.from_string("pip-dummies:controller:default:default:1.0")
        assert descriptor.exact_match(Descriptor("pip-dummies", "controller", "default", "default", "1.0"))

        with pytest.raises(ConfigException) as ex:
            Descriptor.from_string('xxx')
