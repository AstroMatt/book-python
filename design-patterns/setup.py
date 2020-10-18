#!/usr/bin/env python3

from datetime import datetime, timezone
from os import makedirs
from os.path import dirname, abspath, join, basename
from shlex import split
from shutil import rmtree
from subprocess import run


FORMAT = 'html'


SECOND = 1
MINUTE = 60 * SECOND
START_TIME = datetime.now()

sourcedir = dirname(abspath(__file__))
project_name = basename(sourcedir)
outdir = join('/tmp/', project_name)
rmtree(outdir, ignore_errors=True)
makedirs(outdir, exist_ok=True)
run('clear')
cmd = split(f'sphinx-build -a -E -j auto --color -b {FORMAT} {sourcedir} {outdir}')
run(cmd)

last = run('git log -1 --format="%ad" --date=iso', shell=True, capture_output=True).stdout.strip().decode()
last = datetime.strptime(last, '%Y-%m-%d %H:%M:%S %z')
delta = datetime.now(tz=timezone.utc) - last
since = round(delta.total_seconds() / MINUTE)

duration = datetime.now() - START_TIME
duration_seconds = round(duration.total_seconds())
duration_minutes = round(duration_seconds / MINUTE, 1)

print(f'\n\n')
print(f'Build took: {duration_seconds} seconds ({duration_minutes} minutes)')
print(f'Last commit: {last}')
print(f'Since: {since}m')
