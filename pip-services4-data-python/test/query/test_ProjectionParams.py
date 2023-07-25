# -*- coding: utf-8 -*-
"""
    tests.data.test_ProjectionParams
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from pip_services4_data.query import ProjectionParams


class TestProjectionParams():

    def test_create_projection_params_from_null_object(self):
        params = ProjectionParams.from_value(None)
        assert len(params) == 0

    def test_create_projection_from_values(self):
        params = ProjectionParams.from_value(["field1", "field2", "field3"])
        assert len(params) == 3
        assert params[0] == "field1"
        assert params[1] == "field2"
        assert params[2] == "field3"

    def test_convert_parameters_from_string(self):
        params = ProjectionParams.from_string("field1", "field2", "field3")

        assert len(params) == 3
        assert params[0] == "field1"
        assert params[1] == "field2"
        assert params[2] == "field3"
        to_str_param = params.to_string()
        assert type(to_str_param) == str
        assert to_str_param == 'field1,field2,field3'

    def test_parse_parameters_from_string(self):
        parameters = ProjectionParams.from_string("field1", "field2", "field3")

        assert 3 == len(parameters)
        assert "field1" == parameters[0]
        assert "field2" == parameters[1]
        assert "field3" == parameters[2]

        parameters = ProjectionParams.from_string("field1,field2, field3")

        assert 3 == len(parameters)
        assert "field1" == parameters[0]
        assert "field2" == parameters[1]
        assert "field3" == parameters[2]

        parameters = ProjectionParams.from_string("object1(field1)", "object2(field1, field2)", "field3")

        assert 4 == len(parameters)
        assert "object1.field1" == parameters[0]
        assert "object2.field1" == parameters[1]
        assert "object2.field2", parameters[2]
        assert "field3" == parameters[3]

        parameters = ProjectionParams.from_string("object1(object2(field1,field2,object3(field1)))")

        assert 3 == len(parameters)
        assert "object1.object2.field1" == parameters[0]
        assert "object1.object2.field2" == parameters[1]
        assert "object1.object2.object3.field1" == parameters[2]

        parameters = ProjectionParams.from_string("object1(field1, object2(field1, field2, field3, field4), field3)",
                                                  "field2")

        assert 7 == len(parameters)
        assert "object1.field1" == parameters[0]
        assert "object1.object2.field1" == parameters[1]
        assert "object1.object2.field2" == parameters[2]
        assert "object1.object2.field3" == parameters[3]
        assert "object1.object2.field4" == parameters[4]
        assert "object1.field3" == parameters[5]
        assert "field2" == parameters[6]

        parameters = ProjectionParams.from_string("object1(field1, object2(field1), field3)", "field2")

        assert 4 == len(parameters)
        assert "object1.field1" == parameters[0]
        assert "object1.object2.field1" == parameters[1]
        assert "object1.field3" == parameters[2]
        assert "field2" == parameters[3]

        parameters = ProjectionParams.from_string(
            "object1(field1, object2(field1, field2, object3(field1), field4), field3)", "field2")

        assert 7 == len(parameters)
        assert "object1.field1" == parameters[0]
        assert "object1.object2.field1", parameters[1]
        assert "object1.object2.field2", parameters[2]
        assert "object1.object2.object3.field1", parameters[3]
        assert "object1.object2.field4", parameters[4]
        assert "object1.field3", parameters[5]
        assert "field2" == parameters[6]

        parameters = ProjectionParams.from_string("object1(object2(object3(field1)), field2)", "field2")

        assert 3 == len(parameters)
        assert "object1.object2.object3.field1" == parameters[0];
        assert "object1.field2" == parameters[1];
        assert "field2" == parameters[2]

        parameters = ProjectionParams.from_string(
            "field1,object1(field1),object2(field1,field2),object3(field1),field2,field3")

        assert 7 == len(parameters)
        assert "field1" == parameters[0]
        assert "object1.field1" == parameters[1]
        assert "object2.field1" == parameters[2]
        assert "object2.field2" == parameters[3]
        assert "object3.field1" == parameters[4]
        assert "field3" == parameters[6]
        assert "field2" == parameters[5]
