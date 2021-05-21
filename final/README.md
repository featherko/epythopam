![](https://img.shields.io/badge/code%20style-black-000000.svg)

# Final

## Install dev requirements
`pip install -r requirements.txt`


## Parsing

To parse use Cian_parser.py. Don't forget to put your cookies at the header everytime you pass recapcha thorugh your
browser. That's creating database, and stars to filling it up. Also saves your parse progress.


## Getting geocodes

Put your Google api key with geocoding future on into api_key.py

Once it's done execute geo_parse.py


## Heatmap

With available geocode data in your database heatmap will be build-up and saved at /templates/heatmap.html once you
execute heatmap.py


## Histograms

Run histo.py to create histogram pictures from your db and save tem at /static


## Flask implementation

Run flask_part.py
you will get access to it through 127.0.0.1:5000


## FastApi implementation

Run fastapi_try.py
you can access to it through 127.0.0.1:8000
