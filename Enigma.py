import pygame

WIDTH, HEIGHT = 1100, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

pygame.display.set_caption("Enigma")
pygame.font.init()

keyLoc = {'q': [100, 'top'], 'w': [200,'top'], 'e': [300, 'top'], 'r':[400,'top'], 't':[500,'top'], 'y':[600,'top'],'u':[700,'top'],'i':[800,'top'], 'o':[900,'top'], 'p':[1000,'top']
          ,'a': [150, 'mid'], 's': [250, 'mid'], 'd':[350,'mid'], 'f':[450, 'mid'], 'g':[550,'mid'],'h':[650,'mid'],'j':[750,'mid'],'k':[850,'mid'], 'l':[950,'mid']
          ,'z':[250,'bot'],'x':[350,'bot'],'c':[450,'bot'],'v':[550,'bot'],'b':[650,'bot'],'n':[750,'bot'],'m':[850,'bot']}

#Alphabet used for indexing
abc    = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")

#Rotor
offset = -20
rotors = {'I': [WIDTH - 250, 150 + offset, False], 'II': [WIDTH - 150, 150 + offset, False], 'III': [WIDTH - 50, 150 + offset, False], 'IV': [WIDTH - 250, 235 + offset, False], 'V': [WIDTH - 150, 235 + offset, False], 'VI': [WIDTH - 50, 235 + offset, False]
          , 'VII': [WIDTH - 250, 320 + offset, False], 'VIII': [WIDTH - 150, 320 + offset, False], 'Beta': [WIDTH - 50, 320 + offset, False], 'Gamma': [WIDTH - 250, 405 + offset, False]}

I      = ('E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J')
II     = ('A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E')
III    = ('B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O')
IV     = ('E', 'S', 'O', 'V', 'P', 'Z', 'J', 'A', 'Y', 'Q', 'U', 'I', 'R', 'H', 'X', 'L', 'N', 'F', 'T', 'G', 'K', 'D', 'C', 'M', 'W', 'B')
V      = ('V', 'Z', 'B', 'R', 'G', 'I', 'T', 'Y', 'U', 'P', 'S', 'D', 'N', 'H', 'L', 'X', 'A', 'W', 'M', 'J', 'Q', 'O', 'F', 'E', 'C', 'K')
VI     = ('J', 'P', 'G', 'V', 'O', 'U', 'M', 'F', 'Y', 'Q', 'B', 'E', 'N', 'H', 'Z', 'R', 'D', 'K', 'A', 'S', 'X', 'L', 'I', 'C', 'T', 'W')
VII    = ('N', 'Z', 'J', 'H', 'G', 'R', 'C', 'X', 'M', 'Y', 'S', 'W', 'B', 'O', 'U', 'F', 'A', 'I', 'V', 'L', 'P', 'E', 'K', 'Q', 'D', 'T')
VIII   = ('F', 'K', 'Q', 'H', 'T', 'L', 'X', 'O', 'C', 'B', 'J', 'S', 'P', 'D', 'Z', 'R', 'A', 'M', 'E', 'W', 'N', 'I', 'U', 'Y', 'G', 'V')
Beta   = ('L', 'E', 'Y', 'J', 'V', 'C', 'N', 'I', 'X', 'W', 'P', 'B', 'Q', 'M', 'D', 'R', 'T', 'A', 'K', 'Z', 'G', 'F', 'U', 'H', 'O', 'S')
Gamma  = ('F', 'S', 'O', 'K', 'A', 'N', 'U', 'E', 'R', 'H', 'M', 'B', 'T', 'I', 'Y', 'C', 'W', 'L', 'Q', 'P', 'Z', 'X', 'V', 'G', 'J', 'D')

