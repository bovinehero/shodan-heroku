""" Shodan API Helper Module """
import json
import os
import shodan

SHODAN_SECRETS_FILE = "secrets.json"
# sample variables for execution as __main__ delete these when finished
IP = "8.8.8.8"
SERVICE = 'nginx'


def read_json_file(json_file):
    """ read local json file and return as dictionary """
    filename = os.path.join(json_file)
    try:
        with open(filename, mode='r', encoding='utf-8') as f_opened:
            return json.loads(f_opened.read())
    except FileNotFoundError:
        return {}
    f_opened.close()


class ShodanAPI():
    """ Creates an instance of a call to the Shodan API """
    def __init__(self, secrets_file):
        shodan_api_key = read_json_file(
            json_file=secrets_file)['SHODAN_API_KEY']
        self.api = shodan.Shodan(shodan_api_key)

    def api_info(self):
        """ return dict of api functionality API key has access to """
        return self.api.info()

    def services_scanned(self):
        """ return dict of services shodan has scanned """
        return self.api.services()

    def protocols_scanned(self):
        """ return dict of ports and protocols shodan has scanned """
        return self.api.protocols()

    def ports_scanned(self):
        """ return list of ports shodan has scanned """
        return self.api.ports()

    def ip_scanned(self, target_ip):
        """ return dict based on ip string """
        return self.api.host(target_ip)

    def service_search(self, query):
        """ return dict based on search query string """
        return self.api.search(query, page=1, limit=None, offset=None,
                               facets=None, minify=True)


# remove this when finished
if __name__ == "__main__":
    shodan_call_one = ShodanAPI(SHODAN_SECRETS_FILE)
    print(shodan_call_one.api_info())
    print(shodan_call_one.protocols_scanned())
    print(shodan_call_one.services_scanned())
    print(shodan_call_one.ports_scanned())
    print(shodan_call_one.ip_scanned(IP))
    print(shodan_call_one.service_search(SERVICE))
