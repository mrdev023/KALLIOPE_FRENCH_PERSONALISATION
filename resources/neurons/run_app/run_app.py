import subprocess
import os
import logging

from kalliope.core import NeuronModule
from kalliope.core.NeuronModule import MissingParameterException, MissingParameterException

logging.basicConfig()
logger = logging.getLogger("kalliope")

home_dir = os.path.expanduser('~')

entries_dirs = [
    os.path.join(home_dir, ".local/share/applications"),
    "/usr/local/share/applications",
    "/usr/share/applications"
]

def parse_exec(line):
    splitted_line = line.split("=")
    if len(splitted_line) < 2:
        return None
    else:
        return splitted_line[1]

def check_file(file_path, query):
    exec = None # Equals to Exec command of .desktop if is before search terms
    found = False
    for line in open(file_path, 'r').readlines():
        if "exec" in line.lower():
            exec = parse_exec(line)
        if query.lower() in line.lower():
            found = True
        if exec is not None and found is True:
            return exec.split(" ")[0]
    return None

def search_app_name_in_desktop_entries(query: str):
    for d in entries_dirs:
        if os.path.exists(d):
            for f in os.listdir(d):
                if ".desktop" in f:
                    result = check_file(os.path.join(d, f), query)
                    if result is not None:
                        return result
    return None

class Run_app(NeuronModule):
    def __init__(self, **kwargs):
        NeuronModule.__init__(self, **kwargs)

        self.query = kwargs.get('app', None)
        self.found_message = kwargs.get('found_message', None)
        self.not_found_message = kwargs.get('not_found_message', None)

        if self._is_parameters_ok():
            result = search_app_name_in_desktop_entries(self.query)
            if result is not None:
                logger.debug("EXEC: %s" % result)
                subprocess.Popen(result, shell=True)
                self.say(self.found_message)
            else:
                self.say(self.not_found_message)
    
    def _is_parameters_ok(self):
        """
        Check if received parameters are ok to perform operations in the neuron
        :return: true if parameters are ok, raise an exception otherwise
        .. raises:: MissingParameterException
        """
        if self.query is None:
            raise MissingParameterException("Query parameter is missing.")
        if self.found_message is None:
            raise MissingParameterException("Found message parameter is missing.")
        if self.not_found_message is None:
            raise MissingParameterException("Not found message parameter is missing.")
        
        return True