import os

BASE_DIR = os.path.dirname(__file__)
SOURCE_PATH = os.path.join(BASE_DIR, 'source')

SUPPORT_LANG_LIST = [
    'ko',
]


class PathManager:
    @classmethod
    def lang_path(cls, lang='ko'):
        if lang not in SUPPORT_LANG_LIST:
            raise ValueError('unsupported language.')
        return os.path.join(SOURCE_PATH, lang)

    @classmethod
    def suffix_path(cls, lang='ko'):
        return os.path.join(cls.lang_path(lang), 'suffix')

    @classmethod
    def prefix_path(cls, lang='ko'):
        return os.path.join(cls.lang_path(lang), 'prefix.txt')


class Loader:
    def __init__(self, lang='ko'):
        self.lang = lang

    def get_prefix_file(self, mode='r'):
        path = os.path.join(PathManager.prefix_path(self.lang), 'prefix.txt')
        return open(path, mode)

    def get_suffix_file(self, genre, mode='r'):
        path = os.path.join(PathManager.suffix_path(self.lang), '{}.txt'.format(genre))
        return open(path, mode)

    def get_suffix_file_list(self):
        pass

    def get_suffix_list(self, genre=None):
        if genre:
            file = self.get_suffix_file(genre)

    def get_prefix_list(self):
        pass
