# -*- coding: utf-8 -*-
"""
    proxy.py
    ~~~~~~~~
    ⚡⚡⚡ Fast, Lightweight, Pluggable, TLS interception capable proxy server focused on
    Network monitoring, controls & Application development, testing, debugging.
    :copyright: (c) 2013-present by Abhinav Singh and contributors.
    :license: BSD, see LICENSE for more details.
"""
import logging
import requests

from typing import List, Tuple
from ..common.utils import build_http_response
from ..http.parser import HttpParser
from ..http.codes import httpStatusCodes
from ..http.websocket import WebsocketFrame
from ..http.server import HttpWebServerBasePlugin, httpProtocolTypes
from pprint import pprint as pp
import json
import time


logger = logging.getLogger(__name__)
WEBSERVER_IP = "10.0.5.4"
PATH_TO_BLOCK_LIST = "/home/albert752/block_list.txt"


class WebServerPlugin(HttpWebServerBasePlugin):
    """Demonstrates inbuilt web server routing using plugin."""

    def routes(self) -> List[Tuple[int, str]]:
        return [
            (httpProtocolTypes.HTTP, r'/$'),
            (httpProtocolTypes.HTTPS, r'/$'),
            (httpProtocolTypes.WEBSOCKET, r'/$'),
        ]

    def handle_request(self, request: HttpParser) -> None:
        with open(PATH_TO_BLOCK_LIST, 'r') as fp:
            ips = json.load(fp)
            fp.close()
        if self.client.addr[0] not in list(ips.keys()) or time.time() > ips[self.client.addr[0]]:
            response = requests.get("http://" + WEBSERVER_IP).content
            if request.path == b'/':
                self.client.queue(memoryview(build_http_response(
                    httpStatusCodes.OK, body=response)))
            elif request.path == b'/':
                self.client.queue(memoryview(build_http_response(
                    httpStatusCodes.OK, body=response)))

    def on_websocket_open(self) -> None:
        logger.info('Websocket open')

    def on_websocket_message(self, frame: WebsocketFrame) -> None:
        logger.info(frame.data)

    def on_websocket_close(self) -> None:
        logger.info('Websocket close')