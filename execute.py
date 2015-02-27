#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tts.downloader import TtsDownloader

# 文字列渡す場合
tts = TtsDownloader('hello world')
tts.download(path='/Users/a13659/test.mp3')

# url渡す場合
url = 'http://translate.google.com/translate_tts?tl=en&q=hello+world'
tts2 = TtsDownloader()
tts2.download(url, '/Users/a13659/test2.mp3')