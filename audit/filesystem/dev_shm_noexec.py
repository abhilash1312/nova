# -*- coding: utf-8 -*-
'''
Setting this option on a file system prevents users from executing programs from
shared memory. This deters users from introducing potentially malicious software
on the system.
'''
from __future__ import absolute_import
from audit import *
import logging


def __virtual__():
    if 'Linux' in __salt__['grains.get']('kernel'):
        return __virtualname__
    return False


def audit(): ret = _grep('"/dev/shm"', '/etc/fstab')
    if 'noexec' in ret:
        return True
    else:
        return False
