# Built by Chris Nelson and Nico Martinsen 
# Mr. Appel's Computer Science Class Final 2014

import simplegui
width = 700
height = 700
bike1_pos= [(width/2)+20, height/2]
bike2_pos= [(width/2)-20, height/2]

rotation1 = 1.57079633
rotation2 = 1.57079633
move1 = [0, 0]
move2 = [0, 0]

line1=[[(width/2)+20, height/2]]
line2=[[(width/2)-20, height/2]]

gameon=False
winner = "no one"
 
#music
# sound = simplegui.load_sound('https://www.dropbox.com/s/txaru540ddsnxz4/%5Bmp3lemon.net%5D%2014%20-%20Fall.mp3?dl=1')
# sound.set_volume(1)

# sound.play()


bike1 = simplegui.load_image('https://www.dropbox.com/s/bjxvesred888a5w/LightcycleB..png?dl=1')        
bike2 = simplegui.load_image('https://www.dropbox.com/s/q4t0q6c0vilexqo/LightcycleO.png?dl=1')
grid = simplegui.load_image('https://www.dropbox.com/s/x19smirjg21zgfm/grid.jpg?dl=1')

line_size = 4

x=1




print("Welcome To TRON Lightcycles\n")
print("CONTROLS")
print("Orange: Use WASD to control your lightcycle\nBlue: Use the Arrow keys to control your lightycle\n")
print("Press SPACE to start\n")
#####################################################

def draw_handler(canvas):
    #draws bikes and sets rotation
    global winner
    canvas.draw_image(grid, (420/2, 420/2), (420, 420), (width/2, height/2), (width, height))    
    canvas.draw_image(bike1, (628 / 2, 238 / 2), (628, 238), (bike1_pos), (628/15, 238/15), 3*rotation1)
    canvas.draw_image(bike2, (580 / 2, 219 / 2), (580, 219), (bike2_pos), (580/15, 219/15), rotation2)    
    
    
    #draws lines behind each bike    
    canvas.draw_polyline(line1, line_size, 'aqua')
    canvas.draw_polyline(line2, line_size, 'orange')
    
    
    #updates bike position
    bike1_pos[0] += move1[0]
    bike1_pos[1] += move1[1]
    
    bike2_pos[0] += move2[0]
    bike2_pos[1] += move2[1]
    
    #updates each lines points    
    if gameon == True:
        line1.append([bike1_pos[0], bike1_pos[1]])
        line2.append([bike2_pos[0], bike2_pos[1]])        
    
    
    #makes bike unable to hit other line    
    if gameon==True:
        if bike2_pos in line1:
            winner = "Blue"
            game_reset()
            return
   
        if bike1_pos in line2:
            winner = "Orange"
            game_reset()
            return
        
        
#	makes bike unable to hit its own line    
        if bike1_pos in line1[0:-2]:
            winner = "Orange"
            game_reset()
            return
 
        if bike2_pos in line2[0:-2]:
                winner = "Blue" 
                game_reset()
                return

    #resets game if bike hits edge
    if bike1_pos[1] >= height or bike1_pos[1]<=0:
        winner = "Orange"
        game_reset()
        return
        
    if bike1_pos[0] >= width or bike1_pos[0]<=0:
        winner = "Orange"
        game_reset()
        return
        
    if bike2_pos[1] >= height or bike2_pos[1]<=0:
        winner = "Blue"
        game_reset()
        return
        
    if bike2_pos[0] >= width or bike2_pos[0]<=0:
        winner = "Blue"
        game_reset()
        return
        
#game keyboard controls   
def keydown(key): 
    global rotation1, rotation2, move1, move2, x, gameon
    if gameon == True:
        if key==simplegui.KEY_MAP['up']:
            rotation1 = 1.57079633
            move1 = [0, -4]
            
        elif key==simplegui.KEY_MAP['down']:
            rotation1 = 3*1.57079633
            move1 = [0, 4]
        
        elif key==simplegui.KEY_MAP['left']:       
            rotation1 = 0
            move1 = [-4, 0]
        
        elif key==simplegui.KEY_MAP['right']:       
            rotation1 = 2*1.57079633
            move1 = [4, 0]
        
    
        if key==simplegui.KEY_MAP['w']:     
            rotation2 = 1.57079633
            move2 = [0, -4]
        
        elif key==simplegui.KEY_MAP['s']:     
            rotation2 = 3*1.57079633
            move2 = [0, 4]
        
        elif key==simplegui.KEY_MAP['a']:      
            rotation2 = 0
            move2 = [-4, 0]
    
        elif key==simplegui.KEY_MAP['d']:        
            rotation2 = 2*1.57079633
            move2 = [4, 0]

    elif x==1:  
        if key==simplegui.KEY_MAP['space']:        
            move1 = [0, 4]
            move2 = [0, -4]
            x=2
            # sound.play()
            gameon=True
        
#reset game function       
def game_reset():
    global move1, move2, rotation1, rotation2, bike1_pos, bike2_pos, line1, line2, x, winner, gameon
    while gameon == True:        
        move1 = [0, 0]
        move2 = [0, 0]
        rotation1 = 1.57079633
        rotation2 = 1.57079633
        bike1_pos= [(width/2)+20, height/2]
        bike2_pos= [(width/2)-20, height/2]
        line1=[[(width/2)+20, height/2]]
        line2=[[(width/2)-20, height/2]]
        x=1
        print(winner,"wins")
        winner = "no one"
        # sound.play()       
        gameon=False
        
#Increases and Decreases line size       
def line_increase():
    global line_size
    if line_size <39:
        line_size+=2
    else:
        line_size=40
        
def line_decrease():
    global line_size
    if line_size>3:
        line_size-=2
    else:
        line_size=2
        
def quit():
    # global sound
    # sound.rewind()
    frame.stop()
    
frame = simplegui.create_frame("Tron", width, height)
button_reset = frame.add_button("RESET", game_reset)
button_increase = frame.add_button("Increase Line Size", line_increase)
button_decrease = frame.add_button("Decrease Line Size", line_decrease)
button_quit = frame.add_button("Quit", quit, 100)
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(keydown)
frame.start()