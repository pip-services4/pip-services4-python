# -*- coding: utf-8 -*-
"""
    tests.config.test_CommandSet
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services4_components.exec import IExecutable, Parameters
from pip_services4_components.context import ContextResolver

from pip_services4_rpc.commands import Command
from pip_services4_rpc.commands import CommandSet


class MyTestError(Exception):
    def __init__(self, text):
        self.txt = text


class CommandExecTest(IExecutable):
    def execute(self, context, args):
        if ContextResolver.get_trace_id(context) == 'wrongId':
            raise MyTestError('Test error')


class TestCommandSet:

    def get_value(self, context, args):
        return args.get('args')

    def test_get_name(self):
        command = Command('name', None, CommandExecTest())
        assert command is not None
        assert command.get_name() == 'name'

    def make_echo_command(self, name):
        return Command(name, None, self.get_value)

    def test_commands(self):
        commands = CommandSet()
        commands.add_command(self.make_echo_command("command1"))
        commands.add_command(self.make_echo_command("command2"))

        result = commands.execute(None, "command1", Parameters.from_tuples("args", 123))
        assert 123 == result

        result = commands.execute(None, "command1", Parameters.from_tuples("args", "ABC"))
        assert "ABC" == result

        result = commands.execute(None, "command2", Parameters.from_tuples("args", 789))
        assert 789 == result
