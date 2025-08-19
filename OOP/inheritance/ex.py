class Media:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def displayMedia(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        
class DigitalMedia(Media):
    def __init__(self, title, author, fileFormat):
        Media.__init__(self, title, author)
        self.fileFormat = fileFormat
    
    def displayDigitalMedia(self):
        print(f"File Format: {self.fileFormat}")
    
class Ebook(DigitalMedia):
    def __init__(self, title, author, fileFormat, fileSize):
        DigitalMedia.__init__(self, title, author, fileFormat)
        self.fileSize = fileSize
    
    def displayEbook(self):
        print(f"File Size: {self.fileSize}")

a = input()
b = input()
c = input()
d = input()

e = Ebook(a, b, c, d)
e.displayMedia()
e.displayDigitalMedia()
e.displayEbook()