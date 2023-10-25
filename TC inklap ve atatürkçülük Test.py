import tkinter as tk

pencere = tk.Tk()

#fonksiyonlar



def kaybett():

	def geri_getir():
		test_1_tus.place(x=1,y=1)
		test_2_tus.place(x=200,y=1)
		test_3_tus.place(x=399,y=1)
		test_4_tus.place(x=599,y=1)
		test_5_tus.place(x=799,y=1)
		test_6_tus.place(x=999,y=1)
		test_7_tus.place(x=1,y=150)
		test_8_tus.place(x=200,y=150)
		test_9_tus.place(x=399,y=150)
		test_10_tus.place(x=599,y=150)
		test_11_tus.place(x=799,y=150)
		test_12_tus.place(x=999,y=150)
		test_13_tus.place(x=1,y=300)
		test_14_tus.place(x=200,y=300)
		test_15_tus.place(x=399,y=300)
		test_16_tus.place(x=599,y=300)
		test_17_tus.place(x=799,y=300)
		test_18_tus.place(x=999,y=300)
		test_19_tus.place(x=1,y=450)
		test_20_tus.place(x=200,y=450)
		test_21_tus.place(x=399,y=450)
		test_22_tus.place(x=599,y=450)
		test_23_tus.place(x=799,y=450)
		test_24_tus.place(x=999,y=450)

		cizgi.place(x=1,y=519)

		info_tus.place(x=550,y=590)

		geri_don_tus.place(x=-550,y=-590)
		bilgi_notu.place(x=-550,y=-590)


	test_1_tus.place(x=-550,y=-590)
	test_2_tus.place(x=-550,y=-590)
	test_3_tus.place(x=-550,y=-590)
	test_4_tus.place(x=-550,y=-590)
	test_5_tus.place(x=-550,y=-590)
	test_6_tus.place(x=-550,y=-590)
	test_7_tus.place(x=-550,y=-590)
	test_8_tus.place(x=-550,y=-590)
	test_9_tus.place(x=-550,y=-590)
	test_10_tus.place(x=-550,y=-590)
	test_11_tus.place(x=-550,y=-590)
	test_12_tus.place(x=-550,y=-590)
	test_13_tus.place(x=-550,y=-590)
	test_14_tus.place(x=-550,y=-590)
	test_15_tus.place(x=-550,y=-590)
	test_16_tus.place(x=-550,y=-590)
	test_17_tus.place(x=-550,y=-590)
	test_18_tus.place(x=-550,y=-590)
	test_19_tus.place(x=-550,y=-590)
	test_20_tus.place(x=-550,y=-590)
	test_21_tus.place(x=-550,y=-590)
	test_22_tus.place(x=-550,y=-590)
	test_23_tus.place(x=-550,y=-590)
	test_24_tus.place(x=-550,y=-590)
	test_1_tus.place(x=-550,y=-590)

	info_tus.place(x=-550,y=-590)

	cizgi.place(x=-1000,y=-10000)



	bilgi_notu = tk.Label(text="""1.Ünite\nTC inklap ve atatürkçülük sorularu içerir\n\nHazırlayan : Yiğit çıtak\n\nSürüm : 1.0beta\n\n\n\n""",font="italic 30",bg="light yellow")
	bilgi_notu.pack()

	geri_don_tus = tk.Button(text="Geri",font="italic 25",command=geri_getir,bg="light yellow")
	geri_don_tus.pack()















#------------------------------------------------------------------------------------------------------




#Soru fonksiyonları (Çok uzun!)

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

	test1sil = tk.Button(test1p,text="\nTemizle\t\n",bg=reng0070,command = reset)
	test1sil.pack()

def test2():

	def test2a():
		test2A.config(bg="red")

	def test2b():
		test2B.config(bg="red")

	def test2c():
		test2C.config(bg="red")

	def test2d():
		test2D.config(bg="red")

	def test2e():
		test2E.config(bg="red")

	def reset():
		reng007 = "light blue"
		test2A.config(bg=reng007)
		test2B.config(bg=reng007)
		test2C.config(bg=reng007)
		test2D.config(bg=reng007)
		test2E.config(bg=reng007)

	test2p = tk.Toplevel()

	test2p.title("Test 2")
	test2p.geometry("600x430+300+200")


	test2s = tk.Label(test2p,text="""

soru gelecek
 
		""",font="italic 12").pack()

	reng0070 = "light blue"


	test2A = tk.Button(test2p,text="A)\t \t",bg=reng0070,command = test2a)
	test2A.pack()

	test2B = tk.Button(test2p,text="B)\t \t",bg=reng0070,command = test2b)
	test2B.pack()

	test2C = tk.Button(test2p,text="C)\t \t",bg=reng0070,command = test2c)
	test2C.pack()

	test2D = tk.Button(test2p,text="D)\t \t",bg=reng0070,command = test2d)
	test2D.pack()

	test2E = tk.Button(test2p,text="E)\t \t",bg=reng0070,command = test2e)
	test2E.pack()

	test2sil = tk.Button(test2p,text="\nTemizle\t\n",bg=reng0070,command = reset)
	test2sil.pack()

