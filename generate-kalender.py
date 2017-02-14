#!/usr/bin/python

# functions:
# makecolumn, makeleftbody, makerightbody, makeheader, makefooter, makemain

from dateutil.rrule import rrule, DAILY
from datetime import datetime, date
import svgwrite
from dateutil.relativedelta import relativedelta
from yaml import load

class Kalender:
	linecolor = (0,0,0)
	textcolor = (0,0,0)
	linewidth = 1
	colwidth = 59.33
	colheight = 355
	footerheight = 40
	lineheight = 11.3
	headerheight = 40
	colhormarginn = 5
	year = 2017
	weekendcolor = {0:(150,255,150),6:(150,255,150)}
	holydaycolor = (255,150,150)
	headerpictures = [("name", 10),("more-name",10)]
	footerpictures = []
	monthtextsize = 10
	headertextsize = 10
	footertextsize = 4
	headertexttype = "Courier New"
	footertexttype = "Courier New"
	totalwidth = 0
	totalheight = 0

	headertexts = []
	headerlogo = ("name", 10)
	weekdaynames = ["Zo","Ma", "Di", "Wo", "Do", "Vr","Za"]
	monthnames = ["Jan", "Feb", "Mrt", "Apr", "Mei", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dec"]
	calendartitle = "Test title"
	
	headertexts = [["noot","aap","koei"],["nog iets", "en dan nog"],[],[],[],[],[],[],[],[],[],[],[],[]]
	footertexts = [["Aap:", "Noot:", "Mies:"], ["test if empty","image thing"], [],[], [], [], [], ["iets", "nog iets", "testings"],[],[],[],[],[]]
	imagesfooter = ["Nature/Yellow Rapeseed Field/shutterstock_76386769.jpg","","","","","","","","","","",""]
	imagesheader = ["Nature/BeautifulSunset/shutterstock_18465994.jpg","","","","","","","","","","","",""]

	schoolvacations = [(2,18),(2,19),(2,20),(2,21),(2,22),(2,23),(2,24),(2,25),(2,26),(5,22),(5,23),(5,24),(5,25),(5,26),(5,27),(5,28),(5,29),(5,30)]
	holydays = [(3,24),(3,25),(3,26)]



	def __init__(self, yamlcont):
		
		allvars = load(yamlcont)
		self.textcolor = tuple(allvars['textcolor'])
		self.linecolor = tuple(allvars['linecolor'])
		self.monthnames = allvars['monthnames']
		self.year = allvars['year']
		self.weekdaynames = allvars['weekdaynames']
		self.weekendcolor = allvars['weekendcolor']
		self.colheight = allvars['colheight']
		self.colhormarginn = allvars['colhormarginn']
		self.holydaycolor = allvars['holydaycolor']
		self.schoolvacationscolor = allvars['schoolvacationscolor']
		self.headerheight = allvars['headerheight']
		self.headerheight = allvars['headerheight']
		self.calendarfoottext = allvars['calendarfoottext']
		self.linewidth = allvars['linewidth']
		self.fontsizecol = allvars['fontsizecol']
		self.fonttypecol = allvars['fonttypecol']
		self.fonttypemodify = allvars['fonttypemodify']
		self.fonttypecolweekend = allvars['fonttypecolweekend']
		self.calendartitle = allvars['calendartitle']

		self.headertextsize = allvars['headertextsize']
		self.footertextsize = allvars['footertextsize']
		self.headertexttype = allvars['headertexttype']
		self.footertexttype = allvars['footertexttype']
		# self.schoolvacations = allvars['schoolvacations']
		# self.holydays = allvars['holydays']
		self.dwg1 = svgwrite.Drawing('test-front.svg', profile='full')
		self.dwg2 = svgwrite.Drawing('test-back.svg', profile='full')

		self.lineheight = self.colheight / float(31)
		# self.addBGgradient()

		self.background = allvars['background']

	def months_first(self, start_year):
		start = datetime(start_year, 1, 1)
		end = datetime(start_year, 7,1) - relativedelta(days=1)
		return [(d.month, d.year, d.day) for d in rrule(DAILY, dtstart=start, until=end)]

	def months_second(self, start_year):
		start = datetime(start_year, 7, 1)
		end = datetime(start_year, 12,1) - relativedelta(days=1) + relativedelta(months=1)
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

	def makefooter(self, months, drawing, startnum):
		possi = 5
		counter = 1
		indexcounter = startnum
		for monthkey, monthvalue in months.items():

			if counter % 3 == 0:
				self.makefootersquare(self.footertexts[indexcounter],self.imagesfooter[indexcounter], possi, drawing)
				possi += (self.colwidth) + (self.colhormarginn * 2)
				indexcounter += 1
			else:
				self.makefootersquare(self.footertexts[indexcounter],self.imagesfooter[indexcounter], possi, drawing)
				possi += (self.colwidth) + (self.colhormarginn)
				indexcounter += 1
			counter += 1
			
			# if counter % 3 == 0:
			# 	self.makefootersquare(self.footertexts[indexcounter],self.imagesfooter[indexcounter], possi, drawing)
			# 	possi += (self.colwidth * 1.5) + (self.colhormarginn * 2)
			# 	indexcounter += 1
			# 	self.makefootersquare(self.footertexts[indexcounter], self.imagesfooter[indexcounter], possi, drawing)
			# 	possi += (self.colwidth * 1.5) + (self.colhormarginn * 2)
			# 	indexcounter += 1
			# counter += 1

	def makefootersquare(self, texts, image, possi, drawing):


		if image is not "":
			imgobj = drawing.image(image , (possi, self.colheight + 10), (self.colwidth ,self.footerheight))
			# print dir(imgobj)
			print imgobj.attribs
			imgobj.stretch()
			drawing.add(imgobj)

		if image is "" and len(texts) > 0:
			drawing.add(svgwrite.shapes.Rect((possi, self.colheight + 10), (self.colwidth ,self.footerheight), fill="white"))
		
		footersquare = svgwrite.shapes.Rect((possi, self.colheight + 10), (self.colwidth ,self.footerheight), stroke=self.tupcolortostring(self.linecolor))

		drawing.add(footersquare)
		footersquare.fill('white', opacity=0.0)
		height = 0

		

		text_style = "font-size:%ipx; font-family:%s" % (6, "Courier New") 
		for text in texts:
			drawing.add(self.dwg1.text(text , insert=(possi + 2, self.colheight + 16 + height), fill=self.tupcolortostring(self.textcolor), style=text_style))
			height += 6

	def makeheader(self, months, drawing, startnum):
		possi = 0
		counter = 0
		indexcounter = startnum

		for monthkey, monthvalue in months.items():
			
			# print monthvalue
			# print months.items().index((monthkey, monthvalue)), monthkey
			if counter % 3 == 0:
				possi += self.colhormarginn

			self.makeheadersquare(possi,self.imagesheader[indexcounter], drawing, self.headertexts[indexcounter])
			indexcounter += 1
			counter += 1
			possi += self.colwidth + self.colhormarginn

	def makeheadersquare(self, possi,image, drawing, texts):
		
		if image is not "":
			imgobj = drawing.image(image , (possi, -(self.headerheight + 10)), (self.colwidth ,self.footerheight))
			imgobj.stretch()
			drawing.add(imgobj)

		if image is "" and len(texts) > 0:
			drawing.add(svgwrite.shapes.Rect((possi, -(self.headerheight + 10)), (self.colwidth ,self.footerheight), fill="white"))

		headersquare = svgwrite.shapes.Rect((possi, -(self.headerheight + 10)), (self.colwidth, self.headerheight), stroke=self.tupcolortostring(self.linecolor))
		drawing.add(headersquare)
		headersquare.fill('white', opacity=0.0)

		height = 0
		text_style = "font-size:%ipx; font-family:%s" % (6, "Courier New") 
		for text in texts:
			drawing.add(self.dwg1.text(text , insert=(possi + 2, -(self.headerheight + 4) + height), fill=self.tupcolortostring(self.textcolor), style=text_style))
			height += 6

	def addBGgradient(self):
		diagonal_gradient = self.dwg1.linearGradient(self.background['startpos'], self.background['endpos'])
		self.dwg1.defs.add(diagonal_gradient)
		self.dwg2.defs.add(diagonal_gradient)
		diagonal_gradient.add_stop_color(0, self.tupcolortostring(self.background['startcolor']))
		diagonal_gradient.add_stop_color(1, self.tupcolortostring(self.background['endcolor']))
		return diagonal_gradient.get_paint_server()

	def makemain(self):
		possi = 0
		counter = 0

		monthcount = len(self.makeittree( self.months_first(self.year))[self.year])
		backgroundwidth = ((self.colwidth + self.colhormarginn) * monthcount + (2 * self.colhormarginn))

		self.dwg1.add(svgwrite.shapes.Rect((self.colhormarginn-5, -(self.headerheight + self.colhormarginn + 26)), (backgroundwidth, self.colheight + self.footerheight + self.headerheight + 50 ), fill=self.addBGgradient()))

		self.dwg2.add(svgwrite.shapes.Rect((self.colhormarginn-5, -(self.headerheight + self.colhormarginn + 26)), (backgroundwidth, self.colheight + self.footerheight + self.headerheight + 50 ), fill=self.addBGgradient()))

		text_style = "font-size:%ipx; font-family:%s" % (self.headertextsize, self.headertexttype) 
		headertext = self.dwg1.text(self.calendartitle , insert=(self.colhormarginn, -60), fill=self.tupcolortostring(self.textcolor), style=text_style)
		self.dwg1.add(headertext)
		self.dwg2.add(headertext)

		text_style = "font-size:%ipx; font-family:%s" % (self.footertextsize, self.footertexttype) 
		footertexr = self.dwg1.text(self.calendarfoottext , insert=(self.colhormarginn, self.colheight + self.footerheight + self.headerheight - 25), fill=self.tupcolortostring(self.textcolor), style=text_style)
		self.dwg1.add(footertexr)
		self.dwg2.add(footertexr)



		for yearkey, yearvalue in self.makeittree( self.months_second(self.year)).items():

			for monthkey, monthvalue in yearvalue.items():
				if counter % 3 == 0:
					possi += self.colhormarginn
				self.makecolumn(monthvalue['name'], monthvalue['days'], possi, self.dwg2)
				counter += 1
				possi += self.colwidth + self.colhormarginn
				self.totalwidth += self.colwidth + self.colhormarginn

			self.makeheader(yearvalue, self.dwg2, 0)
			self.makefooter(yearvalue, self.dwg2, 0)

		self.totalheight += self.colheight

		possi = 0
		counter = 0
		for yearkey, yearvalue in self.makeittree( self.months_first(self.year)).items():

			for monthkey, monthvalue in yearvalue.items():
				if counter % 3 == 0:
					possi += self.colhormarginn
				self.makecolumn(monthvalue['name'], monthvalue['days'], possi, self.dwg1)
				counter += 1
				possi += self.colwidth + self.colhormarginn
			
			self.makeheader(yearvalue, self.dwg1, 0)
			self.makefooter(yearvalue, self.dwg1, 0)
			

		self.dwg1.save()
		self.dwg2.save()

		print "totwidth:" + str(self.totalwidth) + " totheight:" + str(self.totalheight) + " ratio:" + str(self.totalwidth / self.totalheight)
		

	def makecolumn(self, monthindex, days, position, drawing):


		text_style = "font-size:%ipx; font-family:%s" % (5, "Courier New") 

		drawing.add(drawing.text( self.monthnames[monthindex-1] + "  " +str(self.year), insert=(position, -3), fill=self.tupcolortostring(self.textcolor), style=text_style))
		
		possi = 0

		somecolumn = svgwrite.shapes.Rect((position, 0), (self.colwidth,self.colheight), stroke=self.tupcolortostring(self.linecolor))
		drawing.add(somecolumn)
		somecolumn.fill('white', opacity=1)

		for dayskey, daysvalue in days.items():
			
			if (daysvalue in [0,6]):
				drawing.add(svgwrite.shapes.Rect((position, possi), (self.colwidth,self.lineheight), fill=self.tupcolortostring(self.weekendcolor[daysvalue])))
			possi += self.lineheight

			if (daysvalue not in [0,6]):
				text_style = "font-size:%ipx; font-family:%s" % (self.fontsizecol, self.fonttypecol)
			else:
				text_style = "font-size:%ipx; font-family:%s; font-weight: bold;" % (self.fontsizecol, self.fonttypecol)
			drawing.add(drawing.text(self.weekdaynames[daysvalue] + " " + str(dayskey) , insert=(position + 3, possi - (self.lineheight/float(2.6))), fill=self.tupcolortostring(self.textcolor), style=text_style))
		 	
		possi = 0
		for dayskey, daysvalue in days.items():
			possi += self.lineheight

			if (monthindex, dayskey) in self.schoolvacations:
				drawing.add(svgwrite.shapes.Rect((position + ((self.colwidth/5)*4), possi), (self.colwidth/5,self.lineheight), fill=self.tupcolortostring(self.schoolvacationscolor)))

			if (monthindex, dayskey) in self.holydays:
				drawing.add(svgwrite.shapes.Rect((position + ((self.colwidth/5)*4), possi), (self.colwidth/5,self.lineheight), fill=self.tupcolortostring(self.holydaycolor)))

		possi = 0
		for dayskey, daysvalue in days.items()[:-1]:
			possi += self.lineheight
			drawing.add(drawing.line((position, possi),(self.colwidth + position, possi), stroke=self.tupcolortostring(self.linecolor)))

	

		somecolumn = svgwrite.shapes.Rect((position, 0), (self.colwidth,self.colheight), stroke=self.tupcolortostring(self.linecolor))
		drawing.add(somecolumn)
		somecolumn.fill('white', opacity=0)

	def tupcolortostring(self, colortup):
		return 'rgb(' + str(colortup[0]) + ',' + str(colortup[1]) + ',' + str(colortup[2]) + ')'

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
	f = open('design.yaml', 'r')
	contents = f.read()
	kalendar = Kalender(contents)
	kalendar.makemain()