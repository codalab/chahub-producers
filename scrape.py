import click

from adapters import KaggleAdapter, RampAdapter

@click.command()
@click.option('--adapter_name', help='The adapter to use (kaggle or ramp)')
def scrape(adapter_name):
    scraper = None
    if adapter_name == 'kaggle':
        scraper = KaggleAdapter()
    elif adapter_name == 'ramp':
        scraper = RampAdapter()
    else:
        raise Exception("Unknown adapter specified '{}'!".format(adapter_name))

    scraper.begin()


if __name__ == '__main__':
    scrape()
