
from collections import OrderedDict as OD
from util.columns import *
from util import Data, dev_io_cb, control_cb, monitor_cb, alarm_trace_cb

def columns():
    return get_columns([c_ip_addr])

def alarms_cb(val, read=True, almn=0):
    if read:
        if almn == 0:
            alarms_cb.alarms = val
        else:
            val = alarms_cb.alarms
        v = int(val, 16)
        if v & (1 << almn):
            return '1'
        return 0
    return val

def get_ctrl(dev):
    ctrl = Data(name='LNAHPSU.c', send=True, io_cb=dev_io_cb)
    ctrl.add('outen', label='Output enable', wdgt='combo', state='readonly', value=OD([('ON', '1'), ('OFF', '0')]), text='OFF')
    ctrl.add('thri1', label='I threshold, mA', wdgt='spin', state='readonly', value=Data.spn(500, 1700, 100), text='1200')
    ctrl.add('thri2', label='I threshold, mA', wdgt='spin', state='readonly', value=Data.spn(1, 10), text='6')
    ctrl.add('thri3', label='I threshold, mA', wdgt='spin', state='readonly', value=Data.spn(10, 50), text='20')
    ctrl.add('thru1', label='U threshold1, V', wdgt='spin', state='readonly', value=Data.spn(7, 36), text='7')
    ctrl.add('thru2', label='U threshold2, V', wdgt='spin', state='readonly', value=Data.spn(7, 36), text='23')
    ctrl.add('thru3', label='U threshold3, V', wdgt='spin', state='readonly', value=Data.spn(7, 36), text='25')
    ctrl.add('thru4', label='U threshold4, V', wdgt='spin', state='readonly', value=Data.spn(7, 36), text='36')
    ctrl.add('thru4', label='U threshold4, V', wdgt='spin', state='readonly', value=Data.spn(7, 36), text='36')
    ctrl.add('umi0', label='I0, mA', wdgt='spin', value=Data.spn(1, 100, 0.1), text='13.5')
    ctrl.add('kmi', label='I coef', wdgt='spin', value=Data.spn(0.5, 1.5, 0.000001), text='1.0')
    return ctrl

def get_mntr(dev):
    mntr = Data(name='LNAHPSU.m', send=True, io_cb=dev_io_cb)
    mntr.add('alarms', wdgt='alarm', msg='I threshold', fmt_cb=lambda val, read=True: alarms_cb(val, read, 0), trace_cb=alarm_trace_cb)
    mntr.add('alarms1', wdgt='alarm', msg='U threshold1', fmt_cb=lambda val, read=True: alarms_cb(val, read, 1), trace_cb=alarm_trace_cb, send=False)
    mntr.add('alarms2', wdgt='alarm', msg='U threshold2', fmt_cb=lambda val, read=True: alarms_cb(val, read, 2), trace_cb=alarm_trace_cb, send=False)
    mntr.add('alarms3', wdgt='alarm', msg='U threshold3', fmt_cb=lambda val, read=True: alarms_cb(val, read, 3), trace_cb=alarm_trace_cb, send=False)
    mntr.add('alarms4', wdgt='alarm', msg='U threshold4', fmt_cb=lambda val, read=True: alarms_cb(val, read, 4), trace_cb=alarm_trace_cb, send=False)
    mntr.add('alarms5', wdgt='alarm', msg='LNAH conn', fmt_cb=lambda val, read=True: alarms_cb(val, read, 5), trace_cb=alarm_trace_cb, send=False)
    mntr.add('alarms6', wdgt='alarm', msg='LNAH heat', fmt_cb=lambda val, read=True: alarms_cb(val, read, 6), trace_cb=alarm_trace_cb, send=False)
    mntr.add('umi', wdgt='entry', state='readonly', msg='Current, mA')
    mntr.add('umu', wdgt='entry', state='readonly', msg='Voltage, V')
    return mntr

def get_menu(dev):
    return OD([('Control', control_cb), ('Monitor', monitor_cb)])

