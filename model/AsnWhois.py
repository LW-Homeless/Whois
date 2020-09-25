from util.Formatter import Formatter
from model.AsnWhoisException import AsnWhoisException
from RashlyOutlaid.libwhois import ASNWhois, QueryError
import socket


class AsnWhois:

    def __init__(self, domain):
        self.__query_asn = ''
        self.__ip_address = ''
        self.__domain = domain

    def get_ans_whois(self):
        try:
            # get ip address to domain
            self._get_ip_address_domain()

            self.__query_asn = ASNWhois()
            self.__query_asn.query = [self.__ip_address]
            self.__query_asn.peers = True

            return Formatter.parse_query_ans(self.__query_asn.result[self.__ip_address])
        except socket.gaierror:
            raise AsnWhoisException('get address info failed')
        except QueryError:
            raise AsnWhoisException('Error asn.')

    def _get_ip_address_domain(self):
        try:
            ip_address = socket.gethostbyname(self.__domain)
            self.__ip_address = ip_address
        except socket.gaierror as ex:
            raise ex
