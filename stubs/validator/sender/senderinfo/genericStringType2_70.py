        if ( isinstance( value, basestring ) and 2 <= value.__len__() <= 70 ):
            pass
        else:
            for v in value:
                if ( isinstance( v, basestring ) and 2 <= v.__len__() <= 70 ):
                    pass
                else:
                    raise_value_error( v, 'Expected value between 2..70 characters' )
        return value
