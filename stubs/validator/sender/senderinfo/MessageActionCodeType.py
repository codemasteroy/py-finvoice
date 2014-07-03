        actions = [ 'ADD', 'CHANGE', 'DELETE' ]
        if ( value in actions ):
            pass
        else:
            raise_value_error( value, 'Expected ' + ' or '.join( actions ) )
        return value
