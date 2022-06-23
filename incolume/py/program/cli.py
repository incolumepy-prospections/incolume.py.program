import click
from incolume.py.program_core.main import gen_model, gen_info


@click.group()
@click.option('-c',
              "--configfile",
              prompt="Your file config name",
              default="infosaj/model.yml",
              help="Provide your file YAML config name")
@click.option('-o',
              "--outputfile",
              prompt="Your file output name",
              default='infosaj/index.html',
              help="Provide your file HTML output name")
@click.pass_context
def run(ctx, **kwargs):
    """Generate informativo SAJ."""
    ctx.obj = {**kwargs}

@run.command()
@click.argument('subcommand')
@click.pass_context
def help(ctx, subcommand):
    """Show the help for specific command."""
    subcommand_obj = infosaj.get_command(ctx, subcommand)
    if subcommand_obj is None:
        click.echo("I don't know that command.")
    else:
        click.echo(subcommand_obj.get_help(ctx))

@run.command(name='gen')
@click.pass_context
def generator(ctx):
    """Generate informativo SAJ."""
    click.echo(f'{ctx.obj.get("outputfile")}')
    return gen_info(ctx.obj.get('outputfile'))


@run.command()
@click.pass_context
def model(ctx):
    """Generate model config file."""
    click.echo(f'{ctx.obj.get("configfile")}')
    return gen_model(ctx.obj.get('configfile'))

