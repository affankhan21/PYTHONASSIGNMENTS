ft=int(input("ENTER DISTANCE IN FEET:"))
inc=int(input("ENTER DISTANCE IN INCHES:"))
print("---------- FEET AND INCHES TO CENTIMETRE AND METRE  CONVERSION--------")
fttotal=ft*30.48
inctotal=inc*2.54
totalcm=fttotal+inctotal
fttotal1=ft*0.3048
inctotal1=inc*0.0254
totalm=fttotal1+inctotal1
print(ft," feet and",inc,"inch  in cetimetre is :",totalcm,"centimetres")
print(ft,"feet and",inc," inch in metre is :",totalm,"metres")
print("----------------------------------------------------------------")

