from rq_scraper.utils.get_module_path import get_module_path

# set up logging

# validate environment variables

# set __module_path__
__module_path__ = get_module_path()
print('Module path: {}'.format(__module_path__))

# set version
__version__ = '0.0.1'
print('rq-scraper version: {}'.format(__version__))
