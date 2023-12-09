#!/usr/bin/python3
"""Fabric file to archive the web_static directory
"""
from fabric.operations import local
import datetime
import os


def do_pack():
    """generates a tgz archive from the contents of the web_static directory
    """
    d = datetime.datetime.now()
    y = d.year
    m = d.strftime("%m")
    da = d.strftime("%d")
    h = d.hour
    mi = d.minute
    sec = d.second

    output_name = "web_static_{}{}{}{}{}{}.tgz".format(y, m, da, h, mi, d.sec)

    if not os.path.isdir("./versions"):
        os.mkdir("./versions")

    try:
        local("tar -cvzf versions/{} web_static".format(output_name))
        return "versions/{}".format(output_name)
    except err:
        return None
