#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, getopt
import re

class Contact:
    def __init__(self):
        self.name = ''
        self.emails = []
        self.phones = []
        self.addrs = []

    def _is_email(self, s):
        if s.find('@') != -1:
            # print '[D] ' + s + ' is email'
            return True

        return False
        

    def _is_phone(self, s):
        if re.search('[0-9]{7}', s.replace('-','')):
            # print '[D] ' + s + ' is phone'
            return True

        return False

    def parse(self, raw_record):
        fields = raw_record.replace('；', ' ').split()
        self.name = fields[0]
        for f in fields[1:]:
            if self._is_email(f):
                self.emails.append(f)
            elif self._is_phone(f):
                self.phones.append(f)
            else:               
                self.addrs.append(f)

        # to organize the output here
        c = self.name + ','     # name comes 1st
        for p in self.phones:   # follows the phone No.s
            c += p + ','
        for m in self.emails:   # follows the emails
            c += m + ','
        for a in self.addrs:    # follows the addresses
            c += a + ','

        return c


def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
#   print 'Input file is "', inputfile
#   print 'Output file is "', outputfile


   fin = open(inputfile, 'r')
   if outputfile != '':
       fout = open(outputfile, 'w')
   else:
       fout = None

   for u in fin:
       c = Contact()
       if fout:
           fout.write(c.parse(u))
           fout.write('\n')
       else:
           print c.parse(u)


if __name__ == "__main__":
   main(sys.argv[1:])
