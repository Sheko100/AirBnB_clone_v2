#!/usr/bin/python3
"""Fabric file to archive the web_static directory
"""
from fabric.operations import local
from fabric.utils import puts
import datetime
import os


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
