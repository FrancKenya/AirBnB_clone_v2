#!/usr/bin/python3

"""
A fabric script tha imports a function to create and deploy an archive
"""

from fabric.api import *
do_pack = __import__("1-pack_web_static").do_pack
do_deploy = __import__("2-do_deploy_web_static").do_deploy

env.hosts = ['54.237.97.75', '100.25.144.98']
new_archive_path = do_pack()


@task
def deploy():
    """
    Deploys to server locations
    Return:
        The return value of do_deploy or False if no archive has been created
    """

    if not new_archive_path:
        return False

    else:
        return do_deploy(new_archive_path)
