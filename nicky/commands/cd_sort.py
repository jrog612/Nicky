import click

from managers import SourceManager


@click.command(help='Sorting suffix or prefix file')
@click.argument('kind', default=None)
@click.option('--lang', '-l', default='ko', help='language')
def sort(kind, lang):
    sm = SourceManager(lang)
    if kind in ('p', 'pre', 'prefix'):
        sm.pre_sorting()
    else:
        sm.suf_ordering(kind)