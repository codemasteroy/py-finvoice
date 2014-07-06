        import re
        if ( isinstance( value, basestring ) ):
            if ( re.match( '[0-9]{1,15}(,[0-9]{1,6})?', value ) ):
                pass
            else:
                raise_value_error( value, 'Expected value in the format [0-9]{1,15}(,[0-9]{1,6})?' )
        else:
            for v in value:
                if ( isinstance( v, basestring ) and re.match( '[0-9]{1,15}(,[0-9]{1,6})?', value) ):
                    pass
                else:
                    raise_value_error( v, 'Expected value in the format [0-9]{1,15}(,[0-9]{1,6})?' )
        return value
