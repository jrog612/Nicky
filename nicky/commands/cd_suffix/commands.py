import click


@click.group(help='suffix source managing')
def suffix():
    pass


@suffix.command(help='Add new suffix. You can add multiple values with comma separated.')
@click.argument('genre')
@click.argument('values')
@click.option('--lang', '-l', default='ko', help='language')
def add(genre, values, lang):
    value_list = values.split(',')