def test3():

	def test0a():
		test0A.config(bg="red")

	def test0b():
		test0B.config(bg="red")

	def test0c():
		test0C.config(bg="red")

	def test0d():
		test0D.config(bg="red")

	def test0e():
		test0E.config(bg="red")

	def reset():
		reng007 = "light blue"
		test0A.config(bg=reng007)
		test0B.config(bg=reng007)
		test0C.config(bg=reng007)
		test0D.config(bg=reng007)
		test0E.config(bg=reng007)

	test0p = tk.Toplevel()

	test0p.title("Test 3")
	test0p.geometry("600x430+300+200")


	test0s = tk.Label(test0p,text="""

soru gelecek

		""",font="italic 12").pack()

	reng0070 = "light blue"


	test0A = tk.Button(test0p,text="A)\t \t",bg=reng0070,command = test0a)
	test0A.pack()

	test0B = tk.Button(test0p,text="B)\t \t",bg=reng0070,command = test0b)
	test0B.pack()

	test0C = tk.Button(test0p,text="C)\t \t",bg=reng0070,command = test0c)
	test0C.pack()

	test0D = tk.Button(test0p,text="D)\t \t",bg=reng0070,command = test0d)
	test0D.pack()

	test0E = tk.Button(test0p,text="E)\t \t",bg=reng0070,command = test0e)
	test0E.pack()

	test0sil = tk.Button(test0p,text="\nTemizle\t\n",bg=reng0070,command = reset)
	test0sil.pack()

def test4():

	def test0a():
		test0A.config(bg="red")

	def test0b():
		test0B.config(bg="red")

	def test0c():
		test0C.config(bg="red")

	def test0d():
		test0D.config(bg="red")

	def test0e():
		test0E.config(bg="red")

	def reset():
		reng007 = "light blue"
		test0A.config(bg=reng007)
		test0B.config(bg=reng007)
		test0C.config(bg=reng007)
		test0D.config(bg=reng007)
		test0E.config(bg=reng007)

	test0p = tk.Toplevel()

	test0p.title("Test 4")
	test0p.geometry("600x430+300+200")


	test0s = tk.Label(test0p,text="""

soru gelecek

		""",font="italic 12").pack()

	reng0070 = "light blue"


	test0A = tk.Button(test0p,text="A)\t \t",bg=reng0070,command = test0a)
	test0A.pack()

	test0B = tk.Button(test0p,text="B)\t \t",bg=reng0070,command = test0b)
	test0B.pack()

	test0C = tk.Button(test0p,text="C)\t \t",bg=reng0070,command = test0c)
	test0C.pack()

	test0D = tk.Button(test0p,text="D)\t \t",bg=reng0070,command = test0d)
	test0D.pack()

	test0E = tk.Button(test0p,text="E)\t \t",bg=reng0070,command = test0e)
	test0E.pack()

	test0sil = tk.Button(test0p,text="\nTemizle\t\n",bg=reng0070,command = reset)
	test0sil.pack()

def test5():

	def test0a():
		test0A.config(bg="red")

	def test0b():
		test0B.config(bg="red")

	def test0c():
		test0C.config(bg="red")

	def test0d():
		test0D.config(bg="red")

	def test0e():
		test0E.config(bg="red")

	def reset():
		reng007 = "light blue"
		test0A.config(bg=reng007)
		test0B.config(bg=reng007)
		test0C.config(bg=reng007)
		test0D.config(bg=reng007)
		test0E.config(bg=reng007)

	test0p = tk.Toplevel()

	test0p.title("Test 5")
	test0p.geometry("600x430+300+200")


	test0s = tk.Label(test0p,text="""

soru gelecek

		""",font="italic 12").pack()

	reng0070 = "light blue"


	test0A = tk.Button(test0p,text="A)\t \t",bg=reng0070,command = test0a)
	test0A.pack()

	test0B = tk.Button(test0p,text="B)\t \t",bg=reng0070,command = test0b)
	test0B.pack()

	test0C = tk.Button(test0p,text="C)\t \t",bg=reng0070,command = test0c)
	test0C.pack()

	test0D = tk.Button(test0p,text="D)\t \t",bg=reng0070,command = test0d)
	test0D.pack()

	test0E = tk.Button(test0p,text="E)\t \t",bg=reng0070,command = test0e)
	test0E.pack()

	test0sil = tk.Button(test0p,text="\nTemizle\t\n",bg=reng0070,command = reset)
	test0sil.pack()


def test6():

	def test0a():
		test0A.config(bg="red")

	def test0b():
		test0B.config(bg="red")

	def test0c():
		test0C.config(bg="red")

	def test0d():
		test0D.config(bg="red")

	def test0e():
		test0E.config(bg="red")

	def reset():
		reng007 = "light blue"
		test0A.config(bg=reng007)
		test0B.config(bg=reng007)
		test0C.config(bg=reng007)
		test0D.config(bg=reng007)
		test0E.config(bg=reng007)

	test0p = tk.Toplevel()

	test0p.title("Test 6")
	test0p.geometry("600x430+300+200")


	test0s = tk.Label(test0p,text="""

soru gelecek

		""",font="italic 12").pack()

	reng0070 = "light blue"


	test0A = tk.Button(test0p,text="A)\t \t",bg=reng0070,command = test0a)
	test0A.pack()

	test0B = tk.Button(test0p,text="B)\t \t",bg=reng0070,command = test0b)
	test0B.pack()

	test0C = tk.Button(test0p,text="C)\t \t",bg=reng0070,command = test0c)
	test0C.pack()

	test0D = tk.Button(test0p,text="D)\t \t",bg=reng0070,command = test0d)
	test0D.pack()

	test0E = tk.Button(test0p,text="E)\t \t",bg=reng0070,command = test0e)
	test0E.pack()

	test0sil = tk.Button(test0p,text="\nTemizle\t\n",bg=reng0070,command = reset)
	test0sil.pack()

