#!/usr/bin/env python

import os
import codecs

path = os.path.dirname(os.path.realpath(__file__))
with codecs.open(path+"/Purgatory", "a", "utf-8") as wf:
  wf.write(os.popen('xsel').read().decode('utf8') + '\n')
