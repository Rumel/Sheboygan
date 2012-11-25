import os
import json
import urllib2
import imgur

def getOpener():
	opener = urllib2.build_opener()
	opener.addheaders = [('User-Agent', 'Sheboygan Reddit Downloader')]
	return opener

def buildUrl(base, sub):
	return base + sub + ".json"

def createIfNotExists(dir):
	if(not os.path.exists(dir)):
		os.mkdir(dir)
		print "Created " + dir
	return

def makeDir(dir):
	dls = ".\\downloads\\"
	img = "\\img"
	gif = "\\gif"
	dlDir = dls + dir
	dlDirImg = dlDir + img
	dlDirGif = dlDir + gif
	createIfNotExists(dls)
	createIfNotExists(dlDir)
	createIfNotExists(dlDirImg)
	createIfNotExists(dlDirGif)

class Reddit:
	BASE = "http://www.reddit.com/r/"
	URL = ""
	IMAGEURLS = []
	SUB = ""
	ARTICLES = []
	IMGS = 0
	ALBUMS = 0

	def __init__(self, sub, pages = 1):
		self.SUB = sub
		self.URL = buildUrl(self.BASE, self.SUB)
		self.getArticles(pages)
		return

	def getArticles(self, pages = 1):
		opener = getOpener()
		lastThing = ""
		for i in range(0, int(pages)):
			print "Getting page " + str(i + 1)
			if(i != 0):
				u = opener.open(self.URL + "?after=" + lastThing)
			else:
				u = opener.open(self.URL)
			j = json.load(u)
			d = j[u'data'][u'children']
			for a in d:
				self.ARTICLES.append(a[u'data'])
			try:
				lastThing = d[24][u'data'][u'name']
			except IndexError:
				print "Out of Range"
				break;

	def getImageUrls(self):
		for a in self.ARTICLES:
			self.IMAGEURLS.append(a[u'url'])
		return

	def downloadImage(self, iurl):
		makeDir(self.SUB)
		i = imgur.imgur()
		split = iurl.split(".")
		ext = split[len(split) - 1]
		if(ext == "jpg" or ext == "gif" or ext == "png"):
			i.directlyDownload(iurl, self.SUB)
			self.IMGS = self.IMGS + 1
		elif(iurl.split("/")[2] == "imgur.com" and iurl.split("/")[3] == "a"):
			self.IMGS = self.IMGS + i.downloadAlbum(iurl , self.SUB)
			self.ALBUMS = self.ALBUMS + 1
		elif(iurl.split("/")[2] == "imgur.com"):
			i.downloadImage(iurl, self.SUB)
			self.IMGS = self.IMGS + 1
		return

	def downloadImages(self):
		for i in self.IMAGEURLS:
			self.downloadImage(i)
		return