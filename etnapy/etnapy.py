# -*- coding: utf-8 -*-

"""
A python wrapper to help make python3 apps/bots using the ETNA API

The MIT License (MIT)

Copyright (c) 2019 Yohann MARTIN

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import requests
import functools

from .user import User
from .promo import Promo
from .trophy import Trophy

class Intra():
    """Represents the ETNA intranet. This class give
    functions for getting various information on the
    intranet.

    Attributes
    -----------
    etna_login: str
        The login of the user connected.
    is_logged: bool
        A boolean to know if an user is connected.
    """

    def __init__(self):
        self.session = requests.Session()
        self.etna_login = ""
        self.is_logged = False

    def login(self, user, password):
        """Establish a connection with the intranet.

        Parameters
        ----------
        user : str
            The username.
        password : str
            The password.

        Returns
        -------
        dict or ``None``
            A json dict with some information about the user. Prefer the
            method :func:`user_info` for getting user information. Return
            Returns ``None`` if the connection failed.
        """

        if self.is_logged:
            return None

        payload = {'login': user, 'password': password}
        res = self.session.post('https://auth.etna-alternance.net/identity', data=payload)
        res.encoding = 'utf-8'

        if (res.status_code == requests.codes.ok):
            self.is_logged = True
            self.user = user
            self.pwd = password
            self.etna_login = res.json()["login"]
            return res.json()
        else:
            return None

    def keep_alive(self, func):
        """A simple decorator to make sure you're always connected.
        """

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = self.session.get('https://auth.etna-alternance.net/identity')

            if res.status_code != requests.codes.ok:
                self.etna_login = ""
                self.is_logged = False
                self.login(self.user, self.pwd)
            return func(*args, **kwargs)
        return wrapper

    def keep_alive_async(self, func):
        """A simple decorator to make sure you're always connected.
        This one accept and only accept asynchronous coroutines.
        """
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            res = self.session.get('https://auth.etna-alternance.net/identity')

            if res.status_code != requests.codes.ok:
                self.etna_login = ""
                self.is_logged = False
                self.login(self.user, self.pwd)
            return await func(*args, **kwargs)
        return wrapper

    def user_info(self, user_login=None):
        """Get information about an user.

        Parameters
        ----------
        user_login : Optionnal[str]
            The user login. If no login provided the current connected
            user will be used.

        Returns
        -------
        :class:`User` or ``None``
            The user object containing the formatted information. ``None`` if
            an error occured.
        """

        if not self.is_logged:
            return None

        if user_login is None:
            user_login = self.etna_login

        res = self.session.get('https://auth.etna-alternance.net/api/users/%s' % (user_login,))
        res.encoding = 'utf-8'

        if (res.status_code == requests.codes.ok):
            return User(res.json())
        else:
            return None

    def user_avatar(self, user_login=None):
        """Get the raw bytes of the user avatar.

        Parameters
        ----------
        user_login : Optionnal[str]
            The user login. If no login provided the current connected
            user will be used.
        """

        if not self.is_logged:
            return None

        if user_login is None:
            user_login = self.etna_login

        url = 'https://auth.etna-alternance.net/api/users/%s/photo' % (user_login,)
        res = self.session.get(url, stream=True)
        res.encoding = 'utf-8'

        if (res.status_code == requests.codes.ok):
            return res.raw
        else:
            return None

    def user_promo(self, user_login=None):
        """Get information about an user's promotion.

        Parameters
        ----------
        user_login : Optionnal[str]
            The user login. If no login provided the current connected
            user will be used.

        Returns
        -------
        list of :class:`Promo` or ``None``
            A list of promotion objects containing the formatted information.
            ``None`` if an error occured.
        """

        if not self.is_logged:
            return None

        if user_login is None:
            user_login = self.etna_login

        res = self.session.get('https://intra-api.etna-alternance.net/promo?login=%s' % (user_login,))
        res.encoding = 'utf-8'

        if (res.status_code == requests.codes.ok):
            return [Promo(x) for x in res.json()]
        else:
            return None

    def walls_list(self):
        """Get all the connected user's walls.

        Returns
        -------
        list of str or ``None``
            A list of walls name. ``None`` if an error occured.
        """

        if not self.is_logged:
            return None

        res = self.session.get('https://intra-api.etna-alternance.net/walls')
        res.encoding = 'utf-8'

        if (res.status_code == requests.codes.ok):
            return res.json()
        else:
            return None

    def wall_messages(self, wall_name, start, stop):
        """Get wall's messages.

        Parameters
        ----------
        wall_name : str
            The name of the wall.
        start: int
            The start index of the messages. Start from 0.
        stop: int
            The stop index of the messages.

        Returns
        -------
        dict or ``None``
            A json object of the messages.
        """

        if not self.is_logged:
            return None

        url = 'https://intra-api.etna-alternance.net/walls/%s/conversations?from=%d&size=%d' % (wall_name, start, stop)
        res = self.session.get(url)
        res.encoding = 'utf-8'

        if (res.status_code == requests.codes.ok):
            return res.json()
        else:
            return None

    def user_trophy(self, user_login=None):
        """Get user's trophy.

        Parameters
        ----------
        user_login : Optionnal[str]
            The user login. If no login provided the current connected
            user will be used.

        Returns
        -------
        list of :class:`Trophy` or ``None``
            The list of Trophy objects.
        """

        if not self.is_logged:
            return None

        if user_login is None:
            user_login = self.etna_login

        res = self.session.get('https://achievements.etna-alternance.net/api/users/%s/achievements' % (user_login,))
        res.encoding = 'utf-8'

        if (res.status_code == requests.codes.ok):
            return [Trophy(x) for x in res.json()]
        else:
            return None

    def trophy_picture(self, id_trophy):
        """Get a tuple with the URL of the trophy avatar and the raw
        content (bytes) of the avatar.

        Parameters
        ----------
        id_trophy : int
            The unique ID of a trophy.
        """

        if not self.is_logged:
            return None, None

        url = 'https://achievements.etna-alternance.net/api/achievements/%d.png' % (id_trophy,)
        res = self.session.get(url, stream=True)
        res.encoding = 'utf-8'

        if (res.status_code == requests.codes.ok):
            return url, res.raw
        else:
            return None, None

    def logout(self):
        """Log out from the intranet.
        """

        if not self.is_logged:
            return
        self.session.delete('https://auth.etna-alternance.net/identity')
        self.is_logged = False
        self.etna_login = ""
        self.user = ""
        self.pwd = ""
