# geolocation
[Geolocation API](https://hub.docker.com/r/sourcerer2/geolocation)

## Installation
Docker
``` shell script
docker pull sourcerer2/geolocation
```

## Docs
- [API Reference](https://github.com/elleaech/geolocation/blob/master/docs/location.md)

### Basic Usage
Run:
``` bash
docker run --name geo -it sourcerer2/geolocation
```

```python
from geolocation import Location

somehere  = Location() #all empty
somewhere = Location("San Jose, California, USA")

somewhere.location()
somewhere.location = "Beirut, Lebanon" #redefine location

somewhere.coordinates() #get coordinates tuple

somewhere.timezone
somewhere.timezone = <some coordinates> #redefine timezone

somewhere.time
somewhere.format_time #prettify above result

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
