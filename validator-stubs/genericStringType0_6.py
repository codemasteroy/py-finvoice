        if ( isinstance( value, basestring ) and 0 <= value.__len__() <= 6 ):
            pass
        else:
            raise_value_error( value, 'Expected value between 0..6 characters' )
        return value
