# Location
## Parameters
```
location
- Type: string or tuple or None

If string: Address or Region
If tuple: Coordinates
If None (standard): Must be defined with obj.location = <tuple or string>
```

## Properties
### time
[Delorean Documentation](https://delorean.readthedocs.io/en/latest/quickstart.html#)
```
- Type: Delorean Class
```

### format_time
```
- Description: Formatted time
- Type: string
```

### timezone
[Timezones Documentation](https://github.com/sourcerer0/geolocation/blob/master/docs/timezones.md)
```
- Type: Timezones Class
```

### location
[Geopy Documentation](https://geopy.readthedocs.io/en/stable/#geopy.location.Location)
```
- Description: Location’s raw, unparsed geocoder response. Get from Geopy documentation
- Type: dict
```

### format_location
```
- Description: Most useful, formatted information about location
```

### coordinates
```
- Description: Coordinates from location
```

### up_time
```
- Description: Print time when Location was instantiated
```
