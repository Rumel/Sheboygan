import os
import json
import urllib
import sys
import threading


def formatNumber(num):
    if(num < 10):
        return "00" + str(num)
    elif(num < 100):
        return "0" + str(num)
    else:
        return str(num)


def getJson(jsonUrl):
    try:
        u = urllib.urlopen(jsonUrl)
        return json.load(u)
    except:
        sys.stdout.write("Error occured on getting json\n")
        return 0


class Imgur:
    def __init_(self):

        return

    def directlyDownload(self, url, sub, album="", count=0):
        split = url.split("/")
        last = split[len(split) - 1]
        ext = last.split(".")[1]
        if(ext != "gif"):
            img = ".\\downloads\\" + sub + "\\img\\"
            if(album != ""):
                save = img + album + " - " + formatNumber(count) + "." + ext
            else:
                save = img + last
        else:
            gif = ".\\downloads\\" + sub + "\\gif\\"
            if(album != ""):
                save = gif + album + " - " + formatNumber(count) + ".gif"
            else:
                save = gif + last

        if(not os.path.exists(save)):
            try:
                urllib.urlretrieve(url, save)
            except IOError:
                sys.stdout.write("Imgur didn't respond\n")
            sys.stdout.write('Downloaded ' + save + '\n')
        else:
            sys.stdout.write('Skipping already downloaded\n')

    def downloadAlbum(self, url, sub):
        base = "http://api.imgur.com/2/album/"
        ending = url.split("/")[4]
        jsonUrl = base + ending + ".json"
        j = getJson(jsonUrl)
        if(j == 0):
            return 0

        #Check to see if the album exists
        for d in j:
            if(d == u'error'):
                sys.stdout.wrte('There was an error finding the album\n')
                return 0

        images = j[u'album'][u'images']
        count = 0
        for i in images:
            download = i[u'links'][u'original']
            self.directlyDownload(download, sub, album=ending, count=count)
            count = count + 1
        return count

    def downloadAlbumAsync(self, url, sub):
        base = "http://api.imgur.com/2/album/"
        ending = url.split("/")[4]
        jsonUrl = base + ending + ".json"
        j = getJson(jsonUrl)
        if(j == 0):
            return 0

        #Check to see if the album exists
        for d in j:
            if(d == u'error'):
                sys.stdout.wrte('There was an error finding the album\n')
                return 0

        images = j[u'album'][u'images']
        count = 0
        threads = []
        for i in images:
            count = count + 1
            download = i[u'links'][u'original']
            thread = threading.Thread(target=self.directlyDownload,
                                      args=([download, sub, ending, count]))
            threads.append(thread)
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        return count

    def downloadImage(self, url, sub):
        ending = url.split("/")[3]
        base = "http://api.imgur.com/2/image/"
        jsonUrl = base + ending + ".json"
        try:
            j = getJson(jsonUrl)
            if(j == 0):
                return
            link = j[u'image'][u'links'][u'original']
            self.directlyDownload(link, sub)
        except ValueError:
            sys.stdout.write(url + '\n' + jsonUrl +
                             '\nNo JSON object could be decoded\n')
        except:
            sys.stdout.write('Unkown Error\n')
        return
