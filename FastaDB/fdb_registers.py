# DATA STRUCTURES WHICH ORGANIZE FDB FILES

from datetime import date

class FDBRegister():
    def __init__(self):
        self._description = ""
        self._gene = ""
        self._geneinfo = ""
        self._filename = ""
        self._date = date.today()
        self._user = ""
        self._observations = ""

    def __repr__(self):
        return self._gene

    def build_dictionary(self):
        dictionary = {}

        dictionary["description"] = self._description
        dictionary["gene"] = self._gene
        dictionary["geneinfo"] = self._geneinfo
        dictionary["filename"] = self._filename
        dictionary["date"] = str(self._date)
        dictionary["user"] = self._user
        dictionary["observations"] = self._observations

        return dictionary

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def gene(self):
        return self._gene

    @gene.setter
    def gene(self, gene):
        self._gene = gene

    @property
    def geneinfo(self):
        return self._geneinfo

    @geneinfo.setter
    def geneinfo(self, geneinfo):
        self._geneinfo = geneinfo

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, filename):
        self._filename = filename

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user

    @property
    def observations(self):
        return self._observations

    @observations.setter
    def observations(self, observations):
        self._observations = observations
