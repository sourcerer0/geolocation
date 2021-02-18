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

### self.human_time
```
- Description: Formatted self.time
- Type: string
```

### self.location
[Geopy Documentation](https://geopy.readthedocs.io/en/stable/#geopy.location.Location)
```
- Description: Location’s raw, unparsed geocoder response. Get from Geopy documentation
- Type: dict
```

### self.human_location
```
- Description: Most useful, formatted information about self.location
```

### self.__timezone
```
- Description: Timezone. Initialized as UTC
- Type: string
```


## Methods
### set_timezone()
```
- Description: Finds a probable timezone instead of UTC
- Parameters: None
- Return: None
```

### up_time()
```
- Description: Print time when Location was instantiated
- Parameters: None
- Return: None
```
