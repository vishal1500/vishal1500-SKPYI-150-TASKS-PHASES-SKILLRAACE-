class Book:
    def __init__(self, title, author, publisher, price):
        self._title = title
        self._author = author
        self._publisher = publisher
        self._price = price
        self._author_royalty = 0

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, value):
        self._publisher = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    def royalty(self, copies_sold):
        if copies_sold <= 500:
            self._author_royalty = 0.1 * self._price * copies_sold
        elif copies_sold <= 1500:
            self._author_royalty = (0.1 * 500 * self._price) + (0.125 * self._price * (copies_sold - 500))
        else:
            self._author_royalty = (0.1 * 500 * self._price) + (0.125 * 1000 * self._price) + (0.15 * self._price * (copies_sold - 1500))
        return self._author_royalty


class Ebook(Book):
    def __init__(self, title, author, publisher, price, format):
        super().__init__(title, author, publisher, price)
        self._format = format

    @property
    def format(self):
        return self._format

    @format.setter
    def format(self, value):
        self._format = value

    def royalty(self, copies_sold):
        royalty_amount = super().royalty(copies_sold)
        gst_deducted = royalty_amount * 0.12
        return royalty_amount - gst_deducted