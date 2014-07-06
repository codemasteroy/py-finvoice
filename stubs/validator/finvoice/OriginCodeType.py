        if ( value != "Original" and value != "Copy" and value != "Cancel" ):
            raise_value_error( value, 'Expected "Original", Copy" or "Cancel"' )
        return value
