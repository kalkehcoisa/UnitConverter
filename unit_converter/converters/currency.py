# -*- coding: utf-8 -*-
import requests
import json
from unit_converter.converters.exceptions import ConversionError

from unit_converter.converters.base import Converter


class Currency(Converter):
    name = 'Currency'

    @classmethod
    def _general_method(cls, from_unit, to_unit, value):
        return cls.cur_to_cur(from_unit, to_unit, value)

    _conversors = [
        {
            'name': 'Australian dollars',
            'si': 'AUD',
            '_internal_accepted_names': [
                'aud',
                'australian dollar',
                'australian dollars',
            ],
            '_internal_function_': 'aud',
        },
        {
            'name': 'Bulgarian lev',
            'si': 'BGN',
            '_internal_accepted_names': [
                'bgn',
                'bulgarian lev',
                'lev',
            ],
            '_internal_function_': 'bgn',
        },
        {
            'name': 'Brazil reais',
            'si': 'BRL',
            '_internal_accepted_names': [
                'brl',
                'brazil reais',
            ],
            '_internal_function_': 'brl',
        },
        {
            'name': 'Canadian dollar',
            'si': 'CAD',
            '_internal_accepted_names': [
                'cad',
                'canadian dollar',
            ],
            '_internal_function_': 'cad',
        },
        {
            'name': 'Swiss francs',
            'si': 'CHF',
            '_internal_accepted_names': [
                'chf',
                'franc',
                'francs',
                'swiss franc',
                'swiss francs',
            ],
            '_internal_function_': 'chf',
        },
        {
            'name': 'Chinese yuan',
            'si': 'CNY',
            '_internal_accepted_names': [
                'cny',
                'yuan',
                'chinese yuan',
            ],
            '_internal_function_': 'cny',
        },
        {
            'name': 'Czech koruny',
            'si': 'CZK',
            '_internal_accepted_names': [
                'czk',
                'czech koruny',
            ],
            '_internal_function_': 'czk',
        },
        {
            'name': 'Danish kroner',
            'si': 'DKK',
            '_internal_accepted_names': [
                'dkk',
                'danish kroner',
            ],
            '_internal_function_': 'dkk',
        },
        {
            'name': 'British pounds',
            'si': 'GBP',
            '_internal_accepted_names': [
                'gbp',
                'pounds',
                'british pounds',
            ],
            '_internal_function_': 'gbp',
        },
        {
            'name': 'Euros',
            'si': 'EUR',
            '_internal_accepted_names': [
                'eur',
                'euro',
                'euros',
            ],
            '_internal_function_': 'eur',
        },
        {
            'name': 'Hong Kong dollars',
            'si': 'HKD',
            '_internal_accepted_names': [
                'hkd',
                'hong kong dollar',
                'hong kong dollars',
            ],
            '_internal_function_': 'hkd',
        },
        {
            'name': 'Croatian kune',
            'si': 'HRK',
            '_internal_accepted_names': [
                'hrk',
                'croatian kune',
            ],
            '_internal_function_': 'hrk',
        },
        {
            'name': 'Hungarian Forint',
            'si': 'HUF',
            '_internal_accepted_names': [
                'huf',
                'hungarian forint',
            ],
            '_internal_function_': 'huf',
        },
        {
            'name': 'Indonesian Rupiah',
            'si': 'IDR',
            '_internal_accepted_names': [
                'idr',
                'rupiah',
                'indonesian rupiah',
            ],
            '_internal_function_': 'idr',
        },
        {
            'name': 'Israeli Shekel',
            'si': 'ILS',
            '_internal_accepted_names': [
                'ils',
                'shekel',
                'israeli shekel',
            ],
            '_internal_function_': 'ils',
        },
        {
            'name': 'Indian rupees',
            'si': 'INR',
            '_internal_accepted_names': [
                'inr',
                'rupees',
                'indian rupees',
            ],
            '_internal_function_': 'inr',
        },
        {
            'name': 'Japanese yen',
            'si': 'JPY',
            '_internal_accepted_names': [
                'jpy',
                'yen',
                'japanese yen',
            ],
            '_internal_function_': 'jpy',
        },
        {
            'name': 'South Korean won',
            'si': 'KRW',
            '_internal_accepted_names': [
                'krw',
                'won',
                'south korean won',
            ],
            '_internal_function_': 'krw',
        },
        {
            'name': 'Mexican pesos',
            'si': 'MXN',
            '_internal_accepted_names': [
                'mxn',
                'pesos',
                'mexican pesos',
            ],
            '_internal_function_': 'mxn',
        },
        {
            'name': 'Malaysian Ringgit',
            'si': 'MYR',
            '_internal_accepted_names': [
                'myr',
                'ringgit',
                'malaysian ringgit',
            ],
            '_internal_function_': 'myr',
        },
        {
            'name': 'Norwegian krone',
            'si': 'NOK',
            '_internal_accepted_names': [
                'nok',
                'norwegian krone',
            ],
            '_internal_function_': 'nok',
        },
        {
            'name': 'New Zealand dollars',
            'si': 'NZD',
            '_internal_accepted_names': [
                'nzd',
                'new zealand dollars',
            ],
            '_internal_function_': 'nzd',
        },
        {
            'name': 'Philippines peso',
            'si': 'PHP',
            '_internal_accepted_names': [
                'php',
                'philippines peso',
            ],
            '_internal_function_': 'php',
        },
        {
            'name': 'Polish zloty',
            'si': 'PLN',
            '_internal_accepted_names': [
                'pln',
                'zloty',
                'polish zloty',
            ],
            '_internal_function_': 'pln',
        },
        {
            'name': 'Romanian Leu',
            'si': 'RON',
            '_internal_accepted_names': [
                'ron',
                'leu',
                'romanian leu',
            ],
            '_internal_function_': 'ron',
        },
        {
            'name': 'Russian ruble',
            'si': 'RUB',
            '_internal_accepted_names': [
                'rub',
                'ruble',
                'russian ruble',
            ],
            '_internal_function_': 'rub',
        },
        {
            'name': 'Swedish kronor',
            'si': 'SEK',
            '_internal_accepted_names': [
                'sek',
                'kronor',
                'swedish kronor',
            ],
            '_internal_function_': 'sek',
        },
        {
            'name': 'Singapore dollars',
            'si': 'SGD',
            '_internal_accepted_names': [
                'sgd',
                'singapore dollar',
                'singapore dollars',
            ],
            '_internal_function_': 'sgd',
        },
        {
            'name': 'Thai baht',
            'si': 'THB',
            '_internal_accepted_names': [
                'thb',
                'baht',
                'thai baht',
            ],
            '_internal_function_': 'thb',
        },
        {
            'name': 'Turkish Lira',
            'si': 'TRY',
            '_internal_accepted_names': [
                'try',
                'lira',
                'turkish lira',
            ],
            '_internal_function_': 'try',
        },
        {
            'name': 'US Dollar',
            'si': 'USD',
            '_internal_accepted_names': [
                'usd',
                'dollar',
                'dollars',
                'us dollar',
                'us dollars',
            ],
            '_internal_function_': 'usd',
        },
        {
            'name': 'South African rands',
            'si': 'ZAR',
            '_internal_accepted_names': [
                'zar',
                'rands',
                'south african rands',
            ],
            '_internal_function_': 'zar',
        },
    ]

    # this is the only needed converter function (requesting http://fixer.io/)
    # the currencies to convert from and to are given as params
    @classmethod
    def cur_to_cur(cls, from_unit, to_unit, money):
        '''
        Converts money from from_unit to to_unit
        :param from_unit: The currency to convert from
        :param to_unit: The currency to convert to
        :param money: The given amount of money to convert
        :return: Converted money in to_unit
        '''
        session = requests.Session()
        session.trust_env = False  # disable proxy settings

        response = session.get(cls._build_convert_url(from_unit, to_unit))
        if response.ok:
            result = json.loads(response.content.decode('utf-8'))
            return money * float(result['rates'][to_unit.upper()])
        raise ConversionError(
            'Could not load current exchange rates from server')

    @classmethod
    def _build_convert_url(cls, from_unit, to_unit):
        url = 'https://api.fixer.io/latest?base={base}&symbols={tgt}'.format(
            base=from_unit,
            tgt=to_unit.upper()
        )
        return url
