#!/usr/bin/python3
""" distributes archive to web servers
based on 2-do_deploy_web_static.py"""
import time
import os
from fabric.api import *
from fabric.operations import run, put


env.hosts = ['100.26.161.5', '3.85.148.233']


def do_pack():
    """ generate .tgz archive 1-pack_web_static.py"""
    try:
        local_time = time.strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{:s}.tgz web_static/".
              format(local_time))
        return "versions/web_static_{:s}.tgz".format(local_time)
    except Exception:
        return


def do_deploy(archive_path):
    """ distribute archive to web servers """
    if os.path.isfile(archive_path) is False:
        return False
    try:
        filename = archive_path.split("/")[-1]
        no_ext = filename.split(".")[0]
        path_no_ext = "/data/web_static/releases/{}/".format(no_ext)
        symlink = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(path_no_ext))
        run("tar -xzf /tmp/{} -C {}".format(filename, path_no_ext))
        run("rm /tmp/{}".format(filename))
        run("mv {}web_static/* {}".format(path_no_ext, path_no_ext))
        run("rm -rf {}web_static".format(path_no_ext))
        run("rm -rf {}".format(symlink))
        run("ln -s {} {}".format(path_no_ext, symlink))
        return True
    except ValueError:
        return False


def deploy():
    archive_path = do_pack()
    if archive_path is None:
        return False
    success = do_deploy(archive_path)
    return success
