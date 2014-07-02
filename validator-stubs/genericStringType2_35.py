        if ( isinstance( value, basestring ) and 2 <= value.__len__() <= 35 ):
            pass
        else:
            raise_value_error( value, 'Expected value between 2..35 characters' )
        return value
