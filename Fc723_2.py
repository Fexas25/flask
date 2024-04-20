#libraitem can add item and locate, contains attibute: title, upc, subject, contributors
#store detail in item dictionary
class LibraItem:
    def __init__(self, title, upc, subject, contributors):
        self.title = title
        self.upc = upc
        self.subject = subject
        self.contributors = contributors
        self.item = {}

    #search item by upc or title and return the detail
    def locate(self, Upc):
        print(self.item[Upc])

    #add item by both title or upc
    def additem(self, Title, Upc, Subject, Contributors):
        self.item.update({Title: Contributors})
        self.item.update({Upc: Contributors})


#Contributor has one attribute name
class Contributor:
    def __init__(self, name):
        self.name = name

#Author is one of Contributor
class Author(Contributor):
    def __init__(self):
        pass

#Actor is one of Contributor
class Actor(Contributor):
    def __init__(self):
        pass

#Director is one of Contributor
class Director(Contributor):
    def __init__(self):
        pass

#Artist is one of Contributor
class Artist(Contributor):
    def __init__(self):
        pass

#Editor is one of Contributor
class Editor(Contributor):
    def __init__(self):
        pass