        if ( isinstance( value, basestring ) and 0 <= value.__len__() <= 35 ):
            pass
        else:
            raise_value_error( value, 'Expected value between 0..35 characters' )
        return value
