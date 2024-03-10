#!/usr/bin/python3
"""Module to distrbute archive to the web servers
"""
import os
from fabric.api import run, env, put

env.hosts = ["54.236.48.120", "100.25.146.107"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """Deploys archive file to the web servers
    """

    if not os.path.exists(archive_path):
        return False

    arch_name = archive_path[9:-4]
    remote_path = "/data/web_static/releases/{}/".format(arch_name)

    if put(archive_path, "/tmp/").failed:
        return False

    if run("mkdir /data/web_static/releases/{}".format(arch_name)).failed:
        return False

    if run("tar -xzf /tmp/{}.tgz -C {}".format(arch_name, remote_path)).failed:
        return False

    if run("rm /tmp/{}.tgz".format(arch_name)).failed:
        return False

    if run("mv {}web_static/* {}".format(remote_path, remote_path)).failed:
        return False

    if run("rm -rf {}web_static".format(remote_path)).failed:
        return False

    if run("rm -rf /data/web_static/current").failed:
        return False

    if run("ln -s {} /data/web_static/current".format(remote_path)).failed:
        return False

    print("New version deployed!")
    return True
