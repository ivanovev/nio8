
from collections import OrderedDict as OD
from util import Data, dev_io_cb, control_cb
from util.columns import *

def columns():
    return get_columns([c_ip_addr])

def csp_fmt_cb(val, read=True):
    if read:
        return 'Reserve' if val == '1' else 'Main'
    return '1' if val == 'Reserve' else '0'

def get_ctrl(dev):
    ctrl = Data(name='CSP', send=True, io_cb=dev_io_cb)
    ctrl.add('modem1', label='Modem1 antenna', wdgt='combo', state='readonly', value=['Main', 'Reserve'], text='Main', fmt_cb=csp_fmt_cb)
    ctrl.add('modem2', label='Modem2 antenna', wdgt='combo', state='readonly', value=['Main', 'Reserve'], text='Main', fmt_cb=csp_fmt_cb)
    return ctrl

def get_menu(dev):
    return OD([('Control', control_cb)])

