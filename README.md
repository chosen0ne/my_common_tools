# my_common_tools
some handy tools.

1. ftree

    like 'ls', but display files in tree mode.

#####Usage:
    > > ftree -h
    > Usage: ftree [options] arg1 arg2 ...
    >
    > Options:
    >   -h, --help              show this help message and exit
    >   -d DEPTH, --max-depth=DEPTH
    >                           max depth of directory to view
    >   -s START_DEPTH, --start-depth=START_DEPTH
    >                           start depth of directory to view
    >   -r, --humanreadable     print file size in human readable format
    >   -l, --long              view in long format
    >   -i INDENT, --indent=INDENT
    >                           indent between levels

#####Example:
    > > ftree -l -r lua-5.2.3
    > (0)->  drwxr-xr-x   136B 2014-11-18 11:08:46  lib/
    >   (1)->  -rw-r--r--   324K 2014-11-18 11:08:46  liblua.a
    >   (1)->  drwxr-xr-x   102B 2014-11-18 11:08:46  lua/
    >       (2)->  drwxr-xr-x    68B 2014-11-18 11:08:46  5.2/
    > (0)->  drwxr-xr-x   102B 2014-11-18 11:08:46  man/
    >   (1)->  drwxr-xr-x   136B 2014-11-18 11:08:46  man1/
    >       (2)->  -rw-r--r--     2K 2014-11-18 11:08:46  lua.1
    >       (2)->  -rw-r--r--     2K 2014-11-18 11:08:46  luac.1
    > (0)->  drwxr-xr-x   102B 2014-11-18 11:08:46  share/
    >   (1)->  drwxr-xr-x   102B 2014-11-18 11:08:46  lua/
    >       (2)->  drwxr-xr-x    68B 2014-11-18 11:08:46  5.2/
