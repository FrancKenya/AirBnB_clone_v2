#!/usr/bin/python3
"""
This is a fabric script that generates a .tgz archive fromm contents
of the web static
"""

from datetime import datetime
from fabric.api import *
from pathlib import Path


@task
def do_pack():
    """
    A function generating the .tgz
    Returns:
        Archive path if successful
    """
    # check if version folder exists and create if not existing
    if not Path("versions").exists():
        Path("versions").mkdir()

    # Generate archive name
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    archivepath = f"versions/web_static_{time}.tgz"
    # compress web static folder
    results = local(f"tar -cvzf {archivepath} web_static")
    # check if successful and return the path of the archive
    return archivepath
