import click

from adapters import KaggleAdapter, RampAdapter

@click.command()
@click.option('--adapter', help='The adapter to use (kaggle or ramp)')
def scrape(adapter):
    scrapers = []
    if adapter == 'kaggle' or not adapter:
        scrapers.append(KaggleAdapter())

    if adapter == 'ramp' or not adapter:
        scrapers.append(RampAdapter())

    if adapter and not scrapers:
        # We got an adapter name, but it didn't match any of the above
        raise Exception("Unknown adapter specified '{}'!".format(adapter))

    for scraper in scrapers:
        print("Starting scraper: {}".format(scraper.__class__.__name__))
        scraper.begin()


if __name__ == '__main__':
    scrape()
