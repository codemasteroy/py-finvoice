		if ( value.__len__() > 35 ):
            raise_value_error( value, 'Expected value less than 35 characters' )
        return value
