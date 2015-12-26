# -*- coding: utf-8 -*-
"""
    robo.tests.test_nullpo_handler
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Tests for robo.handlers.nullpo.


    :copyright: (c) 2015 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""
import os
import logging
from unittest import TestCase
from robo.robot import Robot
from robo.handlers.nullpo import Nullpo


class NullAdapter(object):
    def __init__(self, signal):
        self.signal = signal
        self.responses = []

    def say(self, message, **kwargs):
        self.responses.append(message)
        return message


class TestNullpoHandler(TestCase):
    @classmethod
    def setUpClass(cls):
        logger = logging.getLogger('robo')
        logger.level = logging.ERROR
        cls.robot = Robot('test', logger)

        nullpo = Nullpo()
        nullpo.signal = cls.robot.handler_signal
        method = cls.robot.parse_handler_methods(nullpo)
        cls.robot.handlers.extend(method)

        adapter = NullAdapter(cls.robot.handler_signal)
        cls.robot.adapters['null'] = adapter

    def test_should_get_gattu(self):
        """ Nullpo().get() should return gattu. """
        self.robot.handler_signal.send('test nullpo')
        self.assertEqual(self.robot.adapters['null'].responses[0], u'ｶﾞｯ')
        self.robot.adapters['null'].responses = []


class TestRichNullpoHandler(TestCase):
    @classmethod
    def setUpClass(cls):
        os.environ['ROBO_NULLPO_RESPONSE_STYLE'] = 'rich'
        logger = logging.getLogger('robo')
        logger.level = logging.ERROR
        cls.robot = Robot('test', logger)

        nullpo = Nullpo()
        nullpo.signal = cls.robot.handler_signal
        method = cls.robot.parse_handler_methods(nullpo)
        cls.robot.handlers.extend(method)

        adapter = NullAdapter(cls.robot.handler_signal)
        cls.robot.adapters['null'] = adapter

    def test_should_get_rich_gattu(self):
        """ Nullpo().get() should return rich gattu. """
        self.robot.handler_signal.send('test nullpo')
        self.assertNotEqual(self.robot.adapters['null'].responses[0], u'ｶﾞｯ')
        self.robot.adapters['null'].responses = []
