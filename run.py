import sys,getopt
import lib.spider

def usage():
  print '-i for config file'
  print '-h for this'

opts, args = getopt.getopt(sys.argv[1:], "hi:")
config_file = ''
for op, value in opts:
  if op == '-i':
    config_file = value
  elif op == '-h':
    usage()
    sys.exit()
if not config_file:
   usage()
   sys.exit()

lib.spider.run(config_file)
