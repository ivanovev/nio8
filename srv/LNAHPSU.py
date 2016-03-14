
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

def LNAHPSU_alarms(ip_addr='192.168.0.1'):
    """
    Чтение состояния алармов
    @param ip_addr - ip-адрес устройства
    @return 0x01 - перегрузка по току
    @return 0x02 - перегрузка по напряжению 1
    @return 0x04 - перегрузка по напряжению 2
    @return 0x08 - перегрузка по напряжению 3
    @return 0x10 - перегрузка по напряжению 4
    """
    return telnet(ip_addr, 'alarms')

def LNAHPSU_thri(ip_addr='192.168.0.1', thri=''):
    """
    Чтение/задание порога по току
    @param ip_addr - ip-адрес устройства
    @param thri - порог по току
    @return 1 - порог по току
    """
    return telnet(ip_addr, 'thri %s' % thri)

def LNAHPSU_thru1(ip_addr='192.168.0.1', thru1=''):
    """
    Чтение/задание порога по напряжению 1
    @param ip_addr - ip-адрес устройства
    @param thru1 - порог по напряжению 1
    @return 1 - порог по напряжению 1
    """
    return telnet(ip_addr, 'thru1 %s' % thru1)

def LNAHPSU_thru2(ip_addr='192.168.0.1', thru2=''):
    """
    Чтение/задание порога по напряжению 2
    @param ip_addr - ip-адрес устройства
    @param thru1 - порог по напряжению 2
    @return 1 - порог по напряжению 2
    """
    return telnet(ip_addr, 'thru2 %s' % thru2)

def LNAHPSU_thru3(ip_addr='192.168.0.1', thru3=''):
    """
    Чтение/задание порога по напряжению 3
    @param ip_addr - ip-адрес устройства
    @param thru1 - порог по напряжению 3
    @return 1 - порог по напряжению 3
    """
    return telnet(ip_addr, 'thru3 %s' % thru3)

def LNAHPSU_thru4(ip_addr='192.168.0.1', thru4=''):
    """
    Чтение/задание порога по напряжению 4
    @param ip_addr - ip-адрес устройства
    @param thru1 - порог по напряжению 4
    @return 1 - порог по напряжению 4
    """
    return telnet(ip_addr, 'thru4 %s' % thru4)

