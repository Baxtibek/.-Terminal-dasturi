# Modul
import math
son = 16
kv_ildizi = math.sqrt(son)
print(f"{son} ning kvadrat ildizi: {kv_ildizi}")

# Exception
try:
    son1 = 10
    son2 = 0
    natija = son1 / son2
except:
    print("Xato: No'lga bo'lib bo'lmaydi!")