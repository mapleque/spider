import lib.http, lib.parser
'''
[default]
seed=<url>
reg=<reg>
'''
def run(config, next_run_with_config):
    seed = config.get('default', 'seed')
    reg = config.get('default', 'reg')
    html = lib.http.get_url(seed)
    matches = lib.parser.regParse(reg, html)
    for match in matches:
        for ele in match:
            print ele,
        print '\n'

