import pgzrun
import random

WIDTH = 1200
HEIGHT = 600

score = 0
lives = 3
speed = 5
is_game_over = False

galaga = Actor("ship")
galaga.pos = (WIDTH/2,HEIGHT-60)

bullets = []
bugs = []

for i in range(8):
    bug = Actor("bug")
    bug.x = random.randint(0,520)
    bug.y = random.randint(-100,0)

    bugs.append(bug)

def display_score():
    screen.draw.text(f"score: {score}",(50,30),color = "black")
    screen.draw.text(f"lives: {lives}",(50,60),color = "black")

def on_key_down(key):
    if key == keys.SPACE:
        bullet = Actor("bullet")
        bullet.x = galaga.x
        bullet.y = galaga.y -50
        bullets.append(bullet)

def update():
    global lives, score
    #move the ship left or right
    if keyboard.left:
        galaga.x -=speed
        if galaga.x <=0:
            galaga.x =0
    elif keyboard.right:
        galaga.x +=speed
        if galaga.x >=WIDTH:
            galaga.x =WIDTH
    
    #move bullets
    for bullet in bullets:
        if bullet.y <=0:
            bullets.remove(bullet)
        else:
            bullet.y -=10

    #move bugs
    for bug in bugs:
        bug.y +=5
        if bug.y > HEIGHT:
            bug.x = random.randint(0,520)
            bug.y= random.randint(-100,0)

        #check for collision with bullets
        for bullet in bullets:
            if bug.colliderect(bullet):
                sounds.sound.play()
                score += 100
                bullets.remove(bullet)
                bugs.remove(bug)
        
        #check for collision with ship
        if bug.colliderect(galaga):
            lives -= 1 
            bugs.remove(bug)
            if lives == 0:
                game_over()

    #continuosly creating new enemies
    if len(bugs) < 8:     
        bug = Actor("bug")
        bug.x = random.randint(0,520)
        bug.y = random.randint(-100,0)
        bugs.append(bug)


#function to draw game state
def draw():
    if lives > 0:
        screen.clear()
        screen.fill("yellow")
        for bullet in bullets:
            bullet.draw()
        for bug in bugs:
            bug.draw()
        galaga.draw()
        display_score()
    else:
        game_over_screen()

def game_over():
    global is_game_over
    is_game_over = True


#function to draw game over screen
def game_over_screen():
    screen.clear()
    screen.fill("yellow")
    screen.draw.text("GAME OVER",(WIDTH // 2, HEIGHT// 2),fontsize=60, color="black")
    screen.draw.text(f"final score: {score}",(WIDTH // 2, HEIGHT// 2),fontsize=60, color="black")




































            

    





        


    
    








































pgzrun.go()