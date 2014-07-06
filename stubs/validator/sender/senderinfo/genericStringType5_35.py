        if ( isinstance( value, basestring ) ):
            if ( 5 <= value.__len__() <= 35 ):
                pass
            else:
                raise_value_error( value, 'Expected value between 5..35 characters' )
        else:
            for v in value:
                if ( isinstance( v, basestring ) and 5 <= v.__len__() <= 35 ):
                    pass
                else:
                    raise_value_error( v, 'Expected value between 5..35 characters' )
        return value
