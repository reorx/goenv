# coding: utf-8

import os
import sys


DIR_BIN = 'bin'
ENV_KEY_GOPATH = 'GOPATH'
ENV_KEY_PATH = 'PATH'


def format_gopath(gopath):
    if not gopath:
        raise ValueError('must input a path')
    if not os.path.isdir(gopath):
        raise ValueError('must input a dir path')
    # '.' is OK for abspath
    return os.path.abspath(gopath)


def set_goenv(gopath):
    _gopath = os.environ.get('GOPATH')
    _path = os.environ.get('PATH')
    _paths = _path.split(':')
    if _gopath:
        _gopathbin = os.path.join(_gopath, DIR_BIN)
        if _gopathbin in _paths:
            _paths.remove(_gopathbin)

    gopathbin = os.path.join(gopath, DIR_BIN)
    paths = list(_paths)
    paths.insert(0, gopathbin)
    path = ':'.join(paths)

    lines = []
    lines.append(export_str(ENV_KEY_GOPATH, gopath))
    lines.append(export_str(ENV_KEY_PATH, path))
    return '\n'.join(lines)


def export_str(k, v):
    return 'export {}="{}"'.format(k, v)


def main():
    _gopath = sys.argv[1]
    gopath = format_gopath(_gopath)
    export = set_goenv(gopath)
    print export


if __name__ == '__main__':
    main()
