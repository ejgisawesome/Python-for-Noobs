# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 21:06:04 2020

@author: egarcia
"""


## importing external library

import re
#re is included, what it do: regex (regular expression)
string = "'I AM NOT YELLING!', she said, lying."

new = re.sub('[.,\'A-Z+" "]','',string)
#substitute shit?

string = string + "6 298 - 345"
new = re.sub('[^0-9]','',string)
