import os
print("\033[94m")
print('''
   _ _ _      _          _               _    
  (_|_) | ___| |_    ___| |__   ___  ___| | __
  | | | |/ _ \ __|  / __| '_ \ / _ \/ __| |/ /
  | | | |  __/ |_  | (__| | | |  __/ (__|   < 
 _/ |_|_|\___|\__|  \___|_| |_|\___|\___|_|\_\
|__/                                          
	        	
     jilet check sülale çıkarma programına hoşgeldiniz sayın(swantex)
     
     
     
	 
''')
asistansecenek = input("TC GİRİN!")

if(asistansecenek=="1"):
	dosya = input("Dosya yolu belirtiniz > ")
	hedef = input("Hedef yolu belirtiniz >")
	os.system("cp "+dosya+" "+hedef)

elif(asistansecenek=="2"):
	dosya = input("Dizin adı girin > ")
	os.system("mkdir "+dosya)
elif(asistansecenek=="3"):
	dosya = input("Dosya yolu belirtiniz > ")
	os.system("rm -rf "+dosya)
elif(asistansecenek=="4"):
	dosya = input("Dosya yolu belirtiniz > ")
	hedef = input("Hedef yolu belirtiniz >")
	os.system("mv "+dosya+" "+hedef)
elif(asistansecenek=="5"):
	dosya = input("Uzantısı ile beraber dosya adı girin > ")
	os.system("touch "+dosya)
elif(asistansecenek=="6"):
	dosya = input("Dosya yolu belirtiniz > ")
	os.system("cat "+dosya)
elif(asistansecenek=="7"):
	os.system("apt install zip unzip")
	print(''' 

1-) Dosya Sıkıştır

2-) Sıkıştırılmış Dosyayı Çıkar

	''')
	zip = input("Seçiminizi Yapınız > ")
	if(zip=="1"):
		dosya = input("Oluşacak zip adı giriniz > ")
		hedef = input("Ziplenecek dosyayı belirtiniz (uzantı ile) >")
		os.system("zip -r "+dosya+".zip "+hedef)

	elif(zip=="2"):
		dosya = input("Çıkartılacak Dosya Yolu > ")
		os.system("unzip "+dosya)		


elif(asistansecenek=="8"):
	print("Hata")
	root = input("Kök kullanıcıya geçiş yapmak ister misiniz? (e/h) ")
	if(root=="e"):
		os.system("sudo su")
	elif(root=="E"):
		os.system("sudo su")

	elif(root=="h"):
		paket = input("Paket adı giriniz > ")
		os.system("apt install "+paket)
		os.system("pip install "+paket)
		os.system("pkg install "+paket)
		os.system("apt-get install "+paket)
	elif(root=="H"):
		paket = input("Paket adı giriniz > ")
		os.system("apt install "+paket)
		os.system("pip install "+paket)
		os.system("pkg install "+paket)
		os.system("apt-get install "+paket)
elif(asistansecenek=="9"):
	print("-----KENDİSİ	11960809824	MURAT	ÖZDEMİR	24.11.2007	HALİME	53197434950	ABDÜLHAMİT	56017340950	MARDİN	DARGEÇİT	TR
KARDEŞİ	13286765716	DİLA	ÖZDEMİR	23.2.2009	HALİME	53197434950	ABDÜLHAMİT	56017340950	MARDİN	DARGEÇİT	TR
KARDEŞİ	40567856146	NUARİN	ÖZDEMİR	18.5.2012	HALİME	53197434950	ABDÜLHAMİT	56017340950	MARDİN	DARGEÇİT	TR
KARDEŞİ	19484558914	HİRANUR	ÖZDEMİR	14.8.2016	HALİME	53197434950	ABDÜLHAMİT	56017340950	MARDİN	DARGEÇİT	TR
BABASI	56017340950	ABDÜLHAMİT	ÖZDEMİR	6.8.1981	HAZNO	56023340722	HÜSEYİN	56026340668	MARDİN	DARGEÇİT	TR
AMCA/HALA	56002341450	RIDVAN	ÖZDEMİR	1.1.1995	HAZNO	56023340722	HÜSEYİN	56026340668	MARDİN	DARGEÇİT	TR
AMCA/HALA	56020340886	SACİDE	DURMAZ	6.8.1979	HAZNO	56023340722	HÜSEYİN	56026340668	MARDİN	DARGEÇİT	TR
AMCASININ/HALASININ ÇOCUĞU	58861246426	KENAN	DURMAZ	23.8.2008	SACİDE	56020340886	ŞERİF	28199268094	MARDİN	DARGEÇİT	TR
AMCASININ/HALASININ ÇOCUĞU	29222234444	BERİTAN	DURMAZ	28.10.2010	SACİDE	56020340886	ŞERİF	28199268094	MARDİN	DARGEÇİT	TR
AMCASININ/HALASININ ÇOCUĞU	11303831796	AYTEN	DURMAZ	21.8.2006	SACİDE	56020340886	ŞERİF	28199268094	MARDİN	DARGEÇİT	TR
AMCASININ/HALASININ ÇOCUĞU	57472292716	MELİSA	DURMAZ	6.8.2014	SACİDE	56020340886	ŞERİF	28199268094	MARDİN	DARGEÇİT	TR
AMCASININ/HALASININ ÇOCUĞU	37123971238	YUSUF	DURMAZ	12.12.2017	SACİDE	56020340886	ŞERİF	28199268094	MARDİN	DARGEÇİT	TR
AMCA/HALA	56008341232	ÇİĞDEM	ÖZDEMİR	6.5.1990	HAZNO	56023340722	HÜSEYİN	56026340668	MARDİN	DARGEÇİT	TR-----")
	os.system("sudo apt install neofetch")
	os.system("neofetch")
