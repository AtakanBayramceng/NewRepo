
class magaza:
    def __init__(self,magaza_adi,satici_adi,satici_cinsi,satis_tutari):
        self.__magaza_adi=magaza_adi
        self.__satici_adi=satici_adi
        self.__satici_cinsi=satici_cinsi
        self.__satis_tutari=satis_tutari

    def getmagazaadi(self):
        return self.__magaza_adi
    def getsaticiadi(self):
        return self.__satici_adi
    def getsaticins(self):
        return self.__satici_cinsi
    def getsatis_tutari(self):
        return self.__satis_tutari
    

    def set_satici_cinsi(self, satici_cinsi):
        self.__satici_cinsi = satici_cinsi
    def set_satici_adi(self, satici_adi):
        self.__satici_adi = satici_adi
    def set_magaza_adi(self, magaza_adi):
        self.__magaza_adi = magaza_adi
    def set_satis_tutari(self, satis_tutari):
        self.__magaza_adi = satis_tutari
    def __str__(self):
        return f"Mağaza Adi: {self.__magaza_adi}, Satici Adi: {self.__satici_adi}, Satic Cinsi: {self.__satici_cinsi}, Satis tutari: {self.__satis_tutari}"