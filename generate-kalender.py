#!/usr/bin/python

# functions:
# makecolumn, makeleftbody, makerightbody, makeheader, makefooter, makemain

import svgwrite

class Kalender:
	linecolor = (0,0,0)
	textcolor = (0,0,0)
	linewidth = 1
	backgroundcolor1 = (255,255,255)
	backgroundcolor2 = (0,0,0)
	daytexttype = "meh-font"
	daytextsize = 10
	year = 2017
	weekendcolor = ()
	holydaycolor = ()
	headerpictures = [("name",size),("more-name",size)]
	footerpictures = []
	monthtexttype = "font-type"
	monthtextsize = 10
	footertexts = ["sometext","anotherline of text"]
	headertexts = []
	headerlogo = ("name", size)

	def __init__(self, year=2017):
		self.year = year

	def makefooter(self):
		pass

	def makeheader(self):
		pass

	def makemain(self):
		pass

	def makecolumn(self):
		pass

	def makeother(self):
		pass

	def setlinecolor(self):
		pass

	def setlinewidth(self):
		pass

	def setmargins(self,width, height):
		pass

	def setfootertext(self, texts, size, color)
		pass

	def addfootertext(self, texttoadd):
		pass

	def setheadertext(self, texts, size, color):
		pass	

	def addheadertext(self, texts);
		pass

	def settextcolor(self, color);
		pass

	def sethearpicture(self, pictures, maxsize):
		pass

	def addheaderpictures(self, picture):
		pass

	def setfooterpictures(self, pictures, maxsize):
		pass

	def addfooterpictures():
		pass

	def addlogo(self, picture, maxsize):
		pass

