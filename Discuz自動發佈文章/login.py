# -*- coding: utf-8 -*-

import config
import discuz

if __name__ == '__main__':
    my_account = discuz.Discuz()
    my_account.login(config.USERNAME, config.PASSWORD)
