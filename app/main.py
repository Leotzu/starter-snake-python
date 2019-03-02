import json
import os
import random
import bottle
import array as arr #lmr

from api import ping_response, start_response, move_response, end_response

@bottle.route('/')
def index():
    return '''
    Battlesnake documentation can be found at
       <a href="https://docs.battlesnake.io">https://docs.battlesnake.io</a>.
    '''

@bottle.route('/static/<path:path>')
def static(path):
    """
    Given a path, return the static file located relative
    to the static folder.

    This can be used to return the snake head URL in an API response.
    """
    return bottle.static_file(path, root='static/')

@bottle.post('/ping')
def ping():
    """
    A keep-alive endpoint used to prevent cloud application platforms,
    such as Heroku, from sleeping the application instance.
    """
    return ping_response()

@bottle.post('/start')
def start():
    data = bottle.request.json

    """
    TODO: If you intend to have a stateful snake AI,
            initialize your snake state here using the
            request's data if necessary.
    """
    print(json.dumps(data))

    color = "#000000"
    head = "smile"
    tail = "regular"

    return start_response(color, head, tail)  #not sure if it's okay to return 3 parameters. It was initially: return start_response(color)


@bottle.post('/move')
def move():
    data = bottle.request.json

    """
    TODO: Using the data from the endpoint request object, your
            snake AI must choose a direction to move in.
    """
    print(json.dumps(data))
    '''
    Setup:
    '''
    moves = ['up','down','left','right']  #initially, all directions are allowed.
    reports = ['nothing']  #allows reports to be made for later reference (updates every turn: no need to remove reports).
    '''
    count = 0
    while count < 50:
        otherSnakesY[count] = data['board']['snakes']['body'][count]['y'][count]
        otherSnakesX[count] = data['board']['snakes']['body'][count]['x'][count]
        cout += 1
    '''
    '''
    Add, Remove, and Check functions:
    '''
    #Remove options
    def removeUp(moves):
        if 'up' in moves: moves.remove('up')
    def removeDown(moves):
        if 'down' in moves: moves.remove('down')
    def removeLeft(moves):
        if 'left' in moves: moves.remove('left')
    def removeRight(moves):
        if 'right' in moves: moves.remove('right')
    #Check to see what's available
    def checkUp(moves):
        if 'up' in moves: return True
        else: return False
    def checkDown(moves):
        if 'down' in moves: return True
        else: return False
    def checkLeft(moves):
        if 'left' in moves: return True
        else: return False
    def checkRight(moves):
        if 'right' in moves: return True
        else: return False
    #Add reports
    def addReport(reports, str):
        reports.append(str)
    '''
    Data collection:
    '''
    self_0y = data['you']['body'][0]['y']
    self_0x = data['you']['body'][0]['x']
    self_1y = data['you']['body'][1]['y']
    self_1x = data['you']['body'][1]['x']
    tailLen = len(data['you']['body'])
    '''
    Analysis of data:
    '''
    print "TESTING:"

    print "FINISHED TESTING."
    #Avoid where tail will be next turn (!!not taking food into account!!) and DEATH SPIRAL:
    tailCount = 0
    while tailCount < tailLen:
        if (self_0y + 1 == data['you']['body'][tailCount]['y']) and (self_0x == data['you']['body'][tailCount]['x']):
            if tailCount != tailLen - 1:  #Allowing it to go where it's tail just was
                removeDown(moves)
            #DEATH SPIRAL starts here:
            if self_0y + 1 != self_1y:  #if y+1 isn't behind you (essentially checks your direction forward)
                tailCount2 = 1   #Checks if tail exists any distance to the left or right. If so, avoids that direction.
                while tailCount2 < tailLen:
                    if self_0y == data['you']['body'][tailCount2]['y']:
                        if data['you']['body'][tailCount2]['x'] > self_0x:
                            if checkUp(moves) or checkDown(moves) or checkLeft(moves):
                                removeRight(moves)
                        else:
                            if checkUp(moves) or checkDown(moves) or checkRight(moves):
                                removeLeft(moves)
                    tailCount2 += 1
                    #DEATH SPIRAL finished.
        tailCount +=1
    tailCount = 0
    while tailCount < tailLen:
        if (self_0y - 1 == data['you']['body'][tailCount]['y']) and (self_0x == data['you']['body'][tailCount]['x']):
            if tailCount != tailLen - 1:
                removeUp(moves)
            if self_0y - 1 != self_1y:
                tailCount2 = 1
                while tailCount2 < tailLen:
                    if self_0y == data['you']['body'][tailCount2]['y']:
                        if data['you']['body'][tailCount2]['x'] > self_0x:
                            if checkUp(moves) or checkDown(moves) or checkLeft(moves):
                                removeRight(moves)
                        else:
                            if checkUp(moves) or checkDown(moves) or checkRight(moves):
                                removeLeft(moves)
                    tailCount2 += 1
        tailCount += 1
    tailCount = 0
    while tailCount < tailLen:
        if (self_0x + 1 == data['you']['body'][tailCount]['x']) and (self_0y == data['you']['body'][tailCount]['y']):
            if tailCount != tailLen - 1:
                removeRight(moves)
            if self_0x + 1 != self_1x:
                tailCount2 = 1
                while tailCount2 < tailLen:
                    if self_0x == data['you']['body'][tailCount2]['x']:
                        if data['you']['body'][tailCount2]['y'] > self_0y:
                            if checkUp(moves) or checkLeft(moves) or checkRight(moves):
                                removeDown(moves)
                        else:
                            if checkUp(moves) or checkLeft(moves) or checkRight(moves):
                                removeUp(moves)
                    tailCount2 += 1
        tailCount += 1
    tailCount = 0
    while tailCount < tailLen:
        if (self_0x - 1 == data['you']['body'][tailCount]['x']) and (self_0y == data['you']['body'][tailCount]['y']):
            if tailCount != tailLen - 1:
                removeLeft(moves)
            if self_0x - 1 != self_1x:
                tailCount2 = 1
                while tailCount2 < tailLen:
                    if self_0x == data['you']['body'][tailCount2]['x']:
                        if data['you']['body'][tailCount2]['y'] > self_0y:
                            if checkUp(moves) or checkLeft(moves) or checkRight(moves):
                                removeDown(moves)
                        else:
                            if checkUp(moves) or checkLeft(moves) or checkRight(moves):
                                removeUp(moves)
                    tailCount2 += 1
        tailCount += 1
    #Avoid self-made cave trap if possible (it's possible to go down one and survive, but very unlikely):
        #Must be after other checks that regard immediate death moves
    tailCount = 0
    while tailCount < tailLen:
        if self_0y == data['you']['body'][tailCount]['y']:  #if going up or down eventually leads to a tail.
            tailCount2 = 0
            while tailCount2 < tailLen:
                if self_0y - 1 == data['you']['body'][tailCount2]['y']:  #if (left,up) = tail
                    if self_0x - 1 == data['you']['body'][tailCount2]['x']:
                        tailCount3 = 0
                        while tailCount3 < tailLen:
                            if self_0y - 1 == data['you']['body'][tailCount2]['y']:  #if (right,up) = tail
                                if self_0x + 1 == data['you']['body'][tailCount2]['x']:
                                    if checkDown(moves) or checkLeft(moves) or checkRight(moves):
                                        removeUp(moves)
                            tailCount3 += 1
                tailCount2 += 1
        tailCount += 1
    tailCount = 0
    while tailCount < tailLen:
        if self_0y == data['you']['body'][tailCount]['y']:  #if going up or down eventually leads to a tail.
            tailCount2 = 0
            while tailCount2 < tailLen:
                if self_0y + 1 == data['you']['body'][tailCount2]['y']:  #if (left,down) = tail
                    if self_0x - 1 == data['you']['body'][tailCount2]['x']:
                        tailCount3 = 0
                        while tailCount3 < tailLen:
                            if self_0y + 1 == data['you']['body'][tailCount2]['y']:  #if (right,down) = tail
                                if self_0x + 1 == data['you']['body'][tailCount2]['x']:
                                    if checkUp(moves) or checkLeft(moves) or checkRight(moves):
                                        removeDown(moves)
                            tailCount3 += 1
                tailCount2 += 1
        tailCount += 1
    tailCount = 0
    while tailCount < tailLen:
        if self_0x == data['you']['body'][tailCount]['x']:  #if going right or left eventually leads to a tail.
            tailCount2 = 0
            while tailCount2 < tailLen:
                if self_0x - 1 == data['you']['body'][tailCount2]['x']:  #if (left,up) = tail
                    if self_0y - 1 == data['you']['body'][tailCount2]['y']:
                        tailCount3 = 0
                        while tailCount3 < tailLen:
                            if self_0x - 1 == data['you']['body'][tailCount2]['x']:  #if (left,down) = tail
                                if self_0y + 1 == data['you']['body'][tailCount2]['y']:
                                    if checkUp(moves) or checkDown(moves) or checkRight(moves):
                                        removeLeft(moves)
                            tailCount3 += 1
                tailCount2 += 1
        tailCount += 1
    tailCount = 0
    while tailCount < tailLen:
        if self_0x == data['you']['body'][tailCount]['x']:  #if going right or left eventually leads to a tail.
            tailCount2 = 0
            while tailCount2 < tailLen:
                if self_0x + 1 == data['you']['body'][tailCount2]['x']:  #if (right,up) = tail
                    if self_0y - 1 == data['you']['body'][tailCount2]['y']:
                        tailCount3 = 0
                        while tailCount3 < tailLen:
                            if self_0x + 1 == data['you']['body'][tailCount2]['x']:  #if (right,down) = tail
                                if self_0y + 1 == data['you']['body'][tailCount2]['y']:
                                    if checkUp(moves) or checkDown(moves) or checkLeft(moves):
                                        removeRight(moves)
                            tailCount3 += 1
                tailCount2 += 1
        tailCount += 1
    #Avoid walls & Exiting wallride if possible:
    if self_0y == 0:
        removeUp(moves)
        if checkDown(moves):   #Exit wallride
            removeLeft(moves)
            removeRight(moves)
    if self_0y == 14:
        removeDown(moves)
        if checkUp(moves):
            removeLeft(moves)
            removeRight(moves)
    if self_0x == 0:
        removeLeft(moves)
        if checkRight(moves):
            removeUp(moves)
            removeDown(moves)
    if self_0x == 14:
        removeRight(moves)
        if checkLeft(moves):
            removeUp(moves)
            removeDown(moves)
    #Avoid wall-hugging if possible (!!This has to be the LAST CHECK in Analysis!!):
    if self_0y == 1:
        if checkDown(moves) or checkLeft(moves) or checkRight(moves):
            removeUp(moves)
    if self_0y == 13:
        if checkUp(moves) or checkLeft(moves) or checkRight(moves):
            removeDown(moves)
    if self_0x == 1:
        if checkUp(moves) or checkDown(moves) or checkRight(moves):
            removeLeft(moves)
    if self_0x == 13:
        if checkUp(moves) or checkDown(moves) or checkLeft(moves):
            removeRight(moves)
    #Avoid other snakes:
    '''
    tailCount = 0
    while tailCount < tailLen:
        if (self_0y + 1 == data['snakes']['body'][tailCount]['y']) and (self_0x == data['snakes']['body'][tailCount]['x']):
            #if tailCount != tailLen - 1:  #Allowing it to go where it's tail just was
            removeDown(moves)
        tailCount +=1
    tailCount = 0
    while tailCount < tailLen:
        if (self_0y - 1 == data['snakes']['body'][tailCount]['y']) and (self_0x == data['snakes']['body'][tailCount]['x']):
            #if tailCount != tailLen - 1:  #Allowing it to go where it's tail just was
            removeUp(moves)
        tailCount +=1
    tailCount = 0
    while tailCount < tailLen:
        if (self_0x - 1 == data['snakes']['body'][tailCount]['x']) and (self_0y == data['snakes']['body'][tailCount]['y']):
            #if tailCount != tailLen - 1:  #Allowing it to go where it's tail just was
            removeLeft(moves)
        tailCount +=1
    tailCount = 0
    while tailCount < tailLen:
        if (self_0x + 1 == data['snakes']['body'][tailCount]['x']) and (self_0y == data['snakes']['body'][tailCount]['y']):
            #if tailCount != tailLen - 1:  #Allowing it to go where it's tail just was
            removeRight(moves)
        tailCount +=1
    '''

    #Randomly go in with of the moves that are still allowed:
    print "AVAILABLE MOVES: ",moves
    move = random.choice(moves)

    return move_response(move)


@bottle.post('/end')
def end():
    data = bottle.request.json

    """
    TODO: If your snake AI was stateful,
        clean up any stateful objects here.
    """
    print(json.dumps(data))

    return end_response()

# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug=os.getenv('DEBUG', True)
    )
