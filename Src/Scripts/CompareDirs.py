# Licensed to the .NET Foundation under one or more agreements.
# The .NET Foundation licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information.


import sys,nt
sys.path.append(nt.environ['IP_ROOT'] + '\\External\\Regress\\Python24\\Lib')
import filecmp

def compare_dirs(dir1, dir2):
    "Tests whether two folders, including all their contents and subdirectories are identical or not (True == they're the same, False == they are not the same)"
    dc = filecmp.dircmp(dir1,dir2)
    if (
        len(dc.funny_files) <= 0
        and len(dc.left_only) <= 0
        and len(dc.right_only) <= 0
        and len(dc.diff_files) <= 0
    ):
        return all(
            compare_dirs(f'{dir1}\\{subdir}', f'{dir2}\\{subdir}')
            for subdir in dc.common_dirs
        )

    dc.report()
    return False


def main():
    if len(sys.argv)!=3:
        print 'Usage: CompareDirs <dir1> <dir2>'
        sys.exit(-1)
        
    if compare_dirs(sys.argv[1],sys.argv[2]):
        print "The directories are identical"
        sys.exit(0)
    else: #the part that differed is explained via dircmp.report() above
        print "The directories differ"
        sys.exit(1)

if __name__=="__main__":
    main()
