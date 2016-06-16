
from collections import OrderedDict as OD
from util.columns import *
from util import Data, dev_serial_io_cb, monitor_cb

def columns():
    return get_columns([c_ip_addr, c_serial])

def get_mntr(dev):
    mntr = Data(name='LNAH', send=True, io_cb=dev_serial_io_cb)
    mntr.add('temp', wdgt='entry', state='readonly', msg='Temperature')
    return mntr

def get_menu(dev):
    return OD([('Monitor', monitor_cb)])

