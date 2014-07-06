        if ( isinstance( value, basestring ) ):
            if ( 0 <= value.__len__() <= 14 ):
                pass
            else:
                raise_value_error( value, 'Expected value between 0..14 characters' )
        else:
            for v in value:
                if ( isinstance( v, basestring ) and 0 <= v.__len__() <= 14 ):
                    pass
                else:
                    raise_value_error( v, 'Expected value between 0..14 characters' )
        return value
