__author__ = 'yalnazov'

api_key = '<YOUR PRIVATE API KEY>'
magic_token = '098f6bcd4621d373cade4e832627b4f6'


def get_next_amount():
    import time
    return int(str(time.time()).replace('.',''))