# -*- coding: utf-8 -*-
"""
    app.py
    ~~~~~~~~~~~~~~~~~~~~

    Dummy app run implementation

    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
import sys
import traceback

from pip_services4_components.context import Context
from pip_services4_observability.log import ConsoleLogger

from DummyProcess import DummyProcess

if __name__ == '__main__':
    runner = DummyProcess()
    try:
        runner.run()
    except Exception as ex:
        ConsoleLogger().fatal(Context.from_trace_id("dummy"), ex, "Error: ")
        print(traceback.format_exc(ex))
        sys.stderr.write(str(ex) + '\n')
