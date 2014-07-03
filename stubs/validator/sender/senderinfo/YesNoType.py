		if ( value != "YES" and value != "NO" ):
			raise_value_error( value, 'Expected "YES" or "NO"' )
		return value
