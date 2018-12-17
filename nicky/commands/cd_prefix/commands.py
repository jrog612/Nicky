import click


@click.group(help='prefix source managing')
def prefix():
    pass


@prefix.command('add', help='add new prefix')
@click.argument('action')
@click.argument('values')
@click.option('--lang', '-l', default='ko', help='language')
def add(action, value, lang):
    pass
