import click
import sys
sys.path.append('/home/qabilitto/Documents/daterenamer_project')
from renamer.rename_file import DateRenamer
from sys import platform as _platform

import logging
import logging.handlers

logger=logging.getLogger('')
destinations_hash = {"linux":'/dev/log','linux2':'/dev/log','darwin':'var/run/syslog'}

def address_matcher(plt):
    return destinations_hash.get(plt,('localhost',514))

handler=logging.handlers.SysLogHandler(address=address_matcher(_platform))

logger.addHandler(handler)

def print_version(ctx,param,value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('Developed by Techacademy')
    click.echo('dateranamer: v0.1')
    ctx.exit()

@click.command()
@click.option('-p', '--path', help='File name with pull path')
@click.option('-l', 
                '--log', 
                default='WARNING', 
                show_default=True, 
                type=click.Choice([
                    'DEBUG',
                    'INFO',
                    'WARNING',
                    'ERROR',
                    'CRITICAL'
                ]),
                help='Set log level')
@click.option('-v','--verbose',is_flag=True,help="Be verbose (print to console)")
@click.option('--version',
            is_flag=True,
            callback=print_version,
            expose_value=False,
            is_eager=True,
            help='version information.')
@click.pass_context
def all_procedure(ctx,path,log,verbose):
    logger.setLevel(log)

    formatter=logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')

    if verbose:
        ch=logging.StreamHandler()
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    if path:
        obj = DateRenamer(filename=path)
        obj.rename_it()

if __name__ == '__main__':
    all_procedure()