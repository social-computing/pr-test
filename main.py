# coding=utf-8
"""
Copyright Groupe SEB 2012
Written by KI
"""
import sys
import getopt
import logging

def main():
    # parse command line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)
    # process options
    for o, a in opts:
        if o in ("-h", "--help"):
            print __doc__
            sys.exit(0)
    # process arguments
    for arg in args:
        logging.info('oh yeah ! %s', arg)

if __name__ == "__main__":
    main()
