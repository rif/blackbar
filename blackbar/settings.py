# -*- coding: utf-8 -*-
import socket
if socket.gethostname() in ('t61',):
    from blackbar.settings_dev import *
else:
    from blackbar.settings_prod import *