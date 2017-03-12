import logging
import subprocess
import threading
from kalliope.core.NeuronModule import NeuronModule, MissingParameterException

logging.basicConfig()
logger = logging.getLogger("kalliope")


class AsyncSearch(threading.Thread):
    """
    Class used to run an asynchrone Shell command

    .. notes:: Impossible to get the success code of the command
    """
    def __init__(self, search):
        self.stdout = None
        self.stderr = None
        self.search = search
        threading.Thread.__init__(self)

    def search(self):
	print self.search
        p = subprocess.Popen(self.search,
                             shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)

        self.stdout, self.stderr = p.communicate()


class Search(NeuronModule):
    """
    Run a shell command in a synchron mode
    """
    def __init__(self, **kwargs):
        super(Search, self).__init__(**kwargs)

        # get the command
        self.search = kwargs.get('search', None)
	print self.search
	self.search = self.search.replace(" ","+")
	self.search = "firefox https://www.google.fr/search?q="+self.search+"&ie=utf-8&oe=utf-8 &"
        # get if the user select a blocking command or not
        self.async = kwargs.get('async', False)
        self.query = kwargs.get('query', None)

        if self.query is not None:
            self.search = self.search + "\"" + self.query +"\""

        # check parameters
        if self._is_parameters_ok():
            # run the command
            print self.search
            if not self.async:
		print "0"
                p = subprocess.Popen(self.search, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
		print "1"
                (output, err) = p.communicate()
                self.output = output
                self.returncode = p.returncode
                message = {
                    "output": self.output,
                    "returncode": self.returncode
                }
                self.say(message)

            else:
                async_shell = AsyncSearch(search=self.search)
                async_shell.start()

    def _is_parameters_ok(self):
        """
        Check if received parameters are ok to perform operations in the neuron
        :return: true if parameters are ok, raise an exception otherwise

        .. raises:: MissingParameterException
        """
        if self.search is None:
            raise MissingParameterException("cmd parameter required")

        return True
