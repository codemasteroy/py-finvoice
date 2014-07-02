        if ( isinstance( value, basestring ) and 5 <= value.__len__() <= 35 ):
            pass
        else:
            raise_value_error( value, 'Expected value between 5..35 characters' )
        return value
