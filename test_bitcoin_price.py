import unittest
from unittest import TestCase
from unittest.mock import patch, call, Mock

import bitcoin_price

class TestBitcoinPrice(TestCase):
    @patch('requests.get')
    def test_make_api_request_success(self, mock_requests_get): 
        # what am I testing?  Testing for returning a tuple of (response, None) upon success.
        # It doesn't really matter what the 'response' contains, only that a tuple is returned if no Exception is thrown. 
        # arrange
        example_api_response = {'time': {'updated': 'Feb 29, 2024 00:01:04 UTC', 'updatedISO': '2024-02-29T00:01:04+00:00', 'updateduk': 'Feb 29, 2024 at 00:01 GMT'}, 'disclaimer': 'This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org', 'chartName': 'Bitcoin', 'bpi': {'USD': {'code': 'USD', 'symbol': '&#36;', 'rate': '62,408.448', 'description': 'United States Dollar', 'rate_float': 62408.4482}, 'GBP': {'code': 'GBP', 'symbol': '&pound;', 'rate': '49,294.998', 'description': 'British Pound Sterling', 'rate_float': 49294.9979}, 'EUR': {'code': 'EUR', 'symbol': '&euro;', 'rate': '57,580.219', 'description': 'Euro', 'rate_float': 57580.2186}}}
        mock_requests_get().json.return_value = example_api_response
        expected_return_value = (example_api_response, None)
        # action
        actual_return_value = bitcoin_price.make_api_request(mock_requests_get)
        # assert
        self.assertEqual(expected_return_value, actual_return_value)

    # FIXME: How to detect Exceptions (general) when the function returns tuples? 
    @patch('requests.get')
    def test_get_rate_from_api_response_unexpected_structure(self):
        example_bad_url_response = {'statusCode': 404, 'error': 'Not Found', 'message': 'Not Found'}
        expected_return_value = (None, KeyError)
        self.fail('TODO - Should detect some kind of generalizd exception, but how to assert?') 
            # When the exception thrown actually prints "bpi" when throwing an error 
            # (because that's the first KeyError), how do I use testing to detect and assert the Error, 
            # as well as the tuple (None, ${EXCEPTION_OF_SOME_SORT}) ??


    def test_get_rate_from_api_response_valid_rate(self):
        expected_test_rate = (62408.4482, None) # data returned, None object to represent no exceptions. 
        example_api_response = {'time': {'updated': 'Feb 29, 2024 00:01:04 UTC', 'updatedISO': '2024-02-29T00:01:04+00:00', 'updateduk': 'Feb 29, 2024 at 00:01 GMT'}, 'disclaimer': 'This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org', 'chartName': 'Bitcoin', 'bpi': {'USD': {'code': 'USD', 'symbol': '&#36;', 'rate': '62,408.448', 'description': 'United States Dollar', 'rate_float': 62408.4482}, 'GBP': {'code': 'GBP', 'symbol': '&pound;', 'rate': '49,294.998', 'description': 'British Pound Sterling', 'rate_float': 49294.9979}, 'EUR': {'code': 'EUR', 'symbol': '&euro;', 'rate': '57,580.219', 'description': 'Euro', 'rate_float': 57580.2186}}}
        rate_result = bitcoin_price.get_rate_from_api_response(example_api_response)
        self.assertEqual(expected_test_rate, rate_result)

    def test_get_rate_from_api_response_(self):
        expected_test_rate = (62408.4482, None) # data returned, None object to represent no exceptions. 
        example_api_response = {'time': {'updated': 'Feb 29, 2024 00:01:04 UTC', 'updatedISO': '2024-02-29T00:01:04+00:00', 'updateduk': 'Feb 29, 2024 at 00:01 GMT'}, 'disclaimer': 'This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org', 'chartName': 'Bitcoin', 'bpi': {'USD': {'code': 'USD', 'symbol': '&#36;', 'rate': '62,408.448', 'description': 'United States Dollar', 'rate_float': 62408.4482}, 'GBP': {'code': 'GBP', 'symbol': '&pound;', 'rate': '49,294.998', 'description': 'British Pound Sterling', 'rate_float': 49294.9979}, 'EUR': {'code': 'EUR', 'symbol': '&euro;', 'rate': '57,580.219', 'description': 'Euro', 'rate_float': 57580.2186}}}
        rate_result = bitcoin_price.get_rate_from_api_response(example_api_response)
        self.assertEqual(expected_test_rate, rate_result)

    # I'm including the following to demonstrate some understanding of how mock tests work
    @patch('builtins.print')
    def test_print_current_rate(self, mock_print):
        bitcoin_price.print_current_rate(1234.567)
        mock_print.assert_called_once_with('The rate of the USD is $1234.567')

    @patch('builtins.print')
    def test_print_total(self, mock_print):
        bitcoin_price.print_total(7891234.567)
        mock_print.assert_called_once_with('The total amount of USD you have in bitcoin is $7891234.567')

        



if __name__ == '__main__':
    unittest.main()