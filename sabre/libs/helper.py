from os.path import split, join, abspath, exists
from os import environ


class PathHelper:
    """This class provides a set of assisting functions to deal with
    path issues."""

    @classmethod
    def abspath_of_executable(cls, path: str):
        """Given a command that can run in shell (with the current environment
        settings), this function figures out the absolute path to the command.
        e.g.::

            python3 -> /usr/bin/python3

        if the given path does not target to any file, it will raise an
        FileNotFound exception.

        :raises FileNotFoundError: no executable can be found at `path`
        :rtype: str
        """

        base_path, name = split(path)
        if base_path == '':
            # this is the name of a program
            # search from PATH
            if 'PATH' not in environ:
                raise FileNotFoundError
            else:
                for prefix in environ['PATH'].strip().split(':'):
                    prefix = prefix.strip()
                    if exists(join(prefix, name)):
                        return join(prefix, name)

                raise FileNotFoundError
        else:
            full_path = abspath(path)
            if not exists(full_path):
                raise FileNotFoundError
            else:
                return full_path
