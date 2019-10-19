#!/usr/bin/env python3

""" The Sabre Compiler (sc)
"""
from sys import argv

from sabre.libs.compiler import CompilerType


if __name__ == "__main__":
    CompilerType.from_executable(argv[1])
