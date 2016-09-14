# coding=utf-8

import grp
import os
import pwd
import subprocess


#
# Command tools
#

def cmd_output(command):
    """
    Executed command and returns a list of lines from the output
    """
    full_cmd = 'su mycodo && {}'.format(command)
    cmd = subprocess.Popen(full_cmd, stdout=subprocess.PIPE, shell=True)
    cmd_output, cmd_err = cmd.communicate()
    cmd_status = cmd.wait()
    return cmd_output, cmd_err, cmd_status


#
# Filesystem tools
#

def assure_path_exists(new_dir):
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
        set_user_grp(new_dir, 'mycodo', 'mycodo')


def find_owner(filename):
    return pwd.getpwuid(os.stat(filename).st_uid).pw_name


def set_user_grp(filepath, user, group):
    uid = pwd.getpwnam(user).pw_uid
    gid = grp.getgrnam(group).gr_gid
    os.chown(filepath, uid, gid)
