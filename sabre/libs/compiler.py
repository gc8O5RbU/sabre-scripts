from enum import IntEnum
from subprocess import run, PIPE
from os.path import exists, split
from os import environ

from sabre.libs.helper import PathHelper


class CompilerType(IntEnum):

    GCC = 0
    CLANG = 1
    JAVAC = 2
    RUSTC = 3

    @classmethod
    def from_executable(cls, path: str):

        full_path = PathHelper.abspath_of_executable(path)

        # run <executable> -v
        proc_v = run([full_path, '-v'], stdout=PIPE, stderr=PIPE)
        proc_v_stderr = proc_v.stderr.decode().strip().split('\n') or ['']

        if proc_v_stderr[-1].startswith('gcc'):
            return cls.GCC
        else:
            print(proc_v_stderr)
