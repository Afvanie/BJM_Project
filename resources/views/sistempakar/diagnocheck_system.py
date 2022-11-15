
from tkinter import *
import tkinter.font

root = Tk()
root.geometry("400x640")
changefont = tkinter.font.Font(size = 10)
judul = Label(root,text="SISTEM PAKAR DIAGNOSA KERUSAKAN MOBIL",font=changefont)
judul.place(x=90,y=10)

labelfr = LabelFrame(root,text ="Hasil",padx=20,pady=20)
labelfr.place(x=10,y=360)

kerusakan = ["Aki Rusak", "Busi Lemah", "Pompa bahan bakar", "Ring piston rusak", "Malfungsi Idle Speed Control Valve", "Kualitas Oli Sudah tidak bagus", "Malfungsi Fuel Injector"]
gejala = ["Mesin Sulit Dinyalakan", "Suara Klakson Menjadi tidak Nyaring", "Cahaya Lampu Lebih Redup", "Apakah mobil tersendat sendat", "Asap putih akan keluar dari knalpot", "RPM mesin drop, bahkan mati", "mesin mati sendiri saat beban mesin bertambah"]
pengetahuan = [
    ["Aki Rusak", "Mesin Sulit Dinyalakan", 1, 0],
    ["Aki Rusak", "Suara Klakson Menjadi tidak Nyaring", 1, 0],
    ["Aki Rusak", "Cahaya Lampu Lebih Redup", 1, 0],
    ["Busi Lemah", "Mesin Sulit Dinyalakan", 0.6, 0.4],
    ["Busi Lemah", "Suara Klakson Menjadi tidak Nyaring", 0.2, 0.6],
    ["Busi Lemah", "Apakah mobil tersendat sendat", 0.8, 0.2],
    ["Pompa bahan bakar", "Mesin Sulit Dinyalakan", 0.2, 0.6],
    ["Pompa bahan bakar", "Suara Klakson Menjadi tidak Nyaring", 0.4, 0.4],
    ["Pompa bahan bakar", "Apakah mobil tersendat sendat", 0.4, 0.2],
    ["Pompa bahan bakar", "RPM mesin drop, bahkan mati", 0.8, 0.2],
    ["Pompa bahan bakar", "mesin mati sendiri saat beban mesin bertambah", 0.6, 0.2],
    ["Ring piston rusak", "Mesin Sulit Dinyalakan", 0.8, 0.2],
    ["Ring piston rusak", "Suara Klakson Menjadi tidak Nyaring", 0.2, 0.6],
    ["Ring piston rusak", "Cahaya Lampu Lebih Redup", 0.4, 0.2],
    ["Ring piston rusak", "Asap putih akan keluar dari knalpot", 0.4, 0.2],
    ["Malfungsi Idle Speed Control Valve", "Suara Klakson Menjadi tidak Nyaring", 0.8, 0.2],
    ["Malfungsi Idle Speed Control Valve", "Apakah mobil tersendat sendat", 0.4, 0.4],
    ["Malfungsi Idle Speed Control Valve", "RPM mesin drop, bahkan mati", 0.4, 0.2],
    ["Malfungsi Idle Speed Control Valve", "mesin mati sendiri saat beban mesin bertambah", 0.4, 0.2],
    ["Kualitas Oli Sudah tidak bagus", "Suara Klakson Menjadi tidak Nyaring", 0.2, 0.6],
    ["Kualitas Oli Sudah tidak bagus", "RPM mesin drop, bahkan mati", 0.8, 0.2],
    ["Kualitas Oli Sudah tidak bagus", "mesin mati sendiri saat beban mesin bertambah", 0.4, 0.2],
    ["Malfungsi Fuel Injector", "Mesin Sulit Dinyalakan", 0.4, 0.4],
    ["Malfungsi Fuel Injector", "Cahaya Lampu Lebih Redup", 0.8, 0.2],
    ["Malfungsi Fuel Injector", "RPM mesin drop, bahkan mati", 0.6, 0.2],
    ["Malfungsi Fuel Injector", "mesin mati sendiri saat beban mesin bertambah", 0.6, 0.02]
    
]

