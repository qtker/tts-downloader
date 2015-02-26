import urllib2
import urllib
import time
import re
#http://translate.google.com/translate_tts?tl=en&q=Hello.+Everybody.+How+are+you?+I+am+fine.


class TtsDownloader():

    TTS_APT_URL = 'http://translate.google.com/translate_tts?tl=en&q='

    def __init__(self, text=''):
        self.params = self.split_string(text)

    def print_response(self):

        f = open('/Users/tenoritama/test.mp3', 'w')
        url = 'http://translate.google.com/translate_tts?tl=en&q=Hello.+Everybody.+How+are+you?+I+am+fine.'
        #headers = { 'User-Agent' : user_agent, 'Content-Type': 'audio/mp3'}
        headers = {"Host": "translate.google.com",
                   "Referer": "http://www.gstatic.com/translate/sound_player2.swf",
                   "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) "
                                 "AppleWebKit/535.19 (KHTML, like Gecko) "
                                 "Chrome/18.0.1025.163 Safari/535.19"
        }

        req = urllib2.Request(url,'', headers=headers)
        res = urllib2.urlopen(req)
        f.write(res.read())
        # print response.read()
        time.sleep(.5)
        f.close()
        #res = eval(response)['hypotheses']
        #urllib.urlretrieve(url, '/Users/tenoritama/test.mp3')

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
        time.sleep(.5)
        mp3_file.close()