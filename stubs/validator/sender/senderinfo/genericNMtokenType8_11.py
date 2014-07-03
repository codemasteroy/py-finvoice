        if ( isinstance( value, basestring ) and 8 <= value.__len__() <= 11 ):
            pass
        else:
            raise_value_error( value, 'Expected value between 8..11 characters' )
        return value
