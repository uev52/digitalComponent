from gameManagement import *
from screenManagement import *
from testScreen import *
from dice import *


def setup():
    fullScreen()
    frameRate(35)
    noStroke()
    # Caladea = loadFont('Caladea-Regular-48.vlw')
    # textFont(Caladea)
    global map1
    global typer
    map1 = clickableMap(1000,300,500,500,'Map1', 5)
    typer = textInput(300,100,1000,100,'textIn1')
    testScreen = Screen('testScreen')
    screenManager.addScreen(testScreen)
    testScreen.addItem(checkbox(200,200,40,20,'checkbox1',False,'kdfs'))
    testScreen.addItem(linkButton(10,10,100,100,'linkButton1','testScreen2',screenManager))
    testScreen.addItem(textBox(10,10,100,100,'buttonTextBox', ' Goto Screen 2', 20))
    testScreen.addItem(textBox(300,300,1000,1000,'textBox1', 'Screen 1', 100))
    testScreen.addItem(textBox(300,100,1000,100,'textBox3',typer.intext.tString,20))
    testScreen.addItem(funButton(400,400,100,100,'val+',map1.incSize,1))
    testScreen.addItem(funButton(400,550,100,100,'val-',map1.decSize,1))
    map1.editTile(3,3,clickableDesert(0,0,0,0,''))
    map1.editTile(3,2,clickableSwamp(0,0,0,0,''))
    map1.editTile(1,1,clickableForest(0,0,0,0,''))
    map1.editTile(5,2,clickableMountain(0,0,0,0,''))
    map1.editTile(4,2,clickableHighland(0,0,0,0,''))
    testScreen.addItem(map1)
    screenManager.currentScreen = testScreen
    testScreen2 = Screen('testScreen2')
    screenManager.addScreen(testScreen2)
    testScreen2.addItem(linkButton(10,10,100,100,'linkButton2','testScreen',screenManager))
    testScreen2.addItem(textBox(10,10,100,100,'buttonTextBox', ' Goto Screen 1', 20))
    testScreen2.addItem(textBox(300,300,1000,1000,'textBox2', 'Screen 2', 100))
    testScreen2.addItem(typer)
    dice1 = dice(200,500,100,100,'dice1',1)
    dice2 = dice(300,500,100,100,'dice2',2)
    dice3 = dice(400, 500, 100, 100,'dice3',3)
    diceGroup1 = diceGroup(200,500,300,100,'diceGroup1',dice1,dice2,dice3)
    testScreen2.addItem(diceGroup1)
    # testScreen2.addItem(funButton(225, 650, 50, 50,'diceroll1',dice1.diceRoll))

    

    
def draw():
    #reset the background
    background(51)
    # display all items from currentScreen
    screenManager.currentScreen.display()
    
    #check if the mouse hovers over a hoverable
    screenManager.currentScreen.action('hover')
    fill(80)
    
def mouseReleased():
    # check if an item was clicked
    screenManager.currentScreen.action('click')
    
def keyTyped():
     # text input
        screenManager.currentScreen.action('keyPress')
            
