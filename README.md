# csvtojsonp

A very tiny little Google Appengine-based proxy for loading CSVs on 3rd party servers into your JS application

## hacking

Install the [cloud SDK](https://cloud.google.com/sdk/docs/), the App Engine for Python (component id app-engine-python) and the datastore emulator (component id cloud-datastore-emulator).

Run a dev server with:

```
dev_appserver.py app.yaml
```

Test with:

```
curl http://localhost:8080?url=https://raw.githubusercontent.com/mrmonkington/csvtojsonp/master/test.csv
```

## Installation

You need to deploy to Google Cloud App Engine - which is a bit out of scope for this README. But [these instructions are good](https://cloud.google.com/appengine/docs/standard/python/getting-started/deploying-the-application).

## Usage

```
http://host?url=<some_urlencoded_url_of_a_CSV_file>
```

You get the idea :-)
