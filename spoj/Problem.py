
class Problem:

    def __init__(self, pid, pname, plink, quality, users, accuracy):
        self.id = pid
        self.name = pname
        self.link = plink
        self.quality = quality
        self.users = users
        self.accuracy = accuracy

    def __unicode__(self):
        return str(self.id) + ": " + self.name

    def __repr__(self):
        return str(self.id) + ": " + self.name
