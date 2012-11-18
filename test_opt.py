#!/usr/bin/env python

try:
    import pyaux
    pyaux.use_exc_ipdb()
    pyaux.use_exc_log()
except:
    pass

import datetime
import matplotlib.pyplot as plt
import IPython
import logging

logging.basicConfig()

from pybacktest.testers import SimpleBacktester
from pybacktest.opt import Optimizer
from examples.ma_strategy import MACrossoverStrategy as strategy
from pybacktest.data.pandas_bars import pandas_bars_wrap
from pybacktest.data.quotes import get_daily_quotes_yahoo

bars = pandas_bars_wrap(get_daily_quotes_yahoo('GOLD', '20070101', '20120101'))
bars = [list(bars)]

opt = Optimizer(SimpleBacktester, bars, strategy, log_level=logging.DEBUG)
opt.add_opt_param('fast_period', 10, 20, 1)
opt.add_opt_param('slow_period', 20, 50, 1)
opt.run(('sharpe',), processes=8)

print 'Param names: %s' % opt.param_names
print 'Optimization results (param vector : resulting statistics)'
try:
    import pprint
    pprint.pprint(opt.opt_results)
except:
    print opt.opt_results


IPython.embed(banner1='optimizer is in `opt`')
