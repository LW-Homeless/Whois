from model.Whois import Whois
from model.WhoisException import WhoisException
from model.AsnWhoisException import AsnWhoisException
from model.AsnWhois import AsnWhois
from model.Screen import Screen
from colorama import Fore, init


class Main:

    @staticmethod
    def main():
        init()

        screen = Screen()
        screen.print_banner()

        try:
            while True:
                print(Fore.GREEN + '', end='')
                domain = input("Enter your domain > ")
                print('\n')
                w = Whois(domain)

                try:
                    screen.print_result_root_server_whois(w.get_query_root_server())
                    print('\n')
                except WhoisException as ex:
                    print(Fore.RED + '[X] ' + ex.__str__())
                    print(Fore.YELLOW + '[!] Press Ctrl+C to exit')
                    continue

                try:
                    screen.print_query_whois(w.get_query_whois())
                    if 'whois_server' in w.get_query_whois():
                        print('\n')
                        screen.print_query_whois_raw(w.get_query_whois_raw())
                        print('\n')
                    else:
                        print('\n')
                        print(Fore.BLUE + '[i] No Whois Server Found', end='')
                        print('\n')
                except WhoisException as ex:
                    print(Fore.RED + '[X] ' + ex.__str__())
                    print(Fore.YELLOW + '[!] Press Ctrl+C to exit')
                    continue
                except TimeoutError as ex:
                    print(Fore.RED + '[X]' + ex.__str__())
                    exit(0)

                try:
                    asn = AsnWhois(domain)
                    screen.print_query_asn(asn.get_ans_whois())
                except AsnWhoisException as ex:
                    print(Fore.RED + '[X] ' + ex.__str__())
                    print(Fore.YELLOW + '[!] Press Ctrl+C to exit')
                    continue
                except TimeoutError as ex:
                    print(Fore.RED + '[X]' + ex.__str__())
                    exit(0)

                print(Fore.BLUE + '[i] Finished process')
        except KeyboardInterrupt:
            exit(0)


if __name__ == '__main__':
    Main.main()
