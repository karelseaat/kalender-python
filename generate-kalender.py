#!/usr/bin/python

# functions:
# makecolumn, makeleftbody, makerightbody, makeheader, makefooter, makemain

from dateutil.rrule import rrule, DAILY
from datetime import datetime, date
import svgwrite
from dateutil.relativedelta import relativedelta 

class Kalender:
	linecolor = (0,0,0)
	textcolor = (0,0,0)
	linewidth = 1
	colwidth = 50
	colhormarginn = 5
	backgroundcolor1 = (255,255,255)
	backgroundcolor2 = (0,0,0)
	daytexttype = "meh-font"
	daytextsize = 10
	year = 2017
	weekendcolor = ()
	holydaycolor = ()
	headerpictures = [("name", 10),("more-name",10)]
	footerpictures = []
	monthtexttype = "font-type"
	monthtextsize = 10
	footertexts = ["sometext","anotherline of text"]
	headertexts = []
	headerlogo = ("name", 10)
	weekdaynames = ["Zo","Ma", "Di", "Wo", "Do", "Vr","Za"]
	monthnames = ["Jan", "Feb", "Mrt", "Apr", "Mei", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dec"]
	
	schoolvacations = [(2,18),(2,19),(2,20),(2,21),(2,22),(2,23),(2,24),(2,25),(2,26),(5,22),(5,23),(5,24),(5,25),(5,26),(5,27),(5,28),(5,29),(5,30)]
	holydays = []



	def __init__(self, year=2017):
		self.year = year
		self.dwg = svgwrite.Drawing('test.svg', profile='full')

	def months(self, start_year):
		start = datetime(start_year, 1, 1)
		end = datetime(start_year+1, 1,1) - relativedelta(days=1)
		return [(d.month, d.year, d.day) for d in rrule(DAILY, dtstart=start, until=end)]

	def makeittree(self, alist):
		temp = {}
		for x in alist:

			damm = date(x[1], x[0], x[2])

			if x[1] not in temp:
				temp.update({x[1]:{}})
			
			if x[0] not in temp[x[1]]:
				temp[x[1]].update({x[0]:{'days':{}, 'name':int(damm.strftime("%m"))}})

			if x[2] not in temp[x[1]][x[0]]['days']:
				temp[x[1]][x[0]]['days'].update({x[2]:int(damm.strftime("%w"))})

		return temp

	def makefooter(self):
		pass

	def makeheader(self, months):
		possi = 0
		counter = 0
		for monthkey, monthvalue in months.items():
			if counter % 3 == 0:
				possi += self.colhormarginn
			self.makeheadersquare("test", possi)

			counter += 1
			possi += self.colwidth + self.colhormarginn

	def makeheadersquare(self, text ,possi):
		headersquare = svgwrite.shapes.Rect((possi, -40), (self.colwidth,30), stroke='red')
		self.dwg.add(headersquare)
		headersquare.fill('white', opacity=0.0)

	def makemain(self):
		possi = 0
		counter = 0
		for yearkey, yearvalue in self.makeittree( self.months(2018)).items():

			text_style = "font-size:%ipx; font-family:%s" % (10, "Courier New") 
		 	self.dwg.add(self.dwg.text(yearkey , insert=(0, -10), fill="rgb(255,0,255)", style=text_style))

			for monthkey, monthvalue in yearvalue.items():
				if counter % 3 == 0:
					possi += self.colhormarginn
				self.makecolumn(monthvalue['name'], monthvalue['days'], possi)
				counter += 1
				possi += self.colwidth + self.colhormarginn
			
			self.makeheader(yearvalue)


		self.dwg.save()

		

	def makecolumn(self, monthindex, days, position):


		text_style = "font-size:%ipx; font-family:%s" % (5, "Courier New") 

		self.dwg.add(self.dwg.text(self.monthnames[monthindex-1], insert=(position, -3), fill="rgb(255,0,255)", style=text_style))
		
		possi = 0
		for dayskey, daysvalue in days.items():

			possi += 10

			# self.dwg.add(self.dwg.line((position, possi),(self.colwidth + position, possi), stroke='red'))
			
			if (daysvalue in [0,6]):
				self.dwg.add(svgwrite.shapes.Rect((position, possi), (self.colwidth,10), fill='rgb(100,255,100)'))
			
			if (monthindex, dayskey) in self.schoolvacations:
				self.dwg.add(svgwrite.shapes.Rect((position, possi), (self.colwidth/5,10), fill='rgb(255,100,100)'))

			

			text_style = "font-size:%ipx; font-family:%s" % (4, "Courier New") 
			self.dwg.add(self.dwg.text(self.weekdaynames[daysvalue] + " " + str(dayskey) , insert=(position + 3, possi - 3), fill="rgb(255,0,255)", style=text_style))
		 	
 			somecolumn = svgwrite.shapes.Rect((position, 0), (self.colwidth,320), stroke='red')
			self.dwg.add(somecolumn)
			somecolumn.fill('white', opacity=0.0)

		possi = 0
		for dayskey, daysvalue in days.items():
			possi += 10
			self.dwg.add(self.dwg.line((position, possi),(self.colwidth + position, possi), stroke='red'))


	def makeother(self):
		pass

	def setlinecolor(self):
		pass

	def setlinewidth(self):
		pass

	def setmargins(self,width, height):
		pass

	def setfootertext(self, texts, size, color):
		pass

	def addfootertext(self, texttoadd):
		pass

	def setheadertext(self, texts, size, color):
		pass	

	def addheadertext(self, texts):
		pass

	def settextcolor(self, color):
		pass

	def sethearpicture(self, pictures, maxsize):
		pass

	def addheaderpictures(self, picture):
		pass

	def setfooterpictures(self, pictures, maxsize):
		pass

	def addfooterpictures(self):
		pass

	def addlogo(self, picture, maxsize):
		pass

if __name__ == "__main__":
	kalendar = Kalender()
	kalendar.makemain()