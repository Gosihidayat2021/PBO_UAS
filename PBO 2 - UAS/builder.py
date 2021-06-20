# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class getstarted
###########################################################################

class getstarted ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Hi Hidroponik setup", pos = wx.DefaultPosition, size = wx.Size( 552,411 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText35 = wx.StaticText( self, wx.ID_ANY, u"Hi HIDROPONIK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )

		self.m_staticText35.SetFont( wx.Font( 11, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Mont Heavy DEMO" ) )

		bSizer10.Add( self.m_staticText35, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_panel13 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook3 = wx.Notebook( self.m_panel13, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Start = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer15 = wx.BoxSizer( wx.VERTICAL )


		bSizer15.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText40 = wx.StaticText( self.Start, wx.ID_ANY, u"Get Started Hi Hidroponik", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )

		bSizer15.Add( self.m_staticText40, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.btn_mulai = wx.Button( self.Start, wx.ID_ANY, u"Lest go!!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.btn_mulai, 0, wx.ALL|wx.EXPAND, 5 )

		self.btn_market = wx.Button( self.Start, wx.ID_ANY, u"Marketplace", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.btn_market, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer15.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.Start.SetSizer( bSizer15 )
		self.Start.Layout()
		bSizer15.Fit( self.Start )
		self.m_notebook3.AddPage( self.Start, u"Get Started", False )
		self.Forum = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer9 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText36 = wx.StaticText( self.Forum, wx.ID_ANY, u"  Rosidin  ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )

		self.m_staticText36.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial Black" ) )
		self.m_staticText36.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		gSizer9.Add( self.m_staticText36, 0, wx.ALL, 5 )

		self.m_staticText37 = wx.StaticText( self.Forum, wx.ID_ANY, u"  Mahmud  ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )

		self.m_staticText37.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial Black" ) )
		self.m_staticText37.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		gSizer9.Add( self.m_staticText37, 0, wx.ALL, 5 )

		self.m_staticText45 = wx.StaticText( self.Forum, wx.ID_ANY, u"Bagi tips dong letak \nyang pas buat tanaman \nhidroponiknya ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )

		gSizer9.Add( self.m_staticText45, 0, wx.ALL, 5 )

		self.m_staticText46 = wx.StaticText( self.Forum, wx.ID_ANY, u"Gampang banget broo\nkamu bisa letakan aja di \ndepan kandang ayam\nbiar di makan tuh sama ayamnya", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )

		gSizer9.Add( self.m_staticText46, 0, wx.ALL, 5 )


		gSizer9.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer9.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText53 = wx.StaticText( self.Forum, wx.ID_ANY, u"  Astrid  ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText53.Wrap( -1 )

		self.m_staticText53.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial Black" ) )
		self.m_staticText53.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		gSizer9.Add( self.m_staticText53, 0, wx.ALL, 5 )

		self.m_staticText54 = wx.StaticText( self.Forum, wx.ID_ANY, u"  Istrinya pak mahmud  ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText54.Wrap( -1 )

		self.m_staticText54.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial Black" ) )
		self.m_staticText54.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		gSizer9.Add( self.m_staticText54, 0, wx.ALL, 5 )

		self.m_staticText55 = wx.StaticText( self.Forum, wx.ID_ANY, u"Alhamdhulillah tanaman saya \nhabis di buang sama nenek", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText55.Wrap( -1 )

		gSizer9.Add( self.m_staticText55, 0, wx.ALL, 5 )

		self.m_staticText56 = wx.StaticText( self.Forum, wx.ID_ANY, u"Wah ayah mulai pintar \nberbudidaya tanamannya", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText56.Wrap( -1 )

		gSizer9.Add( self.m_staticText56, 0, wx.ALL, 5 )


		gSizer9.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer9.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText68 = wx.StaticText( self.Forum, wx.ID_ANY, u"Input nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText68.Wrap( -1 )

		self.m_staticText68.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Bernard MT Condensed" ) )

		gSizer9.Add( self.m_staticText68, 0, wx.ALL, 5 )

		self.m_staticText69 = wx.StaticText( self.Forum, wx.ID_ANY, u"Input komentar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText69.Wrap( -1 )

		self.m_staticText69.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Bernard MT Condensed" ) )

		gSizer9.Add( self.m_staticText69, 0, wx.ALL, 5 )

		self.inputnama = wx.TextCtrl( self.Forum, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.inputnama, 0, wx.ALL, 5 )

		self.inputkomen = wx.TextCtrl( self.Forum, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.inputkomen, 0, wx.ALL, 5 )

		self.btn_kirim = wx.Button( self.Forum, wx.ID_ANY, u"Kirim", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.btn_kirim, 0, wx.ALL, 5 )


		self.Forum.SetSizer( gSizer9 )
		self.Forum.Layout()
		gSizer9.Fit( self.Forum )
		self.m_notebook3.AddPage( self.Forum, u"Forum", False )
		self.m_panel61 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText22 = wx.StaticText( self.m_panel61, wx.ID_ANY, u"AKTIVITAS TANAMAN ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		self.m_staticText22.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial Black" ) )

		bSizer8.Add( self.m_staticText22, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gSizer7 = wx.GridSizer( 0, 3, 0, 0 )

		self.m_staticText34 = wx.StaticText( self.m_panel61, wx.ID_ANY, u"Input Tanaman : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		gSizer7.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.input_tanaman = wx.TextCtrl( self.m_panel61, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.input_tanaman, 0, wx.ALL, 5 )

		self.btn_tambah = wx.Button( self.m_panel61, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.btn_tambah, 0, wx.ALL, 5 )


		gSizer7.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.data_tanaman = wx.grid.Grid( self.m_panel61, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.data_tanaman.CreateGrid( 5, 3 )
		self.data_tanaman.EnableEditing( True )
		self.data_tanaman.EnableGridLines( True )
		self.data_tanaman.EnableDragGridSize( False )
		self.data_tanaman.SetMargins( 0, 0 )

		# Columns
		self.data_tanaman.EnableDragColMove( False )
		self.data_tanaman.EnableDragColSize( True )
		self.data_tanaman.SetColLabelSize( 30 )
		self.data_tanaman.SetColLabelValue( 0, u"Tanaman" )
		self.data_tanaman.SetColLabelValue( 1, u"Umur" )
		self.data_tanaman.SetColLabelValue( 2, u"Keadaan" )
		self.data_tanaman.SetColLabelValue( 3, u"Tanaman" )
		self.data_tanaman.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.data_tanaman.EnableDragRowSize( True )
		self.data_tanaman.SetRowLabelSize( 80 )
		self.data_tanaman.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.data_tanaman.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		gSizer7.Add( self.data_tanaman, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		gSizer7.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer7.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer7.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer7.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer7.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer7.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText24 = wx.StaticText( self.m_panel61, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		self.m_staticText24.Hide()

		gSizer7.Add( self.m_staticText24, 0, wx.ALL, 5 )

		self.m_staticText25 = wx.StaticText( self.m_panel61, wx.ID_ANY, u"Disiram ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		gSizer7.Add( self.m_staticText25, 0, wx.ALL, 5 )

		self.disiram = wx.CheckBox( self.m_panel61, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.disiram, 0, wx.ALL, 5 )

		self.m_staticText31 = wx.StaticText( self.m_panel61, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.Hide()

		gSizer7.Add( self.m_staticText31, 0, wx.ALL, 5 )

		self.m_staticText32 = wx.StaticText( self.m_panel61, wx.ID_ANY, u"Diberi pupuk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		gSizer7.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.dipupuk = wx.CheckBox( self.m_panel61, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.dipupuk, 0, wx.ALL, 5 )


		bSizer8.Add( gSizer7, 1, wx.EXPAND, 5 )


		self.m_panel61.SetSizer( bSizer8 )
		self.m_panel61.Layout()
		bSizer8.Fit( self.m_panel61 )
		self.m_notebook3.AddPage( self.m_panel61, u"Tanamanku", False )

		bSizer13.Add( self.m_notebook3, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel13.SetSizer( bSizer13 )
		self.m_panel13.Layout()
		bSizer13.Fit( self.m_panel13 )
		bSizer10.Add( self.m_panel13, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer10 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_mulai.Bind( wx.EVT_BUTTON, self.started_start )
		self.btn_market.Bind( wx.EVT_BUTTON, self.goto_market )
		self.btn_kirim.Bind( wx.EVT_BUTTON, self.kirimKomentar )
		self.btn_tambah.Bind( wx.EVT_BUTTON, self.Tambah )
		self.data_tanaman.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.pilih_tanaman )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def started_start( self, event ):
		event.Skip()

	def goto_market( self, event ):
		event.Skip()

	def kirimKomentar( self, event ):
		event.Skip()

	def Tambah( self, event ):
		event.Skip()

	def pilih_tanaman( self, event ):
		event.Skip()


###########################################################################
## Class marketplace
###########################################################################

class marketplace ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Marketplace", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.Marketplace = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer3 = wx.GridSizer( 0, 3, 0, 0 )

		self.m_staticText26 = wx.StaticText( self.Marketplace, wx.ID_ANY, u"Pilih Kategori", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )

		gSizer3.Add( self.m_staticText26, 0, wx.ALL, 5 )

		boxkategoriChoices = [ u"Tanaman", u"Benih", u"Alat", u"Pupuk" ]
		self.boxkategori = wx.ComboBox( self.Marketplace, wx.ID_ANY, u"Kategori", wx.DefaultPosition, wx.DefaultSize, boxkategoriChoices, 0 )
		gSizer3.Add( self.boxkategori, 0, wx.ALL, 5 )

		self.btn_cari = wx.Button( self.Marketplace, wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.btn_cari, 0, wx.ALL, 5 )

		self.data_barang = wx.grid.Grid( self.Marketplace, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.data_barang.CreateGrid( 7, 5 )
		self.data_barang.EnableEditing( True )
		self.data_barang.EnableGridLines( True )
		self.data_barang.EnableDragGridSize( False )
		self.data_barang.SetMargins( 0, 0 )

		# Columns
		self.data_barang.EnableDragColMove( False )
		self.data_barang.EnableDragColSize( True )
		self.data_barang.SetColLabelSize( 30 )
		self.data_barang.SetColLabelValue( 0, u"Kategori" )
		self.data_barang.SetColLabelValue( 1, u"Nama Barang " )
		self.data_barang.SetColLabelValue( 2, u"Harga" )
		self.data_barang.SetColLabelValue( 3, u"Jumlah" )
		self.data_barang.SetColLabelValue( 4, u"Beli" )
		self.data_barang.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.data_barang.EnableDragRowSize( True )
		self.data_barang.SetRowLabelSize( 80 )
		self.data_barang.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.data_barang.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		gSizer3.Add( self.data_barang, 0, wx.ALL, 5 )


		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.Marketplace.SetSizer( gSizer3 )
		self.Marketplace.Layout()
		gSizer3.Fit( self.Marketplace )
		bSizer8.Add( self.Marketplace, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.boxkategori.Bind( wx.EVT_COMBOBOX, self.Cari )
		self.btn_cari.Bind( wx.EVT_BUTTON, self.cari_kategori )
		self.data_barang.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.pilih_cell )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Cari( self, event ):
		event.Skip()

	def cari_kategori( self, event ):
		event.Skip()

	def pilih_cell( self, event ):
		event.Skip()


###########################################################################
## Class started1
###########################################################################

class started1 ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pop Up Tutorial", pos = wx.DefaultPosition, size = wx.Size( 478,190 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText59 = wx.StaticText( self, wx.ID_ANY, u"Budidaya Tanaman Hidroponik Sederhana", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText59.Wrap( -1 )

		bSizer17.Add( self.m_staticText59, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText58 = wx.StaticText( self, wx.ID_ANY, u"Hidroponik Sistem Wick\n\nCara bercocok tanam hidroponik sistem wick sangat cocok diterapkan bagi pemula. Sistem penanaman ini cock untuk jenis tanaman kecil, seperti sawi, kangkung, bayam, dan jenis sayuran kecil yang tidak membutuhkan banyak air.\n\n", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText58.Wrap( -1 )

		bSizer17.Add( self.m_staticText58, 0, wx.ALL, 5 )


		bSizer17.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button32 = wx.Button( self, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_button32, 0, wx.ALL, 5 )


		self.SetSizer( bSizer17 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button32.Bind( wx.EVT_BUTTON, self.next1 )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def next1( self, event ):
		event.Skip()


###########################################################################
## Class started2
###########################################################################

class started2 ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pop Up Tutorial", pos = wx.DefaultPosition, size = wx.Size( 480,312 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText59 = wx.StaticText( self, wx.ID_ANY, u"Budidaya Tanaman Hidroponik Sederhana", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText59.Wrap( -1 )

		bSizer17.Add( self.m_staticText59, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText58 = wx.StaticText( self, wx.ID_ANY, u"Hidroponik sistem wick mengharuskan Anda selalu mengganti larutan nutrisi dibawahnya, layaknya tanaman yang lain, ia juga butuh penyiraman. Cara bercocok tanam hidroponik sistem wick yakni,\n\nSiapkan alat-alat berupa :\n\n# 1 botol air mineral bekas, masih layak pakai\n# Alat pemotong, seperti cutter atau gunting\n# Sumbu kompor atau kain flannel\n# Alat untuk melubangi, bisa solder atau paku\n# Air nutrisi\n\n", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText58.Wrap( -1 )

		bSizer17.Add( self.m_staticText58, 0, wx.ALL, 5 )


		bSizer17.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button32 = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_button32, 0, wx.ALL, 5 )

		self.m_button36 = wx.Button( self, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_button36, 0, wx.ALL, 5 )


		self.SetSizer( bSizer17 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button32.Bind( wx.EVT_BUTTON, self.back1 )
		self.m_button36.Bind( wx.EVT_BUTTON, self.next2 )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def back1( self, event ):
		event.Skip()

	def next2( self, event ):
		event.Skip()


###########################################################################
## Class started3
###########################################################################

class started3 ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pop Up Tutorial", pos = wx.DefaultPosition, size = wx.Size( 480,298 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText59 = wx.StaticText( self, wx.ID_ANY, u"Budidaya Tanaman Hidroponik Sederhana", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText59.Wrap( -1 )

		bSizer17.Add( self.m_staticText59, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText58 = wx.StaticText( self, wx.ID_ANY, u"Cara membuat :\n\nPotong botol bekas menjadi 2 bagian.\nLubangi tutup botol menggunakan paku yang dipanaskan kemudian tusuk tutupnya.\nGabungkan kedua bagian botol, dengan membalik bagian moncong (tutup botol) menghadap ke bawah.\nPasang sumbu kompor atau kain flannel pada lubang di tutup botol tadi, pastikan bahwa sumbu dapat mengaliri air nutrisi terserap sempurna.\nTanam bibit tanaman pada bagian atas botol dengan tanah secukupnya.\nIsi bagian bawah botol dengan air nutrisi.\nPastikan jarak bibit yang ditanam lebih dekat dengan dasar botol plastic, supaya mendapat nutrisi secara penuh.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText58.Wrap( -1 )

		bSizer17.Add( self.m_staticText58, 0, wx.ALL, 5 )


		bSizer17.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button38 = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_button38, 0, wx.ALL, 5 )

		self.m_button32 = wx.Button( self, wx.ID_ANY, u"Home", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_button32, 0, wx.ALL, 5 )


		self.SetSizer( bSizer17 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button38.Bind( wx.EVT_BUTTON, self.back2 )
		self.m_button32.Bind( wx.EVT_BUTTON, self.Home )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def back2( self, event ):
		event.Skip()

	def Home( self, event ):
		event.Skip()


