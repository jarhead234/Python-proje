import db  

def urunEkle(urunAdi,fiyat):
    db.urunler.append({
        "id": len(db.urunler) + 1,
        "urunAdı": urunAdi,
        "urunFiyatı": fiyat 
    })


def urunGuncelle(id,urunAdi,fiyat):
    for urun in db.urunler:
        if(urun["id"] == id):
            urun["urunAdı"] == urunAdi
            urun["urunFiyatı"] == fiyat
            break


def urunleriGetir():
    for urun in db.urunler:
        print(f"id {urun["id"]} urunAdı: {urun["urunAdı"]} fiyat: {urun["fiyat"]}")