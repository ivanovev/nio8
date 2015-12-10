
from ctl.srv.SAM7X import SAM7X_telnet as telnet

def CSP_modem1(ip_addr='192.168.0.1', modem1=''):
    """
    Чтение/установка антенны для первого модема
    @param modem1 - 0 - основная антенна, 1 - резервная
    @return modem1
    """
    return telnet(ip_addr, 'modem1', modem1)

def CSP_modem2(ip_addr='192.168.0.1', modem2=''):
    """
    Чтение/установка антенны для первого модема
    @param modem2 - 0 - основная антенна, 1 - резервная
    @return modem2
    """
    return telnet(ip_addr, 'modem2', modem2)

