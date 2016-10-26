# -*- coding: utf-8 -*-

from converters.exceptions import ConversionError, RequireAdditionalParamError


class UnitsManager(object):
    '''
    Class responsible to manage the unit converters
    of this application.
    '''
    _units = ()

    def __init__(self, *ag, **kw):
        from converters import circle
        from converters import currency
        from converters.electric import electric
        from converters.force import force
        from converters.pressure import pressure
        from converters.speed import speed
        from converters.temperature import temperature

        self._units = (
            circle.Circle,
            currency.Currency,
            electric,
            force,
            pressure,
            speed,
            temperature,
        )

    def __iter__(self):
        yield (x for x in self._units)

    def register(self, converter):
        '''
        Method that receives a new converter and adds it to
        this manager.
        Useful to add custom new methods without needing to edit
        the core of this application.
        '''
        if converter is not None and callable(converter):
            self._units.append(converter)

    def find_unit_converter(self, unit):
        '''
        Internal: Load the conversor of one unit from the UNITS array
        :param unit: The unit which should be included in the
            '_internal_accepted_names' in a conversor of the UNITS array
        :return: The conversor from the UNITS array or None if none was found
        '''
        unit = unit.lower()
        for conversor in self._units:
            for cat in conversor._conversors:
                if unit in cat['_internal_accepted_names']:
                    return conversor
        return None

    def find_unit(self, unit):
        '''
        Internal: Load one specific unit from the UNITS array
        :param unit: The name of the unit (should be included
            in the '_internal_accepted_names' or 'name')
        :return: The unit from the UNITS array or None if none was found
        '''
        unit = unit.lower()
        for category in self._units:
            for cat in category._conversors:
                if unit in cat['_internal_accepted_names']:
                    return cat
        return None

    def find_unit_name(self, unit):
        '''
        Internal: Load one specific unit from the UNITS array
        :param unit: The name of the unit (should be included
            in the '_internal_accepted_names' or 'name')
        :return: The unit from the UNITS array or None if none was found
        '''
        unit = unit.lower()
        for category in self._units:
            for cat in category._conversors:
                if unit in cat['_internal_accepted_names']:
                    return cat['_internal_function_']
        return None

    def can_convert(self, from_unit, to_unit):
        '''
        Check if the given units can be converted
        :param from_unit: The source unit to convert from
        :param to_unit: The target unit to convert to
        :return: bool - true if unit can be converted
                        false otherwise
        '''
        # There must be an implementation to convert the units
        from_unit = self.find_unit_converter(from_unit)
        to_unit = self.find_unit_converter(to_unit)

        if from_unit is None or to_unit is None:
            return False

        # The units have to be in the same category
        # (mph to watts does not make any sense)
        if from_unit != to_unit:
            return False

        return True

    def get_si(self, unit):
        '''
        Load the SI string for the given unit
        :param unit: The unit for which the SI string should be loaded
        :return: String - SI string or None if none was found
        '''
        cat_unit = self.find_unit(unit)
        if cat_unit is None:
            return None
        return cat_unit['si']

    def convert(self, from_unit, to_unit, value, *args, **kwargs):
        '''
        Convert the value from one unit to another
        :param from_unit: Source unit
        :param to_unit: Target unit
        :param args: Additional parameters (values)
        :param kwargs: Additional parameters (additional values
            like for conversion watts to ohms)
        :return: Converted number
        '''
        if not self.can_convert(from_unit, to_unit):
            raise ConversionError(
                'Cannot convert from {0} to {1}'.format(from_unit, to_unit))

        conversor = self.find_unit_converter(from_unit)
        to_unit = self.find_unit_name(to_unit)

        return conversor.convert(from_unit, to_unit, value)

        # raise ConversionError('No conversion possible')


UNITS = UnitsManager()