def test7():

	def test0a():
		test0A.config(bg="red")

	def test0b():
		test0B.config(bg="red")

	def test0c():
		test0C.config(bg="red")

	def test0d():
		test0D.config(bg="red")

	def test0e():
		test0E.config(bg="red")

	def reset():
		reng007 = "light blue"
		test0A.config(bg=reng007)
		test0B.config(bg=reng007)
		test0C.config(bg=reng007)
		test0D.config(bg=reng007)
		test0E.config(bg=reng007)

	test0p = tk.Toplevel()

	test0p.title("Test 7")
	test0p.geometry("600x430+300+200")


	test0s = tk.Label(test0p,text="""

soru gelecek

		""",font="italic 12").pack()

	reng0070 = "light blue"


	test0A = tk.Button(test0p,text="A)\t \t",bg=reng0070,command = test0a)
	test0A.pack()

	test0B = tk.Button(test0p,text="B)\t \t",bg=reng0070,command = test0b)
	test0B.pack()

	test0C = tk.Button(test0p,text="C)\t \t",bg=reng0070,command = test0c)
	test0C.pack()

	test0D = tk.Button(test0p,text="D)\t \t",bg=reng0070,command = test0d)
	test0D.pack()

	test0E = tk.Button(test0p,text="E)\t \t",bg=reng0070,command = test0e)
	test0E.pack()

	test0sil = tk.Button(test0p,text="\nTemizle\t\n",bg=reng0070,command = reset)
	test0sil.pack()

def test8():

	def test0a():
		test0A.config(bg="red")

	def test0b():
		test0B.config(bg="red")

	def test0c():
		test0C.config(bg="red")

	def test0d():
		test0D.config(bg="red")

	def test0e():
		test0E.config(bg="red")

	def reset():
		reng007 = "light blue"
		test0A.config(bg=reng007)
		test0B.config(bg=reng007)
		test0C.config(bg=reng007)
		test0D.config(bg=reng007)
		test0E.config(bg=reng007)

	test0p = tk.Toplevel()

	test0p.title("Test 8")
	test0p.geometry("600x430+300+200")


	test0s = tk.Label(test0p,text="""

soru gelecek

		""",font="italic 12").pack()

	reng0070 = "light blue"


	test0A = tk.Button(test0p,text="A)\t \t",bg=reng0070,command = test0a)
	test0A.pack()

	test0B = tk.Button(test0p,text="B)\t \t",bg=reng0070,command = test0b)
	test0B.pack()

	test0C = tk.Button(test0p,text="C)\t \t",bg=reng0070,command = test0c)
	test0C.pack()

	test0D = tk.Button(test0p,text="D)\t \t",bg=reng0070,command = test0d)
	test0D.pack()

	test0E = tk.Button(test0p,text="E)\t \t",bg=reng0070,command = test0e)
	test0E.pack()

	test0sil = tk.Button(test0p,text="\nTemizle\t\n",bg=reng0070,command = reset)
	test0sil.pack()

def test9():

	def test0a():
		test0A.config(bg="red")

	def test0b():
		test0B.config(bg="red")

	def test0c():
		test0C.config(bg="red")

	def test0d():
		test0D.config(bg="red")

	def test0e():
		test0E.config(bg="red")

	def reset():
		reng007 = "light blue"
		test0A.config(bg=reng007)
		test0B.config(bg=reng007)
		test0C.config(bg=reng007)
		test0D.config(bg=reng007)
		test0E.config(bg=reng007)

	test0p = tk.Toplevel()

	test0p.title("Test 9")
	test0p.geometry("600x430+300+200")


	test0s = tk.Label(test0p,text="""

soru gelecek

		""",font="italic 12").pack()

	reng0070 = "light blue"


	test0A = tk.Button(test0p,text="A)\t \t",bg=reng0070,command = test0a)
	test0A.pack()

	test0B = tk.Button(test0p,text="B)\t \t",bg=reng0070,command = test0b)
	test0B.pack()

	test0C = tk.Button(test0p,text="C)\t \t",bg=reng0070,command = test0c)
	test0C.pack()

	test0D = tk.Button(test0p,text="D)\t \t",bg=reng0070,command = test0d)
	test0D.pack()

	test0E = tk.Button(test0p,text="E)\t \t",bg=reng0070,command = test0e)
	test0E.pack()

	test0sil = tk.Button(test0p,text="\nTemizle\t\n",bg=reng0070,command = reset)
	test0sil.pack()

