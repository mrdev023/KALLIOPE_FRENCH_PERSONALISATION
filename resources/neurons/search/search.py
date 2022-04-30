import subprocess

from kalliope.core import NeuronModule
from kalliope.core.NeuronModule import MissingParameterException, MissingParameterException

class Search(NeuronModule):
    def __init__(self, **kwargs):
        NeuronModule.__init__(self, **kwargs)

        self.query = kwargs.get('search', None)

        if self._is_parameters_ok():
            subprocess.Popen("xdg-open \"https://www.google.fr/search?q="+self.query+"&ie=utf-8&oe=utf-8\"", shell=True)
    
    def _is_parameters_ok(self):
        """
        Check if received parameters are ok to perform operations in the neuron
        :return: true if parameters are ok, raise an exception otherwise
        .. raises:: MissingParameterException
        """
        if self.query is None:
            raise MissingParameterException("Query parameter is missing.")
        
        return True
