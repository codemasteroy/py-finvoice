        if ( isinstance( value, basestring ) ):
            if ( 0 <= value.__len__() <= 70 ):
                pass
            else:
                raise_value_error( value, 'Expected value between 0..70 characters' )
        else:
            for v in value:
                if ( isinstance( v, basestring ) and 0 <= v.__len__() <= 70 ):
                    pass
                else:
                    raise_value_error( v, 'Expected value between 0..70 characters' )
        return value
