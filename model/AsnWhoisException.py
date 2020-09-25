class AsnWhoisException(Exception):

    def __init__(self, msg=None):

        if msg is None:
            msg = 'Error executing ASN query'

        super(AsnWhoisException, self).__init__(msg)
