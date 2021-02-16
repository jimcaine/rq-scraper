import setuptools

version = '0.0.1'

setuptools.setup(
    name='rq_scraper',
    version=version,
    author='Jim Caine',
    description='Framework for web scraping using Redis Queue.',
    packages=setuptools.find_packages()
)
