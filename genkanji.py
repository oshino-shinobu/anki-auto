#!/usr/bin/env python

import codecs

kdict = {}
with codecs.open("KanjiDic","r","utf-8") as kdf:
  for line in kdf:
    kdict[line[0]] = line

with codecs.open("Words", "r", "utf-8") as wf, codecs.open("KanjiForImport", "a", "utf-8") as kif:
  for line in wf:
    for c in line:
      if c in kdict:
        kif.write(kdict[c])
