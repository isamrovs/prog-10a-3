from math import*
sk1=int(input("Ievadiet trijstūra vislielāko leņķi: "))
sk2=int(input("Ievadiet otro trijstūra leņķi: "))
sk3=int(input("Ievadiet trešo trijstūra leņķi: "))
if sk1+sk2+sk3==180:
 if sk1==90:
   print("Tas ir taisnleņķa trijstūris!")
 elif sk1>90:
   print("Tas ir platleņķa trijstūris!")
 elif sk1<90:
   print("Tas ir šaurleņķu trijstūris!")
else:
  print("Tas nav trijstūris!")