def test10():

	def test0a():
		test0A.config(bg="red")

	def test0b():
		test0B.config(bg="red")

	def test0c():
		test0C.config(bg="red")

	def test0d():
		test0D.config(bg="red")

	def test0e():
		test0E.config(bg="red")

	def reset():
		reng007 = "light blue"
		test0A.config(bg=reng007)
		test0B.config(bg=reng007)
		test0C.config(bg=reng007)
		test0D.config(bg=reng007)
		test0E.config(bg=reng007)

	test0p = tk.Toplevel()

	test0p.title("Test 10")
	test0p.geometry("600x430+300+200")


	test0s = tk.Label(test0p,text="""

soru gelecek

		""",font="italic 12").pack()

	reng0070 = "light blue"


	test0A = tk.Button(test0p,text="A)\t \t",bg=reng0070,command = test0a)
	test0A.pack()

	test0B = tk.Button(test0p,text="B)\t \t",bg=reng0070,command = test0b)
	test0B.pack()

	test0C = tk.Button(test0p,text="C)\t \t",bg=reng0070,command = test0c)
	test0C.pack()

	test0D = tk.Button(test0p,text="D)\t \t",bg=reng0070,command = test0d)
	test0D.pack()

	test0E = tk.Button(test0p,text="E)\t \t",bg=reng0070,command = test0e)
	test0E.pack()

	test0sil = tk.Button(test0p,text="\nTemizle\t\n",bg=reng0070,command = reset)
	test0sil.pack()

def test11():

	def test0a():
		test0A.config(bg="red")

	def test0b():
		test0B.config(bg="red")

	def test0c():
		test0C.config(bg="red")

	def test0d():
		test0D.config(bg="red")

	def test0e():
		test0E.config(bg="red")

	def reset():
		reng007 = "light blue"
		test0A.config(bg=reng007)
		test0B.config(bg=reng007)
		test0C.config(bg=reng007)
		test0D.config(bg=reng007)
		test0E.config(bg=reng007)

	test0p = tk.Toplevel()

	test0p.title("Test 11")
	test0p.geometry("600x430+300+200")


	test0s = tk.Label(test0p,text="""

soru gelecek

		""",font="italic 12").pack()

	reng0070 = "light blue"


	test0A = tk.Button(test0p,text="A)\t \t",bg=reng0070,command = test0a)
	test0A.pack()

	test0B = tk.Button(test0p,text="B)\t \t",bg=reng0070,command = test0b)
	test0B.pack()

	test0C = tk.Button(test0p,text="C)\t \t",bg=reng0070,command = test0c)
	test0C.pack()

	test0D = tk.Button(test0p,text="D)\t \t",bg=reng0070,command = test0d)
	test0D.pack()

	test0E = tk.Button(test0p,text="E)\t \t",bg=reng0070,command = test0e)
	test0E.pack()

	test0sil = tk.Button(test0p,text="\nTemizle\t\n",bg=reng0070,command = reset)
	test0sil.pack()

def test12():

	def test0a():
		test0A.config(bg="red")

	def test0b():
		test0B.config(bg="red")

	def test0c():
		test0C.config(bg="red")

	def test0d():
		test0D.config(bg="red")

	def test0e():
		test0E.config(bg="red")

	def reset():
		reng007 = "light blue"
		test0A.config(bg=reng007)
		test0B.config(bg=reng007)
		test0C.config(bg=reng007)
		test0D.config(bg=reng007)
		test0E.config(bg=reng007)

	test0p = tk.Toplevel()

	test0p.title("Test 12")
	test0p.geometry("600x430+300+200")


	test0s = tk.Label(test0p,text="""

soru gelecek

		""",font="italic 12").pack()

	reng0070 = "light blue"


	test0A = tk.Button(test0p,text="A)\t \t",bg=reng0070,command = test0a)
	test0A.pack()

	test0B = tk.Button(test0p,text="B)\t \t",bg=reng0070,command = test0b)
	test0B.pack()

	test0C = tk.Button(test0p,text="C)\t \t",bg=reng0070,command = test0c)
	test0C.pack()

	test0D = tk.Button(test0p,text="D)\t \t",bg=reng0070,command = test0d)
	test0D.pack()

	test0E = tk.Button(test0p,text="E)\t \t",bg=reng0070,command = test0e)
	test0E.pack()

	test0sil = tk.Button(test0p,text="\nTemizle\t\n",bg=reng0070,command = reset)
	test0sil.pack()

def test13():

	def test0a():
		test0A.config(bg="red")

	def test0b():
		test0B.config(bg="red")

	def test0c():
		test0C.config(bg="red")

	def test0d():
		test0D.config(bg="red")

	def test0e():
		test0E.config(bg="red")

	def reset():
		reng007 = "light blue"
		test0A.config(bg=reng007)
		test0B.config(bg=reng007)
		test0C.config(bg=reng007)
		test0D.config(bg=reng007)
		test0E.config(bg=reng007)

	test0p = tk.Toplevel()

	test0p.title("Test 13")
	test0p.geometry("600x430+300+200")


	test0s = tk.Label(test0p,text="""

soru gelecek

		""",font="italic 12").pack()

	reng0070 = "light blue"


	test0A = tk.Button(test0p,text="A)\t \t",bg=reng0070,command = test0a)
	test0A.pack()

	test0B = tk.Button(test0p,text="B)\t \t",bg=reng0070,command = test0b)
	test0B.pack()

	test0C = tk.Button(test0p,text="C)\t \t",bg=reng0070,command = test0c)
	test0C.pack()

	test0D = tk.Button(test0p,text="D)\t \t",bg=reng0070,command = test0d)
	test0D.pack()

	test0E = tk.Button(test0p,text="E)\t \t",bg=reng0070,command = test0e)
	test0E.pack()

	test0sil = tk.Button(test0p,text="\nTemizle\t\n",bg=reng0070,command = reset)
	test0sil.pack()

