from util.Formatter import Formatter
from model.WhoisException import WhoisException
import pythonwhois
import pythonwhois.shared
import socket


class Whois:

    def __init__(self, domain):
        self.__domain = domain
        self.__query_root_server = ''
        self.__query_whois = ''
        self.__query_whois_raw = ''

    def get_query_root_server(self):
        try:
            self.__query_root_server = pythonwhois.net.get_root_server(self.__domain)
            return self.__query_root_server
        except pythonwhois.shared.WhoisException as ex:
            raise WhoisException(msg='No root WHOIS server found for domain.')
        except socket.gaierror:
            raise WhoisException(msg='Connection failed, check your internet')

    def get_query_whois(self):
        try:
            self.__query_whois = pythonwhois.get_whois(self.__domain)
            self.__query_whois = Formatter.parse_query_whois(self.__query_whois)
            return self.__query_whois
        except pythonwhois.shared.WhoisException:
            raise WhoisException('No root WHOIS server found for domain.')
        except socket.gaierror:
            raise WhoisException('Connection failed, check your internet')

    def get_query_whois_raw(self):
        try:
            self.__query_whois_raw = pythonwhois.net.get_whois_raw(domain=self.__domain,
                                                                   server=self.get_query_whois()['whois_server'][0])

            self.__query_whois_raw = Formatter.parse_query_whois_raw(self.__query_whois_raw)
            return self.__query_whois_raw
        except pythonwhois.shared.WhoisException as ex:
            raise ex
        except socket.gaierror:
            raise WhoisException('Connection failed, check your internet')
