#!/usr/bin/env python
# coding: utf8
#
#
# @file:    ftree
# @author:  chosen0ne(louzhenlin86@126.com)
# @date:    2015/01/16 08:32:18

import glob
import os
import os.path
import stat
import itertools
from optparse import OptionParser
from datetime import datetime
from collections import OrderedDict

opts = None


def main():
    global opts
    opts, args = opt_parse()
    pathes = args if args else ['.']
    for fpath in pathes:
        print '@', fpath
        travel_dir(fpath, 0)


def opt_parse():
    parser = OptionParser()
    parser.add_option('-d', '--max-depth', dest='depth', type='int',
                      help='max depth of directory to view', default=3)
    parser.add_option('-s', '--start-depth', dest='start_depth', type='int',
                      help='start depth of directory to view', default=0)
    parser.add_option('-r', '--humanreadable', dest='readable',
                      help='print file size in human readable format',
                      action='store_true',)
    parser.add_option('-l', '--long', dest='longfmt', action='store_true',
                      help='view in long format')
    parser.add_option('-i', '--indent', dest='indent', type='int',
                      help='indent between different levels', default=4)
    opts, args = parser.parse_args()

    return opts, args


def travel_dir(path, cur_depth):
    if cur_depth >= opts.start_depth + opts.depth:
        return

    g = glob.glob(path + '/*')

    # compute max size bit
    max_size = 0
    fstats = OrderedDict()
    for fpath in g:
        statinfo = os.stat(fpath)
        fstats[fpath] = statinfo
        if statinfo.st_size > max_size:
            max_size = statinfo.st_size

    bc = size_bit(max_size) + 1

    for fpath, statinfo in fstats.items():
        if cur_depth >= opts.start_depth:
            full_path = cur_depth == opts.start_depth and opts.start_depth != 0
            print_node(cur_depth, fpath, bc, statinfo, full_path)

        if os.path.isdir(fpath):
            travel_dir(fpath, cur_depth + 1)


def print_node(depth, path, bit_count, statinfo, fullpath=False):
    indent = ''.join(itertools.repeat(' ', opts.indent))
    prefix = ''.join(itertools.repeat(indent, depth))
    prefix += '% 4s-> ' % ('(%d)' % depth)
    mode = statinfo.st_mode
    if opts.longfmt:
        line = fetch_full_info(statinfo, mode, bit_count)
    else:
        line = ''

    fpath = path
    if not fullpath:
        path = os.path.basename(path)

    print '\033[0m', prefix,

    if stat.S_ISREG(mode):
        if is_runnable(fpath):
            line = line + '*' + path
            pyellow(line)
        else:
            line = line + path
            pwhite(line)
    elif stat.S_ISDIR(mode):
        line = line + path + '/'
        pgreen(line)


def is_runnable(path):
    if os.access(path, os.X_OK):
        return True

    return False


def fetch_full_info(statinfo, mode, bit_count):
    # permitssion bit
    if stat.S_ISREG(mode):
        line = '-'
    elif stat.S_ISDIR(mode):
        line = 'd'

    for t in ['S_IRUSR', 'S_IWUSR', 'S_IXUSR', 'S_IRGRP', 'S_IWGRP', 'S_IXGRP',
              'S_IROTH', 'S_IWOTH', 'S_IXOTH']:
        if getattr(stat, t) & stat.S_IMODE(mode):
            line += t[3].lower()
        else:
            line += '-'

    # size
    line += '  '
    if opts.readable:
        line += '% 5s ' % readable_size(statinfo.st_size)
    else:
        line += ('% ' + str(bit_count) + 'd  ') % statinfo.st_size
    line += '%s  ' % datestr(statinfo.st_ctime)

    return line


def datestr(ts):
    d = datetime.fromtimestamp(ts)
    return d.strftime('%Y-%m-%d %H:%M:%S')


def size_bit(size):
    bit_count = 0
    while size != 0:
        bit_count += 1
        size /= 10

    return bit_count


def readable_size(size):
    units = ['B', 'K', 'M', 'G']
    idx = -1
    rsize = 0
    while size > 0:
        rsize = size
        size /= 1024
        idx += 1

    return str(rsize) + units[idx]


def pnone(line):
    print line


def pwhite(line):
    print "\033[0m" + line


def pgreen(line):
    print "\033[36m" + line


def pyellow(line):
    print "\033[33m" + line


if __name__ == '__main__':
    main()
