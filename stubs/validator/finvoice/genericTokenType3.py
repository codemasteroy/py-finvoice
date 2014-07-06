        if ( isinstance( value, basestring ) ):
            if ( value.__len__() == 3 ):
                pass
            else:
                raise_value_error( value, 'Expected value with 3 characters' )
        else:
            for v in value:
                if ( isinstance( v, basestring ) and v.__len__() <= 3 ):
                    pass
                else:
                    raise_value_error( v, 'Expected value with 3 characters' )
        return value
