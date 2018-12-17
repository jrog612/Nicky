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
        return open(os.path.join(PathManager.prefix_path(self.lang), 'prefix.txt'), mode)

    def get_suffix_file(self, genre, mode='r'):
        return open(os.path.join(PathManager.suffix_path(self.lang), '{}.txt'.format(genre)), mode)

    def get_suffix_file_list(self):
        return list(os.listdir(PathManager.suffix_path(self.lang)))

    def get_suffix_list(self, genre=None):
        if genre:
            return [i for i in self.get_suffix_file(genre).read().split('\n') if i]
        else:
            genre_list = [i.replace('.txt', '') for i in self.get_suffix_file_list()]
            ret_data = []

            for gn in genre_list:
                ret_data.extend(self.get_suffix_list(gn))

            return sorted(ret_data)

    def get_prefix_list(self):
        return [i for i in self.get_prefix_file().read().split('\n') if i]
