# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10uQoF5OVjZhuXn3TMG-eXIaoP0F-iW_z
"""

def tashxis(belgi):
  if belgi == "istina":
    return "Parasetamol iching"
  elif belgi == "bosh ogriq":
    return "Trimol iching"
  elif belgi == "Tish ogriq":
    return "Quepen iching"
  elif belgi == "Qol ogriq":
    return "Tramatoligga bor "
  elif belgi == "Ayoq ogriq":
    return "Qoy yogi surt"
  elif belgi == "Koz ogriq":
    return "telizor kamroq kor"
  elif belgi == "Burun ogriq":
    return "pnisol seping"
  elif belgi == "Teri kalalligi":
    return "kasmetoligga boring +998934576584"
  elif belgi == "qoloq ogriq":
    return "lineks iching"
  elif belgi == "qorin ogriq":
    return "sotremon iching"
  else:
    return "SHifokorga murojat qiling"
belgi=input ("Kasallik belgisini kiriting ")
natija=tashxis(belgi)
print(natija)

def Taomlar(Kun):
  if Kun == "Dushanba":
    return "tovuq goshli shorva"
  elif Kun == "Seshanba":
    return "mol goshtidan stek"
  elif Kun == "Chorshanba":
    return "tuxumli amlet"
  elif Kun == "Payshanba":
    return "savzavotlardan salat va bishteks "
  elif Kun == "Juma":
    return "oq guruchdan mastava"
  elif Kun == "Shanba":
    return "Baliq goshtidan sushi"
  else:
    return "men nima istemol qilmoqchiman"
Kun=input ("kun tartibi ")
natija=Taomlar(Kun)
print(natija)