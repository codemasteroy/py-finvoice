        if ( isinstance( value, basestring ) and value.__len__() == 2 ):
            pass
        else:
            raise_value_error( value, 'Expected ISO 3166-1 alpha-2' )
        return value
