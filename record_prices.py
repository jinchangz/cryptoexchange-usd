
import json
from pprint import pprint
import sys
import subprocess
from datetime import datetime
import itertools
import linecache
import os
import time

interval = 1

def get_exchange(ex, con):
    filename = os.path.normpath(os.path.join(os.path.abspath('./'),'tickers/' + ex + '_ticker.json' ))
    with open(filename) as f:
        exchange = json.load(f)
        exchange['exchange'] = ex
    return exchange[con]

def is_add_file(con):
    filename = os.path.normpath(os.path.join(os.path.abspath('./'),'prices/' + con + '_' + today + '.csv'))
    if not os.path.isfile(filename):
        with open(filename, mode='w') as f:
            f.write(','.join(list(map(str, exs)))+'\n')

if __name__ == '__main__':

    exs = ['bf', 'cc', 'bb', 'qx', 'zf']
    cons = ['ask','bid','last']
    today = ''

    while True:

        if not(today == datetime.now().strftime("%Y_%m_%d")):
            today = datetime.now().strftime("%Y_%m_%d")
            for con in cons:
                is_add_file(con)
        
        for con in cons:
            exchanges = []
            filename = os.path.normpath(os.path.join(os.path.abspath('./'),'prices/' + con + '_' + today + '.csv'))

            for ex in exs:
                exchanges.append(get_exchange(ex, con))

            prices = ','.join(list(map(str, exchanges)))
            cmd = "echo " + prices + " >> " + filename
            subprocess.run(cmd, shell=True)

        time.sleep(interval)




