import os
import re
import time
import traceback


def logger(info=None):
    rw = open(f'{os.getcwd()}/Logs.log', 'a+')
    if info is not None:
        rw.write(f'{"=" * 10}\n')
        rw.write(f'{time.strftime("/%H:%M:%S/")} [INFO] {info} \n')
        rw.write(f'{"=" * 10}\n')

    def logger_dec(fn):

        def logger_wrap(*args):
            returned_str = None
            rw.write(f'{"=" * 10}\n')
            try:
                returned = fn(*args)
                rw.write(f'{time.strftime("/%H:%M:%S/")} [LOADED] {fn.__name__} successful execute. \n')
            except Exception as ex:
                returned = args
                r = traceback.format_exc().split(', ')
                for i in r:
                    if re.search('line', i):
                        returned_str = f'{i}'
                        break
                rw.write(
                    f'{time.strftime("/%H:%M:%S/")} [ERROR] Function [{fn.__name__}] Loading error: \n {ex} in {returned_str} \n')
                print(
                    '[ERROR]Error, look at the information in the logs!\n[ERROR]Function returned the original value!')
            rw.write(f'{"=" * 10}\n')
            rw.close()
            return returned

        return logger_wrap

    return logger_dec
