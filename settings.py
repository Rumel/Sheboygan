from reddit import Link

settingsFile = '''# Lines that begin with # are ignored
async = False
nsfw = False
upvotes =
comments =
downvotes =
score =
author =
'''


def convertSetting(s, t):
    s = str(s).lstrip().rstrip()
    if(t == "bool"):
        if(str.lower(s) == "true"):
            return True
        elif(str.lower(s) == "false"):
            return False
    elif(t == "string"):
        if s == "":
            return None
        return s
    elif(t == "int"):
        try:
            i = int(s)
            return i
        except ValueError:
            return None
    else:
        return None


def treatString(s):
    return str.lower(s).lstrip().rstrip()


class Settings:
    async = False
    nsfw = False
    upvotes = None
    comments = None
    downvotes = None
    score = None
    author = None

    def __init__(self):
        try:
            f = open('settings.txt', 'r')
            lines = f.readlines()
            for li in lines:
                l = li.lstrip().rstrip().split('=')

                if l[0][0] is not "#":
                    if treatString(l[0]) == "nsfw":
                        s = convertSetting(l[1], "bool")
                        if s is not None:
                            self.nsfw = s
                    elif treatString(l[0]) == "upvotes":
                        s = convertSetting(l[1], "int")
                        if s is not None:
                            self.upvotes = s
                    elif treatString(l[0]) == "comments":
                        s = convertSetting(l[1], "int")
                        if s is not None:
                            self.comments = s
                    elif treatString(l[0]) == "downvotes":
                        s = convertSetting(l[1], "int")
                        if s is not None:
                            self.downvotes = s
                    elif treatString(l[0]) == "score":
                        s = convertSetting(l[1], "int")
                        if s is not None:
                            self.score = s
                    elif treatString(l[0]) == "author":
                        s = convertSetting(l[1], "string")
                        if s is not None:
                            self.author = s
                    elif treatString(l[0]) == "async":
                        s = convertSetting(l[1], "bool")
                        if s is not None:
                            self.async = s
        except IOError:
            print "Settings file doesn't exist"
            print "Would you like one created? y or n"
            answer = raw_input()
            if(answer == "y"):
                self.CreateSettingsFile()
            else:
                print "Continuing with default settings"
        return

    def VerifySettings(self, link):
        reject = False
        if(self.nsfw is False and link.NSFW is True):
            print "Rejected NFSW"
            reject = True

        if(self.upvotes is not None):
            if link.Ups >= self.upvotes:
                print "Rejected not enough upvotes"
                reject = True

        if(self.comments is not None):
            if link.Num_Comments >= self.comments:
                print "Rejected not enough comments"
                reject = True

        if(self.downvotes is not None):
            if link.Downs <= self.downvotes:
                print "Rejected too many downvotes"
                reject = True

        if(self.score is not None):
            if link.Score >= self.score:
                print "Rejected score too low"
                reject = True

        if(self.author is not None):
            if link.Author != self.author:
                print "Rejected incorrect author"
                reject = True

        if reject is True:
            return False
        else:
            return True

    def CreateSettingsFile(self):
        global settingsFile
        f = open('settings.txt', 'w')
        f.write(settingsFile)
        return
