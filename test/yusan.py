# -*- coding: utf-8 -*-
from python_bitbankcc import public_api

bitbank = public_api.bitbankcc_public()

print(bitbank.get_ticker("mona_jpy"))

print(bitbank.get_depth("mona_jpy"))
""""""
