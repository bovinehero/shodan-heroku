import re
import run

print(run.SECRETS_FILE)

IP_REGEX = \
        "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\
.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

INPUTS = [
    "8.8.8.8888",
    "hello",
    "8.8.8.8",
    "fgnwciugwancHGAN0UGO GNCWAOPUGNT WEF"
]

def test_validation():
    for input_str in INPUTS:
        output = run.validate_user_input(input_str)
        if not re.search(IP_REGEX, input_str):
            assert not output
        else:
            assert output