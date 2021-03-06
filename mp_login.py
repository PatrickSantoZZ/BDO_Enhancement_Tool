#- * -coding: utf - 8 - * -
"""

@author: ☙ Ryan McConnell ♈♑ rammcconnell@gmail.com ❧
"""
import os
from typing import Tuple, Union

from .common import relative_path_convert, BasePriceUpdator
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtWebEngineWidgets, QtWebEngineCore
from .utilities import sanitizeFileName, string_between
import urllib3
from urllib.parse import urlencode
from urllib import request
import json
import time

GetWorldMarketSubList = '/Home/GetWorldMarketSubList'
GetWorldMarketSubList_body = '__RequestVerificationToken={}&mainKey={}&usingCleint=0'


class CentralMarketPriceUpdator(BasePriceUpdator):
    def __init__(self, profile, connection, cookies, token):
        self.profile = profile
        self.connection = connection
        self.cookies = cookies
        self.GetWorldMarketSubList_token = token

    def get_update(self, id: str) -> Tuple[float, Union[None, list]]:
        r = self.connection.request('POST', GetWorldMarketSubList,
                         body=GetWorldMarketSubList_body.format(self.GetWorldMarketSubList_token, int(id)).encode(
                             'utf-8'),
                         headers={
                             'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                             'Cookie': self.cookies,
                             'User-Agent': self.profile.httpUserAgent()
                         })
        r_obj = json.loads(r.data.decode('utf-8'))
        list = r_obj['detailList']
        expires = time.time() + 1800
        if len(list) > 0:
            return expires, [x['pricePerOne'] for x in r_obj['detailList']]
        else:
            return expires, None

    def __del__(self):
        self.connection.close()


class MPBrowser(QtWebEngineWidgets.QWebEngineView):
    pass


class suppressPage(QtWebEngineWidgets.QWebEnginePage):
    def javaScriptConsoleMessage(self, level, message: str, lineNumber: int, sourceID: str) -> None:
        return

    def load(self, url: QtCore.QUrl) -> None:
        super(suppressPage, self).load(url)


class DlgMPLogin(QtWidgets.QDialog):
    sig_Market_Ready = QtCore.pyqtSignal(object, name='')

    def __init__(self, parent):
        super(DlgMPLogin, self).__init__(parent)

        self.resize(QtCore.QSize(365, 580))


        self.web = MPBrowser()
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.addWidget(self.web)

        self.profile = QtWebEngineWidgets.QWebEngineProfile('cookies', self.web)
        self.cookie_store = self.profile.cookieStore()

        self.cookie__RequestVerificationToken = None
        self.frmGetItemSellBuyInfo_token = None
        self.host_local = None
        self.cooks = {}


        self.cookie_store.cookieAdded.connect(self.onCookieAdded)
        #self.web.loadFinished.connect(self.web_loadFinished)

        page = suppressPage(self.profile, self.web)
        page.loadFinished.connect(self.web_loadFinished)
        self.page = page
        self.web.setPage(page)
        self.update_page = True
        self.price_updator = None
        self.this_connection = None

    def showEvent(self, a0) -> None:
        super(DlgMPLogin, self).showEvent(a0)
        if self.update_page:
            self.web.setUrl(QtCore.QUrl("https://market.blackdesertonline.com/"))
            self.update_page = False

    def onCookieAdded(self, cooke):
        name = cooke.name().data().decode('utf-8')
        value = cooke.value().data().decode('utf-8')
        self.cooks[name] = value
        #print('{}: {}'.format(name, cooke.value()))
        if name == '__RequestVerificationToken':
            self.set_cookie__RequestVerificationToken(value)

    def set_cookie__RequestVerificationToken(self, token):
        self.cookie__RequestVerificationToken = token

    def web_loadFinished(self):
        page = self.web.page()
        loc = page.url().path()
        host = page.url().host()

        if host == 'marketweb-na.blackdesertonline.com':
            self.host_local = 'https://' + host
            if self.this_connection is not None:
                self.this_connection.close()
            #conn = urllib3.connection_from_url(self.host_local)
            self.connection_pool = urllib3.HTTPSConnectionPool(host, maxsize=1, block=True)
            agent = self.profile.httpUserAgent()
            r = self.connection_pool.request('GET', '/Home/list/hot',
                                        headers={
                                            'Cookie': urlencode(self.cooks).replace('&', '; '),
                                            'User-Agent': agent
                                        })
            self.hot_load(r.data.decode('utf-8'))

    def hot_load(self, txt):
        dat = string_between(txt, '<form id="frmGetItemSellBuyInfo">', '</form>').strip()
        sdat = string_between(dat, 'value="', '"')
        self.frmGetItemSellBuyInfo_token = ''.join(sdat.split())
        dat = string_between(txt, '<form id="frmGetWorldMarketSubList"', '</form>').strip()
        sdat = string_between(dat, 'value="', '"')
        self.GetWorldMarketSubList_token = ''.join(sdat.split())
        coks = urlencode(self.cooks).replace('&', '; ')

        self.price_updator = CentralMarketPriceUpdator(self.profile, self.connection_pool, coks, self.GetWorldMarketSubList_token)
        self.sig_Market_Ready.emit(self.price_updator)
