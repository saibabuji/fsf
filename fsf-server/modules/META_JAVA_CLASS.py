#!/usr/bin/env python
#
# Author: Jason Batchelor
# Description: Get metadata concerning Java class files
# Date: 02/07/2017 (updated)
'''
   Copyright 2017 Emerson Electric Co.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''
import sys
from javatools import classinfo
from javatools import unpack_class

# Stub class to interface with classinfo
class classinfo_options:

   def __init__(self):
      self.class_provides = True
      self.class_requires = True
      self.constpool = True
      self.api_ignore = ''
      self.show = 'SHOW_PRIVATE'

# Needs to be the filename of your module
def META_JAVA_CLASS(s, buff):
   # Function must return a dictionary
   META_DICT = {}

   options = classinfo_options()
   info = unpack_class(buff)
   META_DICT = classinfo.cli_simplify_classinfo(options, info)
   _constants_pool = []
   for x in META_DICT['constants_pool']:
      _constants_pool.append({"index": x[0], "type": x[1], "value": x[2]})
   META_DICT["constants_pool"] = _constants_pool
   return META_DICT

if __name__ == '__main__':
   # For testing, s object can be None type if unused in function
   print META_JAVA_CLASS(None, sys.stdin.read())
