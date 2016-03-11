
from ctl.srv.STM32ETH import STM32ETH_telnet as telnet

def LNAHPSU_outen(ip_addr='192.168.0.1', en=''):
    """
    Включение/выключение блока питания
    @param ip_addr - ip-адрес устройства
    @param en - 0 - выкл., 1 - вкл.
    @return en
    """
    return telnet(ip_addr, 'outen', en)

def LNAHPSU_umi(ip_addr='192.168.0.1'):
    """
    Чтение тока грелки
    @param ip_addr - ip-адрес устройства
    @return I
    """
    return telnet(ip_addr, 'umi')

def LNAHPSU_umu(ip_addr='192.168.0.1'):
    """
    Чтение напряжения грелки
    @param ip_addr - ip-адрес устройства
    @return U
    """
    return telnet(ip_addr, 'umu')

