        if ( isinstance( value, basestring ) ):
            if ( 1 <= value.__len__() <= 8 ):
                pass
            else:
                raise_value_error( value, 'Expected value between 1..8 characters' )
        else:
            for v in value:
                if ( isinstance( v, basestring ) and 1 <= v.__len__() <= 8 ):
                    pass
                else:
                    raise_value_error( v, 'Expected value between 1..8 characters' )
        return value
