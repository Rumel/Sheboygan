import reddit

sub = raw_input("What subreddit would you like?\n")
pages = raw_input("How many pages?\n")

sub = reddit.Reddit(sub, pages)
sub.getImageUrls()
sub.downloadImages()

print "Downloaded " + str(sub.IMGS) + " images"
print "Downloaded " + str(sub.ALBUMS) + " albums"