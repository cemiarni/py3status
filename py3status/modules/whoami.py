# -*- coding: utf-8 -*-
"""
Display the currently logged in user.

Inspired by i3 FAQ:
        https://faq.i3wm.org/question/1618/add-user-name-to-status-bar/
"""

from getpass import getuser
from time import time


class Py3status:
    """
    """
    # available configuration parameters
    cache_timeout = 1800

    def whoami(self, i3s_output_list, i3s_config):
        """
        We use the getpass module to get the current user.
        """
        # here you can change the format of the output
        # default is just to show the username
        username = '{}'.format(getuser())

        response = {
            'cached_until': time() + self.cache_timeout,
            'full_text': username
        }
        return response

if __name__ == "__main__":
    """
    Run module in test mode.
    """
    from py3status.module_test import module_test
    module_test(Py3status)
