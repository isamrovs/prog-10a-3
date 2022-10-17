from math import*
sk1=int(input("Ievadiet mēneša numuru: "))
if sk1<13:
  if sk1==1:
   print("Tas is janvāris!")
  elif sk1==2:
    print("Tas is februāris!")
  elif sk1==3:
    print("Tas is marts!")
  elif sk1==4:
    print("Tas is aprīlis!")
  elif sk1==5:
    print("Tas is maijs!")
  elif sk1==6:
    print("Tas is jūnijs!")
  elif sk1==7:
    print("Tas is jūlijs!")
  elif sk1==8:
    print("Tas is augusts!")
  elif sk1==9:
    print("Tas is septembris!")
  elif sk1==10:
    print("Tas is oktobris!")
  elif sk1==11:
    print("Tas is novembris!")
  elif sk1==12:
    print("Tas is decembris!")
else:
  print("Šāda mēneša nav!")