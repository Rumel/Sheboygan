from reddit import Link

settingsFile = '''# Lines that begin with # are ignored
nsfw = False
upvotes = -1
comments = -1
downvotes = -1
score = -1
author = 
'''


def convertSetting(s):
    try:
        if(str.lower(s) == "true"):
            return True
        elif(str.lower(s) == "false"):
            return False
        else:
            try:
                i = int(s)
                return i
            except ValueError:
                return s
    except IndexError:
        return None
    return


def treatString(s):
    return str.lower(s).lstrip().rstrip()


class Settings:
    nsfw = False
    upvotes = -1
    comments = -1
    downvotes = -1
    score = 0
    author = ""

    def __init__(self):
        try:
            f = open('settings.txt', 'r')
            print "Opened"
            lines = f.readlines()
            for li in lines:
                print li
                l = li.split('=')
                if l[0][0] is not "#":
                    if treatString(l[0]) == "nsfw":
                        s = convertSetting(l[1])
                        if s is not None:
                            self.nsfw = s
                    elif treatString(l[0]) == "upvotes":
                        s = convertSetting(l[1])
                        if s is not None:
                            self.upvotes = s
                    elif treatString(l[0]) == "comments":
                        s = convertSetting(l[1])
                        if s is not None:
                            self.comments = s
                    elif treatString(l[0]) == "downvotes":
                        s = convertSetting(l[1])
                        if s is not None:
                            self.downvotes = s
                    elif treatString(l[0]) == "score":
                        s = convertSetting(l[1])
                        if s is not None:
                            self.score = s
                    elif treatString(l[0]) == "author":
                        s = convertSetting(l[1])
                        if s is not None:
                            self.author = s
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
        if(self.nsfw is False and link.NSFW is True):
            print "Rejected NFSW"
            return False
        return True

    def CreateSettingsFile(self):
        global settingsFile
        f = open('settings.txt', 'w')
        f.write(settingsFile)
        return
