        if ( isinstance( value, basestring ) and 1 <= value.__len__() <= 35 ):
            pass
        else:
            raise_value_error( value, 'Expected value between 1..35 characters' )
        return value
