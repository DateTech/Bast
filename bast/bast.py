"""
    Bast Web Framework
    (c) Majiyagbe Oluwole <oluwole564@gmail.com>

    For full copyright and license information, view the LICENSE distributed with the Source Code
"""

import logging
import os
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options, parse_command_line
from tornado.web import Application, StaticFileHandler
from .environment import load_env
from colorama import init, Fore

__author__ = "Majiyagbe Oluwole"
__copyright__ = ""
__license__ = "M.I.T License"
__version__ = "1.0"
__status__ = "Under Development"


class Bast(Application):
    def __init__(self, route, **settings):
        """
         Bast Server Class. Runs on Tornado HTTP Server (http://www.tornadoweb.org/en/stable/)

        Constructor for the Bast Server. Takes an instance of the route as parameter.
        The Web handler with routes are handled here.

        Config files are also loaded from the config/config.ini folder.
        Appropriate configurations are loaded from the config file into the os environment for use
        :param route:
        """
        # self.settings = settings
        super().__init__(**settings)
        init()
        self.host = '127.0.0.1'
        self.port = 2000
        self.debug = True

        # self.load_config()
        load_env()

        self.handler = route.all().url
        self.handler.append((r'/css/(.*)', StaticFileHandler, {"path": os.path.abspath(".") + "/public/static/css"}))
        self.handler.append((r'/script/(.*)', StaticFileHandler, {"path": os.path.abspath(".") + "/public/static/js"}))
        self.handler.append(
            (r'/images/(.*)', StaticFileHandler, {"path": os.path.abspath('.') + "/public/static/images"}))

        # append the URL for static files to exception
        self.handler.append((r'/exp/(.*)', StaticFileHandler, {'path': os.path.join(os.path.dirname(os.path.realpath(__file__)), "exception")}))

    def run(self):
        """
        Function to Run the server. Server runs on host: 127.0.0.1 and port: 2000 by default. Debug is also set to false
        by default

        Can be overriden by using the config.ini file
        """
        define("port", default=self.port, help="Run on given port", type=int)
        define("host", default=self.host, help="Run on given host", type=str)
        define("debug", default=self.debug, help="True for development", type=bool)

        parse_command_line()

        print(Fore.GREEN + "Starting Bast Server....")
        print(Fore.GREEN + "Bast Server Running on %s:%s" % (options.host, options.port))

        application = Application(self.handler, debug=options.debug)
        server = HTTPServer(application)
        server.listen(options.port, options.host)
        IOLoop.current().start()
