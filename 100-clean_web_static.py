#!/usr/bin/python3
"""Module to clean out-of-date archives
"""
from fabric.api import env, local, run
env.hosts = ["34.232.68.147", "100.26.230.98"]
env.user = "ubuntu"


def do_clean(number=0):
    """Cleans the out-of-date archives locally and on the web servers
    """

    result = local("ls -ltr versions", capture=True)

    limit = 1 if number == 0 else int(number)
    arch_lst = result.split('\n')
    arch_date = []
    for arch in arch_lst[1:]:
        arch_date.append(arch[-18:-4])
    arch_count = len(arch_date)

    while (limit > 0):
        date = arch_date[limit - 1]
        lcl_arch = "versions/web_static_{}.tgz".format(date)
        rmt_arch = "/data/web_static/releases/web_static.{}".format(date)
        local("rm {}".format(lcl_arch))
        run("rm -r {}".format(rmt_arch))
        limit = limit - 1
