""" Shodan API Helper Module """
import json
import os
import shodan

SHODAN_SECRETS_FILE = "secrets.json"
# sample variables for execution as __main__
ip = "8.8.8.8"
service = 'nginx'


# potentially move this to run
def read_json_file(json_file):
    """ read local json file and return as dictionary """
    filename = os.path.join(json_file)
    try:
        with open(filename, mode='r') as f:
            return json.loads(f.read())
    except FileNotFoundError:
        return {}


class ShodanAPI():
    """ Creates an instance of a call to the Shodan API """ 
    def __init__(self, secrets_file):
        SHODAN_API_KEY = read_json_file(
            json_file=secrets_file)['SHODAN_API_KEY']
        self.api = shodan.Shodan(SHODAN_API_KEY)

    def api_info(self):
        return self.api.info()
    
    def services_scanned(self):
        return self.api.services()

    def protocols_scanned(self):
        return self.api.protocols()

    def ports_scanned(self):
        return self.api.ports()

    def ip_scanned(self, ip):
        return self.api.host(ip)

    def service_search(self, query):
        return self.api.search(query, page=1, limit=None, offset=None,
                               facets=None, minify=True)


# remove this when finished
if __name__ == "__main__":
    shodan_call_one = ShodanAPI(SHODAN_SECRETS_FILE)
    print(shodan_call_one.api_info())
    print(shodan_call_one.protocols_scanned())
    print(shodan_call_one.services_scanned())
    print(shodan_call_one.ports_scanned())
    print(shodan_call_one.ip_scanned(ip))
    print(shodan_call_one.service_search(service))

