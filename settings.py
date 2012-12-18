from reddit import Link


class Settings:
    nsfw = False

    def __init__(self):
        return

    def VerifySettings(self, link):
        if(self.nsfw is False and link.NSFW is True):
            print "Rejected NFSW"
            return False
        return True
