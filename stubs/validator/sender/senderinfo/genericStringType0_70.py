        if ( isinstance( value, basestring ) and 0 <= value.__len__() <= 70 ):
            pass
        else:
            raise_value_error( value, 'Expected value between 0..70 characters' )
        return value
