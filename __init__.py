
from . import gui, srv
from util.columns import *
from util.misc import app_devtypes, app_devdata

devdata = lambda: app_devdata('NIO8', get_columns([c_ip_addr, c_serial]), app_devtypes(gui))

