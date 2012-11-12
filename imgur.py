import os
import json
import urllib

def formatNumber(num):
	if(num < 10):
		return "00" + str(num)
	elif(num < 100):
		return "0" + str(num)
	else:
		return num

class imgur:
	def __init_(self):

		return

	def directlyDownload(self, url, sub, album = "", count = 0):
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
				save = gif + album + " - "  + formatNumber(count) + ".gif"
			else:
				save = gif + last

		if(not os.path.exists(save)):
			urllib.urlretrieve(url, save)
			print "Downloaded " + save
		else:
			print "Skipping already downloaded"

	def downloadAlbum(self, url, sub):
		base = "http://api.imgur.com/2/album/"
		ending = url.split("/")[4]
		jsonUrl = base + ending + ".json"
		u = urllib.urlopen(jsonUrl)
		j = json.load(u)
		images = j[u'album'][u'images']
		count = 1
		for i in images:
			download = i[u'links'][u'original']
			self.directlyDownload(download, sub, album = ending, count = count)
			count = count + 1
		return count

	def downloadImage(self, url, sub):
		ending = url.split("/")[3]
		base = "http://api.imgur.com/2/image/"
		jsonUrl = base + ending + ".json"
		try:
			u = urllib.urlopen(jsonUrl)
			j = json.load(u)
			link = j[u'image'][u'links'][u'original']
			self.directlyDownload(link, sub)
		except ValueError:
			print url
			print jsonUrl
			print "No JSON object could be decoded"
		except:
			print "Unknown Error"
		return