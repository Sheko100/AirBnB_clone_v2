#!/usr/bin/python3
"""Module that creates and distributes an archive to the web servers
"""
from fabric.api import env
do_pack = __import__("1-pack_web_static").do_pack
do_deploy = __import__("2-do_deploy_web_static").do_deploy

env.hosts = ["34.232.68.147", "100.26.230.98"]
env.use = "ubuntu"


def deploy():
    """Creates and deploys an archive to web servers
    """

    arch_path = do_pack()
    if arch_path is None:
        return False

    is_deployed = do_deploy(arch_path)

    return is_deployed
