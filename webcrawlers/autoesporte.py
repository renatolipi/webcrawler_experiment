# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as BS
import requests


class AutoEsporteWC(object):

    URL = 'http://revistaautoesporte.globo.com/rss/ultimas/feed.xml'

    def _get_content(self):
        response = requests.get(self.URL)

        if response.status_code == 200:
            return response.content

        return {}

    def _get_content_description(self, inner_data):
        def _get_links_list(inner_data):
            links = inner_data.find_all('a')
            return [link.get('href') for link in links]

        def _get_p_list(inner_data):
            texts = inner_data.find_all('p')
            # return [text for text in texts]
            return []

        def _get_img_list(inner_data):
            images = inner_data.find_all('img')
            return [image.get('src') for image in images]

        description = [
            {'type': 'text',
             'content': _get_p_list(inner_data)},
            {'type': 'image',
             'content': _get_img_list(inner_data)},
            {'type': 'links',
             'content': _get_links_list(inner_data)}
        ]
        return description

    def _jsonify_content(self, content):
        feed_list = []

        parsed_content = BS(content, "html.parser")
        items = parsed_content.find_all('item')

        for item in items:
            inner_data = BS(item.description.string, "html.parser")
            json_item = {
                'title': item.title.string or '',
                'link': item.link.string or '',
                'description': self._get_content_description(inner_data)
            }
            feed_list.append({'item': json_item})

        json_content = {'feed': feed_list}

        return json_content

    def get_json_content(self):
        content = self._get_content() or {}
        if content:
            content = self._jsonify_content(content)

        return content
