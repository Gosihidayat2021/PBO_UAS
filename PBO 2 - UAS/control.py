import wx
import csv
from builder import *
kategori = []
nama = []
harga = []
jumlah = []
e=0
with open('data_barang.csv') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=';')
    line_count = 0
    for row in csv_reader:
        kategori.append(row[0])
        nama.append(row[1])
        harga.append(row[2])
        jumlah.append(row[3])
class App(wx.App):
    appFrame = None
    def OnInit(self):
        self.appFrame = homemenu(getstarted(None))
        self.appFrame.Show()
        return True

class homemenu(getstarted):
    def started_start(self,event):
        self.appFrame = startedone(started1(None))
        self.appFrame.Show()
    def kirimKomentar(self,event):
        wx.MessageBox ('Terima Kasih atas komentar anda\nKomentar telah direkam')
    def goto_market(self,event):
        self.appFrame = databarang(marketplace(None))
        self.appFrame.Show()
class startedone(started1):
    def next1(self,event):
        self.Close()
        self.appFrame = startedtwo(started2(None))
        self.appFrame.Show()
class startedtwo(started2):
    def back1(self,event):
        self.Close()
        self.appFrame = startedone(started1(None))
        self.appFrame.Show()
    def next2(self,event):
        self.Close()
        self.appFrame = startedthree(started3(None))
        self.appFrame.Show()
class startedthree(started3):
    def back2(self,event):
        self.Close()
        self.appFrame = startedtwo(started2(None))
        self.appFrame.Show()
    def Home(self,event):
        self.Close()
        self.appFrame = homemenu(getstarted(None))
        self.appFrame.Show()
        
class databarang(marketplace):
    
    def pilih_cell(self, event):
        row = event.GetRow()
        col = event.GetCol()
        print('row :',row)
        print('col :',col)
        if col == 4:
            nama = self.data_barang.GetCellValue(row,1)
            harga = self.data_barang.GetCellValue(row,2)
            wx.MessageBox ('Anda akan membeli %s dengan harga : %d' %(nama,int(harga)))    

    def pilih_tanaman(self, event):
        row = event.GetRow()
        col = event.GetCol()
        print('row :',row)
        print('col :',col)
    
    def cari_kategori(self,event):
        d=0
        pilihan = self.boxkategori.GetCurrentSelection()
        print (pilihan)
        if pilihan == 0:
            for a in range(len(kategori)):
                if (kategori[a]=="Tanaman"):
                    self.data_barang.SetCellValue(int(d),0,kategori[a])
                    self.data_barang.SetCellValue(int(d),1,nama[a])
                    self.data_barang.SetCellValue(int(d),2,harga[a])
                    self.data_barang.SetCellValue(int(d),3,jumlah[a])
                    self.data_barang.SetCellValue(int(d),4,'Beli')
                    d+=1
        elif pilihan == 1:
            for a in range(len(kategori)):
                if (kategori[a]=="Benih"):
                    self.data_barang.SetCellValue(int(d),0,kategori[a])
                    self.data_barang.SetCellValue(int(d),1,nama[a])
                    self.data_barang.SetCellValue(int(d),2,harga[a])
                    self.data_barang.SetCellValue(int(d),3,jumlah[a])
                    self.data_barang.SetCellValue(int(d),4,'Beli')
                    d+=1
        elif pilihan == 2:
            for a in range(len(kategori)):
                if (kategori[a]=="Alat"):
                    self.data_barang.SetCellValue(int(d),0,kategori[a])
                    self.data_barang.SetCellValue(int(d),1,nama[a])
                    self.data_barang.SetCellValue(int(d),2,harga[a])
                    self.data_barang.SetCellValue(int(d),3,jumlah[a])
                    self.data_barang.SetCellValue(int(d),4,'Beli')
                    d+=1
        else:
            for a in range(len(kategori)):
                if (kategori[a]=="Pupuk"):
                    self.data_barang.SetCellValue(int(d),0,kategori[a])
                    self.data_barang.SetCellValue(int(d),1,nama[a])
                    self.data_barang.SetCellValue(int(d),2,harga[a])
                    self.data_barang.SetCellValue(int(d),3,jumlah[a])
                    self.data_barang.SetCellValue(int(d),4,'Beli')
                    d+=1

def datatanaman(getstarted):
    def Tambah(self,event):
        tanamanku = self.input_tanaman.GetValue()
        self.data_tanaman.SetCellValue(int(e),0,tanamanku)
        self.data_tanaman.SetCellValue(int(e),1,0)
        self.data_tanaman.SetCellValue(int(e),2,"Baik")
        e+=1
        
        
        

    
