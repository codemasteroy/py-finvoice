        if ( isinstance( value, basestring ) and 1 <= value.__len__() <= 48 ):
            pass
        else:
            raise_value_error( value, 'Expected value between 1..48 characters' )
        return value
