
from ctl.srv.STM32ETH import STM32ETH_telnet as telnet

def ATTEN_atten1(ip_addr='192.168.0.1', atten=''):
    """
    Чтение/установка величины подавления
    @param ip_addr - ip-адрес устройства
    @param atten - [0..31]
    @return atten
    """
    return telnet(ip_addr, 'atten1', atten)

