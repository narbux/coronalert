# CoronAlert

Program that checks Dutch Corona Vaccination program for birth years that can make appointments.

## Configuration

Environment variables:

- GOTIFY_KEY
- GOTIFY_URL
- YEARS

## Sample docker-compose.yml

```YAML
version: '3'

services:
  coronalert:
    image: narbux/coronalert:latest
    container_name: coronalert
    restart: unless-stopped
    environment:
      - "GOTIFY_KEY=KEY"
      - "GOTIFY_URL=URL"
      - "YEARS=1950,1960"
```