def test14():

	def test0a():
		test0A.config(bg="red")

	def test0b():
		test0B.config(bg="red")

	def test0c():
		test0C.config(bg="red")

	def test0d():
		test0D.config(bg="red")

	def test0e():
		test0E.config(bg="red")

	def reset():
		reng007 = "light blue"
		test0A.config(bg=reng007)
		test0B.config(bg=reng007)
		test0C.config(bg=reng007)
		test0D.config(bg=reng007)
		test0E.config(bg=reng007)

	test0p = tk.Toplevel()

	test0p.title("Test 14")
	test0p.geometry("600x430+300+200")


	test0s = tk.Label(test0p,text="""

soru gelecek

		""",font="italic 12").pack()

	reng0070 = "light blue"


	test0A = tk.Button(test0p,text="A)\t \t",bg=reng0070,command = test0a)
	test0A.pack()

	test0B = tk.Button(test0p,text="B)\t \t",bg=reng0070,command = test0b)
	test0B.pack()

	test0C = tk.Button(test0p,text="C)\t \t",bg=reng0070,command = test0c)
	test0C.pack()

	test0D = tk.Button(test0p,text="D)\t \t",bg=reng0070,command = test0d)
	test0D.pack()

	test0E = tk.Button(test0p,text="E)\t \t",bg=reng0070,command = test0e)
	test0E.pack()

	test0sil = tk.Button(test0p,text="\nTemizle\t\n",bg=reng0070,command = reset)
	test0sil.pack()

def test15():

	def test0a():
		test0A.config(bg="red")

	def test0b():
		test0B.config(bg="red")

	def test0c():
		test0C.config(bg="red")

	def test0d():
		test0D.config(bg="red")

	def test0e():
		test0E.config(bg="red")

	def reset():
		reng007 = "light blue"
		test0A.config(bg=reng007)
		test0B.config(bg=reng007)
		test0C.config(bg=reng007)
		test0D.config(bg=reng007)
		test0E.config(bg=reng007)

	test0p = tk.Toplevel()

	test0p.title("Test 15")
	test0p.geometry("600x430+300+200")


	test0s = tk.Label(test0p,text="""

soru gelecek

		""",font="italic 12").pack()

	reng0070 = "light blue"


	test0A = tk.Button(test0p,text="A)\t \t",bg=reng0070,command = test0a)
	test0A.pack()

	test0B = tk.Button(test0p,text="B)\t \t",bg=reng0070,command = test0b)
	test0B.pack()

	test0C = tk.Button(test0p,text="C)\t \t",bg=reng0070,command = test0c)
	test0C.pack()

	test0D = tk.Button(test0p,text="D)\t \t",bg=reng0070,command = test0d)
	test0D.pack()

	test0E = tk.Button(test0p,text="E)\t \t",bg=reng0070,command = test0e)
	test0E.pack()

	test0sil = tk.Button(test0p,text="\nTemizle\t\n",bg=reng0070,command = reset)
	test0sil.pack()

def test16():

	def test0a():
		test0A.config(bg="red")

	def test0b():
		test0B.config(bg="red")

	def test0c():
		test0C.config(bg="red")

	def test0d():
		test0D.config(bg="red")

	def test0e():
		test0E.config(bg="red")

	def reset():
		reng007 = "light blue"
		test0A.config(bg=reng007)
		test0B.config(bg=reng007)
		test0C.config(bg=reng007)
		test0D.config(bg=reng007)
		test0E.config(bg=reng007)

	test0p = tk.Toplevel()

	test0p.title("Test 16")
	test0p.geometry("600x430+300+200")


	test0s = tk.Label(test0p,text="""

soru gelecek

		""",font="italic 12").pack()

	reng0070 = "light blue"


	test0A = tk.Button(test0p,text="A)\t \t",bg=reng0070,command = test0a)
	test0A.pack()

	test0B = tk.Button(test0p,text="B)\t \t",bg=reng0070,command = test0b)
	test0B.pack()

	test0C = tk.Button(test0p,text="C)\t \t",bg=reng0070,command = test0c)
	test0C.pack()

	test0D = tk.Button(test0p,text="D)\t \t",bg=reng0070,command = test0d)
	test0D.pack()

	test0E = tk.Button(test0p,text="E)\t \t",bg=reng0070,command = test0e)
	test0E.pack()

	test0sil = tk.Button(test0p,text="\nTemizle\t\n",bg=reng0070,command = reset)
	test0sil.pack()

def test17():

	def test0a():
		test0A.config(bg="red")

	def test0b():
		test0B.config(bg="red")

	def test0c():
		test0C.config(bg="red")

	def test0d():
		test0D.config(bg="red")

	def test0e():
		test0E.config(bg="red")

	def reset():
		reng007 = "light blue"
		test0A.config(bg=reng007)
		test0B.config(bg=reng007)
		test0C.config(bg=reng007)
		test0D.config(bg=reng007)
		test0E.config(bg=reng007)

	test0p = tk.Toplevel()

	test0p.title("Test 17")
	test0p.geometry("600x430+300+200")


	test0s = tk.Label(test0p,text="""

soru gelecek

		""",font="italic 12").pack()

	reng0070 = "light blue"


	test0A = tk.Button(test0p,text="A)\t \t",bg=reng0070,command = test0a)
	test0A.pack()

	test0B = tk.Button(test0p,text="B)\t \t",bg=reng0070,command = test0b)
	test0B.pack()

	test0C = tk.Button(test0p,text="C)\t \t",bg=reng0070,command = test0c)
	test0C.pack()

	test0D = tk.Button(test0p,text="D)\t \t",bg=reng0070,command = test0d)
	test0D.pack()

	test0E = tk.Button(test0p,text="E)\t \t",bg=reng0070,command = test0e)
	test0E.pack()

	test0sil = tk.Button(test0p,text="\nTemizle\t\n",bg=reng0070,command = reset)
	test0sil.pack()

