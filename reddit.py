import os
import json
import urllib2
import imgur
import time
import threading

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
	LINKS = []
	SUB = ""
	IMGS = 0
	ALBUMS = 0

	def __init__(self, sub, pages = 1):
		self.SUB = sub
		self.URL = buildUrl(self.BASE, self.SUB)
		self.getLinks(pages)
		return

	def getLinks(self, pages = 1):
		print "This will take approximately " + str(int(pages) * 2) + " seconds."
		print "This is due to Reddit's two second API rule"
		opener = getOpener()
		after = ""
		for i in range(0, int(pages)):
			print "Getting page " + str(i + 1)
			if(i != 0):
				u = opener.open(self.URL + "?after=" + after)
			else:
				u = opener.open(self.URL)
			page = json.load(u)
			children = page[u'data'][u'children']
			for l in children:
				self.LINKS.append(Link(l))
			after = page[u'data'][u'after']
			if(after is None):
				break
		time.sleep(2)


	def downloadImage(self, iurl):
		i = imgur.Imgur()
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
		makeDir(self.SUB)
		for i in self.LINKS:
			self.downloadImage(i.URL)
		return

	def downloadImagesAsync(self):
		makeDir(self.SUB)
		for i in self.LINKS:
			#self.downloadImage(i.URL)
			thread = threading.Thread(target=self.downloadImage, args=([i.URL]))
			thread.start()
		return

class Link:
	def __init__(self, link):
		self.Kind = link[u'kind']
		data = link[u'data']
		self.Domain = data[u'domain']
		self.Banned_by = data[u'banned_by']
		self.Media_embed = data[u'media_embed']
		self.Subreddit = data[u'subreddit']
		self.Selftext_html = data[u'selftext_html']
		self.Likes = data[u'likes']
		self.Id = data[u'id']
		self.Clicked = data[u'clicked']
		self.Title = data[u'title']
		self.Num_Comments = data[u'num_comments']
		self.Score = data[u'score']
		self.Approved_By = data[u'approved_by']
		self.NSFW = data[u'over_18']
		self.Hidden = data[u'hidden']
		self.Thumbnail = data[u'thumbnail']
		self.Subreddit_id = data[u'subreddit_id']
		self.Edited = data[u'edited']
		self.Link_flair_css_class = data[u'link_flair_css_class']
		self.Downs = data[u'downs']
		self.Saved = data[u'saved']
		self.Is_self = data[u'is_self']
		self.Permalink = data[u'permalink']
		self.Name = data[u'name']
		self.Created = data[u'created']
		self.URL = data[u'url']
		self.Author_flair_text = data[u'author_flair_text']
		self.Author = data[u'author']
		self.Media = data[u'media']
		self.Num_reports = data[u'num_reports']
		self.Ups = data[u'ups']
		return