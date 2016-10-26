
class Converter(object):

    @classmethod
    def _find_conversor(self, unit):
        unit = unit.lower()
        for conversor in self._conversors:
            if unit in conversor['_internal_accepted_names']:
                return conversor
        return None

    @classmethod
    def convert(cls, from_unit, to_unit, value):
        if hasattr(cls, '_general_method'):
            return cls._general_method(from_unit, to_unit, value)
        else:
            from_u = cls._find_conversor(from_unit)
            return from_u['_internal_conversion'][to_unit](value)
