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

class Promo():
    """Represents an promotion on the intranet. This class parse
    and give formatted information about an promotion.

    Attributes
    -----------
    id: int
        The internal unique ID of the promotion.
    target_name: str
        The full name of the promotion.
    term_name: str
        The name and month of the promotion.
    learning_start: :class:`datetime.datetime`
        The start date of the promotion.
    learning_end: :class:`datetime.datetime`
        The end date of the promotion.
    learning_duration: int
        The duration of the promotion in days.
    promo: str
        The year of the promotion.
    spe: str
        The speciality of promotion.
    wall_name: str
        The name of the wall associated with the promotion.
    """

    def __init__(self, json_data):
        self.id = json_data["id"]
        self.target_name = json_data["target_name"]
        self.term_name = json_data["term_name"]
        self.learning_start = datetime.strptime(json_data["learning_start"], '%Y-%m-%d').date()
        self.learning_end = datetime.strptime(json_data["learning_end"], '%Y-%m-%d').date()
        self.learning_duration = json_data["learning_duration"]
        self.promo = json_data["promo"]
        self.spe = json_data["spe"]
        self.wall_name = json_data["wall_name"]
