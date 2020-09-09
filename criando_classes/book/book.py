# exercise book

class book:
    page = ''
    letter = ''
    ink = ''
    title = ''

    def __init__(self, page, title):
        self.page = page
        self.title = title

    def mudar_pagina(self, som="flip through"):
        print(som)
    
    def nome(self):
        print('Title')