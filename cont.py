#!/usr/bin/python

import sys, getopt

# get phone numbers of a single uses
def get_phones(u):
    pno = []
    fs = u.split()
    # examine each field of the split record
    for f in fs:
        if len(f)>6 and f.replace('-', '').isdigit():
            pno.append(f)
    return fs[0], pno

# get emails of all users
def dict_phones(ulist):
    pnos = {}

    for u in ulist:
        k, v = get_phones(u)
        pnos[k] = v

    return pnos


# get emails of a single uses
def get_emails(u):
    emails = []
    fs = u.split()    
    for f in fs:
        if f.find('@') != -1:
            emails.append(f)
    return fs[0], emails


# get emails of all users
def dict_emails(ulist):
    emails = {}

    for u in ulist:
        k, v = get_emails(u)
        emails[k] = v

    return emails
        

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
   print 'Input file is "', inputfile
   print 'Output file is "', outputfile


   users = open(inputfile, 'r')
   ems = dict_emails(users)
   users.close()
   users = open(inputfile, 'r')
   pnos = dict_phones(users)
   users.close()

   o = open(outputfile, 'w')
   for k in ems.keys():
       print (k)
       print (ems[k])
       print pnos[k]
       o.write('{} {} {}\n'.format(k, ems[k], pnos[k]))

   # for k, v in ems.iteritems():
   #     o.write('{} {}\n'.format(k, v))


if __name__ == "__main__":
   main(sys.argv[1:])
