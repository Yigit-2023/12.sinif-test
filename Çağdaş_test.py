import tkinter as tk

pencere = tk.Tk()

#fonksiyonlar
def test1():

	def test1a():
		test1A.config(bg="red")

	def test1b():
		test1B.config(bg="red")

	def test1c():
		test1C.config(bg="green")

	def test1d():
		test1D.config(bg="red")

	def test1e():
		test1E.config(bg="red")

	def reset():
		reng007 = "light blue"
		test1A.config(bg=reng007)
		test1B.config(bg=reng007)
		test1C.config(bg=reng007)
		test1D.config(bg=reng007)
		test1E.config(bg=reng007)

	test1p = tk.Toplevel()

	test1p.title("Test 1")
	test1p.geometry("600x430+300+200")


	test1s = tk.Label(test1p,text="""
I.  Çanakkale

II. Suriye

III.Kafkas

Yukarıda verilen cephelerden hangileri 1.dünya
Savaşı'nda Osmanlı devleti'nin taaruz amaçlı
açtığı cepheler arasında yer alır?

		""",font="italic 12").pack()

	reng0070 = "light blue"


	test1A = tk.Button(test1p,text="A)\tYalnız I\t",bg=reng0070,command = test1a)
	test1A.pack()

	test1B = tk.Button(test1p,text="B)\tYalnız II\t",bg=reng0070,command = test1b)
	test1B.pack()

	test1C = tk.Button(test1p,text="C)\tYalnız III\t",bg=reng0070,command = test1c)
	test1C.pack()

	test1D = tk.Button(test1p,text="D)\tI ve III\t",bg=reng0070,command = test1d)
	test1D.pack()

	test1E = tk.Button(test1p,text="E)\tII ve III\t",bg=reng0070,command = test1e)
	test1E.pack()

	test1sil = tk.Button(test1p,text="\nSİL\t\n",bg=reng0070,command = reset)
	test1sil.pack()





#pencere ayarları
pencere.title("Çağdaş Testleri")
pencere.state("zoomed")
pencere.config(bg="light yellow")

buton_rengi = "grey"
buton_boyut = "35"

test_1_tus = tk.Button(pencere,text="Test 1",font=f"italic {buton_boyut}",bg=buton_rengi,command=test1)
test_1_tus.pack()

test_2_tus = tk.Button(pencere,text="Test 2",font=f"italic {buton_boyut}",bg=buton_rengi)
test_2_tus.pack()

test_3_tus = tk.Button(pencere,text="Test 3",font=f"italic {buton_boyut}",bg=buton_rengi)
test_3_tus.pack()



while True:
	giris = input()
	if giris == "kaynak kod":
		print("https://github.com/Yigit-2023/12.sinif-test\n")
	else:
		print()

pencere.mainloop()



