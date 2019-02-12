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

class Trophy():
    """Represents an trophy on the intranet. This class parse
    and give formatted information about an trophy.

    Attributes
    -----------
    id: int
        The internal unique ID of the trophy.
    name: str
        The name of the trophy.
    description: str
        The description of the trophy.
    type: str
        The type of the trophy.
    image_url: str
        The URL of the trophy's image.
    achieved_at: :class:`datetime.datetime`
        The date of presentation of the trophy.
    """

    def __init__(self, json_data):
        self.id = json_data["id"]
        self.name = json_data["name"]
        self.description = json_data["description"]
        self.type = json_data["type"]
        self.image_url = 'https://achievements.etna-alternance.net/api/achievements/%d.png' % (self.id)
        self.achieved_at = datetime.strptime(json_data["achieved_at"][0], '%Y-%m-%d %H:%M:%S')
