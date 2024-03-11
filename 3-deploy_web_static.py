#!/usr/bin/python3
"""Module that creates and distributes an archive to the web servers
"""

import datetime
from fabric.api import run, env, put
from fabric.operations import local
from fabric.utils import puts
import os

env.hosts = ["54.236.48.120", "100.25.146.107"]
env.user = "ubuntu"


def do_pack():
    """generates a tgz archive from the contents of the web_static directory
    """
    d = datetime.datetime.now()
    y = d.strftime("%Y")
    m = d.strftime("%m")
    da = d.strftime("%d")
    h = d.strftime("%H")
    mi = d.strftime("%M")
    sec = d.strftime("%S")

    output_name = "web_static_{}{}{}{}{}{}.tgz".format(y, m, da, h, mi, sec)
    path = "versions/{}".format(output_name)

    if not os.path.isdir("./versions"):
        os.mkdir("./versions")

    puts("Packing web_static to {}".format(path))
    try:
        if local("tar -cvzf {} web_static".format(path)).succeeded:
            puts("web_static packed: {}".format(path))
            return path
    except Exception:
        return None


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


def deploy():
    """Creates and deploys an archive to web servers
    """

    arch_path = do_pack()
    if arch_path is None:
        return False

    is_deployed = do_deploy(arch_path)

    return is_deployed
