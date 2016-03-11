
from collections import OrderedDict as OD
from util import Data, dev_io_cb, control_cb, monitor_cb
from util.columns import *

def columns():
    return get_columns([c_ip_addr])

def get_ctrl(dev):
    ctrl = Data(name='LNAHPSU.c', send=True, io_cb=dev_io_cb)
    ctrl.add('outen', label='Output enable', wdgt='combo', state='readonly', value=OD([('ON', '1'), ('OFF', '0')]), text='OFF')
    return ctrl

def get_mntr(dev):
    mntr = Data(name='LNAHPSU.m', send=True, io_cb=dev_io_cb)
    mntr.add('umi', wdgt='entry', state='readonly', msg='Current, mA')
    mntr.add('umu', wdgt='entry', state='readonly', msg='Voltage, V')
    return mntr

def get_menu(dev):
    return OD([('Control', control_cb), ('Monitor', monitor_cb)])

