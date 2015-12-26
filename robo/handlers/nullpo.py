# -*- coding: utf-8 -*-
"""
    robo.handlers.nullpo
    ~~~~~~~~~~~~~~~~~~~~

    Porting from
    `hubot-nullpo <https://github.com/qckanemoto/hubot-nullpo/>`_.


    :copyright: (c) 2015 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""
import os
from robo.decorators import cmd


class Nullpo(object):
    def __init__(self):
        self.rich = os.environ.get('ROBO_NULLPO_RESPONSE_STYLE', '')

    @cmd(regex=r'^(ぬるぽ|ヌルポ|nullpo)$', description='Say ｶﾞｯ')
    def get(self, message, **kwargs):
        if self.rich == 'rich':
            body = u"""
            　 Λ＿Λ　　　　＼＼
             （　・∀・）　　　|　|　ｶﾞｯ
             と　　　　）　　　|　|
             　 Ｙ　/ノ　　　 人
             　　 /　）　 　 < 　>_Λ∩
              ＿/し´　／／. Ｖ｀Д´）/
              （＿フ彡　　　　　　 /　>>@{0}
            """.format(message.send_from)
        else:
            body = u'ｶﾞｯ'

        return body
