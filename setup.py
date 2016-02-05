# coding: utf-8

from distutils.core import setup

LONGDOC = """
Please go to https://github.com/someus/TextRank4ZH for more info.
"""

setup(
    name='Hanzi2Pinyin',
    version='0.1',
    description='将汉字转换为拼音',
    long_description=LONGDOC,
    author='Letian Sun',
    author_email='sunlt1699@gmail.com',
    url='https://github.com/someus/TextRank4ZH',
    license="MIT",
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Chinese (Traditional)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Linguistic',
    ],
    keywords='NLP,Chinese',
    packages=['Hanzi2Pinyin'],
    package_dir={'Hanzi2Pinyin':'Hanzi2Pinyin'},
    package_data={'Hanzi2Pinyin':['*.py', 'data/*.db']},
)