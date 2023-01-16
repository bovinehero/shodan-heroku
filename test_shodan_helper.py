"""Module providing unit testing of shodan_helper."""

from shodan_helper import ShodanAPI, SHODAN_SECRETS_FILE

SHODAN_TEST_CALL = ShodanAPI(SHODAN_SECRETS_FILE)
IP_ADDRS = [
    "8.8.8.8",
    "hello",
    "fbewUFGEWPOFUEWFFwe]fmwepfq0=efghwefghw    ]e",
    "256.33.21.104",
    "\t\n"
]


def test_plan():
    """ Ensure API is using the correct tier for the app """
    api_info = SHODAN_TEST_CALL.api_info()
    assert api_info['plan'] == 'oss', "Should be on free plan"


def test_services():
    """ Ensure Shodan has services to scan on this tier """
    services = SHODAN_TEST_CALL.services_scanned()
    assert len(services) > 0, "Should have some services"


def test_protcols():
    """ Ensure Shodan has protocols to scan on this tier """
    protocols = SHODAN_TEST_CALL.protocols_scanned()
    assert len(protocols) > 0, "Should have some protcols"


def test_ports():
    """ Ensure Shodan has ports to scan on this tier """
    ports = SHODAN_TEST_CALL.ports_scanned()
    assert len(ports) > 0, "Should have some ports"


def test_scanned():
    """ Ensure Shodan dB responds to user inputs on this tier """
    for ip_addr in IP_ADDRS:
        scanned = SHODAN_TEST_CALL.ip_scanned(target_ip=ip_addr)
        try:
            assert scanned, "Input should be a valid IP Address"
        except AssertionError:
            print(scanned)
            assert not scanned, "Call should return None\
 when Shodan API error"
