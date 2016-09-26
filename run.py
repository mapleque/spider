import sys,getopt,spider
import ConfigParser

def usage():
  print '-i for config file'
  print '-o for output path'
  print '-h for this'

opts, args = getopt.getopt(sys.argv[1:], "hi:o:")
config_file = ''
out_path = ''
for op, value in opts:
  if op == '-i':
    config_file = value
  elif op == '-o':
    out_path = value
  elif op == '-h':
    usage()
    sys.exit()
if not config_file or not out_path:
   usage()
   sys.exit()
cf = ConfigParser.ConfigParser()
cf.read(config_file)
seed = cf.get('all', 'seed')
reg = cf.get('all', 'reg')
strategy = cf.get('all', 'strategy')
if not seed or not reg or not strategy:
  print 'invalid config'
  sys.exit()
spider.spider(seed, reg, strategy, out_path)
