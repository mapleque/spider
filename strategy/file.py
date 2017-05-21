import lib.util
'''
[file]
seed=<file>
reg=<file>
format=<str>
out=<file>
[recursion]
config=<file>
'''
def run(config, next_run_with_config):
    seed_file = config.get('file', 'seed')
    reg_file = config.get('file', 'reg')
    out = config.get('file', 'out')
    seeds = lib.io.readfile(seed_file)
    regs = lib.io.readfile(reg_file)
    data_format = config.get('file', 'format')
    text = ''
    for seed in seeds:
        if not seed:
            continue
        html = lib.http.get_url(seed)
        for reg in regs:
            matches = lib.parser.regParse(reg, html)
            if len(matches)>0:
                for match in matches:
                    tar_data = data_format
                    for item in match:
                        index = match.index(item)
                        print tar_data,item,index
                        o_data = lib.util.full2half(item).strip().encode('utf-8')
                        tar_data = tar_data.replace('$'+str(index), o_data)
                    tar_data = tar_data.replace('&#10;', '\n')
                    text += tar_data
                break;
    lib.io.save2file(text, out)

    if config.has_section('recursion'):
        recursion_config = config.get('recursion', 'config')
        next_run_with_config(recursion_config)
