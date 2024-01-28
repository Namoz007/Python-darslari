class hayvon:
    def __init__(self,nom,ovqat,manzil,gender,country,harakat) -> None:
        self.n = nom
        self.o = ovqat
        self.m = manzil
        self.gen = gender
        self.count = country
        self.har = harakat
    def harakat(self):
        return "Yugur"
    def gender(self):
        return self.gen
    def country(self):
        return self.count
    def adress(self):
        return self.m
    def ovqat(self):
        return self.o
    def nom(self):
        return self.n
    def info(self):
        return f"""
Animal name : {self.n}
Animal food : {self.o}
Animal adress : {self.m}
Animal gender : {self.gen}
Animal country : {self.count}
Animal harakat : {self.har}        
        """
class yirtqich(hayvon):
    pass
class uy(hayvon):
    pass
h1 = hayvon("Yo'lbars","go'sht",'savanna ormonlari','erkak',"Sudan",'tez yuguradi')
print(h1.info())