def test18():

	def test0a():
		test0A.config(bg="red")

	def test0b():
		test0B.config(bg="red")

	def test0c():
		test0C.config(bg="red")

	def test0d():
		test0D.config(bg="red")

	def test0e():
		test0E.config(bg="red")

	def reset():
		reng007 = "light blue"
		test0A.config(bg=reng007)
		test0B.config(bg=reng007)
		test0C.config(bg=reng007)
		test0D.config(bg=reng007)
		test0E.config(bg=reng007)

	test0p = tk.Toplevel()

	test0p.title("Test 18")
	test0p.geometry("600x430+300+200")


	test0s = tk.Label(test0p,text="""

soru gelecek

		""",font="italic 12").pack()

	reng0070 = "light blue"


	test0A = tk.Button(test0p,text="A)\t \t",bg=reng0070,command = test0a)
	test0A.pack()

	test0B = tk.Button(test0p,text="B)\t \t",bg=reng0070,command = test0b)
	test0B.pack()

	test0C = tk.Button(test0p,text="C)\t \t",bg=reng0070,command = test0c)
	test0C.pack()

	test0D = tk.Button(test0p,text="D)\t \t",bg=reng0070,command = test0d)
	test0D.pack()

	test0E = tk.Button(test0p,text="E)\t \t",bg=reng0070,command = test0e)
	test0E.pack()

	test0sil = tk.Button(test0p,text="\nTemizle\t\n",bg=reng0070,command = reset)
	test0sil.pack()

def test19():

	def test0a():
		test0A.config(bg="red")

	def test0b():
		test0B.config(bg="red")

	def test0c():
		test0C.config(bg="red")

	def test0d():
		test0D.config(bg="red")

	def test0e():
		test0E.config(bg="red")

	def reset():
		reng007 = "light blue"
		test0A.config(bg=reng007)
		test0B.config(bg=reng007)
		test0C.config(bg=reng007)
		test0D.config(bg=reng007)
		test0E.config(bg=reng007)

	test0p = tk.Toplevel()

	test0p.title("Test 19")
	test0p.geometry("600x430+300+200")


	test0s = tk.Label(test0p,text="""

soru gelecek

		""",font="italic 12").pack()

	reng0070 = "light blue"


	test0A = tk.Button(test0p,text="A)\t \t",bg=reng0070,command = test0a)
	test0A.pack()

	test0B = tk.Button(test0p,text="B)\t \t",bg=reng0070,command = test0b)
	test0B.pack()

	test0C = tk.Button(test0p,text="C)\t \t",bg=reng0070,command = test0c)
	test0C.pack()

	test0D = tk.Button(test0p,text="D)\t \t",bg=reng0070,command = test0d)
	test0D.pack()

	test0E = tk.Button(test0p,text="E)\t \t",bg=reng0070,command = test0e)
	test0E.pack()

	test0sil = tk.Button(test0p,text="\nTemizle\t\n",bg=reng0070,command = reset)
	test0sil.pack()

def test20():

	def test0a():
		test0A.config(bg="red")

	def test0b():
		test0B.config(bg="red")

	def test0c():
		test0C.config(bg="red")

	def test0d():
		test0D.config(bg="red")

	def test0e():
		test0E.config(bg="red")

	def reset():
		reng007 = "light blue"
		test0A.config(bg=reng007)
		test0B.config(bg=reng007)
		test0C.config(bg=reng007)
		test0D.config(bg=reng007)
		test0E.config(bg=reng007)

	test0p = tk.Toplevel()

	test0p.title("Test 20")
	test0p.geometry("600x430+300+200")


	test0s = tk.Label(test0p,text="""

soru gelecek

		""",font="italic 12").pack()

	reng0070 = "light blue"


	test0A = tk.Button(test0p,text="A)\t \t",bg=reng0070,command = test0a)
	test0A.pack()

	test0B = tk.Button(test0p,text="B)\t \t",bg=reng0070,command = test0b)
	test0B.pack()

	test0C = tk.Button(test0p,text="C)\t \t",bg=reng0070,command = test0c)
	test0C.pack()

	test0D = tk.Button(test0p,text="D)\t \t",bg=reng0070,command = test0d)
	test0D.pack()

	test0E = tk.Button(test0p,text="E)\t \t",bg=reng0070,command = test0e)
	test0E.pack()

	test0sil = tk.Button(test0p,text="\nTemizle\t\n",bg=reng0070,command = reset)
	test0sil.pack()

