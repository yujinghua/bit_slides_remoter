# bit_slides_remoter
## Say Hello
This is a project of a customized slides remoter by using BBC Micro:bit. Enjoy the freedom !
## Current Versions
So far, there are versions as follows.
So far, there are versions as follows.

|   | Common Slides Files | HTML Slides |
| - | ------------------- | ----------- |
|#1 Button| x | x |
|#2 Gestures (X & Y accelerate meter)| x | TODO|
|#3 Both C#1 & C#2| x | TODO |
|#4 ... TODO|  |  |

## User Guideline 
Here is the DIY guideline for this Micro:bit Slides Remoter.
(Only tested on MAC. 
Tests on other OS -> TODO)

### Prepare Mirco:bit
1) Buy the HW:
BBC Micro:bit with necessary accessories (batteries, cables, cool case)
More details in https://microbit.org .
2) Download 'microbit-SlidesRemoter.hex' into your Micro:bit.
3) Done !

### Prepare your slides
There are two options here.
#### O#1 HTML Slides
You can create a HTML slides by using jupyter lab/notebook. One example is in ‘webbtExamples'
1) Create a new .ipynb file
2) In order to connect it to Mirco:bit via web bluetooth, add a button with Markdown context in the first cell  as follows:

<img src="/fig/cell_code.png" width="400" height="40" alt="cell code"/>

3) Design your slides in the following cells
4) Export Notebook As … -> Export Notebook as Reveal.js Slides
5) Put ‘btnWebbt.js’ and your exported html file into the same path
6) Done !
#### O#2 Common Slides
1) Prepare your slides as usual

### Control it!
#### O#1 HTML Slides
1) Open your slides with the browser which supports web bluetooth (e.g. Google Chroma. More refers to: https://github.com/WebBluetoothCG/web-bluetooth/blob/master/implementation-status.md)
2) Click the ‘Connect’ button, connect Micro:bit and start to use !

#### O#2 Common Slides
1) Run commands in terminal, e.g. :
python3 btnCtrl.py
(Run different .py files according to the chosen controlling type)
Some python packages you may need to support the program, including pyautogui and bleak.
2) Start to show your slides and control it.

### Control type
1) Via button
button A -> previous slide
button B -> next slide

2) Via Gestures
(Face the Micro:bit’ LED side to you)
shake along x axis to the right side -> previous slide
shake alone y axis to the down side -> next slide

## Micro:bit Programming Details for Developer
1) Open ‘makecode’ https://makecode.microbit.org/ by (e.g.) Google Chrome
2) Create a new project (My Projects -> ＋ New Projects)
3) Configure the project as follows:
Gear wheel -> Project Settings -> No Pairing Required: Anyone can connect via Bluetooth.
Gear wheel -> Extensions -> enable ‘bluetooth' (which will disable the ‘radio' module)
4) Draw your codes as below
5) Connect micro:bit via USB to download codes or download .hex file and drag it into micro:bit

<img src="/fig/bit_code.png" width="350" height="190" alt="cell code"/>

