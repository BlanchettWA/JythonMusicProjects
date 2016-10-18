from midi import *
from gui import *
from music import *

device = MidiIn()
settingsWindow = Display("Trikora Settings",600,500)

dispX = input("How wide should the graphic display be")
dispY = input("How tall should the graphic display be?")

graphicDisplay = Display("Trikora Visualizer",dispX,dispY)

titleFonts = Font("Serif", Font.ITALIC, 16)
settingsWindow.drawLabel("Part Z",0,0,Color.BLACK,titleFonts)
settingsWindow.drawLine(50,10,500,10,Color.RED,3)
settingsWindow.drawLabel("Part I",0,100,Color.BLACK,titleFonts)
settingsWindow.drawLine(50,110,500,110,Color.GREEN,3)
settingsWindow.drawLabel("Part II",0,200,Color.BLACK,titleFonts)
settingsWindow.drawLine(50,210,500,210,Color.BLUE,3)

#Violin, Ice Rain, and Bass. Create the instrument variables
#for the parts and set them to a default. This is so they can be
#easily referenced later. 
c0Instrument = 40
c0InstrumentLabel = Label("Sound #" + str(c0Instrument) + "      ")
Play.setInstrument(40,0)
c1Instrument = 96
c1InstrumentLabel = Label("Sound #" + str(c1Instrument) + "       ")
Play.setInstrument(96,1)
c2Instrument = 33
c2InstrumentLabel = Label("Sound #" + str(c2Instrument) + "         ")
Play.setInstrument(33,2)

mappedRed = mapValue(c0Instrument,0,127,0,255)
mappedGreen = mapValue(c1Instrument,0,127,0,255)
mappedBlue = mapValue(c2Instrument,0,127,0,255)

graphicDisplay.setColor(Color(mappedRed,mappedGreen,mappedBlue))

#Create all the modifier variables that will be used later
c0Volume = 80
Play.setVolume(80,0)
c0VolumeLabel = Label("Volume: " + str(int((c0Volume/127.0)*100)) + "%        ")
c1Volume = 80
Play.setVolume(80,1)
c1VolumeLabel = Label("Volume: " + str(int((c1Volume/127.0)*100)) + "%         ")
c2Volume = 80
Play.setVolume(80,2)
c2VolumeLabel = Label("Volume: " + str(int((c2Volume/127.0)*100)) + "%         ")
c0Detune = 0
c0DetuneLabel = Label("Detune:  " + str(c0Detune) + "         ")
c1Detune = 0
c1DetuneLabel = Label("Detune:  " + str(c1Detune) + "         ")
c2Detune = 0
c2DetuneLabel = Label("Detune:  " + str(c2Detune) + "         ")

#Create functions and sliders to facilite the changing of the channel volume
def adjc0Vol(v):
   global c0Volume,c0VolumeLabel
   c0Volume = v
   Play.setVolume(c0Volume,0)
   c0VolumeLabel.setText("Volume: " + str(int((c0Volume/127.0)*100)) + "%")
   
def adjc1Vol(v):
   global c1Volume,c1VolumeLabel
   c1Volume = v
   Play.setVolume(c1Volume,1)
   c1VolumeLabel.setText("Volume: " + str(int((c1Volume/127.0)*100)) + "%")
   
def adjc2Vol(v):
   global c2Volume,c2VolumeLabel
   c2Volume = v
   Play.setVolume(c2Volume,2)
   c2VolumeLabel.setText("Volume: " + str(int((c2Volume/127.0)*100)) + "%")
   
c0VolumeSlider = Slider(HORIZONTAL,0,127,80,adjc0Vol)
c1VolumeSlider = Slider(HORIZONTAL,0,127,80,adjc1Vol)
c2VolumeSlider = Slider(HORIZONTAL,0,127,80,adjc2Vol)

settingsWindow.add(c0VolumeSlider,0,25)
settingsWindow.add(c0VolumeLabel,75,50)
settingsWindow.add(c1VolumeSlider,0,125)
settingsWindow.add(c1VolumeLabel,75,150)
settingsWindow.add(c2VolumeSlider,0,225)
settingsWindow.add(c2VolumeLabel,75,250)
#Create functions and sliders to change the channel detune
def adjc0Detune(d):
   global c0Detune,c0DetuneLabel
   c0Detune = d
   Play.setPitchBend(c0Detune,0)
   c0DetuneLabel.setText("Detune: " + str(c0Detune))

def adjc1Detune(d):
   global c1Detune,c1DetuneLabel
   c1Detune = d
   Play.setPitchBend(c1Detune,1)
   c1DetuneLabel.setText("Detune: " + str(c1Detune))

