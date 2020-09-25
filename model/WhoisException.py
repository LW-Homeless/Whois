class WhoisException(Exception):

    def __init__(self, msg=None):

        if msg is None:
            msg = 'Error executing Whois query'

        super(WhoisException, self).__init__(msg)
