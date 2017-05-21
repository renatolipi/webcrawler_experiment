# -*- coding: utf-8 -*-

import requests


class AutoEsporteWC(object):

    URL = 'http://revistaautoesporte.globo.com/rss/ultimas/feed.xml'

    def _get_content(self):
        response = requests.get(self.URL)

        if response.status_code == 200:
            return response.content

        return None

    def get_json_content(self):

        return self._get_content()