def test21():

	def test0a():
		test0A.config(bg="red")

	def test0b():
		test0B.config(bg="red")

	def test0c():
		test0C.config(bg="red")

	def test0d():
		test0D.config(bg="red")

	def test0e():
		test0E.config(bg="red")

	def reset():
		reng007 = "light blue"
		test0A.config(bg=reng007)
		test0B.config(bg=reng007)
		test0C.config(bg=reng007)
		test0D.config(bg=reng007)
		test0E.config(bg=reng007)

	test0p = tk.Toplevel()

	test0p.title("Test 21")
	test0p.geometry("600x430+300+200")


	test0s = tk.Label(test0p,text="""

soru gelecek

		""",font="italic 12").pack()

	reng0070 = "light blue"


	test0A = tk.Button(test0p,text="A)\t \t",bg=reng0070,command = test0a)
	test0A.pack()

	test0B = tk.Button(test0p,text="B)\t \t",bg=reng0070,command = test0b)
	test0B.pack()

	test0C = tk.Button(test0p,text="C)\t \t",bg=reng0070,command = test0c)
	test0C.pack()

	test0D = tk.Button(test0p,text="D)\t \t",bg=reng0070,command = test0d)
	test0D.pack()

	test0E = tk.Button(test0p,text="E)\t \t",bg=reng0070,command = test0e)
	test0E.pack()

	test0sil = tk.Button(test0p,text="\nTemizle\t\n",bg=reng0070,command = reset)
	test0sil.pack()

def test22():

	def test0a():
		test0A.config(bg="red")

	def test0b():
		test0B.config(bg="red")

	def test0c():
		test0C.config(bg="red")

	def test0d():
		test0D.config(bg="red")

	def test0e():
		test0E.config(bg="red")

	def reset():
		reng007 = "light blue"
		test0A.config(bg=reng007)
		test0B.config(bg=reng007)
		test0C.config(bg=reng007)
		test0D.config(bg=reng007)
		test0E.config(bg=reng007)

	test0p = tk.Toplevel()

	test0p.title("Test 22")
	test0p.geometry("600x430+300+200")


	test0s = tk.Label(test0p,text="""

soru gelecek

		""",font="italic 12").pack()

	reng0070 = "light blue"


	test0A = tk.Button(test0p,text="A)\t \t",bg=reng0070,command = test0a)
	test0A.pack()

	test0B = tk.Button(test0p,text="B)\t \t",bg=reng0070,command = test0b)
	test0B.pack()

	test0C = tk.Button(test0p,text="C)\t \t",bg=reng0070,command = test0c)
	test0C.pack()

	test0D = tk.Button(test0p,text="D)\t \t",bg=reng0070,command = test0d)
	test0D.pack()

	test0E = tk.Button(test0p,text="E)\t \t",bg=reng0070,command = test0e)
	test0E.pack()

	test0sil = tk.Button(test0p,text="\nTemizle\t\n",bg=reng0070,command = reset)
	test0sil.pack()

def test23():

	def test0a():
		test0A.config(bg="red")

	def test0b():
		test0B.config(bg="red")

	def test0c():
		test0C.config(bg="red")

	def test0d():
		test0D.config(bg="red")

	def test0e():
		test0E.config(bg="red")

	def reset():
		reng007 = "light blue"
		test0A.config(bg=reng007)
		test0B.config(bg=reng007)
		test0C.config(bg=reng007)
		test0D.config(bg=reng007)
		test0E.config(bg=reng007)

	test0p = tk.Toplevel()

	test0p.title("Test 23")
	test0p.geometry("600x430+300+200")


	test0s = tk.Label(test0p,text="""

soru gelecek

		""",font="italic 12").pack()

	reng0070 = "light blue"


	test0A = tk.Button(test0p,text="A)\t \t",bg=reng0070,command = test0a)
	test0A.pack()

	test0B = tk.Button(test0p,text="B)\t \t",bg=reng0070,command = test0b)
	test0B.pack()

	test0C = tk.Button(test0p,text="C)\t \t",bg=reng0070,command = test0c)
	test0C.pack()

	test0D = tk.Button(test0p,text="D)\t \t",bg=reng0070,command = test0d)
	test0D.pack()

	test0E = tk.Button(test0p,text="E)\t \t",bg=reng0070,command = test0e)
	test0E.pack()

	test0sil = tk.Button(test0p,text="\nTemizle\t\n",bg=reng0070,command = reset)
	test0sil.pack()

def test24():

	def test0a():
		test0A.config(bg="red")

	def test0b():
		test0B.config(bg="red")

	def test0c():
		test0C.config(bg="red")

	def test0d():
		test0D.config(bg="red")

	def test0e():
		test0E.config(bg="red")

	def reset():
		reng007 = "light blue"
		test0A.config(bg=reng007)
		test0B.config(bg=reng007)
		test0C.config(bg=reng007)
		test0D.config(bg=reng007)
		test0E.config(bg=reng007)

	test0p = tk.Toplevel()

	test0p.title("Test 24")
	test0p.geometry("600x430+300+200")


	test0s = tk.Label(test0p,text="""

soru gelecek

		""",font="italic 12").pack()

	reng0070 = "light blue"


	test0A = tk.Button(test0p,text="A)\t \t",bg=reng0070,command = test0a)
	test0A.pack()

	test0B = tk.Button(test0p,text="B)\t \t",bg=reng0070,command = test0b)
	test0B.pack()

	test0C = tk.Button(test0p,text="C)\t \t",bg=reng0070,command = test0c)
	test0C.pack()

	test0D = tk.Button(test0p,text="D)\t \t",bg=reng0070,command = test0d)
	test0D.pack()

	test0E = tk.Button(test0p,text="E)\t \t",bg=reng0070,command = test0e)
	test0E.pack()

	test0sil = tk.Button(test0p,text="\nTemizle\t\n",bg=reng0070,command = reset)
	test0sil.pack()





