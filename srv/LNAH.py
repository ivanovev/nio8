
from serial import Serial
from threading import Thread
from time import sleep

lnahth = None
lnahport = ''
lnahtemp = ''
lnahstr = ''
lnahcmd = ''

def lnah_parse_data(s):
    global lnahtemp, lnahstr
    s = s.strip("\n\r \0")
    lnahstr = s
    ss = s.split()
    if len(ss) > 6:
        lnahtemp = ss[5]

def lnah_listen_thread_func(port):
    global lnahth, lnahport, lnahcmd
    lnahport = port
    if port[:3] != 'COM':
        if port.find('/dev/') == -1:
            port = '/dev/' + port
    try:
        ser = Serial(port, 9600, 8, 'N', 1, timeout=2)
        s = ''
        while lnahth:
            if lnahcmd:
                ser.write(lnahcmd.encode('ascii'))
                lnahcmd = ''
            ch = ser.read()
            if len(ch):
                chr0 = chr(ch[0])
                if chr0 == '\r':
                    lnah_parse_data(s)
                    s = ''
                else:
                    s += chr0
    except:
        lnahth = None
    print('lnahthread stop')

def LNAH_listen(port='COM8'):
    global lnahth, lnahport
    if not port:
        return lnahport
    if lnahth:
        return lnahport
    lnahth = Thread(target=lnah_listen_thread_func, args=(port,))
    lnahth.start()
    for i in range(0, 10):
        sleep(.1)
        if lnahtemp:
            break
    return port

def LNAH_stop():
    global lnahth, lnahport
    if lnahth:
        print('lnah stop')
        lnahth = None
        lnahtemp = ''
    return lnahport

def LNAH_temp(port='COM8'):
    global lnahth, lnahtemp
    if not lnahth:
        LNAH_listen(port)
    return lnahtemp

def LNAH_str(port='COM8'):
    global lnahth, lnahstr
    if not lnahth:
        LNAH_listen(port)
    return lnahstr

def LNAH_cmd(port='COM8', cmd=''):
    global lnahth, lnahcmd
    if not lnahth:
        LNAH_listen(port)
    lnahcmd = cmd
    return lnahcmd

