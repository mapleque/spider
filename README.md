This is a spider project implement by python.

All you have to do is edit your config file.

Here 2 example for your.

## default

This example just fetch the target html and match your regular expression.

As the config file ```config/default.ini``` define ```base.strategy```, the spider will run with default strategy implement in ```strategy/default.py```.

In default strategy, fetching, matching and printing, witch config by default config setion.

Run with cmd to see:
```
python run.py -i config/default.ini
```
## file

This example play a recursion task.

If you use the file strategy, which define in ```config/file.ini```, and config recursion section, the spider will run next task with ```recursion.config```, after current task finish. Therefore, in ```config/child_file.ini```, we config the seed file with ```config/file.out```, which write out by the first task.

Format string help you control file out file format, using ```$n``` refer to your regular expression param.

All the seeds in your seeds file will be fetch and match.

In matching, regular expression will be try from top util there is matched.

## extend

You can extend the strategy by implement the interface ```run(config_file_name, next_run_with_config_func)``` and the config format behind ase section.
