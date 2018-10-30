#!/usr/bin/env python3

import sys
import kp_utility_module as kp_u
from pathlib import Path
from colorama import Fore
from colorama import Style
from colorama import init
init()

base_mnt_path = '/tmp/mnt/'
base_plex_path = '/tmp/plex/'


def is_symlink(dest_path):
    """
    Check if a file/directory is a symbolic link

    Args:
        The destination path to where the symlink will reside

    Returns:
        bool: True if it is a symbolic link

    Raises:
        Exception: ?????
    """
    p = Path(dest_path)

    if p.exists():
        if p.is_symlink():
            return True
        else:
            return False
    else:
        return False


def scrape_mount_points(subdir_type):
    """
    Search for all directories under, '/base_mnt_path/src_*/subdir_type', create a symbolic link in
    '/base_plex_path/subdir_type

    Args:
        The category for the sub-directory under '/base_plex_path', in which to create the symbolic link

    Returns:
        N/A

    Raises:
        Exception: ?????
    """
    p = Path(base_mnt_path)
    lst = p.glob('src_*/'+subdir_type+'/*')
    print(f'{Style.BRIGHT}TARGET DIRECTORY: ', base_plex_path+subdir_type, f'{Style.RESET_ALL}')

    for src_path_dir in list(lst):
        str_src_path_dir = str(src_path_dir)
        src_dirname = str_src_path_dir.split('/')[-1]
        str_dest_path_dir = base_plex_path+subdir_type+'/'+src_dirname

        if not is_symlink(str_dest_path_dir):
            print(f'Does not exist, creating symlink: {Fore.GREEN}', str_dest_path_dir, f'{Style.RESET_ALL}')
        else:
            print('Does exist as a symlink, skipping')


def main(category):
    kp_u.print_args()

    scrape_mount_points(category)


if __name__ == '__main__':
    if kp_u.check_args(1):
        main(sys.argv[1])

# TEST
