# geolocation
[Geolocation Library](https://hub.docker.com/r/sourcerer2/geolocation)

## Installation
Docker
``` shell script
docker pull sourcerer2/geolocation

docker run --name geo -it sourcerer2/geolocation
```

## Docs
- [API Reference](https://github.com/elleaech/geolocation/blob/master/docs/location.md)

### Basic Usage
```python
from geolocation import Location

somewhere = Location("San José, California, USA")
# somewhere = Location() //location is empty

somewhere.location #raw location data
# somewhere.location = "Beirut, Libanon" //redefine location


somewhere.coordinates #tuple
somewhere.format_location #formatted location data

somewhere.timezone #UTC
somewhere.timezone.set_timezone(somewhere.coordinates) #search for location's timezone

somewhere.time #raw time data
somewhere.format_time


somewhere.up_time() #init time
```

## Contributing & Issue Tracker
Branch & [Pull Request](https://github.com/elleaech/geolocation/pulls)
- [Issues](https://github.com/elleaech/geolocation/issues)

### Get source
```shell script
git clone git@github.com:elleaech/geolocation.git && cd geolocation

python3 -m virtualenv . && pip3 install -r requirements.txt
```

## License
[Apache License 2.0](https://github.com/elleaech/geolocation/blob/master/LICENSE)
