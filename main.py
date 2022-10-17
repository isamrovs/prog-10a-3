from math import*
sk1=int(input("Ievadiet ciparu: "))
if sk1>0:
  if sk1<10:
    print("Tas ir vienciparu skaitlis!")
if sk1<0:
  if sk1>-10:
    print("Tas ir vienciparu skaitlis!")
if sk1==0:
  print("Tas ir vienciparu skaitlis!")
if sk1>0:
  if sk1>9:
    if sk1<100:
      print("Tas ir divciparu skaitlis!")
if sk1<0:
 if sk1<-9:
  if sk1>-100:
   print("Tas ir divciparu skaitlis!")
if sk1>0:
  if sk1>99:
   if sk1<1000:
     print("Tas ir trīsciparu skaitlis!")
if sk1<0:
  if sk1<-99:
   if sk1>-1000:
     print("Tas ir trīsciparu skaitlis!")
if sk1>0:
  if sk1>999:
    print("Tas ir vairāk ciparu skaitlis!")
if sk1<0:
  if sk1<-999:
    print("Tas ir vairāk ciparu skaitlis!")
if sk1>0:
 print("Skaitlis ir pozitīvs!")
if sk1<0:
  print("Skaitlis ir negatīvs!")
if sk1==0:
  print("Tas nav pozitīvs un nav negatīvs skaitlis!")