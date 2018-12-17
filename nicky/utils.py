import os

BASE_DIR = os.path.dirname(__file__)
SOURCE_PATH = os.path.join(BASE_DIR, 'source')
COMMANDS_PATH = os.path.join(BASE_DIR, 'commands')

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
