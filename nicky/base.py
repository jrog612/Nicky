import random

from nicky.managers import LoadManager


class Nicky:
    def __init__(self, lang='ko'):
        self.lang = lang
        self.loader = LoadManager(lang)

    def get_nickname(self, count=1, suffix_genre=None):
        prefix = self.loader.get_prefix_list()
        suffix = self.loader.get_suffix_list(suffix_genre)
        return ['{} {}'.format(random.choice(prefix), random.choice(suffix)) for _ in range(count)]
