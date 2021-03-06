# -*- coding: utf-8 -*-
from hip2unicode.tools.binary_converter import binary_converter
import os
import codecs


def corpus_converter(path=None, corpus_folder='corpus', converted_corpus_folder='converted_corpus', conversions=None):

    if not path:
        path = os.path.abspath(os.getcwd())
    
    print '\nCurrent folder is "%s".' % path

    corpus_path = os.path.join(path, corpus_folder)
    converted_corpus_path = os.path.join(path, converted_corpus_folder)

    # проверяем наличие папки corpus в текущем каталоге
    
    if not os.path.exists(corpus_path):
        print 'Corpus folder with the name "%s" does not exist.' % corpus_folder
        raw_input('Press ENTER to exit program.')
        quit()

    def all_files(path):
        result = []
        for dirpath, subdirs, filenames in os.walk(path):
            if filenames:
                result.extend([os.path.join(dirpath, filename) for filename in filenames])
        return result

    def make_all_folders(path):
        p = os.path.dirname(path)
        if not os.path.exists(p):
            make_all_folders(p)
            os.mkdir(p)

    file_list = all_files(corpus_path)
    if not file_list:
        print 'There is no file to convert in the corpus folder.'
        raw_input('Press ENTER to exit program.')
        quit()

    # проверяем, существует ли папка converted_corpus
    # если не существует, создаём её
    converted_corpus_folder_exists = os.path.exists(converted_corpus_path)

    if converted_corpus_folder_exists:
        # проверяем, есть ли в ней файлы, и при наличии, удаляем их
        stuff_file_list = all_files(converted_corpus_path)
        for f in stuff_file_list:
            os.remove(f)
    else:
        os.mkdir(converted_corpus_path)

    enc_list = ['cp1251', 'koi8-r', 'utf-8',]
    print 'Converting files ',
    for file_path in file_list:

        new_path = file_path.replace(corpus_path, converted_corpus_path)
        
        # меняем все расширения на TXT
        new_path = '%(file_path)s%(ext_sep)s%(ext)s' % {
            'file_path': os.path.splitext(new_path)[0],
            'ext_sep': os.extsep,
            'ext': 'txt'
            }

        make_all_folders(new_path)
        binary_converter(file_path, new_path)
        
corpus_converter(
    converted_corpus_folder='corpus-utf-8',
    )
