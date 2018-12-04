from gameManagement import *
from screenManagement import *
from testScreen import *
from dice import *
from winScreen import *


def setup():
    fullScreen()
    print(width,height)
    frameRate(35)
    noStroke()
    textAlign(CENTER,CENTER)
    game = Game()
    map1 = clickableMap(0.3*width,0.1*height,0.75 * min(width,height),0.75 * min(width,height),'Map1', 5)
    typer = textInput(300,100,1000,100,'textIn1')
    testScreen = Screen('testScreen')
    screenManager.addScreen(testScreen)
    testScreen.addItem(linkButton(10,10,100,100,'linkButton1','winScreen',screenManager, tString = 'Go to winScreen'))
    testScreen.addItem(textBox(0,0,width,100,'textBox1', 'Map', 50))
    testScreen.addItem(funButton(0.2*width,0.4*height,100,100,'val+',map1.incSize,1,tString='+'))
    testScreen.addItem(funButton(0.2*width,0.6*height,100,100,'val-',map1.decSize,1,tString='-'))
    testScreen.addItem(map1)
    testScreen.addItem(colourPicker(1300,300,100,100,'desertPicker','#DAA33A'))
    testScreen.addItem(colourPicker(1600,300,100,100,'forestPicker','#8CA74D'))
    testScreen.addItem(colourPicker(1300,500,100,100,'highlandPicker','#C02823'))
    testScreen.addItem(colourPicker(1600,500,100,100,'mountainPicker','#F0E5B4'))
    testScreen.addItem(colourPicker(1300,700,100,100,'swampPicker','#3D342D'))
    testScreen.addItem(colourPicker(1600,700,100,100,'waterPicker','#4A8EA5'))

    testScreen2 = Screen('testScreen2')
    screenManager.addScreen(testScreen2)
    testScreen2.addItem(linkButton(10,10,100,100,'linkButton2','testScreen',screenManager, tString = 'Go to Screen 1'))
    testScreen2.addItem(textBox(300,300,1000,1000,'textBox2', 'Screen 2', 100))
    testScreen2.addItem(typer)
    dice1 = dice(200,500,100,100,'dice1',1)
    dice2 = dice(300,500,100,100,'dice2',2)
    dice3 = dice(400,500,100,100,'dice3',3)
    dice4 = dice(500,500,100,100,'dice4',4)
    dice5 = dice(600,500,100,100,'dice5',5)
    dice6 = dice(700,500,100,100,'dice6',6)
    dice7 = dice(200,300,100,100,'dice7',1)
    dice8 = dice(300,300,100,100,'dice8',2)
    dice9 = dice(400,300,100,100,'dice9',3)
    dice10 = dice(500,300,100,100,'dice10',4)
    dice11 = dice(600,300,100,100,'dice11',5)
    dice12 = dice(700,300,100,100,'dice12',6)
    diceGroup1 = diceGroup(200,500,600,100,'diceGroup1',dice1,dice2,dice3,dice4,dice5,dice6)
    diceGroup2 = diceGroup(200,300,600,100,'diceGroup2',dice7,dice8,dice9,dice10,dice11,dice12)
    testScreen2.addItem(diceGroup1)
    testScreen2.addItem(diceGroup2)
    diceScreen = Screen('diceScreen')
    screenManager.addScreen(diceScreen)
    diceScreen.addItem(diceGroup1)
    diceScreen.addItem(diceGroup2)
    testScreen2.addItem(dropDown(500,500,500,50,'dropdown1','This is a dropdown menu', 'this is option 1', 'this is option 2'))
    
    winScreen = Screen("winScreen")
    screenManager.addScreen(winScreen)
    winScreen.addItem(textBox(250,100,900,100,'textBox1', 'Choose one of the following winconditions', 50))
    winScreen.addItem(textBox(350,250,500,100,'textBox1', 'last one standing', 30))
    winScreen.addItem(textBox(700,250,500,100,'textBox1', '3 castles', 30))
    winScreen.addItem(textBox(1200,250,500,100,'textBox1', 'fist conqueror wins', 30))
    winScreen.addItem(checkbox(400,300,50,25,"last one standing",False,"default"))
    winScreen.addItem(checkbox(800,300,50,25,"3 castles",False,"3caslte"))
    winScreen.addItem(checkbox(1200,300,50,25,"first knocked out",False,"1st"))
    winScreen.addItem(linkButton(10,10,100,100,'linkButton1','testScreen',screenManager, tString='Go to Map'))
    winScreen.addItem(linkButton(10,120,100,100,'linkButton2','battleSim',screenManager, tString='Go to Battle'))
    winScreen.addItem(textBox(250,400,3000,1000,'`textBox1', 'TEST', 30))
    winScreen.addItem(linkButton(250,400,120,50,'testWin','winScreen2',screenManager))
    winScreen2 = Screen('winScreen2')
    screenManager.addScreen(winScreen2)
    winScreen2.addItem(textBox(200,250,1000,500,'winText','Winner Winner Chicken Dinner',100,tColor = '17325547'))
    winScreen2.addItem(textBox(200,450,1000,500,'winText',player+' won',30,tColor = '17325547'))
    # winScreen2.addItem(textBox(500,500,100,100,'winText','restart',100,tColor = '17325547'))


    startScreen = Screen('startScreen')
    screenManager.addScreen(startScreen)
    startScreen.addItem(img(width/2 - 250,height/2 - 400,500,600,'logo',imgUrl = 'data\Logo.png'))
    startScreen.addItem(linkButton(width/2-50,height - 140,100,50,'startToSetting','settingScreen',screenManager,tString = 'Start'))
    screenManager.currentScreen = startScreen


    settingScreen = Screen('settingScreen')
    screenManager.addScreen(settingScreen)
    settingScreen.addItem(textBox(500,500,300,30,'AmountOfPlayersText', 'Amount of Players:',20))
    settingScreen.addItem(amountInput(850,500,30,30,'AmountOfplayersInput'))
    settingScreen.addItem(linkButton(width/2-50,height - 140,100,50,'settingToTest','testScreen',screenManager,tString = 'Start'))
    # settingScreen.additem(funButton())

    battleSimScreen = Screen('battleSim')
    screenManager.addScreen(battleSimScreen)
    testScreen.addItem(linkButton(10,230,100,100,'battleSimScreen','battleSim',screenManager,tString = 'Battle Simulator'))
    battleSimScreen.addItem(linkButton(10,10,100,100,'linkButton2','testScreen',screenManager, tString = 'Go to Map'))
    # battleSimScreen.addItem(linkButton(10,120,100,100,'diceScreen','diceScreen',screenManager, tString = 'Go to Dice'))
    battleSimScreen.addItem(textBox(760,10,400,200,'title', 'Battle Simulator', 60))
    battleSimScreen.addItem(textBox(150,300,100,100,'attacker', 'Attacker', 20))
    battleSimScreen.addItem(textInput(150,375,500,50,'attackerInput'))
    battleSimScreen.addItem(textBox(1670,300,100,100,'troops1', 'Troops', 20))
    battleSimScreen.addItem(textInput(1270,375,500,50,'troopsInput'))
    battleSimScreen.addItem(textBox(150,500,100,100,'defender', 'Defender', 20))
    battleSimScreen.addItem(textInput(150,575,500,50,'defenderInput'))
    battleSimScreen.addItem(textBox(1670,500,100,100,'troops2', 'Troops', 20))
    battleSimScreen.addItem(textInput(1270,575,500,50,'defenderInput'))
    battleSimScreen.addItem(checkbox(1670,650,20,20,'walls',0,'walls'))
    battleSimScreen.addItem(textBox(1680,645,100,24,'walls', 'Walls', 20))
    battleSimScreen.addItem(checkbox(1670,690,20,20,'tower',0,'tower'))
    battleSimScreen.addItem(textBox(1680,685,100,24,'tower', 'Tower', 20))
    battleSimScreen.addItem(checkbox(1670,730,20,20,'castle',0,'castle'))
    battleSimScreen.addItem(textBox(1680,725,100,24,'castle', 'Castle', 20))
    battleSimScreen.addItem(checkbox(1670,770,20,20,'palace',0,'palace'))
    battleSimScreen.addItem(textBox(1680,765,100,24,'palace', 'Palace', 20))
    battleSimScreen.addItem(linkButton(860,880,200,100,'rollButton','diceScreen',screenManager, tString = 'Roll'))




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
