# -*- coding: utf-8 -*-
"""
    tests.refer.test_DependencyResolver
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from pip_services4_components.config import ConfigParams
from pip_services4_components.refer import Descriptor, DependencyResolver, References


class TestDependencyResolver:

    def test_resolve_depedencies(self):
        ref1 = "AAA"
        ref2 = "BBB"
        refs = References.from_tuples(
            "Reference1", ref1,
            Descriptor("pip-services-commons", "reference", "object", "ref2", "1.0"), ref2
        )

        resolver = DependencyResolver.from_tuples(
            "ref1", "Reference1",
            "ref2", Descriptor("pip-services-commons", "reference", "*", "*", "*")
        )
        resolver.set_references(refs)

        assert ref1 == resolver.get_one_required("ref1")
        assert ref2 == resolver.get_one_required("ref2")
        assert None == resolver.get_one_optional("ref3")

    def test_configure_depedencies(self):
        ref1 = "AAA"
        ref2 = "BBB"
        refs = References.from_tuples(
            "Reference1", ref1,
            Descriptor("pip-services-commons", "reference", "object", "ref2", "1.0"), ref2
        )

        config = ConfigParams.from_tuples(
            "dependencies.ref1", "Reference1",
            "dependencies.ref2", "pip-services-commons:reference:*:*:*",
            "dependencies.ref3", None
        )

        resolver = DependencyResolver(config)
        resolver.set_references(refs)

        assert ref1 == resolver.get_one_required("ref1")
        assert ref2 == resolver.get_one_required("ref2")
        assert None == resolver.get_one_optional("ref3")
