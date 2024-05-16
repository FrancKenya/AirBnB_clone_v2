#!/usr/bin/python3

"""
A fabric script that deletes out of date archives using the do_clean fuction
"""

from fabric.api import *
from pathlib import Path
import os

env.hosts = ['54.237.97.75', '100.25.144.98']

@task
def do_clean(number=0):
    """
    Function deleting unwanted archives
    Args:
         number: the number of the archives, including the most recent, to keep
         If number is 0 or 1, keep only the most recent version of your archive.
         if number is 2, keep the most recent, and second most recent versions
         of your archive.
    """
    path = Path("versions")
    files = sorted(path.glob("web_static_*.tgz"), key=os.path.getmtime)
    
    
    if number == 0 or number == 1:
       kept_archives = files[-1:]
    else:
        kept_archives = files[-number:]

    with cd("versions"):
       for i in files:
          if str(i) not in kept_archives:
              local(f"rm -r {i}")

    env_paths = Path("/data/web_static/releases")
    with cd("/data/web_static/releases"):
        filesNames = sorted(env_paths.glob("web_static_*.tgz"), key=os.path.getmtime)
        for i in filesNames:
            if str(i) not in kept_archives:
                run(f"rm -r {i}")