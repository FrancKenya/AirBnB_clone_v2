#!/usr/bin/python3
""" A fabric script that distributes an archive to web servers """

from fabric.api import sudo, put, env
from pathlib import Path
env.hosts = ['18.207.3.97', '100.26.212.29']


def do_deploy(archive_path):
    """
    Deploys to server locations
    Args:
        archive_path: Path to the archive
    Returns:
        True if successful, false if otherwise
    """
    path_obj = Path(archive_path)
    if not path_obj.exists():
        return False

    tmpDest = f"/tmp/{path_obj.name}"
    destDir = f"/data/web_static/releases/{path_obj.stem}/"
    # Upload archive to tmp
    put(archive_path, tmpDest)

    # Execute deployment steps
    exec_1 = sudo(f"mkdir -p {destDir}")
    exec_2 = sudo(f"tar -xzf {tmpDest} -C {destDir}")
    exec_3 = sudo(f"rm {tmpDest}")
    exec_4 = sudo(f"mv {destDir}/web_static/* {destDir}")
    exec_5 = sudo(f"rm -rf {destDir}/web_static")
    exec_6 = sudo(f"rm -rf /data/web_static/current")
    exec_7 = sudo(f"ln -s {destDir} /data/web_static/current")
    exec_list = [exec_1, exec_2, exec_3, exec_4, exec_5, exec_6, exec_7]
    return True if all([obj.succeeded for obj in exec_list]) else False
