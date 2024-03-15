#Sol pulido 
#12/07/23
#purpose of code 

from os import linesep
from cmu_graphics import *

from cmu_graphics.shape_logic import opacityTest
#background for the graphics 
app.background ='lavender'

Label("~ Mini - Me ~", 200,40, font="Didone",size=30, fill="purple")
Circle(200, 200 , 140, fill="darkRed")
Oval(200, 180, 130, 120, fill="wheat")
Oval(185,170,25,10, fill="white")
Oval(223,170,25,10, fill="white")
Circle(187, 170, 6, fill="steelBlue")
Circle(225, 170, 6, fill="steelBlue")
Circle(189, 170, 3, fill="black")
Circle(227, 170, 3, fill="black")
Line(175, 154, 199,155, fill="darkKhaki")
Line(220, 154, 240,155, fill="darkKhaki")
Line(205,180,208,199, fill ="bisque")
Line(207,199,197,199, fill ="bisque")
Oval(205, 214, 30, 15, fill="tan")
Line(217,214, 190, 215, fill="saddleBrown")
Rect(178,235, 50, 18, fill = "dimGray")
Rect(155,240, 90, 50, fill = "dimGray")
Rect(155,268, 90, 50, fill = "dimGray")
Oval(153, 275, 18, 70, fill="dimGray")
Oval(245, 275, 18, 70, fill="dimGray")
Line(200, 243, 200, 317, fill="gray")


cmu_graphics.run()






#-------------practice/exaples----------------

#square --> need key work " Rect(left , top, heigh) " 
#Rect(0,0 , 50 , 50 ,fill = "violet")

#circle --> need key work  " circle (centerX , centerY , radius , fill = "") 
#Circle(30,90, 25, fill = "brown")

#other shapes --> 
                  # oval (left , top , width , height , fill = "")
#Oval(80, 40, 40, 30, fill = "skyblue")
                  #star (centerX , centerY , radius , fill = "")
#Star(200, 350, 40, 4, fill = "lavanda")
#---------------------------------------
#practice
#Circle(300, 90, 40, fill = "gray")
#Oval(200, 20, 40, 30, fill = "green")
#Star(300, 300, 40, 10, fill = "red")
#Rect(350,0, 50, 50, fill = "yellow")
# --------------------------------------
#RegularPolygon(centerX , centerY , radius , points/sides , fill = "")) 
#RegularPolygon(250, 200, 40, 5, fill = "yellow")
#any shape polygon 
## polygon (x1 , y1 , x2 , y2 , x3 , y3, x4 , y4 , x5 , y5 , x6, y6)
#Polygon(200, 200, 200, 200,100, 90, 300, 40, 20, 200, fill = "orange")
#line(x1 , y1 , x2 , y2)
#Line(100, 300,200, 300, fill = "black" , lineWidth = 10 , dashes= True)

#for text
##Label(value,centerX , centerY , font = "", size = "", color = "")
#Label("heyy there!" , 200, 240, font = "Ariel", size = 20, bold=True)

#---------------practice----------------------
#Star(350, 200, 40, 4, fill = "white" , opacity= 60)
#Circle(100,350, 40, fill = "crimson",opacity=10)
#Circle(50,200,40, fill=gradient("lightCyan","lightSteelBlue","cyan","mediumSlateBlue"))
#Circle(50,200,40, fill=gradient("lightCyan","lightSteelBlue","cyan","mediumSlateBlue"
# Write your code here
# Not sure where to start?
# Check out README.md under "Files"

