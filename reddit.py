import os
import json
import urllib2
import imgur

base = "http://www.reddit.com/r/"

imgs = 0
albums = 0

def getOpener():
	opener = urllib2.build_opener()
	opener.addheaders = [('User-Agent', 'Sheboygan Reddit Downloader')]
	return opener

def buildUrl(sub):
	global base
	return base + sub + ".json"

def getArticles(url, pages = 1):
	articles = []
	opener = getOpener()
	lastThing = ""
	for i in range(0, pages):
		print "Getting page " + str(i + 1)
		if(i != 0):
			u = opener.open(url + "?after=" + lastThing)
		else:
			u = opener.open(url)
		j = json.load(u)
		d = j[u'data'][u'children']
		for a in d:
			articles.append(a[u'data'])
		try:
			lastThing = d[24][u'data'][u'name']
		except IndexError:
			print "Out of Range"
			break;
	return articles

def getImageUrls(articles):
	urls = []
	for a in articles:
		urls.append(a[u'url'])
	return urls

def makeDir(dir):
	if(not os.path.exists(".\\downloads\\")):
		os.mkdir(".\\downloads\\")
		print "Created " + ".\\downloads\\"
	if(not os.path.exists(".\\downloads\\" + dir)):		
		os.mkdir(".\\downloads\\" + dir)
		print "Created " + ".\\downloads\\" + dir
	if(not os.path.exists(".\\downloads\\" + dir +"\\img")):
		os.mkdir(".\\downloads\\" + dir + "\\img")
		print "Created " + ".\\downloads\\" + dir + "\\img"
	if(not os.path.exists(".\\downloads\\" + dir + "\\gif")):
		os.mkdir(".\\downloads\\" + dir + "\\gif")
		print "Created " + ".\\downloads\\" + dir + "\\gif"

def downloadImage(url, sub):
	makeDir(sub)
	global albums
	global imgs
	i = imgur.imgur()
	split = url.split(".")
	ext = split[len(split) - 1]
	if(ext == "jpg" or ext == "gif" or ext == "png"):
		i.directlyDownload(url, sub)
		imgs = imgs + 1
	elif(url.split("/")[2] == "imgur.com" and url.split("/")[3] == "a"):
		imgs = imgs + i.downloadAlbum(url, sub)
		albums = albums + 1
	elif(url.split("/")[2] == "imgur.com"):
		i.downloadImage(url, sub)
		imgs = imgs + 1
	return

sub = raw_input("What subreddit would you like?\n")
pages = raw_input("How many pages?\n")

url = buildUrl(sub)

images = getImageUrls(getArticles(url, int(pages)))

for i in images:
	downloadImage(i, sub)

print "Downloaded " + str(imgs) + " images"
print "Downloaded " + str(albums) + " albums"