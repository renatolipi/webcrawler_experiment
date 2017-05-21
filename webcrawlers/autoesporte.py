# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as BS
import requests


class AutoEsporteWC(object):

    URL = 'http://revistaautoesporte.globo.com/rss/ultimas/feed.xml'

    def _get_content(self):
        response = requests.get(self.URL)

        if response.status_code == 200:
            return response.content

        return None

    def _get_content_description(self, descricao):
        description = []
        return description

    def _jsonify_content(self, content):
        feed_list = []

        parsed_content = BS(content, "html.parser")
        items = parsed_content.find_all('item')

        for item in items:
            descricao = BS(item.description.string, "html.parser")
            json_item = {
                'title': item.title.string or '',
                'link': item.link.string or '',
                'description': self._get_content_description(descricao)
            }
            feed_list.append({'item': json_item})

        json_content = {'feed': feed_list}

        return json_content

    def get_json_content(self):
        content = self._get_content() or {}
        if content:
            content = self._jsonify_content(content)

        return content
