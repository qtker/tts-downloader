#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tts.downloader import TtsDownloader

tts = TtsDownloader('hello world')
tts.download(path='/Users/hogehoge/test.mp3')