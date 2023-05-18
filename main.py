import classessatis
def magaza_satistutar(instancelar:dict,magazaAdi:str):
    tutar=0
    liststici=[]
    for i in instancelar.values():
        if magazaAdi.__eq__(i.getmagazaadi()):
            tutar+=i.getsatis_tutari()
            liststici.append(i.getsaticiadi())
    setsaticilar=list(set(liststici))
    satis_tutari_lst=[]
    satis_adedi_lst=[]
    for j in setsaticilar:
        tutarsatici=0
        adedsatici=0
        for i in instancelar.values():
            if j==i.getsaticiadi():
                tutarsatici+=i.getsatis_tutari()
                adedsatici+=1
        satis_tutari_lst.append(tutarsatici)
        satis_adedi_lst.append(adedsatici)

    return tutar , setsaticilar, satis_tutari_lst , satis_adedi_lst

    
magaza_adi=""
satici_adi=""
satici_cinsi=""
satis_tutari=0
instancelar={}
while (True):
    print("\n\n=======================  MENU ================================")
    print("(-1)-For EXIT press -1")
    print("(1)-Yeni magaza olusturmak icin 1 bas")
    print("(2)-Magaza adina gore toplam tutar hesaplamak icin 2 ye basiniz ")
    print("(3)-Tum magaza bilgileri icin 3 basiniz")
    print("===============================================================\n\n")
    inputval=str(input("Seciniz : "))
    if inputval=="-1":
        break
    elif inputval=="1":
        magaza_adi=str(input("Magaza adi giriniz: "))
        satici_adi=str(input("Satici adi giriniz: "))
        satici_cinsi=str(input("Satici cinsi  giriniz: "))
        satis_tutari=int(input("Satis tutari  giriniz: "))
        new_instance=classessatis.magaza(magaza_adi,satici_adi,satici_cinsi,satis_tutari)
        instancelar[new_instance.getmagazaadi]=new_instance
    elif inputval=="2":
        admagaza=(input("Arama yapilacak magaza adi giriniz :"))
        toplamtutar,birdenfazlasatanlar,satilanfiyat,satisadedi=magaza_satistutar(instancelar,admagaza)
        print(f"{admagaza} magazasi icin toplam satis tutari {toplamtutar} TL'dir")
        for i in range(0,len(birdenfazlasatanlar)):
            print(f"{birdenfazlasatanlar[i]} isimli satici ,{satisadedi[i]} kere satis yaparak toplamda {satilanfiyat[i]} TL tutarinda satis yapti")
    elif inputval=="3":
        for i in instancelar.values():
            print(i.__str__())
    else:
        print("yanlis input")

