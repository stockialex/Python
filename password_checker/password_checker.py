import requests
import hashlib


def request_api_data(query_char):
    url = ('https://api.pwnedpasswords.com/range/' + query_char)
    result = requests.get(url)
    if result.status_code != 200:
        raise RuntimeError(f'Error fetching: {result.status_code}, check the api URL or the password\n')
    return result


def get_password_leak_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for hashx, count in hashes:
        if hashx == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    hashpass = hashlib.sha1(password.encode('UTF-8')).hexdigest().upper()
    first_five, tail = hashpass[:5], hashpass[5:]
    response = request_api_data(first_five)
    return get_password_leak_count(response, tail)


def ask_password():
    # you can check multiple passwords in a single execution
    password_list = []
    print("Password checker. Type the password/s you want to check.\nType nothing to finish\n")
    while True:
        user_password = input("Password: ")
        if user_password != '':
            password_list.append(user_password)
        else:
            break
    return password_list


def check_user_password():
    psw_list = ask_password()
    for password in psw_list:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times. You should change it\n')
        else:
            print(f'Nice, {password} wasn\'t found!\n')
    print('Done. See you soon!\n')


if __name__ == '__main__':
    check_user_password()
