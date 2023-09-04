# run following command using cmd/powershell/terminal
# python setup.py install
# python setup.py py2exe
from distutils.core import setup
import py2exe
setup(windows=['test_case.py']) # relative location of target file
