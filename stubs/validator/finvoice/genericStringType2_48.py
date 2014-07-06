        if ( isinstance( value, basestring ) ):
            if ( 2 <= value.__len__() <= 48 ):
                pass
            else:
                raise_value_error( value, 'Expected value between 2..48 characters' )
        else:
            for v in value:
                if ( isinstance( v, basestring ) and 2 <= v.__len__() <= 48 ):
                    pass
                else:
                    raise_value_error( v, 'Expected value between 2..48 characters' )
        return value
