""" Shodan API Helper Module """
import json
import os
import shodan

SHODAN_SECRETS_FILE = "secrets.json"
IP = "8.8.8.8"
SERVICE = 'nginx'


def read_json_file(json_file):
    """ read local json file and return as dictionary
    Parameters:
    json_file(str) name of the json file to be read

    Returns:
    dict: contents of file
    """
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
        """ fetch functionality API key has access to
        Returns:
        dict: API usage allowances based on API key
        """
        return self.api.info()

    def services_scanned(self):
        """ fetch services shodan scans
        Returns:
        list: Service name and description key pair values \
        of services shodan can scan
        """
        return self.api.services()

    def protocols_scanned(self):
        """ fetch ports and protocols shodan can scan
        Returns:
        list: Port and Protocol key pair values of protocls \
        shodan scans by default
        """
        return self.api.protocols()

    def ports_scanned(self):
        """ fetch ports shodan can scan
        Returns:
        list: Port Numbers shodan scans by default
        """
        return self.api.ports()

    def ip_scanned(self, target_ip):
        """ fetch machine details from the shodan dB
        Parameters:
        target_ip(str) target IP to be checked against the API

        Returns:
        dict: contents of file
        None: if no IP found or other error discovered
        """
        try:
            return self.api.host(target_ip)
        except shodan.exception.APIError as err:
            print(f'[-] Shodan responds: {err}')
            print('[-] Please try a different target or contact administrator')
            return None
