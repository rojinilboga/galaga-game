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
    screen.draw.text(f"score: {score}",(50,30))
    screen.draw.text(f"lives: {lives}",(50,60))

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
            

    





        


    
    








































pgzrun.go()