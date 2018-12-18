import click

from nicky.managers import SourceManager


@click.command(help='Add new suffix or Prefix. You can add multiple values with comma separated.')
@click.argument('kind')
@click.argument('values')
@click.option('--lang', '-l', default='ko', help='language')
def add(kind, values, lang):
    sm = SourceManager(lang)
    value_list = values.split(',')

    if kind in ('p', 'pre', 'prefix'):
        sm.pre_add(value_list)
    else:
        sm.suf_add(kind, value_list)