#!/usr/bin/env python3


import subprocess


def mpc_action(action):
    subprocess.run(['mpc', action])
