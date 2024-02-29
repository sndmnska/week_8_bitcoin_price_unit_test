"""
This app checks the price of bitcoin using the following API:  http://www.coindesk.com/api  <--- Non functional

Use alternate API to generate fake data instead. https://claraj.github.io/mock-bitcoin/currentprice.json 

OR, use the link that actually does seem to be working! :D   https://api.coindesk.com/v1/bpi/currentprice.json
"""
import requests

# url = 'http://www.coindesk.com/api' # API Not functional
# url = 'https://claraj.github.io/mock-bitcoin/currentprice.json' 
url = 'https://api.coindesk.com/v1/bpi/currentprice.json'



# What do you do for API calls regarding exceptions?

def main():
    number_of_bitcoin = input('How many bitcoin do you have? ')
    response, error = make_api_request(url) # How to handle exceptions in program?
    if error:
        print(error)
        print("Could not get api response")
        return
    if response:
        rate, error = get_rate_from_api_response(response)
        if error:
            print(error)
            print("Api response not structured as expected") 
            return
        if rate:
            print_current_rate(rate)
            rate = convert_string_to_float(rate)
            number_of_bitcoin = convert_string_to_float(number_of_bitcoin)
            total = calculate_bitcoin_total(rate, number_of_bitcoin)
            print_total(total)

    


def print_current_rate(rate):
    print(f'The rate of the USD is ${rate}')

def calculate_bitcoin_total(rate, user_bitcoin):
    return rate * user_bitcoin

def print_total(total):
    print(f'The total amount of USD you have in bitcoin is ${total}')

def convert_string_to_float(str):
    return float(str)

def make_api_request(url):
    try:
        response = requests.get(url).json()
        return response, None
    except Exception as e:
        return None, e

def get_rate_from_api_response(response): # error handling - pass / fail what happens?
    try: 
        rate = response['bpi']['USD']['rate_float']
        return rate, None
    except Exception as e:
        return None, e

#bpi = response.get('bpi')  returns None if no key match


if __name__ == '__main__':
    main()

    