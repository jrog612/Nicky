import click

from managers import SourceManager


@click.group(help='suffix source managing')
def suffix():
    pass


@suffix.command(help='Add new suffix. You can add multiple values with comma separated.')
@click.argument('genre')
@click.argument('values')
@click.option('--lang', '-l', default='ko', help='language')
def add(genre, values, lang):
    value_list = values.split(',')
    sm = SourceManager(lang)
    sm.suf_add(genre, value_list)


@suffix.command(help='Ordering suffix file')
@click.argument('genre', default=None)
@click.option('--lang', '-l', default='ko', help='language')
def ordering(genre, lang):
    sm = SourceManager(lang)
    sm.suf_ordering(genre)
