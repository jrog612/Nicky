import os

from utils import SOURCE_PATH, SUPPORT_LANG_LIST


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


class LoadManager:
    def __init__(self, lang='ko'):
        self.lang = lang

    def get_prefix_file(self, mode='r'):
        return open(PathManager.prefix_path(self.lang), mode)

    def get_suffix_file(self, genre, mode='r'):
        if genre not in self.get_suffix_file_list():
            open(os.path.join(PathManager.suffix_path(self.lang), '{}.txt'.format(genre)), 'w').close()
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


class SourceManager:
    def __init__(self, lang='ko'):
        self.lang = lang
        self.loader = LoadManager(lang)

    def write(self, values, item_list, f):
        for v in values:
            if not v:
                continue
            elif v in item_list:
                print('{} is already exists'.format(v))
            else:
                item_list.append(v)

        item_list.sort()
        f.write('\n'.join(item_list))
        f.close()

    def suf_add(self, genre, values):
        li = self.loader.get_suffix_list(genre)
        f = self.loader.get_suffix_file(genre, 'w')
        self.write(values, li, f)

    def suf_ordering(self, genre=None):
        if genre is None:
            for g in self.loader.get_suffix_file_list():
                self.suf_ordering(g)
        else:
            li = self.loader.get_suffix_list(genre)
            f = self.loader.get_suffix_file(genre, 'w')
            self.write([], li, f)

    def pre_ordering(self):
        li = self.loader.get_prefix_list()
        f = self.loader.get_prefix_file('w')
        self.write([], li, f)

    def pre_add(self, values):
        li = self.loader.get_prefix_list()
        f = self.loader.get_prefix_file('w')
        self.write(values, li, f)
