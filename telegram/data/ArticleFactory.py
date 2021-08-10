from data.Article import Article


class ArticleFactory:

    @staticmethod
    def create(data: dict) -> Article:
        """
        :param data: ['title', 'text', 'src', 'img_src', 'parser']
        :return:
        """
        if data:
            return Article(data.get("title"), data.get("text"), data.get("src"), data.get("img_src"), data.get("parser"))
        else:
            return Article("", "", "", "", "")
