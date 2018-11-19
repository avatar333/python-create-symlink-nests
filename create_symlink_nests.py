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
category_list = ['movies', 'tvseries', 'anime_movies', 'anime_series', 'doccies']


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
    lst = p.glob('src_*/'+subdir_type+'/*')  # Need to glob the the source path, to get a list of source dirs

    print(f'{Style.BRIGHT}TARGET DIRECTORY: ', base_plex_path+subdir_type, f'{Style.RESET_ALL}')

    for src_path_dir in list(lst):
        str_src_path_dir = str(src_path_dir)
        src_dirname = str_src_path_dir.split('/')[-1]
        str_dest_path_dir = base_plex_path+subdir_type+'/'+src_dirname

        if not is_symlink(str_dest_path_dir):
            print(f'Does not exist, creating symlink: {Style.BRIGHT}{Fore.GREEN}', str_dest_path_dir,
                  f'{Style.RESET_ALL}')
            symlink_target = Path(str_dest_path_dir)
            symlink_target.symlink_to(str_src_path_dir)
        else:
            print(f'Does exist as a symlink, skipping: {Fore.YELLOW}', str_src_path_dir, f'{Style.RESET_ALL}')


def main(category):
    """
    Supply the given category string to the scrap_mount_points function

    Args:
        A single category to be scraped, or 'all' for all valid categories

    Returns:
        None, but exit(1) if an invalid category is supplied

    Raises:
        Exception: ?????
    """

    if category in category_list and category != 'all':
        scrape_mount_points(category)
    elif category == 'all':
        for my_category in category_list:
            scrape_mount_points(my_category)
            print('')
    else:
        print(f'Please supply a valid parameter:\n',
              f'Valid options: movies|tvseries|anime_series|doccies|anime_movies|all)')
        exit(1)


if __name__ == '__main__':
    if kp_u.check_args(1):
        main(sys.argv[1])

