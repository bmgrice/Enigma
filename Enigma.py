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
rotors = {'I': [WIDTH - 250, 150, False], 'II': [WIDTH - 150, 150, False], 'III': [WIDTH - 50, 150, False], 'IV': [WIDTH - 250, 250, False], 'V': [WIDTH - 150, 250, False], 'VI': [WIDTH - 50, 250, False]
          , 'VII': [WIDTH - 250, 350, False], 'VIII': [WIDTH - 150, 350, False], 'Beta': [WIDTH - 50, 350, False], 'Gamma': [WIDTH - 250, 450, False]}

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
reflectors = ('A', 'B', 'C', 'B_Thin', 'C_Thin')
A      = ('E', 'J', 'M', 'Z', 'A', 'L', 'Y', 'X', 'V', 'B', 'W', 'F', 'C', 'R', 'Q', 'U', 'O', 'N', 'T', 'S', 'P', 'I', 'K', 'H', 'G', 'D')
B      = ('Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G', 'O', 'K', 'M', 'I', 'E', 'B', 'F', 'Z', 'C', 'W', 'V', 'J', 'A', 'T')
C      = ('F', 'V', 'P', 'J', 'I', 'A', 'O', 'Y', 'E', 'D', 'R', 'Z', 'X', 'W', 'G', 'C', 'T', 'K', 'U', 'Q', 'S', 'B', 'N', 'M', 'H', 'L')
B_Thin = ('E', 'N', 'K', 'Q', 'A', 'U', 'Y', 'W', 'J', 'I', 'C', 'O', 'P', 'B', 'L', 'M', 'D', 'X', 'Z', 'V', 'F', 'T', 'H', 'R', 'G', 'S')
C_Thin = ('R', 'D', 'O', 'B', 'J', 'N', 'T', 'K', 'V', 'E', 'H', 'M', 'L', 'F', 'C', 'W', 'Z', 'A', 'X', 'G', 'Y', 'I', 'P', 'S', 'U', 'Q')

setting = []

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

    def draw(self, WIN):    
        pygame.draw.rect(WIN, self.colour, (self.x,self.y, self.width, self.height), border_radius=10)

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
    def __init__(self):
        self.colour = (100,100,100)
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.label = pygame.font.SysFont('Corbel',35)
    
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
        self.radius = 10
        self.name = name
        self.location = location
        self.load = load
        self.label = pygame.font.SysFont('Corbel',25)
        self.x = location[0]
        self.y = location[1]


    def drawHolder(self, WIN):
        pygame.draw.circle(WIN, self.colour, self.location, 40)
        
        self.text = self.label.render(self.name, True, (0,0,0))
        WIN.blit(self.text, self.text.get_rect(center = (self.location[0],self.location[1])) )


    def drawRotor(self, WIN):
        self.rotorWhite = pygame.draw.circle(WIN, self.white, self.location, 40)
        self.rotorText = self.label.render(self.name, True, (0,0,0))
        WIN.blit(self.rotorText, self.text.get_rect(center = (self.location[0],self.location[1])) )


    def drag(self, event, eventPos, rotorsList):
        dragFlag = False
        for rotors in rotorsList:
            if rotors.rotorWhite.collidepoint(event.pos):
                to_move = rotors
                dragFlag = True
                print("1")
        return dragFlag, eventPos, to_move
    
    def move(self, eventPos,mouse, event, rotorsList):
        offset_x = mouse[0] - eventPos[0]
        offset_y = mouse[1] - eventPos[1]
        
        for rotors in rotorsList:
            if rotors.rotorWhite.collidepoint(event.pos):
                print(offset_x, offset_y)
                self.x = self.rotorWhite.x + offset_x
                self.y = self.rotorWhite.y + offset_y


    

def draw(win, mouse, covers, open_covers, rotorButton, rotorExit, keyPressed, rotorsLoad, dragFlag):
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
    
    

    #bg = pygame.draw.rect(WIN,"Brown", (100,50, 700, 250))
    

    

    for cover in covers:
        cover.draw(win)
    
    if open_covers == False:
        rotorButton.draw(win, (WIDTH-215,96,125,40), "Rotors", mouse)

    else:
        rotorExit.draw(win, (WIDTH-215, 676, 125, 40), "Close", mouse)

        
        
        for rotorsObj in rotorsLoad:
            rotorsObj.drawHolder(win)
            if rotorsObj.load or dragFlag:
                pass
            else:
                
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

    rotorButton = button()
    rotorExit = button()
    
    rotorsLoad = []
    for rotorRef in rotors:
        rotorRef = rotor(rotorRef, [rotors[rotorRef][0], rotors[rotorRef][1]], rotors[rotorRef][2])
        rotorsLoad.append(rotorRef)

    
    
    keyName = ""
    keyPressed = False
    dragFlag = False
    eventPos = (0,0)
    to_move = None

    while run:
        clock.tick(FPS)
        mouse = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            
            if event.type == pygame.QUIT:
                run = False
                break

            elif event.type == pygame.KEYDOWN and keys.count(True) == 1 and event.key in range(97,123) and rotor_choice_open == False:
                keyName = pygame.key.name(event.key)
                keyPressed = True

            elif event.type == pygame.KEYUP and keys.count(True) == 0 and event.key in range(97,123) and rotor_choice_open == False:
                keyName = ""
                keyPressed = False

            if event.type == pygame.MOUSEBUTTONDOWN and WIDTH-215 <= mouse[0] <= WIDTH-215+125 and 96 <= mouse[1] <= (96+40) and rotor_choice_open == False:
                rotor_choice_open = True
                cover_movement(rotor_choice_open, rotor_choice, rotor_cover)

            elif event.type == pygame.MOUSEBUTTONDOWN and WIDTH-215 <= mouse[0] <= WIDTH-215+125 and 676 <= mouse[1] <= (676+40) and rotor_choice_open == True:
                rotor_choice_open = False
                cover_movement(rotor_choice_open, rotor_choice, rotor_cover)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                eventPos = mouse
                dragFlag, eventPos, to_move = rotorRef.drag(event, eventPos, rotorsLoad)
                

            elif event.type == pygame.MOUSEMOTION:
                if dragFlag == True:
                    rotorRef.move(eventPos, mouse, event, rotorsLoad, to_move)
                    pass
            
            elif event.type == pygame.MOUSEBUTTONUP:
                dragFlag = False

        
        draw(WIN, mouse, [rotor_bg, rotor_choice, rotor_cover], rotor_choice_open, rotorButton, rotorExit, keyName, rotorsLoad, dragFlag)  

        

            

    pygame.quit
        

if __name__ == "__main__":
    
    main()