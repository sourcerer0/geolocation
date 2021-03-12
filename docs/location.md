# Location
## Parameters
```
location
- Type: string or tuple or None

If string: Address or Region
If tuple: Coordinates
If None (standard): Must be defined with obj.location = <tuple or string>
```

## Attributes
### self.time
[Delorean Documentation](https://delorean.readthedocs.io/en/latest/quickstart.html#)
```
- Type: Delorean Class
```

### self.format_time
```
- Description: Formatted self.time
- Type: string
```

### self.timezone
[Timezones Documentation](https://github.com/sourcerer0/geolocation/blob/master/docs/timezones.md)
```
- Type: Timezones Class
```

### self.location
[Geopy Documentation](https://geopy.readthedocs.io/en/stable/#geopy.location.Location)
```
- Description: Location’s raw, unparsed geocoder response. Get from Geopy documentation
- Type: dict
```

### self.format_location
```
- Description: Most useful, formatted information about self.location
```

### self.coordinates
```
- Description: Coordinates from self.location
```


## Methods
### up_time()
```
- Description: Print time when Location was instantiated
- Parameters: None
- Return: None
```
