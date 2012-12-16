import reddit
import time

sub = raw_input("What subreddit would you like?\n")
pages = raw_input("How many pages?\n")

sub = reddit.Reddit(sub, pages)
x = time.clock()
sub.downloadImagesAsync()
y = time.clock()

print y - x

print "Downloaded " + str(sub.IMGS) + " images"
print "Downloaded " + str(sub.ALBUMS) + " albums"
