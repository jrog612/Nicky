import os

from utils import PathManager


class Loader:
    def __init__(self, lang='ko'):
        self.lang = lang

    def get_prefix_file(self, mode='r'):
        return open(PathManager.prefix_path(self.lang), mode)

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


class SourceManager:
    def __init__(self, lang='ko'):
        self.lang = lang
        self.loader = Loader(lang)

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

    def pre_add(self, values):
        li = self.loader.get_prefix_list()
        f = self.loader.get_prefix_file('w')
        self.write(values, li, f)
