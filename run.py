# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import shodan

def poc():
    """ just a poc function """
    #change this to ENVs or getpass.getpass
    SHODAN_API_KEY = input('Enter your Shodan API Key: ')
    api = shodan.Shodan(SHODAN_API_KEY)
    info = api.host('8.8.8.8')
    print(info)


def main():
    """ main finction to handle the runtime """
    poc()


if __name__ == "__main__":
    main()