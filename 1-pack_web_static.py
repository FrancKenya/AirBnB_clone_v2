#!/usr/bin/python3
"""
A fabric script that generates a .tgz archive fromm contents
of the web static
"""
from fabric.api import local, task
from datetime import datetime
from pathlib import Path

@task
def do_pack():
    """
    fabric function to generate the .tgz
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
    if results.succeeded:
        print(f"Archive created: {archivepath}")
        return archivepath
    else:
        print("Failed to create the archive.")
        return None
