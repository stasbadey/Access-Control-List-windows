import re

import click


def validate_mode_file(ctx, param, value):
    if len(value) != 3 or not re.match(r'^[0-7]+$', value):
        raise click.BadParameter("Format must be 3 number from 0-7")
    return value
