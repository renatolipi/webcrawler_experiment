# -*- coding: utf-8 -*-

# RACING NEWS FROM AUTOSPORT.COM #


class AutoSport(object):
    URL = 'http://www.autosport.com/rss/feed/all'

    def get_json_content(self):
        return {}


class Formula1(AutoSport):
    URL = 'http://www.autosport.com/rss/feed/f1'


class F2(AutoSport):
    URL = 'http://www.autosport.com/rss/feed/f2'


class Formula3(AutoSport):
    URL = 'http://www.autosport.com/rss/feed/f3'


class FormulaE(AutoSport):
    URL = 'http://www.autosport.com/rss/feed/fe'


class IndyCar(AutoSport):
    URL = 'http://www.autosport.com/rss/feed/indycar'


class IndyLights(AutoSport):
    URL = 'http://www.autosport.com/rss/feed/lights'


class Nascar(AutoSport):
    URL = 'http://www.autosport.com/rss/feed/nascar'


class DTM(AutoSport):
    URL = 'http://www.autosport.com/rss/feed/dtm'


class WTCC(AutoSport):
    URL = 'http://www.autosport.com/rss/feed/wtcc'


class BTCC(AutoSport):
    URL = 'http://www.autosport.com/rss/feed/btcc'


class WEC(AutoSport):
    URL = '     http://www.autosport.com/rss/feed/wec'
