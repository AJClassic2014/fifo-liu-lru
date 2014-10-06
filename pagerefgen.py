#!/usr/bin/python

import getopt
import random
import sys

pages=12
length=12

def usage():
  print """

    pagerefgen.py [-f npages | --pages=npages] [-l nrefs | --length=nrefs]

This program generates a random sequence of page numbers.  The page
numbers are drawn from a logical address space containing npages
pages.  The sequence will be of length nrefs.

  npages = the number of pages in the virtual address space
  nrefs  = the total number of page references in the address string

"""

def generate(n,l):
  seq=[]
  for count in range(l):
    nextref=random.randint(0,n)
    seq.append(nextref)
  return seq


if __name__ == '__main__':
  (vals,path)=getopt.getopt(sys.argv[1:],'p:l:',
                ['pages=','length='])
  for (opt,val) in vals:
    if opt=='-p' or opt=='--pages':
      pages=int(val)
    if opt=='-l' or opt=='--length':
      length=int(val)
  if len(path)!=0:
    usage()
    sys.exit(1)
  seq=map(str,generate(pages,length))
  for s in seq:
    print "%s" % s,