from tkinter import E


nilai = int (input('Enter any number:'))

# jika nilai 90 ~ 100 maka mendapat nilai A 
# jika nilai 80 ~ 89 maka mendapat nilai B
# jika nilai 70 ~ 79 maka mendapat nilai C
# jika nilai 60 ~ 69 maka mendapat nilai D
# jika nilai kurang dari 60 mendapat nilai F


if(nilai >= 90 and  nilai <=100 ): #jika nilai 90 ~100 maka mendapatkan A
    print( f'nilai {nilai} mendapatkan A') 
elif (nilai >= 80 and nilai <90): 
        print( f'nilai {nilai} mendapatkan Bukan A') 
elif (nilai >= 70 and nilai < 80 ) :
     print(f'nilai {nilai}mendapatkan C') 
elif (nilai >=60 and nilai <70 ) :
    print(f'nilai {nilai}  mendapatkan D')
elif (nilai < 60) :
    print(f'nilai {nilai}  mendapatkan F')
else :
    print(f'nilai {nilai} Tidak dalam Rentang')


   

    