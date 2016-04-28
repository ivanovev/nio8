
from collections import OrderedDict as OD
from util import Data, dev_io_cb, control_cb
from util.columns import *

def columns():
    return get_columns([c_ip_addr])

def atten_fmt_cb(val, read=True):
    if read:
        val = int(val)
        val = '%d' % val
    return val

def get_ctrl(dev):
    ctrl = Data(name='ATTEN', send=True, io_cb=dev_io_cb)
    ctrl.add('atten1', label='Attenuation', wdgt='spin', value=Data.spn(0, 31), text='16', fmt_cb=atten_fmt_cb)
    return ctrl

def get_menu(dev):
    return OD([('Control', control_cb)])

