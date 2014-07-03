        codes = [ '00', '01', '02' ]
        if ( value in codes ):
            pass
        else:
            raise_value_error( value, 'Expected ' + ' or '.join( codes ) )
        return value
