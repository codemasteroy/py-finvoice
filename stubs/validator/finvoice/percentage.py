        import re
        if ( isinstance( value, basestring ) ):
            if ( re.match( '[1-9]?[0-9]{1,2}(,[0-9]{1,3})?', value ) ):
                pass
            else:
                raise_value_error( value, 'Expected value in the format [1-9]?[0-9]{1,2}(,[0-9]{1,3})?' )
        else:
            for v in value:
                if ( isinstance( v, basestring ) and re.match( '[1-9]?[0-9]{1,2}(,[0-9]{1,3})?', value) ):
                    pass
                else:
                    raise_value_error( v, 'Expected value in the format [1-9]?[0-9]{1,2}(,[0-9]{1,3})?' )
        return value
