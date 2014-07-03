        identifiers = [ '00', '02' ]
        if ( value in identifiers ):
            pass
        else:
            raise_value_error( value, 'Expected "00" or "02"' + ' or '.join( identifiers ) )
        return value
