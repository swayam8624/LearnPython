# terminal command : python file.py password1 pass2 .
# checks how many times a passwords been hacked
# uses hashing : SHA1/md5 Hash , its one way
# faster data access


# import pwnedpasswords
import sys
import requests
import hashlib


def request_api_data(query_char):
    url = 'http://api.pwnedpasswords.com/range/' + query_char
    # method k-anonymity using only first few letters of the hashed password
    # generally first 5 letters .
    # saves us from giving actual entire password

    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching : {res.status_code}, check the api and try again')
    return res


'''
def read_response(response):
    print(response.text) #no of times these passwords have been hacked
'''


def get_pass_leaks_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    # hashes return the hashed passwords but excluding the first 5 characters like in tail
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0  # we want to return 0 only if for has ended


def pwned_api_check(password):
    print((hashlib.sha1(password.encode('utf-8')).hexdigest().upper()))
    sha1pass = (hashlib.sha1(password.encode('utf-8'))).hexdigest().upper()
    first5, tail = sha1pass[:5], sha1pass[5:]
    response = request_api_data(first5)
    print(first5, tail)
    return get_pass_leaks_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} , you should probably change your password')
        else:
            print(f'{password} was not found')

    return 'done'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
# this input method considers special characters as word breakers
# better to read password from text file