#-----------------------------------------------------------------------------------------------------------------

















#pencere ayarları
pencere.title("İnklap Testleri")
pencere.state("zoomed")
pencere.config(bg="light yellow")
pencere.minsize(1200,500)

buton_rengi = "grey"
buton_boyut = "25"

test_1_tus = tk.Button(pencere,text="Test 1 ",font=f"italic {buton_boyut}",bg=buton_rengi,command=test1)
test_1_tus.place(x=1,y=1)

test_2_tus = tk.Button(pencere,text="Test 2 ",font=f"italic {buton_boyut}",bg=buton_rengi,command=test2)
test_2_tus.place(x=200,y=1)

test_3_tus = tk.Button(pencere,text="Test 3 ",font=f"italic {buton_boyut}",bg=buton_rengi,command=test3)
test_3_tus.place(x=399,y=1)

test_4_tus = tk.Button(pencere,text="Test 4 ",font=f"italic {buton_boyut}",bg=buton_rengi,command=test4)
test_4_tus.place(x=599,y=1)

test_5_tus = tk.Button(pencere,text="Test 5 ",font=f"italic {buton_boyut}",bg=buton_rengi,command=test5)
test_5_tus.place(x=799,y=1)

test_6_tus = tk.Button(pencere,text="Test 6 ",font=f"italic {buton_boyut}",bg=buton_rengi,command=test6)
test_6_tus.place(x=999,y=1)

test_7_tus = tk.Button(pencere,text="Test 7 ",font=f"italic {buton_boyut}",bg=buton_rengi,command=test7)
test_7_tus.place(x=1,y=150)

test_8_tus = tk.Button(pencere,text="Test 8 ",font=f"italic {buton_boyut}",bg=buton_rengi,command=test8)
test_8_tus.place(x=200,y=150)

test_9_tus = tk.Button(pencere,text="Test 9 ",font=f"italic {buton_boyut}",bg=buton_rengi,command=test9)
test_9_tus.place(x=399,y=150)

test_10_tus = tk.Button(pencere,text="Test 10",font=f"italic {buton_boyut}",bg=buton_rengi,command=test10)
test_10_tus.place(x=599,y=150)

test_11_tus = tk.Button(pencere,text="Test 11",font=f"italic {buton_boyut}",bg=buton_rengi,command=test11)
test_11_tus.place(x=799,y=150)

test_12_tus = tk.Button(pencere,text="Test 12",font=f"italic {buton_boyut}",bg=buton_rengi,command=test12)
test_12_tus.place(x=999,y=150)

test_13_tus = tk.Button(pencere,text="Test 13",font=f"italic {buton_boyut}",bg=buton_rengi,command=test13)
test_13_tus.place(x=1,y=300)

test_14_tus = tk.Button(pencere,text="Test 14",font=f"italic {buton_boyut}",bg=buton_rengi,command=test14)
test_14_tus.place(x=200,y=300)

test_15_tus = tk.Button(pencere,text="Test 15",font=f"italic {buton_boyut}",bg=buton_rengi,command=test15)
test_15_tus.place(x=399,y=300)

test_16_tus = tk.Button(pencere,text="Test 16",font=f"italic {buton_boyut}",bg=buton_rengi,command=test16)
test_16_tus.place(x=599,y=300)

test_17_tus = tk.Button(pencere,text="Test 17",font=f"italic {buton_boyut}",bg=buton_rengi,command=test17)
test_17_tus.place(x=799,y=300)

test_18_tus = tk.Button(pencere,text="Test 18",font=f"italic {buton_boyut}",bg=buton_rengi,command=test18)
test_18_tus.place(x=999,y=300)

test_19_tus = tk.Button(pencere,text="Test 19",font=f"italic {buton_boyut}",bg=buton_rengi,command=test19)
test_19_tus.place(x=1,y=450)

test_20_tus = tk.Button(pencere,text="Test 20",font=f"italic {buton_boyut}",bg=buton_rengi,command=test20)
test_20_tus.place(x=200,y=450)

test_21_tus = tk.Button(pencere,text="Test 21",font=f"italic {buton_boyut}",bg=buton_rengi,command=test21)
test_21_tus.place(x=399,y=450)

test_22_tus = tk.Button(pencere,text="Test 22",font=f"italic {buton_boyut}",bg=buton_rengi,command=test22)
test_22_tus.place(x=599,y=450)

test_23_tus = tk.Button(pencere,text="Test 23",font=f"italic {buton_boyut}",bg=buton_rengi,command=test23)
test_23_tus.place(x=799,y=450)

test_24_tus = tk.Button(pencere,text="Test 24",font=f"italic {buton_boyut}",bg=buton_rengi,command=test24)
test_24_tus.place(x=999,y=450)

cizgi = tk.Label(text="_______________________________________________________________________________________________________________________________",font="italic 40",bg="light yellow")
cizgi.place(x=1,y=519)

info_tus = tk.Button(text= "Bilgi",font=f"italic {buton_boyut}",command=kaybett,bg="light yellow")
info_tus.place(x=550,y=590)


while True:
	giris = input()
	if giris == "kaynak kod":
		print("https://github.com/Yigit-2023/12.sinif-test\n")
	else:
		print()

pencere.mainloop()



