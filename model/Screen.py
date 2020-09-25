from colorama import Fore
from tabulate import tabulate


class Screen:

    def __init__(self):

        self.__title_app = '''
             __    __ _           _                                      
            / / /\ \ \ |__   ___ (_)___        ___ _ __  _   _ _ __ ___  
            \ \/  \/ / '_ \ / _ \| / __|_____ / _ \ '_ \| | | | '_ ` _ \ 
             \  /\  /| | | | (_) | \__ \_____|  __/ | | | |_| | | | | | |
              \/  \/ |_| |_|\___/|_|___/      \___|_| |_|\__,_|_| |_| |_|
             -------------------------------------------------------------
             Create by : Homeless
             Version : 1.0.0
             -------------------------------------------------------------
             '''
        self.__head =[]
        self.__table = []

    def print_banner(self):
        print(Fore.GREEN + self.__title_app)

    def print_result_root_server_whois(self, query_root_server):
        self.__head = ['Whois: Root-Server']
        self.__table = [[query_root_server]]
        print(Fore.RED + 'Whois: Root-Server')
        print(tabulate(self.__table, tablefmt='fancy_grid'), end='')

        del self.__head[:]
        del self.__table[:]

    def print_query_whois(self, query_whois):
        self.__table = []
        for keys in query_whois.keys():

            if isinstance(query_whois[keys], list):
                for value in query_whois[keys]:
                    self.__table.append([keys, value])

            elif isinstance(query_whois[keys], dict):
                for k, v in query_whois[keys].items():
                    self.__table.append([k, v])
        print(Fore.RED + 'Query Whois')
        print(tabulate(self.__table, tablefmt='fancy_grid'), end='')
        del self.__table[:]

    def print_query_whois_raw(self, query_whois_raw):
        self.__table = []
        for item in query_whois_raw:
            self.__table.append([item])
        print(Fore.RED + 'Query Whois Server')
        print(tabulate(self.__table, self.__head, tablefmt='fancy_grid'), end='')
        del self.__table[:]

    def print_query_asn(self, query_asn):
        self.__table = []
        for keys, values in query_asn.items():
            self.__table.append([keys, values])
        print(Fore.RED + 'Query ASN')
        print(tabulate(self.__table, self.__head, tablefmt='fancy_grid'))
        del self.__table[:]
        del self.__head[:]
