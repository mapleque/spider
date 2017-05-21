import parser,http,io,conf
def run(config_file):
    config = conf.load_config(config_file)
    strategy = config.get('base', 'strategy')
    if not strategy:
        strategy = 'default'
    if strategy:
        index = __import__('strategy.' + strategy)
        st = getattr(index, strategy)
        st.run(config, run)
