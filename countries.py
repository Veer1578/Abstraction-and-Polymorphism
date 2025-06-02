class India:
    def capital(self):
        print('Capital of India is New Delhi')
    def power(self):
        print('India has the 4th strongest military')
    def GDP(self):
        print('India GDP is 4 trillion')


class USA:
    def capital(self):
        print('Capital of USA is Washington DC')

    def power(self):
        print('USA has the strongest military')

    def GDP(self):
        print('USA GDP is 21 trillion')

india = India()
usa = USA()

for i in (india, usa):
    i.capital()
    i.power()
    i.GDP()
