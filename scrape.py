import click

from adapters import KaggleAdapter, RampAdapter

@click.command()
@click.option('--adapter_name', help='The adapter to use (kaggle or ramp)')
def scrape(adapter_name):
    scrapers = []
    if adapter_name == 'kaggle' or not adapter_name:
        scrapers.append(KaggleAdapter())

    if adapter_name == 'ramp' or not adapter_name:
        scrapers.append(RampAdapter())

    if adapter_name and not scrapers:
        # We got an adapter name, but it didn't match any of the above
        raise Exception("Unknown adapter specified '{}'!".format(adapter_name))

    for scraper in scrapers:
        scraper.begin()


if __name__ == '__main__':
    scrape()
