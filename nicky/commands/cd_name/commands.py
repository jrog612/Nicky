import click

from base import Nicky


@click.command(help='nickname generating')
@click.argument('count', default=1)
@click.option('--genre', '-g', help='suffix genre')
@click.option('--lang', '-l', default='ko', help='language')
def name(count, genre, lang):
    nicky = Nicky(lang)
    nickname = nicky.get_nickname(count, genre)
    print('\n'.join(nickname))
