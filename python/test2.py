import urllib
import httpimport

with httpimport.remote_repo(['package1'], 'https://raw.githubusercontent.com/boconnor2017/hesiod/pygame-dev/python/lib_general.py'):
  import package1 as heslibgen 

