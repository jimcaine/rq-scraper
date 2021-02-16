import os
import site
from pathlib import Path

def get_module_path():
    """
    Returns the module path of the package.  The module path will be the
    repository directory if the editable flag is used in pip install, otherwise,
    it will be located in the site-packages directory of the python / pip
    installation that was used.
    """

    # define the package name
    package_name = 'rq-scraper'

    # define the site packages directory for the environment
    site_packages_dir = Path(site.getsitepackages()[0])

    # if egg-link is in site packages dir, assign module path to one directory
    # down from current file
    egg_link_path = os.path.join(site_packages_dir, '{}.egg-link' \
        .format(package_name))

    if os.path.exists(egg_link_path):
        module_path = os.path.join(
            str(Path(__file__)).split(package_name)[0],
            package_name)

    # assign module path to site-packages if egg-link does not exist in
    # site packages dir
    else:
        module_path = os.path.join(site_packages_dir, package_name)

    return module_path
