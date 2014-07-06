        if ( isinstance( value, basestring ) ):
            if ( 8 <= value.__len__() <= 11 ):
                pass
            else:
                raise_value_error( value, 'Expected value between 8..11 characters' )
        else:
            for v in value:
                if ( isinstance( v, basestring ) and 8 <= v.__len__() <= 11 ):
                    pass
                else:
                    raise_value_error( v, 'Expected value between 8..11 characters' )
        return value
