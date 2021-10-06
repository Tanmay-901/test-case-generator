# command: python setup.py py2exe
from distutils.core import setup
import py2exe
setup(windows=['final_release/test_case.py'])
