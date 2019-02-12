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

from datetime import datetime

class User():
    """Represents an user on the intranet. This class parse
    and give formatted information about an user.

    Attributes
    -----------
    id: int
        The internal unique ID of the user.
    login: str
        The unique login (username) of the user.
    firstname: str
        The first name of the user.
    lastname: str
        The last name of the user.
    email: str
        The ETNA email of the user.
    close: bool
        An boolean to know if the account of the user is closed.
    closed_at: Optional[`datetime.datetime`]
        The date of closure of the account if it took place.
    roles: list of str
        The roles of the user.
    created_at: :class:`datetime.datetime`
        The date of creation of the account.
    updated_at: :class:`datetime.datetime`
        The date of the last update of the account.
    deleted_at: Optional[`datetime.datetime`]
        The date of deletion of the account if the account has been deleted.
    """

    def __init__(self, json_data):
        self.id = json_data["id"]
        self.login = json_data["login"]
        self.firstname = json_data["firstname"]
        self.lastname = json_data["lastname"]
        self.email = json_data["email"]
        if isinstance(json_data["close"], (bool)):
            self.close = False
        else:
            self.close = True
            self.closed_at = datetime.strptime(json_data["close"], '%Y-%m-%d %H:%M:%S')
        self.roles = json_data["roles"]
        if json_data["created_at"] is not None:
            self.created_at = datetime.strptime(json_data["created_at"], '%Y-%m-%d %H:%M:%S')
        if json_data["updated_at"] is not None:
            self.updated_at = datetime.strptime(json_data["updated_at"], '%Y-%m-%d %H:%M:%S')
        if json_data["deleted_at"] is not None:
            self.deleted_at = datetime.strptime(json_data["deleted_at"], '%Y-%m-%d %H:%M:%S')

    @property
    def identity(self):
        """A property that returns the first name and last name with a space
        between.
        """
        return self.firstname + ' ' + self.lastname

    def is_closed(self):
        if self.close:
            return True, self.closed_at
        else:
            return False, None
