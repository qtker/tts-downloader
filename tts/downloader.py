import urllib2
import re


class TtsDownloader():

    TTS_API_URL = 'http://translate.google.com/translate_tts?tl=en&q='

    def __init__(self, text=None):
        self.params = self.check_max_char(self.split_string(text))\
            if text is not None else []

    def split_string(self, text):
        tmp = re.sub(r'\s+', ' ', text)
        tmp = tmp.split(' ')
        return tmp

    def make_url(self, params):
        url = self.TTS_API_URL + '+'.join(params)
        return url

    def download(self, path='/', url=None):
        if url is None:
            url = self.make_url(self.params)

        mp3_file = open(path, 'w')
        headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)"}
        request = urllib2.Request(url, '', headers=headers)
        try:
            response = urllib2.urlopen(request)
            mp3_file.write(response.read())
        except urllib2.URLError as e:
            print 'url error : %s' % e
        mp3_file.close()

    def check_max_char(self, params):
        if len(params) > 100:
            return params[0:100]
        else:
            return params