#Reflector
reflectors = {'A': [WIDTH - 250, 550 + offset, False], 'B': [WIDTH - 150, 550 + offset, False], 'C': [WIDTH - 50, 550 + offset, False], 'B_Thin': [WIDTH - 250, 635 + offset, False], 'C_Thin': [WIDTH - 150, 635 + offset, False]}
A      = ('E', 'J', 'M', 'Z', 'A', 'L', 'Y', 'X', 'V', 'B', 'W', 'F', 'C', 'R', 'Q', 'U', 'O', 'N', 'T', 'S', 'P', 'I', 'K', 'H', 'G', 'D')
B      = ('Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G', 'O', 'K', 'M', 'I', 'E', 'B', 'F', 'Z', 'C', 'W', 'V', 'J', 'A', 'T')
C      = ('F', 'V', 'P', 'J', 'I', 'A', 'O', 'Y', 'E', 'D', 'R', 'Z', 'X', 'W', 'G', 'C', 'T', 'K', 'U', 'Q', 'S', 'B', 'N', 'M', 'H', 'L')
B_Thin = ('E', 'N', 'K', 'Q', 'A', 'U', 'Y', 'W', 'J', 'I', 'C', 'O', 'P', 'B', 'L', 'M', 'D', 'X', 'Z', 'V', 'F', 'T', 'H', 'R', 'G', 'S')
C_Thin = ('R', 'D', 'O', 'B', 'J', 'N', 'T', 'K', 'V', 'E', 'H', 'M', 'L', 'F', 'C', 'W', 'Z', 'A', 'X', 'G', 'Y', 'I', 'P', 'S', 'U', 'Q')

setting = [None, None, None, None]

# BG = pygame.image.load("/imgs/bg.jpeg")
## can scale with BG = pygame.transform.scale(image.load("/imgs/bg.jpeg"), (WIDTH, HEIGHT))
## documentation helps to scale with aspect ratio

Lit = False




class topKey():
    def __init__(self, x, letter, keyName, y):
        self.white = (255,255,255)
        self.yellow = (255,255,0)
        self.black = (0,0,0)
        self.myfont = pygame.font.SysFont("monospace",30)
        self.letter = letter
        self.Pos_x = x
        self.keyName = keyName
        if y == 'top':
            self.Pos_y = 400
        elif y == 'mid':
            self.Pos_y = 500
        elif y == 'bot':
            self.Pos_y = 600



        
        if letter.lower() == self.keyName.lower():
            pygame.draw.circle(WIN, self.yellow, (self.Pos_x,self.Pos_y), 30)
            label = self.myfont.render(self.letter,1,self.black)
        else:
            pygame.draw.circle(WIN, self.white, (self.Pos_x,self.Pos_y), 30,2)
            label = self.myfont.render(self.letter,1,self.white)
        WIN.blit(label,(self.Pos_x-8,self.Pos_y-16))



    def lamp(self):
        label = self.myfont.render(self.letter,1,self.black)

        if self.lit == True:
            WIN.blit(label,(self.Pos_x-8,self.Pos_y-16))
            lamp = pygame.draw.circle(WIN, self.yellow, (self.Pos_x,self.Pos_y), 30)
            
        else:
            lamp = pygame.draw.circle(WIN, self.black, (self.Pos_x,self.Pos_y), 30)
    

class cover():
    def __init__(self, colour, x, y, width, height):
        self.vel = 600
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.tick_count = 0
        self.label = pygame.font.SysFont('Corbel',25)

    def draw(self, WIN):    
        pygame.draw.rect(WIN, self.colour, (self.x,self.y, self.width, self.height), border_radius=10)
        self.text = self.label.render("Rotors", True, (0,0,0))
        WIN.blit(self.text,(WIDTH-280,60))
        self.text = self.label.render("Reflectors", True, (0,0,0))
        WIN.blit(self.text,(WIDTH-280,450))

    def move(self, Horizontal, open):
        if open == True:
            direction = 1
        else:
            direction = -1

        if Horizontal:
            self.x -= self.vel*direction
        else:
            self.y -= self.vel*direction


class button():
    def __init__(self, location):
        self.colour = (100,100,100)
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.label = pygame.font.SysFont('Corbel',35)
        self.x = location[0]
        self.y = location [1]
        self.width = location[2]
        self.height = location [3]
    
    def draw(self, WIN, dimension, buttonText, mouse):
        if dimension[0] <= mouse[0] <= dimension[0]+dimension[2] and dimension[1] <= mouse[1] <= dimension[1]+dimension[3]:
            hover = True
        else:
            hover = False


        if hover:
            pygame.draw.rect(WIN,self.colour, dimension, border_radius=10 )
        else:
            pygame.draw.rect(WIN,self.white, dimension, border_radius=10 )

        self.text = self.label.render(buttonText, True, self.black)
        WIN.blit(self.text,(dimension[0]+15,dimension[1]+5))        

    def hover(self, hover, dimension, buttonText):
        if hover == True:
            pygame.draw.rect(WIN,self.colour, dimension, border_radius=10 )
        else:
            pygame.draw.rect(WIN,self.white, dimension, border_radius=10 )

        self.text = self.label.render(buttonText, True, self.black)
        WIN.blit(self.text,(WIDTH-200,100))

