import os

from bast.controller import Controller


class ExampleController(Controller):
    def index(self):
        self.view('index.html', {'data': os.environ['DB_NAME']})

    def test(self, param):
        self.write(param)
