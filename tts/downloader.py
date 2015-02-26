import urllib2
import time
import re


class TtsDownloader():

    TTS_APT_URL = 'http://translate.google.com/translate_tts?tl=en&q='

    def __init__(self, text=''):
        self.params = self.split_string(text)

    def split_string(self, text):
        tmp = re.sub(r'\s+', ' ', text)
        tmp = tmp.split(" ")
        return tmp

    def make_url(self, params=[]):
        url = self.TTS_APT_URL + '+'.join(params)
        return url

    def download(self, url=None, path='/'):
        if url is None:
            url = self.make_url(self.params)

        mp3_file = open(path, 'w')
        headers = {"Host": "translate.google.com",
                   "Referer": "http://www.gstatic.com/translate/sound_player2.swf",
                   "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) "
                                 "AppleWebKit/535.19 (KHTML, like Gecko) "
                                 "Chrome/18.0.1025.163 Safari/535.19"}
        reqest = urllib2.Request(url, '', headers=headers)
        response = urllib2.urlopen(reqest)
        mp3_file.write(response.read())
        mp3_file.close()