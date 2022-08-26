#!/usr/bin/env python

import os
from importlib.machinery import SourceFileLoader

import setuptools


if __name__ == "__main__":
    version = SourceFileLoader("version", os.environ["VERSION_FILE"]).load_module()
    setuptools.setup(name="rxy", version=str(version.VERSION))