def adjc2Detune(d):
   global c2Detune,c2DetuneLabel
   c2Detune = d
   Play.setPitchBend(c2Detune,2)
   c2DetuneLabel.setText("Detune: " + str(c2Detune))

c0DetuneSlider = Slider(HORIZONTAL,-8192,8192,0,adjc0Detune)
c1DetuneSlider = Slider(HORIZONTAL,-8192,8192,0,adjc1Detune)
c2DetuneSlider = Slider(HORIZONTAL,-8192,8192,0,adjc2Detune)

settingsWindow.add(c0DetuneSlider,220,25)
settingsWindow.add(c0DetuneLabel,295,50)
settingsWindow.add(c1DetuneSlider,220,125)
settingsWindow.add(c1DetuneLabel,295,150)
settingsWindow.add(c2DetuneSlider,220,225)
settingsWindow.add(c2DetuneLabel,295,250)

def adjc0Instrument(ins):
   global c0Instrument,c0InstrumentLabel
   c0Instrument = ins
   mappedRed = mapValue(c0Instrument,0,127,0,255)
   graphicDisplay.setColor(Color(mappedRed,mappedGreen,mappedBlue))
   Play.setInstrument(c0Instrument,0)
   c0InstrumentLabel.setText("Sound #" + str(c0Instrument))

def adjc1Instrument(ins):
   global c1Instrument,c1InstrumentLabel
   c1Instrument = ins
   mappedGreen = mapValue(c1Instrument,0,127,0,255)
   graphicDisplay.setColor(Color(mappedRed,mappedGreen,mappedBlue))
   Play.setInstrument(c0Instrument,1)
   c1InstrumentLabel.setText("Sound #" + str(c1Instrument))

def adjc2Instrument(ins):
   global c2Instrument,c2InstrumentLabel
   c2Instrument = ins
   mappedBlue = mapValue(c2Instrument,0,127,0,255)
   graphicDisplay.setColor(Color(mappedRed,mappedGreen,mappedBlue))
   Play.setInstrument(c2Instrument,2)
   c2InstrumentLabel.setText("Sound #" + str(c2Instrument))

c0InstrumentSlider = Slider(HORIZONTAL,0,127,40,adjc0Instrument)
c1InstrumentSlider = Slider(HORIZONTAL,0,127,96,adjc1Instrument)
c2InstrumentSlider = Slider(HORIZONTAL,0,127,33,adjc2Instrument)

settingsWindow.add(c0InstrumentSlider,10,70)
settingsWindow.add(c0InstrumentLabel,220,70)

settingsWindow.add(c1InstrumentSlider,10,170)
settingsWindow.add(c1InstrumentLabel,220,170)

settingsWindow.add(c2InstrumentSlider,10,270)
settingsWindow.add(c2InstrumentLabel,220,270)



positionX = 0

addingList = []



def keyboardDown(te,channel,pitch,velocity):
   global graphicDisplay,positionX,dispY,dispX,mappedRed,mappedGreen,mappedBlue
   Play.noteOn(pitch,velocity,0)
   Play.noteOn(pitch,velocity,2)
   Play.noteOn(pitch,velocity,1)
   
   dropSize = mapValue(velocity,0,127,0,(dispX/10))
   addedsizes = 1
   targetRed = 255- mappedRed
   targetGreen = 255- mappedGreen
   targetBlue = 255 - mappedBlue
   while addedsizes < dropSize:
      
      cir = Circle(positionX,(dispY - mapValue(pitch,0,127,0,dispY)),addedsizes,Color(int((addedsizes/dropSize*1.0)*targetRed),int((addedsizes/dropSize*1.0)*targetGreen),int((addedsizes/dropSize*1.0)*targetBlue)),False,2)
      graphicDisplay.add(cir)
      addingList.append(cir)
      addedsizes += 4
      
   
   positionX = positionX + dropSize
   if positionX > dispX:
      positionX = 0
   

def keyboardUp(te,channel,pitch,velocity):
   global graphicDisplay,addingList
   Play.noteOff(pitch,0)
   Play.noteOff(pitch,2)
   Play.noteOff(pitch,1)
   numwork = len(addingList)
   icount = 1
   for mark in addingList:
      mark.setColor(colorGradient(mark.getColor(),graphicDisplay.getColor(),(numwork+2))[icount])
      if mark.getColor() == graphicDisplay.getColor():
         addingList.remove(mark)
      icount += 1    
   

device.onNoteOn(keyboardDown)
device.onNoteOff(keyboardUp)








