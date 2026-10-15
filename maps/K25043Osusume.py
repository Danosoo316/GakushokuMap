from maps.AbstractGakushoku import AbstractGakushoku

class K25043Sample(AbstractGakushoku):

    def get_menu(self):
        return "お弁当を持ってくる"

    def get_summary(self):
        return "学食は混むから並ばずに済む"

    def get_author(self):
        return "K25043"