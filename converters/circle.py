# -*- coding: utf-8 -*-

import math

from converters.base import Converter


class Circle(Converter):
    name = 'Circle'

    _conversors = [
        {
            'category': 'circle',
            'name': 'Radians',
            'si': 'rad',
            '_internal_accepted_names': [
                'rad',
                'radians',
            ],
            '_internal_function_': 'radians',
            '_internal_conversion': {
                'degrees': lambda radians: math.degrees(radians),  # radians to degrees
            }
        },
        {
            'category': 'circle',
            'name': 'Degrees',
            'si': '°',
            '_internal_accepted_names': [
                'deg',
                'degree',
                'degrees',
            ],
            '_internal_function_': 'degrees',
            '_internal_conversion': {
                'radians': lambda degrees: math.radians(degrees),  # degrees to radians
            }
        },
    ]
