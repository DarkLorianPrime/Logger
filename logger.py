import os
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
            rw.write(f'{"=" * 10}\n')
            try:
                returned = fn(*args)
                rw.write(f'{time.strftime("/%H:%M:%S/")} [LOADED] {fn.__name__} successful execute. \n')
            except Exception as ex:
                returned = args
                rw.write(f'{time.strftime("/%H:%M:%S/")} [ERROR] Function {fn.__name__} Loading error: \n {ex} in \n')
                print('Error, look at the information in the logs!\nFunction returned the original value!')
            rw.write(f'{"=" * 10}\n')
            rw.close()
            return returned

        return logger_wrap

    return logger_dec


@logger('Info for logs')
def print_lower(text):
    d = 0 / 0
    print(d)
    lower_text = text.lower()
    return lower_text


print(print_lower('I KNOW YOU WILL SAY HI TO ME IF WE MEET AGAIN'))


