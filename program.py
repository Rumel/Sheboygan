import reddit
import time
import sys

try:
    f = open(sys.argv[1], 'r')
    lines = f.readlines()
    for l in lines:
        split = l.split(' ')
        print "Downloading", split[0]
        sub = reddit.Reddit(split[0], split[1])
        sub.downloadImagesAsync()
except IndexError:
    sub = raw_input("What subreddit would you like?\n")
    pages = raw_input("How many pages?\n")
    sub = reddit.Reddit(sub, pages)
    x = time.clock()
    sub.downloadImagesAsync()
    y = time.clock()

    print y - x

    print "Downloaded " + str(sub.IMGS) + " images"
    print "Downloaded " + str(sub.ALBUMS) + " albums"