Mesin_Sulit_Dinyalakan = Label(root,text = "Apakah Anda Mengalami Mesin Sulit Dinyalakan?")
Suara_tidak_Nyaring = Label(root,text = "Apakah Anda Mengalami Suara Klakson Menjadi tidak Nyaring?")
cahayaredup = Label(root,text = "Apakah Anda Cahaya Lampu Lebih Redup?")
tersendat_sendat = Label(root,text = "Apakah Anda Apakah mobil tersendat sendat?")
Asap_putih_knalpot = Label(root,text = "Apakah Anda Mengalami Asap putih akan keluar dari knalpot?")
rpmdrop = Label(root,text = "Apakah Anda Mengalami RPM mesin drop, bahkan mati?")
mesin_mati_beban_mesin_bertambah = Label(root,text = "Apakah Anda Mengalami mesin mati sendiri saat beban mesin bertambah?")

Mesin_Sulit_Dinyalakan.place(x = 20, y = 40)
Suara_tidak_Nyaring.place(x = 20, y = 80)
cahayaredup.place(x = 20, y = 120)
tersendat_sendat.place(x = 20, y = 160)
Asap_putih_knalpot.place(x = 20, y = 200)
rpmdrop.place(x = 20, y = 240)
mesin_mati_beban_mesin_bertambah.place(x = 20, y = 280)

dm = StringVar()
dm.set("none")
rbdm1 = Radiobutton(root, text ="Ya",variable=dm,value="ya").place(x=20, y=60)
rbdm1 = Radiobutton(root, text ="Tidak",variable=dm,value="tidak").place(x=80, y=60)

bt = StringVar()
bt.set("none")
rbbt1 = Radiobutton(root, text ="Ya",variable=bt,value="ya").place(x=20, y=100)
rbbt1 = Radiobutton(root, text ="Tidak",variable=bt,value="tidak").place(x=80, y=100)

st = StringVar()
st.set("none")
rbst1 = Radiobutton(root, text ="Ya",variable=st,value="ya").place(x=20, y=140)
rbst1 = Radiobutton(root, text ="Tidak",variable=st,value="tidak").place(x=80, y=140)

kr = StringVar()
kr.set("none")
rbkr1 = Radiobutton(root, text ="Ya",variable=kr,value="ya").place(x=20, y=180)
rbkr1 = Radiobutton(root, text ="Tidak",variable=kr,value="tidak").place(x=80, y=180)

dr = StringVar()
dr.set("none")
rbdr1 = Radiobutton(root, text ="Ya",variable=dr,value="ya").place(x=20, y=220)
rbdr1 = Radiobutton(root, text ="Tidak",variable=dr,value="tidak").place(x=80, y=220)

sn = StringVar()
sn.set("none")
rbsn1 = Radiobutton(root, text ="Ya",variable=sn,value="ya").place(x=20, y=260)
rbsn1 = Radiobutton(root, text ="Tidak",variable=sn,value="tidak").place(x=80, y=260)

nd = StringVar()
nd.set("none")
rbnd1 = Radiobutton(root, text ="Ya",variable=nd,value="ya").place(x=20, y=300)
rbnd1 = Radiobutton(root, text ="Tidak",variable=nd,value="tidak").place(x=80, y=300)
        
