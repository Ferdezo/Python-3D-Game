__author__ = 'Ferdezo'

from visual import *

#game utilities
score = 0
lifes = 3

alive = True

#scene dimensions
scene_x = 3
scene_y = 3
scene_z = 6

#player & generator dimensions
px = 1
py = 1
pz = 0.1

#cordinates
offset = 0.5
start_pos = vector (0, offset, -3)

#3D objects
ball = sphere(pos = start_pos, color = color.red, radius = 0.1)
player = box(pos = vector(0, offset, 3), color = color.green, size = (px, py, pz))
generator = box (pos = start_pos, color = color.yellow, size = (px, py, pz))
glass = box(pos = vector(0, 1.5, 0), color = color.blue, size = (scene_x, scene_y, scene_z), opacity = 0.1)

#velocity & acceleration
ball.velocity = vector(1, 1, 2)
generator.velocity = vector(2, 0.25, 0)
gravity = 0.25
a = 1
step = 0.5

#player boundries
playerLeft = player.pos.x - offset
playerRight = player.pos.x + offset
playerUp = player.pos.y + offset
playerDown = player.pos.y - offset

while alive:

    ### GENERATOR ###
    generator.pos.x += generator.velocity.x * gravity
    generator.pos.y += generator.velocity.y * gravity

    #vertical boundries
    if(generator.pos.y >= 3 - offset) or (generator.pos.y < 0 + offset):
        generator.velocity.y *= -1

    #horizontal boundries
    if(generator.pos.x >= 1.5 - offset) or (generator.pos.x < -1.5 + offset):
        generator.velocity.x *= -1

    ### BALLS ###
    ball.pos.x += ball.velocity.x * gravity
    ball.pos.y += ball.velocity.y * gravity
    ball.pos.z += ball.velocity.z * gravity

    #vertical boundries
    if(ball.pos.y >= scene_y - offset) or (ball.pos.y < 0 + offset):
        ball.velocity.y *= -1

    #horizotnal boundries
    if(ball.pos.x >= 1 + offset) or (ball.pos.x < - 1 - offset):
        ball.velocity.x *= -1

    #hit check
    if(ball.pos.z > 3):
        if(ball.pos.x >= playerLeft) and (ball.pos.x <= playerRight):
            if(ball.pos.y >= playerDown) and (ball.pos.y <= playerUp):
                lifes -= 1
                if lifes == 0:
                    alive = False
                print("HIT!")

        score += 1
        ball.pos = generator.pos
        ball.velocity.x = random.random() + a
        # ball.velocity.y = random.random() + a
        # ball.velocity.z = random.random() + a

    ### PLAYER ###
    #movement
    if scene.kb.keys:
        key = scene.kb.getkey()
        if key == "left":
            if player.pos.x > -1 + offset:
                player.pos.x = player.pos.x - step

        if key == "right":
            if player.pos.x < 1 - offset:
                player.pos.x = player.pos.x + step

        print(player.pos.y)

        if key == "up":
            if(player.pos.y < 3 - offset):
                player.pos.y = player.pos.y + step

        if key == "down":
            if(player.pos.y > 0 + offset):
                player.pos.y = player.pos.y - step

        #update boundries
        playerLeft = player.pos.x - offset
        playerRight = player.pos.x + offset
        playerUp = player.pos.y + offset
        playerDown = player.pos.y - offset

    rate(15)