class rotor():
    def __init__(self, name, location, load):
        self.colour = (100,100,100)
        self.white = (255,255,255)
        self.radius = 40
        self.name = name
        self.location = location
        self.load = load
        self.label = pygame.font.SysFont('Corbel',25)
        self.x = location[0]
        self.y = location[1]



    def drawHolder(self, WIN):
        pygame.draw.circle(WIN, self.colour, self.location, self.radius)
        
        self.text = self.label.render(self.name, True, (0,0,0))
        WIN.blit(self.text, self.text.get_rect(center = (self.location[0],self.location[1])) )


    def drawRotor(self, WIN):
        self.rotorWhite = pygame.draw.circle(WIN, self.white, (self.x, self.y), self.radius)
        self.rotorText = self.label.render(self.name, True, (0,0,0))
        WIN.blit(self.rotorText, self.text.get_rect(center = (self.x,self.y) ))


    def drag(self, event, rotorsList):
        dragFlag = False
        to_move = None

        for rotors in rotorsList:
            if rotors.rotorWhite.collidepoint(event.pos):
                to_move = rotors
                dragFlag = True
        return dragFlag, to_move
    
    def move(self, eventPos,mouse, event, rotorsList, to_move):
        offset_x = mouse[0] - eventPos[0]
        offset_y = mouse[1] - eventPos[1]

        return offset_x, offset_y




    

def draw(win, mouse, covers, open_covers, rotorButton, rotorExit, rotorClear, keyPressed, rotorsLoad, dragFlag, to_move, offset_x, offset_y, eventPos, rotorHolder):
    win.fill((0,0,0))
    
    # WIN.blit(BG, (0, 0))
    topKey(keyLoc['q'][0], "Q", keyPressed, keyLoc['q'][1])
    topKey(keyLoc['w'][0], "W", keyPressed, keyLoc['w'][1])
    topKey(keyLoc['e'][0], "E", keyPressed, keyLoc['e'][1])
    topKey(keyLoc['r'][0], "R", keyPressed, keyLoc['r'][1])
    topKey(keyLoc['t'][0], "T", keyPressed, keyLoc['t'][1])
    topKey(keyLoc['y'][0], "Y", keyPressed, keyLoc['y'][1])
    topKey(keyLoc['u'][0], "U", keyPressed, keyLoc['u'][1])
    topKey(keyLoc['i'][0], "I", keyPressed, keyLoc['i'][1])
    topKey(keyLoc['o'][0], "O", keyPressed, keyLoc['o'][1])
    topKey(keyLoc['p'][0], "P", keyPressed, keyLoc['p'][1])

    topKey(keyLoc['a'][0], "A", keyPressed, keyLoc['a'][1])
    topKey(keyLoc['s'][0], "S", keyPressed, keyLoc['s'][1])
    topKey(keyLoc['d'][0], "D", keyPressed, keyLoc['d'][1])
    topKey(keyLoc['f'][0], "F", keyPressed, keyLoc['f'][1])
    topKey(keyLoc['g'][0], "G", keyPressed, keyLoc['g'][1])
    topKey(keyLoc['h'][0], "H", keyPressed, keyLoc['h'][1])
    topKey(keyLoc['j'][0], "J", keyPressed, keyLoc['j'][1])
    topKey(keyLoc['k'][0], "K", keyPressed, keyLoc['k'][1])
    topKey(keyLoc['l'][0], "L", keyPressed, keyLoc['l'][1])

    topKey(keyLoc['z'][0], "Z", keyPressed, keyLoc['z'][1])
    topKey(keyLoc['x'][0], "X", keyPressed, keyLoc['x'][1])
    topKey(keyLoc['c'][0], "C", keyPressed, keyLoc['c'][1])
    topKey(keyLoc['v'][0], "V", keyPressed, keyLoc['v'][1])
    topKey(keyLoc['b'][0], "B", keyPressed, keyLoc['b'][1])
    topKey(keyLoc['n'][0], "N", keyPressed, keyLoc['n'][1])
    topKey(keyLoc['m'][0], "M", keyPressed, keyLoc['m'][1])
    
    
    for cover in covers:
        cover.draw(win)
    
    if open_covers == False:
        rotorButton.draw(win, (WIDTH-215,96,125,40), "Rotors", mouse)

    else:
        rotorExit.draw(win, (WIDTH-135, 676, 125, 40), "Close", mouse)
        rotorClear.draw(win, (WIDTH-285, 676, 125, 40), "Clear", mouse)

        for holders in rotorHolder:
            holders.drawHolder(win)
        
        for rotorsObj in rotorsLoad:
            rotorsObj.drawHolder(win)
            
            if rotorsObj.load:
                pass
            else:
                if rotorsObj == to_move:
                    if dragFlag:
                        rotorsObj.x = rotorsObj.x + offset_x
                        rotorsObj.y = rotorsObj.y + offset_y
                        
                    rotorsObj.x = eventPos[0]
                    rotorsObj.y = eventPos[1]

                rotorsObj.drawRotor(win)
        
        
                
                
                

    pygame.display.update()





