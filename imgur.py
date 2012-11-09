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
		base = "http://www.imgur.com/r/"
		jsonUrl = base + sub + "/" + ending + ".json"
		try:
			u = urllib.urlopen(jsonUrl)
			j = json.load(u)
			data = j[u'data'][u'image']
			h = str(data[u'hash'])
			ext = str(data[u'ext'])
			download = "http://i.imgur.com/" + h + ext
			self.directlyDownload(download, sub)
		except ValueError:
			print url
			print jsonUrl
			print "No JSON object could be decoded"
		except:
			print "Unknown Error"
		return