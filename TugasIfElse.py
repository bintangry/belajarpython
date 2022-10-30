# jika nilai 90 ~ 100 maka mendapat nilai A 
# jika nilai 80 ~ 89 maka mendapat nilai B
# jika nilai 70 ~ 79 maka mendapat nilai C
# jika nilai 60 ~ 69 maka mendapat nilai D
# jika nilai kurang dari 60 mendapat nilai F



#matematika
#english
#b indo
#pkn
#biologi
#fisika

# 1. buat variable mata pelajaran 
# 2. biar nilai rata rata (math + indo)/5
# 3. nilai rata rata do selection

nilaimtk= int (input('nilaimtk:'))
nilaibhs= int (input('nilaibhs:'))
nilaieng= int (input('nilaieng:'))
nilaipkn= int (input('nilaipkn:'))
nilaibiologi= int (input('nilaibiologi:'))
nilaifisika= int (input('nilaifisika:'))

ratarata= (nilaimtk + nilaibhs + nilaieng + nilaipkn + nilaibiologi + nilaifisika) / 6

print( "ratarata= ", ratarata)

if(ratarata >= 90 and  ratarata <=100 ): #jika nilai 90 ~100 maka mendapatkan A
    print( f'nilai {ratarata} mendapatkan A') 
elif (ratarata >= 80 and ratarata <90): 
        print( f'nilai {ratarata} mendapatkan Bukan A') 
elif (ratarata >= 70 and ratarata < 80 ) :
     print(f'nilai {ratarata}mendapatkan C') 
elif (ratarata >=60 and ratarata <70 ) :
    print(f'nilai {ratarata}  mendapatkan D')
elif (ratarata< 60) :
    print(f'nilai {ratarata}  mendapatkan F')
else :
    print(f'nilai {ratarata} Tidak dalam Rentang')


        