        if ( isinstance( value, basestring ) and 0 <= value.__len__() <= 512 ):
            pass
        else:
            raise_value_error( value, 'Expected value between 0..512 characters' )
        return value
