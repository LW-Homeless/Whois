class Formatter:

    @staticmethod
    def parse_query_whois(query):

        w = query

        # Delete the item 'raw' on object pythonwhois
        del w['raw']

        # formatting the values None

        for keys, values in w.items():

            if isinstance(values, list):

                for value in values:
                    if value is None:
                        values[value] = 'No record'

            elif isinstance(values, dict):
                for k, v in values.items():
                    if v is None:
                        values[k] = 'No record'
        # formatting the values datetime
        date_record = ['creation_date', 'expiration_date', 'updated_date']

        for date in date_record:
            if date in w:
                date_time = w[date]
                w[date] = [date_time[0].strftime('%Y/%m/%d-%H:%M:%S')]

        return w

    @staticmethod
    def parse_query_whois_raw(query):
        query = query[0].split('\n')
        query = query[:-46]
        return query

    @staticmethod
    def parse_query_ans(query):

        result_asn = {'ASN:': query.asn, 'Prefix:': query.prefix, 'ASName:': query.asname, 'CN:': query.cn,
                      'ISP:': query.isp, 'Peers:': query.peers}

        return result_asn
