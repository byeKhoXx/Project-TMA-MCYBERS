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


logger = logging.getLogger(__name__)
WEBSERVER_IP = "10.0.5.4"


class WebServerPlugin(HttpWebServerBasePlugin):
    """Demonstrates inbuilt web server routing using plugin."""

    def routes(self) -> List[Tuple[int, str]]:
        return [
            (httpProtocolTypes.HTTP, r'/$'),
            (httpProtocolTypes.HTTPS, r'/$'),
            (httpProtocolTypes.WEBSOCKET, r'/$'),
        ]

    def handle_request(self, request: HttpParser) -> None:
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