import click

from managers import SourceManager


@click.group(help='prefix source managing')
def prefix():
    pass


@prefix.command('add', help='add new prefix')
@click.argument('values')
@click.option('--lang', '-l', default='ko', help='language')
def add(values, lang):
    value_list = values.split(',')
    sm = SourceManager(lang)
    sm.pre_add(value_list)
