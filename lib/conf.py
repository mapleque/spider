import ConfigParser
def load_config(config_file):
    cf = ConfigParser.ConfigParser()
    cf.read(config_file)
    return cf