def cover_movement(rotor_choice_open, rotor_choice, rotor_cover):
    rotor_choice.move(True, rotor_choice_open)
    rotor_cover.move(False, rotor_choice_open)


def main():
    run = True
    clock = pygame.time.Clock()

    # initial location of rotorchoice rectangle
    rotor_choice_open = False
    rotor_choice = cover("Brown", WIDTH+300, HEIGHT-750, 300, 700)
    rotor_bg = cover("Brown", 100, 50, 600, 200)
    rotor_cover = cover("Black", 100, 50, 600, 200) 

    rotorButton = button((WIDTH-215,96,125,40))
    rotorExit = button((WIDTH-135, 676, 125, 40))
    rotorClear = button((WIDTH-285, 676, 125, 40))
    
    rotorsLoad = []
    for rotorRef in rotors:
        rotorRef = rotor(rotorRef, [rotors[rotorRef][0], rotors[rotorRef][1]], rotors[rotorRef][2])
        rotorsLoad.append(rotorRef)
    
    for reflectorRef in reflectors:
        reflectorRef = rotor(reflectorRef, [reflectors[reflectorRef][0], reflectors[reflectorRef][1]], reflectors[reflectorRef][2])
        rotorsLoad.append(reflectorRef)

    rotorHolder = []
    i = 0
    for holderRef in range(4):
        holderRef = rotor(holderRef, [170 + int(holderRef)*140,150], "")
        if i == 0:
            holderRef.name = "Reflect"
        else:
            holderRef.name = str(i)
        
        rotorHolder.append(holderRef)
        i += 1


    
    keyName = ""
    keyPressed = False
    dragFlag = False
    eventPos = (0,0)
    to_move = None
    offset_x = 0
    offset_y = 0
    holderSnap = 60

    while run:
        clock.tick(FPS)
        mouse = pygame.mouse.get_pos()
        
        
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            
            if event.type == pygame.QUIT:
                run = False
                break

            # Events that check the key pressed. If a key is pressed, a second won't be read. Key's can't be pressed when the rotor cover is open. KeyUP reverses the restrictions
            elif event.type == pygame.KEYDOWN and keys.count(True) == 1 and event.key in range(97,123) and rotor_choice_open == False:
                keyName = pygame.key.name(event.key)
                keyPressed = True

            elif event.type == pygame.KEYUP and keys.count(True) == 0 and event.key in range(97,123) and rotor_choice_open == False:
                keyName = ""
                keyPressed = False

            # Event to check if the mouse clicks the button to open the rotor cover and rotor selection
            if event.type == pygame.MOUSEBUTTONDOWN and rotorButton.x <= mouse[0] <= rotorButton.x + rotorButton.width and rotorButton.y <= mouse[1] <= rotorButton.y + rotorButton.height and rotor_choice_open == False:
                rotor_choice_open = True
                cover_movement(rotor_choice_open, rotor_choice, rotor_cover)

            # Event to check if the exit button has been clicked, closing the rotor selection
            elif event.type == pygame.MOUSEBUTTONDOWN and rotorExit.x <= mouse[0] <= rotorExit.x + rotorExit.width and rotorExit.y <= mouse[1] <= rotorExit.y + rotorExit.height and rotor_choice_open == True:
                rotor_choice_open = False
                cover_movement(rotor_choice_open, rotor_choice, rotor_cover)

            # Event to check if the Clear button has been pressed. This should cycle through the list of rotors resetting their coordinates to their initial locations specified at the top    
            elif event.type == pygame.MOUSEBUTTONDOWN and rotorClear.x <= mouse[0] <= rotorClear.x + rotorClear.width and rotorClear.y <= mouse[1] <= rotorClear.y + rotorClear.height and rotor_choice_open == True:
                
                for rotorsClear in rotorsLoad:
                    print(rotorsClear.name)
                    if rotorsClear.name in rotors:
                        rotorsClear.x = rotors[rotorsClear.name][0]
                        rotorsClear.y = rotors[rotorsClear.name][1]

                    else:
                        rotorsClear.x = reflectors[rotorsClear.name][0]
                        rotorsClear.y = reflectors[rotorsClear.name][1]
                # print(rotorHolder)
                # for holderRef in rotorHolder:
                #     print(holderRef.load)
                #     setting[setting.index(holderRef.load)] = None
                #     holderRef.load = ""
                
                
                

            # The next three events are used for dragging the rotors to their locations. The mouse button down specified which rotor is moving (to_move).
            # eventPos is the location where the mouse first clicked on a rotor. This is updated on each loop of the draw to move the rotors position relative to the mouse
            # dragFlag is a check to ensure that only when a rotor is being dragged does the MOUSEMOTION and MOUSEBUTTONUP events execute 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if rotor_choice_open:
                    eventPos = mouse
                    dragFlag, to_move = rotorRef.drag(event, rotorsLoad)
                
            # this event updates teh offset from the location that the mouse is at at the start of a loop to where it ends up. The offset is what is used to update the rotors x,y coordinates
            # The eventPos updates here with each movement
            elif event.type == pygame.MOUSEMOTION:
                if dragFlag == True:
                    offset_x, offset_y = rotorRef.move(eventPos, mouse, event, rotorsLoad, to_move)
                    eventPos = mouse
            
            # The below event is significant as depending on which item is moving where, different things happen. i.e. reflectors shouldn't be dropped where rotors are placed and vice versa.
            # Reflectors/rotors shouldn't be able to be placed on top of each other
            # the dragFlag resets and the final eventPos (i.e. reflector/rotor location) is updated
            elif event.type == pygame.MOUSEBUTTONUP:
                if dragFlag == True:
                    dragFlag = False
                    eventPos = mouse

                    # The initial check on the if statement is if the rotors or reflectors have been "released" in the rotor choice window that appears on the right. If they have, then
                    # they will take their positions from the initial locations from the lists at the top 
                    if rotor_choice.x < eventPos[0] < rotor_choice.x + rotor_choice.width and rotor_choice.y < eventPos[1] < rotor_choice.y + rotor_choice.height:
                        if to_move.name in rotors:
                            eventPos = (rotors[to_move.name][0], rotors[to_move.name][1])
                            
                        else:
                            eventPos = (reflectors[to_move.name][0], reflectors[to_move.name][1])
                        
                        # Releasing the rotor back to its original holder should clear the rotor from the settings array used for the logic
                        if to_move.name in setting:
                            setting[setting.index(to_move.name)] = None
                        
                        # The rotor holders in the top box should also be cleared of which rotor was loaded onto them - <could/should this be merged with the setting array? Duplicate information>
                        for holderRef in rotorHolder:
                            if holderRef.load == to_move.name:
                                holderRef.load = None

                    # the below loop checks each location where the rotors can be loaded into
                    for holderRef in rotorHolder:
                        # If the holder is the reflector and the reflector that is being moved (to_move) is in the reflectors list and it is dropped on the reflector location (+/- a buffer), then
                            # if the holder location is empty or the holder location is registed to the reflector being moved
                                # then update the holder to the rotor being moved <could nest an if statement inside instead of the additional "or">
                                # and update the location of the to_move reflector to the holder location (snaps into place)
                                # The setting location is then updated with the moved rotor
                            # if the holder location isn't "free", then the reflector snaps back to it's original location in the choice window on the right

                        if holderRef.name == "Reflect":
                            if holderRef.x - holderRef.radius/2 - holderSnap < eventPos[0] < holderRef.x + holderRef.radius/2 + holderSnap and holderRef.y - holderRef.radius/2 - holderSnap < eventPos[1] < holderRef.y + holderRef.radius/2 + holderSnap \
                                and to_move.name in reflectors:

                                if holderRef.load == "" or holderRef.load == None or holderRef.load == to_move.name:
                                    holderRef.load = to_move.name
                                    eventPos = (holderRef.x, holderRef.y)
                                    setting[0] = to_move.name
                                    print(setting)
                                else:
                                    eventPos = (reflectors[to_move.name][0], reflectors[to_move.name][1])
                               
                            # if the rotor being moved (to_move) is a rotor and not a reflector, then move it back to the choice window
                            elif holderRef.x - holderRef.radius/2 - holderSnap < eventPos[0] < holderRef.x + holderRef.radius/2 + holderSnap and holderRef.y - holderRef.radius/2 - holderSnap < eventPos[1] < holderRef.y + holderRef.radius/2 + holderSnap \
                                and to_move.name in rotors:
                                eventPos = (rotors[to_move.name][0], rotors[to_move.name][1])




                        # If the holder isn't a reflector, then do the same checks for rotors (if the moved object is a rotor and if its an empty holder or the object is already registered)
                        elif holderRef.name != "Reflect":
                            if holderRef.x - holderRef.radius/2 - holderSnap < eventPos[0] < holderRef.x + holderRef.radius/2 + holderSnap and holderRef.y - holderRef.radius/2 - holderSnap < eventPos[1] < holderRef.y + holderRef.radius/2 + holderSnap \
                                and to_move.name in rotors:
                                
                               
                                if holderRef.load == "" or holderRef.load == None or holderRef.load == to_move.name:
                                    # As there are several holders for the rotors, this checks if the rotor is loaded elsewhere. If it is, then clear the location of the "old" holder
                                    for holderRefCheck in rotorHolder:
                                        if holderRefCheck.load == to_move.name and holderRefCheck.load != holderRef.load:
                                            holderRefCheck.load = None
                                    # update the holder load reference with the object thats been placed there
                                    holderRef.load = to_move.name
                                    # check if the moved object already exists in the settings array, if so, then clear it
                                    if to_move.name in setting:
                                        setting[setting.index(to_move.name)] = None

                                    # snap the rotor to its holder location
                                    eventPos = (holderRef.x, holderRef.y)

                                    #add the rotor ID to the setting
                                    setting[int(holderRef.name)] = to_move.name
                                    print(setting)
                                    print(holderRef.load)

                                # if the rotor holder isn't empty, then     
                                else:
                                    # check if the rotor is in another location, if it is, clear it from the load status <should the settings also be removed like above?>
                                    for holderRefCheck in rotorHolder:
                                        if holderRefCheck.load == to_move.name and holderRefCheck.load != holderRef.load:
                                            holderRefCheck.load = None

                                    # then move the rotor to its original storage
                                    eventPos = (rotors[to_move.name][0], rotors[to_move.name][1])

                            # if it a reflector being dropped into a rotor spot, then snap the reflector back to its storage in the rotor choice window on the right
                            elif holderRef.x - holderRef.radius/2 - holderSnap < eventPos[0] < holderRef.x + holderRef.radius/2 + holderSnap and holderRef.y - holderRef.radius/2 - holderSnap < eventPos[1] < holderRef.y + holderRef.radius/2 + holderSnap \
                                and to_move.name in reflectors:
                                
                                eventPos = (reflectors[to_move.name][0], reflectors[to_move.name][1])
                            
                                


        # draw all of the relevant parts <should this be split into seperate draw groups e.g. draw_rotor, draw_keys, draw_buttons etc>
        draw(WIN, mouse, [rotor_bg, rotor_choice, rotor_cover], rotor_choice_open, rotorButton, rotorExit, rotorClear, keyName, rotorsLoad, dragFlag, to_move, offset_x, offset_y, eventPos, rotorHolder)  

        #after the objects have been drawn, reset the offsets for the dragged rotors
        offset_x = 0
        offset_y = 0
        
        
        
        
        

            

    pygame.quit
        

if __name__ == "__main__":
    
    main()
