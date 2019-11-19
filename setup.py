""" A setuptools based setup module. """

__author__ = "Matt Pritchard"
__date__ = "2019-11-19"
__copyright__ = "Copyright 2019 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level directory"


import os, re
from setuptools import setup

base_name='jasmintheme_bootstrap3_standalone'

v_file = open(os.path.join(os.path.dirname(__file__), 
                       base_name, '__init__.py'))
VERSION = re.compile(r".*__version__ = '(.*?)'",
                     re.S).match(v_file.read()).group(1)
                     
README = open(os.path.join(os.path.dirname(__file__), 'README.txt')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = base_name,
    version = VERSION,
    packages = [base_name,],
    include_package_data = True,
    license = 'BSD License',
    description = 'JASMIN django app templates',
    long_description = README,
    url = 'http://team.ceda.ac.uk/svn/ceda/ceda_software/jasminsite/themes/jasmintheme_bootstrap3_standalone',
    author = 'Matt Pritchard',
    author_email = 'matt.pritchard@stfc.ac.uk',
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'BSD licence, see LICENCE',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
      
    # Adds dependencies    
    #install_requires = [],
)
