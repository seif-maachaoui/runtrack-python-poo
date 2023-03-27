class Livre:
    def __init__(self, title, author, pages):
        self.__title = "Dragon Ball"
        self.__author = "Akira Toriyama"
        self.__pages = 20

    def set_title(self, title):
        self.__title = title
        return self.__title
    
    def get_title(self):
        return self.__title
    
    def set_author(self, author):
        self.__author = author
        return self.__author

    def get_author(self):
        return self.__author  
    
    def set_pages(self, pages):
        if int(pages) >= 0:
            self.__pages = pages
            return self.__pages
        else:
            print("Erreur, veuillez choisir un nombre entier positif")
            return False
    
    def get_pages(self):
        return self.__pages

livre1 = Livre("Dragon Ball", "Akira Toriyama", 20)

print("Le titre du livre actuel est ", livre1.get_title())
livre1.set_title("The Hobbit")
print("Le nouveau titre du livre est", livre1.get_title())

print("\nL'auteur du livre actuel est ", livre1.get_author())
livre1.set_author(" J. R. R. Tolkien")
print("Le nouvel auteur du livre est", livre1.get_author())

print("\nLe nombre de pages actuel est de", livre1.get_pages(), "pages")
livre1.set_pages(380)
print("Le nouveau nombre de pages est de", livre1.get_pages(), "pages")





    

        