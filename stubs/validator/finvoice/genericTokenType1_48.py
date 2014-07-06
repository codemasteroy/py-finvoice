        if ( isinstance( value, basestring ) ):
            if ( 1 <= value.__len__() <= 48 ):
                pass
            else:
                raise_value_error( value, 'Expected value between 1..48 characters' )
        else:
            for v in value:
                if ( isinstance( v, basestring ) and 1 <= v.__len__() <= 48 ):
                    pass
                else:
                    raise_value_error( v, 'Expected value between 1..48 characters' )
        import re
        return re.sub( ' {2,}',' ', re.sub( '\t|\r|\n', '', value.strip() ) )
