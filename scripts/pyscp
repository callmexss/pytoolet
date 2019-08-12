#!/usr/bin/python3

import os
import click


@click.command()
@click.option('--upload', help='Upload a file to remote server.')
@click.option('--download', help='Download a file to remote server.')
@click.option('--cmd', default='ls', help='Some handy commands.')
def run(upload, download, cmd):
    """Simple exchange files between two computers."""
    if upload:
        os.system('scp {} root@theoceanside.cn:/home/tester/remote/'.format(upload))
    elif download:
        os.system('scp root@theoceanside.cn:/home/tester/remote/{} .'.format(download))
    else:
        if cmd == 'ls':
            os.system('ssh root@theoceanside.cn ls -l /home/tester/remote')


if __name__ == '__main__':
    run()
