Produces content for Chahub.

Installation
============

```
$ git clone git@github.com:codalab/chahub-producers.git
$ cd chahub-producers
$ pip install -r requirements.txt
```

You'll need to get an **API KEY** from a Chahub admin, please post an issue if you'd like to produce content for Chahub!

Usage
=====

```bash
$ export CHAHUB_API_URL='https://chahub.org/api/v1/'
# You can only get a Chahub API key from a Chahub admin
$ export CHAHUB_API_KEY=123925d-ac20-455c-asdf-bf624asdfbef
$ python scrape.py --adapter_name kaggle
```

