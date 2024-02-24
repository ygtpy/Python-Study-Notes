

import matematikModule

matematikModule.topla(5,6)
matematikModule.carp(6,5)


#renameing (yeniden adlandirma) yapabliriz
import matematikModule as mm

mm.carp(2,2)
mm.topla(2,2)

# fonksiyon disinda herseyi cekebiliriz
print(mm.customer["lastName"])


# sadece belirli bir class ı cekmek istersek
from matematikModule import topla

topla(6,6)

from matematikModule import customer

print(customer["firstName"])