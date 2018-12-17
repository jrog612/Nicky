#! /usr/bin/env python
import importlib
import os

import click

from utils import COMMANDS_PATH


@click.group()
def cli():
    pass


for i in os.listdir(COMMANDS_PATH):
    if i.find('cd_') == 0:
        module = importlib.import_module('commands.{}'.format(i))
        cli.add_command(getattr(module, i.replace('cd_', '')))
    else:
        continue

if __name__ == '__main__':
    cli()
