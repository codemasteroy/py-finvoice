        if ( value != "PAID" and value != "NOTPAID" and value != "PARTLYPAID" ):
            raise_value_error( value, 'Expected "PAID", "NOTPAID" or "PARTLYPAID"' )
        return value
