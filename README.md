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
    > > lua-5.2.3  ftree -l -r bin include
    > @ bin
    >     (0)->  -rwxr-xr-x   187K 2014-11-18 11:08:46  *lua
    >     (0)->  -rwxr-xr-x   130K 2014-11-18 11:08:46  *luac
    > @ include
    >     (0)->  -rw-r--r--     7K 2014-11-18 11:08:46  lauxlib.h
    >     (0)->  -rw-r--r--    13K 2014-11-18 11:08:46  lua.h
    >     (0)->  -rw-r--r--   191B 2014-11-18 11:08:46  lua.hpp
    >     (0)->  -rw-r--r--    15K 2014-11-18 11:08:46  luaconf.h
    >     (0)->  -rw-r--r--     1K 2014-11-18 11:08:46  lualib.h
