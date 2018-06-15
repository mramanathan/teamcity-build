#!/usr/bin/env python

import os

print("system name: ", os.environ["HOSTNAME"])
print("Default path: ", os.environ['PATH'])
print("TC's build agent config file: ", os.environ['CONFIG_FILE'])
