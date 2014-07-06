        if ( isinstance( value, basestring ) ):
            if ( 1 <= value.__len__() <= 70 ):
                pass
            else:
                raise_value_error( value, 'Expected value between 1..70 characters' )
        else:
            for v in value:
                if ( isinstance( v, basestring ) and 1 <= v.__len__() <= 70 ):
                    pass
                else:
                    raise_value_error( v, 'Expected value between 1..70 characters' )
        return value
