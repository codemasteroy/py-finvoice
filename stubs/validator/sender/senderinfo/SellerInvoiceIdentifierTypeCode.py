        identifiers = [ '01', '02', '03', '04', '05', '06', '07', '08', '09','99' ]
        if ( value in identifiers ):
            pass
        else:
            raise_value_error( value, 'Expected ' + ' or '.join( identifiers ) )
        return value