def hitung():
            gejala_dipilih = []
            if dm.get() == "ya":
                gejala_dipilih.append(gejala[0])
            if bt.get() == "ya":
                gejala_dipilih.append(gejala[1])
            if st.get() == "ya":
                gejala_dipilih.append(gejala[2])
            if kr.get() == "ya":
                gejala_dipilih.append(gejala[3])
            if dr.get() == "ya":
                gejala_dipilih.append(gejala[4])
            if sn.get() == "ya":
                gejala_dipilih.append(gejala[5])
            if nd.get() == "ya":
                gejala_dipilih.append(gejala[6])

            kerusakan_terpilih = []
            for i in range(len(pengetahuan)):
                for j in range(len(gejala_dipilih)):
                    if (pengetahuan[i][1] == gejala_dipilih[j]):
                        if pengetahuan[i][0] not in kerusakan_terpilih:
                            kerusakan_terpilih.append(pengetahuan[i][0])
            print("kerusakan terpilih", kerusakan_terpilih)

            list_cf = []
            for i in range(len(kerusakan_terpilih)):
                print("===="+kerusakan_terpilih[i]+"====")
                jmlpengetahuan = 0
                pengetahuanke = 0
                for j in range(len(pengetahuan)):
                            if(pengetahuan[j][0] == kerusakan_terpilih[i]) and (pengetahuan[j][1] in gejala_dipilih):
                                jmlpengetahuan = jmlpengetahuan + 1
                mblama = 0
                mdlama = 0
                for j in range(len(pengetahuan)):
                    if(pengetahuan[j][0] == kerusakan_terpilih[i]) and (pengetahuan[j][1] in gejala_dipilih):
                        pengetahuanke = pengetahuanke + 1
                        if (jmlpengetahuan == 1):
                            mb = pengetahuan[j][2]
                            md = pengetahuan[j][3]
                            cf = mb - md
                            print("mb = ", mb)
                            print("md = ", md)
                            print("cf = mb - md = ", mb, " - ", md, " = ", cf);
                            list_cf.append(cf)
                        elif (jmlpengetahuan > 1):
                            if (pengetahuanke == 1):
                                mblama = pengetahuan [j][2]
                                mdlama = pengetahuan [j][3]
                                print ("mblama = ", mblama)
                                print ("mdlama = ", mdlama)
                            elif (pengetahuanke == 2):
                                mbbaru = pengetahuan[j][2]
                                mdbaru = pengetahuan[j][3]
                                mbsementara = (mblama + mbbaru) * (1 - mblama)
                                mdsementara = (mdlama + mdbaru) * (1 - mdlama)
                                print("mbsementara = (mblama + mbbaru) * (1 - mblama) = (",\
                                    mblama, " + ", mbbaru, ") * (1 - ", mblama, ") = ", mbsementara)
                                print("mdsementara = (mdlama + mdbaru) * (1 - mdlama) = (",\
                                    mdlama, " + ", mdbaru, ") * (1 - ", mdlama, ") = ", mdsementara)
                                if (jmlpengetahuan == 2):
                                    mb = mbsementara
                                    md = mdsementara
                                    cf = mb - md
                                    print ("mb = mbsementara = ", mb)
                                    print ("md = mdsementara = ", md)
                                    print ("cf = mb - md = ", mb, " - ", md, " = ", cf)
                                    list_cf.append(cf)
                            elif(pengetahuanke >= 3):
                                mblama = mbsementara
                                mdlama = mdsementara
                                print("mblama = mbsementara = ", mblama)
                                print("mdlama = mdsementara = ", mdlama)
                                mbbaru = pengetahuan[j][2]
                                mdbaru = pengetahuan[j][3]
                                print("mbbaru = ", mbbaru)
                                print("mdbaru = ", mdbaru)
                                mbsementara = (mblama + mbbaru) * (1 - mblama)
                                mdsementara = (mdlama + mdbaru) * (1 - mdlama)
                                print("mbsementara = (mblama + mbbaru) * (1 - mblama) = (", \
                                    mblama, " + ", mbbaru, ") * (1- ", mblama, ") = ",mbsementara)
                                print("mdsementara = (mdlama + mdbaru) * (1 - mdlama) = (", \
                                    mdlama, " + ", mdbaru, ") * (1- ", mdlama, ") = ",mdsementara)
                                if(jmlpengetahuan == pengetahuanke):
                                    mb = mbsementara
                                    md = mdsementara
                                    cf = mb - md
                                    print("mb = mbsementara = ", mb)
                                    print("md = mdsementara = ", md)
                                    print("cf = mb - md = ",mb, " - ", md, " = ", cf)
                                    list_cf.append(cf)
            print("Kerusakan Terpilih", kerusakan_terpilih)
            print(list_cf)
            kerusakanrangking = []
            cfrangking = []
            for i in range(len(kerusakan_terpilih)):
                kerusakanrangking.append(kerusakan_terpilih[i])
                cfrangking.append(list_cf[i])
            for i in range(len(kerusakan_terpilih)):
                for j in range (len(kerusakan_terpilih)):
                    if j > i:
                        if cfrangking[j] > cfrangking[i]:
                            tmpcf = cfrangking[i]
                            tmpkerusakan = kerusakanrangking[i]
                            cfrangking[i] = cfrangking[j]
                            kerusakanrangking[i] = kerusakanrangking[j]
                            cfrangking[j] = tmpcf
                            kerusakanrangking[j] = tmpkerusakan
            print("rangking kerusakan", kerusakanrangking)
            print("rangking CF:", cfrangking)
            garis = Label(text="---------------------------HASIL PERHITUNGAN---------------------------").place(x=5,y=360)
            txtkerusakan = Label(text="Diagnosis kerusakan anda adalah : ").place(x=20, y=380)
            lblkerusakanrangking = Label(text=kerusakanrangking[0], fg = "blue").place(x=20, y=400)
            txtkerusakan2 = Label(text="Kemungkinan kerusakan lain adalah : ").place(x=20, y=420)
            lblkerusakanrangking2 = Label(text=kerusakanrangking[1], fg = "blue").place(x=20, y=440)
            txtkerusakan2 = Label(text="Hasil perhitungan nilai CF dari kerusakan anda adalah : ").place(x=20, y=460)
            lblcfrangking = Label(text=cfrangking[0], fg = "blue").place(x=20,y=480)

            if kerusakanrangking[0] == "Aki Rusak":
                sol = Label(text="Solusi dari Kerusakan mobil anda : ").place(x=20,y=500)
                sol2 = Label(text="1. Lakukan Charge pada Aki").place(x=20,y=520)
                sol3 = Label(text="2. Ganti Aki Anda").place(x=20,y=540)
                garis1 = Label(text="------------------------------------------------------------------").place(x=5,y=560)
            elif kerusakanrangking[0] == "Busi Lemah":
                sol = Label(text="Solusi dari Kerusakan mobil anda : ").place(x=20,y=500)
                sol2 = Label(text="1. Coba bersihkan Busi anda").place(x=20,y=520)
                sol3 = Label(text="2. Mengganti Busi Mobil Anda").place(x=20,y=540)
                garis1 = Label(text="-----------------------------------------------------------------------------").place(x=5,y=560)
            elif kerusakanrangking[0] == "Pompa bahan bakar":
                sol = Label(text="Solusi dari Kerusakan mobil anda : ").place(x=20,y=500)
                sol2 = Label(text="1. Servis Pompa Bahan Bakar").place(x=20,y=520)
                sol3 = Label(text="2. Mengganti Pompa Bahan Bakar Mobil Anda").place(x=20,y=540)
                garis1 = Label(text="-----------------------------------------------------------------------------").place(x=5,y=580)
            elif kerusakanrangking[0] == "Ring piston rusak":
                sol = Label(text="Solusi dari Kerusakan mobil anda : ").place(x=20,y=500)
                sol2 = Label(text="1. Ganti Ring Piston Mobil Anda").place(x=20,y=520)
                garis1 = Label(text="-----------------------------------------------------------------------------").place(x=5,y=580)
            elif kerusakanrangking[0] == "Kualitas Oli Sudah tidak bagus":
                sol = Label(text="Solusi dari Kerusakan mobil anda : ").place(x=20,y=500)
                sol2 = Label(text="1. Cek keadaan oli anda").place(x=20,y=520)
                sol3 = Label(text="2. Mengganti Oli").place(x=20,y=540)
                garis1 = Label(text="-----------------------------------------------------------------------------").place(x=5,y=580)
            elif kerusakanrangking[0] == "Malfungsi Fuel Injector":
                sol = Label(text="Solusi dari Kerusakan mobil anda : ").place(x=20,y=500)
                sol2 = Label(text="1. Bersihkan Fuel Injektor mobil anda").place(x=20,y=520)
                sol3 = Label(text="2. Ganti Fuel Injektor Mobil Anda").place(x=20,y=540)
                garis1 = Label(text="-----------------------------------------------------------------------------").place(x=5,y=600)


btn = Button(root,text="Hitung",command=hitung).place(x=20, y=330)
root.mainloop()