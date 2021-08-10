class Article:
    title = ""
    text = ""
    src = ""
    img_src = ""
    parser = ""

    def __init__(self, title, text, src, img_src, parser):
        self.title = title
        self.text = text
        self.src = src
        self.img_src = img_src
        self.parser = parser


    def toArray(self):
        return {"title": self.title,
                "text": self.text,
                "src": self.src,
                "img_src": self.img_src,
                "parser": self.parser}