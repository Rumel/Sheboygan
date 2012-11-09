import os
import json
import urllib

class imgur:
	def __init_(self):

		return

	def directlyDownload(self, url, sub):
		split = url.split("/")
		last = split[len(split) - 1]
		if(last.split(".")[1] != "gif"):
			save = ".\\downloads\\" + sub + "\\img\\" + last
		else:
			save = ".\\downloads\\" + sub + "\\gif\\" + last

		if(not os.path.exists(save)):
			urllib.urlretrieve(url, save)
			print "Downloaded " + save
		else:
			print "Skipping already downloaded"

	def downloadAlbum(self, url, sub):
		print "Albums not ready"
		return

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