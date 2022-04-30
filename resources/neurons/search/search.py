import logging
import subprocess

from kalliope.core import NeuronModule
from kalliope.core.NeuronModule import MissingParameterException

class Search(NeuronModule):
    def __init__(self, **kwargs):
        super(Search, self).__init__(**kwargs)

        self.query = kwargs.get('search', None)

        if self.query is not None:
            command = "xdg-open \"https://www.google.fr/search?q="+self.query+"&ie=utf-8&oe=utf-8\" &"
            p = subprocess.Popen(command, shell=True)
