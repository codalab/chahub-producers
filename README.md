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


Running on Heroku
=================

1. Get Chahub Producer API keys from a Chahub admin (post an issue on our Github for help with this) for each producer you'd like to make
1. In our case we setup one for Kaggle and one for RAMP
1. Set your API key environment variables on Heroku, like `CHAHUB_API_KEY_KAGGLE` and `CHAHUB_API_KEY_RAMP`
1. Setup Heroku Scheduler (in Resources tab)
1. "Add a new job"
1. Put in the command `python scrape.py`
1. Run it once daily using a free dyno
