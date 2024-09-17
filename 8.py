from abc import ABC, abstractmethod
import json

class TELEFON(ABC):
    def __init__(self, brend, model, tezkor_xotira_hajmi):
        self.brend = brend
        self.model = model
        self.__id = id(self)
        self._narxi = 0
        self.tezkor_xotira_hajmi = tezkor_xotira_hajmi

    def brendini_olish(self):
        return self.brend

    def modelini_olish(self):
        return self.model

    def id_sini_korish(self):
        return self.__id

    @abstractmethod
    def narx_qoyish(self, narx):
        pass

    @abstractmethod
    def narxini_korish(self):
        pass

    def to_dict(self):
        return {
            "brend": self.brend,
            "model": self.model,
            "tezkor_xotira_hajmi": self.tezkor_xotira_hajmi,
            "id": self.__id,
            "narx": self._narxi
        }

# Iphone class
class iphone(TELEFON):
    def __init__(self, model, tezkor_xotira_hajmi):
        super().__init__("Iphone", model, tezkor_xotira_hajmi)

    def narx_qoyish(self, narx):
        self._narxi = narx

    def narxini_korish(self):
        return self._narxi

# Samsung class
class samsung(TELEFON):
    def __init__(self, model, tezkor_xotira_hajmi):
        super().__init__("Samsung", model, tezkor_xotira_hajmi)

    def narx_qoyish(self, narx):
        self._narxi = narx

    def narxini_korish(self):
        return self._narxi

# Faylga yozish
def telefonlarni_faylga_yozish(telefonlar, fayl_nomi):
    with open(fayl_nomi, "w") as fayl:
        json.dump([phone.to_dict() for phone in telefonlar], fayl)

# Fayldan o'qish
def telefonlarni_faldan_oqish(fayl_nomi):
    telefonlar = []
    try:
        with open(fayl_nomi, 'r') as fayl:
            data = json.load(fayl)
            for item in data:
                if item['brend'] == 'Iphone':
                    telefon = iphone(item['model'], item['tezkor_xotira_hajmi'])
                elif item['brend'] == 'Samsung':
                    telefon = samsung(item['model'], item['tezkor_xotira_hajmi'])
                telefon._TELEFON__id = item['id']
                telefon._narxi = item['narx']
                telefonlar.append(telefon)
    except FileNotFoundError:
        pass
    return telefonlar

# Asosiy menyu funksiyasi
def menyu():
    telefonlar = telefonlarni_faldan_oqish('telefonlar.json')
    while True:
        print("\n1. Telefon qo'shish")
        print("2. Telefonlarni ko'rish")
        print("3. Bir telefon ustida amallar bajarish")
        print("0. Chiqish")
        tanlov = input("Tanlang: ")
        if tanlov == '0':
            telefonlarni_faylga_yozish(telefonlar, 'telefonlar.json')
            print("Dastur tugatildi!")
            break
        elif tanlov == '1':
            brend = input("Brendni tanlang (Iphone/Samsung): ")
            model = input("Modelni kiriting: ")
            tezkor_xotira_hajmi = input("Tezkor xotira hajmini kiriting: ")
            if brend.lower() == 'iphone':
                telefon = iphone(model, tezkor_xotira_hajmi)
            elif brend.lower() == 'samsung':
                telefon = samsung(model, tezkor_xotira_hajmi)
            else:
                print("Noto'g'ri brend")
                continue
            telefonlar.append(telefon)
            print(f"{brend} {model} qo'shildi")
        elif tanlov == '2':
            if not telefonlar:
                print("Telefonlar ro'yxati bo'sh")
            else:
                for telefon in telefonlar:
                    print(f"ID: {telefon.id_sini_korish()}, Brend: {telefon.brendini_olish()}, Model: {telefon.modelini_olish()}")
        elif tanlov == '3':
            telefon_id = int(input("Telefon ID sini kiriting: "))
            telefon = next((tel for tel in telefonlar if tel.id_sini_korish() == telefon_id), 0)
            if telefon == 0:
                print("Bunday ID li telefon topilmadi")
            else:
                print(f"1. ID sini ko'rish: {telefon.id_sini_korish()}")
                narx = input("2. Narxini o'rnating (Enter bosish orqali o'tkazib yuborish): ")
                if narx:
                    telefon.narx_qoyish(int(narx))
                print(f"3. Narxini ko'rish: {telefon.narxini_korish()}")
        else:
            print("Noto'g'ri tanlov. Qayta urinib ko'ring!")

menyu()
