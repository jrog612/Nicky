
class LoadMixin:
    def load_prefix(self, lang='ko'):
        lang_path = self.get_lang_path(lang)
        prefix_path = os.path.join(lang_path, 'prefix')

    def get_lang_path(self, lang='ko'):
        lang_path = os.path.join(SOURCE_PATH, lang)
        if not os.path.isdir(lang_path):
            raise ValueError('Invalid language.')

        return lang_path

    def load_suffix(self, lang='ko'):
        lang_path = self.get_lang_path(lang)
        suffix_path = os.path.join(lang_path, 'suffix')


class Nicky:
    def __init__(self, lang='ko'):
        self.lang = lang

    def get_nickname(self, count=1):
        pass
