import click


@click.group(help='suffix source managing')
@click.argument('action')
@click.argument('genre')
@click.argument('value')
@click.option('--lang', default='ko', help='language')
def suffix(action, genre, value, lang):
    pass



