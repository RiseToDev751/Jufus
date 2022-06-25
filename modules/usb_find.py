#!/usr/bin/env python3

import os
import re
import subprocess


def usb_drive(show_all=False):
    devices_list = []

    lsblk = subprocess.run(["lsblk",
                            "--output", "NAME",
                            "--noheadings",
                            "--nodeps"], stdout=subprocess.PIPE).stdout.decode("utf-8")

    devices = re.sub("sr[0-9]|cdrom[0-9]", "", lsblk).split()

    for device in devices:
        if is_removable_and_writable_device(device):
            if not show_all:
                continue

        # FIXME: Needs a more reliable detection mechanism instead of simply assuming it is under /dev
        block_device = "/dev/" + device

        device_capacity = subprocess.run(["lsblk",
                                          "--output", "SIZE",
                                          "--noheadings",
                                          "--nodeps",
                                          block_device], stdout=subprocess.PIPE).stdout.decode("utf-8").strip()

        device_model = subprocess.run(["lsblk",
                                       "--output", "MODEL",
                                       "--noheadings",
                                       "--nodeps",
                                       block_device], stdout=subprocess.PIPE).stdout.decode("utf-8").strip()

        if device_model != "":
            devices_list.append(block_device)
        else:
            devices_list.append(block_device)

    return devices_list


def is_removable_and_writable_device(block_device_name):
    sysfs_block_device_dir = "/sys/block/" + block_device_name

    # We consider device not removable if the removable sysfs item not exist
    if os.path.isfile(sysfs_block_device_dir + "/removable"):
        with open(sysfs_block_device_dir + "/removable") as removable:
            removable_content = removable.read()

        with open(sysfs_block_device_dir + "/ro") as ro:
            ro_content = ro.read()

        if removable_content.strip("\n") == "1" and ro_content.strip("\n") == "0":
            return 0
        else:
            return 1
    else:
        return 1

print(usb_drive(show_all=False))