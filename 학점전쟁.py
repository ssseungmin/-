import pygame
from pygame.rect import *
import random


def replay():
    global isGameOver, score
    isGameOver = False
    score = 0
    for i in range(len(gradeA)):
        recGradeA[i].y = -1
    for i in range(len(gradeB)):
        recGradeB[i].y = -2
    for i in range(len(gradeC)):
        recGradeC[i].y = -3
    for i in range(len(gradeF)):
        recGradeF[i].y = -3
    for i in range(len(pen)):
        recPen[i].y = -1

def eventProcess():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

            if event.key == pygame.K_LEFT:
                move.x = -1
            if event.key == pygame.K_RIGHT:
                move.x = 1
            if event.key == pygame.K_UP:
                move.y = -1
            if event.key == pygame.K_DOWN:
                move.y = 1
            if event.key == pygame.K_r:
                replay()
            if event.key == pygame.K_SPACE:
                makePen()
                
def movePlayer():
    if not isGameOver:
        recPlayer.x += move.x
        recPlayer.y += move.y
    if recPlayer.x < 0:
        recPlayer.x = 0
    if recPlayer.x > SCREEN_WIDTH-recPlayer.width:
        recPlayer.x = SCREEN_WIDTH-recPlayer.width
    if recPlayer.y < 0:
        recPlayer.y = 0
    if recPlayer.y > SCREEN_HEIGHT-recPlayer.height:
        recPlayer.y = SCREEN_HEIGHT-recPlayer.height        
    SCREEN.blit(player, recPlayer)

def timeDelay500ms():
    global time_delay_500ms
    if time_delay_500ms > 5:
        time_delay_500ms = 0
        return True    
    time_delay_500ms += 1
    return False

def makeGradeA():
    if isGameOver:
        return
    if timeDelay500ms():
        idex = random.randint(0, len(gradeA)-1)
        if recGradeA[idex].y == -1:
            recGradeA[idex].x = random.randint(0, SCREEN_WIDTH)
            recGradeA[idex].y = 0

def moveGradeA():
    makeGradeA()
    for i in range(len(gradeA)):
        if recGradeA[i].y == -1:
            continue
        if not isGameOver:
            recGradeA[i].y += 1
        if recGradeA[i].y > SCREEN_HEIGHT:
            recGradeA[i].y = 0
        SCREEN.blit(gradeA[i], recGradeA[i])

def makeGradeB():
    if isGameOver:
        return
    if timeDelay500ms():
        idex = random.randint(0, len(gradeB)-1)
        if recGradeB[idex].y == -1:
            recGradeB[idex].x = random.randint(0, SCREEN_WIDTH)
            recGradeB[idex].y = 0

def moveGradeB():
    makeGradeB()
    for i in range(len(gradeB)):
        if recGradeB[i].y == -1:
            continue
        if not isGameOver:
            recGradeB[i].y += 1
        if recGradeB[i].y > SCREEN_HEIGHT:
            recGradeB[i].y = 0
        SCREEN.blit(gradeB[i], recGradeB[i])
        
def makeGradeC():
    if isGameOver:
        return
    if timeDelay500ms():
        idex = random.randint(0, len(gradeC)-1)
        if recGradeC[idex].y == -1:
            recGradeC[idex].x = random.randint(0, SCREEN_WIDTH)
            recGradeC[idex].y = 0

def moveGradeC():
    makeGradeC()
    for i in range(len(gradeC)):
        if recGradeC[i].y == -1:
            continue
        if not isGameOver:
            recGradeC[i].y += 1
        if recGradeC[i].y > SCREEN_HEIGHT:
            recGradeC[i].y = 0
        SCREEN.blit(gradeC[i], recGradeC[i])
        
def makeGradeF():
    if isGameOver:
        return
    if timeDelay500ms():
        idex = random.randint(0, len(gradeF)-1)
        if recGradeF[idex].y == -1:
            recGradeF[idex].x = random.randint(0, SCREEN_WIDTH)
            recGradeF[idex].y = 0

def moveGradeF():
    makeGradeF()
    for i in range(len(gradeF)):
        if recGradeF[i].y == -1:
            continue
        if not isGameOver:
            recGradeF[i].y += 1
        if recGradeF[i].y > SCREEN_HEIGHT:
            recGradeF[i].y = 0
        SCREEN.blit(gradeF[i], recGradeF[i])

def DetectionCrashPen():
    global score, isGameOver
    if isGameOver:
        return
    for rec in recGradeA:
        if rec.y == -1:
            continue
        for recM in recPen:
            if recM.y == -1:
                continue
            if rec.top < recM.bottom \
                    and recM.top < rec.bottom \
                    and rec.left < recM.right \
                    and recM.left < rec.right:
                rec.y = -1
                recM.y = -1
                score += 1000
                break
    for rec in recGradeB:
        if rec.y == -1:
           continue
        for recM in recPen:
            if recM.y == -1:
                 continue
            if rec.top < recM.bottom \
                    and recM.top < rec.bottom \
                    and rec.left < recM.right \
                    and recM.left < rec.right:
                rec.y = -1
                recM.y = -1
                score += 700
                break
    for rec in recGradeC:
        if rec.y == -1:
           continue
        for recM in recPen:
            if recM.y == -1:
                 continue
            if rec.top < recM.bottom \
                    and recM.top < rec.bottom \
                    and rec.left < recM.right \
                    and recM.left < rec.right:
                rec.y = -1
                recM.y = -1
                score += 400
                break

def makePen():
    if isGameOver:
        return
    for i in range(len(pen)):
        if recPen[i].y == -1:
            recPen[i].x = recPlayer.x
            recPen[i].y = recPlayer.y
            break

def movePen():
    for i in range(len(pen)):
        if recPen[i].y == -1:
            continue
        if not isGameOver:
            recPen[i].y -= 1
        if recPen[i].y < 0:
            recPen[i].y = -1
        SCREEN.blit(pen[i], recPen[i])

def DetectionCrash():   
    global score, isGameOver
    if isGameOver:
        return
    for rec in recGradeF:
        if rec.y == -1:
            continue
        if rec.top < recPlayer.bottom \
            and recPlayer.top < rec.bottom \
            and rec.left < recPlayer.right \
            and recPlayer.left < rec.right:
            isGameOver = True
            break
    

def flash():
    global time_dealy_4sec, toggle
    time_dealy_4sec += 1
    if time_dealy_4sec > 40:
        time_dealy_4sec = 0
        toggle = ~toggle    
    return toggle

def screenText():   
    mFont = pygame.font.SysFont("arial",20, True, False)
    SCREEN.blit(mFont.render(
     f'[score]: {score}', True, 'blue'), (10, 10, 0, 0))

    if isGameOver and flash():
        SCREEN.blit(mFont.render(
            'Game Over...', True, 'red'), (150, 300, 0, 0))
        SCREEN.blit(mFont.render(
            'press [R] -> REPLAY', True, 'yellow'), (120, 320, 0, 0))
        SCREEN.blit(mFont.render(
            f'[Final Score] => [{score}]', True, 'green'), (110, 340, 0, 0))

##변수초기화
isActive = True
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
move = Rect(0,0,0,0)
time_delay_500ms = 0
time_dealy_4sec = 0
toggle = False
score = 0
isGameOver = False

##스크린 생성
pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('CodingNoew!!')

##플레이어 생성
player = pygame.image.load('플레이어.png')
player = pygame.transform.scale(player,(30,30))
recPlayer = player.get_rect()
recPlayer.centerx = (SCREEN_WIDTH/2)
recPlayer.centery = (SCREEN_HEIGHT/2)

##A학점 생성
gradeA = [pygame.image.load('A.png') for i in range(2)]
recGradeA = [None for i in range(len(gradeA))]
for i in range(len(gradeA)):
    gradeA[i] = pygame.transform.scale(gradeA[i], (20, 20))
    recGradeA[i] = gradeA[i].get_rect()
    recGradeA[i].y = -1
##B학점 생성
gradeB = [pygame.image.load('B.png') for i in range(4)]
recGradeB = [None for i in range(len(gradeB))]
for i in range(len(gradeB)):
    gradeB[i] = pygame.transform.scale(gradeB[i], (20, 20))
    recGradeB[i] = gradeB[i].get_rect()
    recGradeB[i].y = -2
##C학점 생성
gradeC = [pygame.image.load('C.png') for i in range(6)]
recGradeC = [None for i in range(len(gradeC))]
for i in range(len(gradeC)):
    gradeC[i] = pygame.transform.scale(gradeC[i], (20, 20))
    recGradeC[i] = gradeC[i].get_rect()
    recGradeC[i].y = -3
##F학점 생성
gradeF = [pygame.image.load('F.png') for i in range(6)]
recGradeF = [None for i in range(len(gradeF))]
for i in range(len(gradeF)):
    gradeF[i] = pygame.transform.scale(gradeF[i], (20, 20))
    recGradeF[i] = gradeF[i].get_rect()
    recGradeF[i].y = -3

##펜 생성
pen = [pygame.image.load('펜.png') for i in range(40)]
recPen = [None for i in range(len(pen))]
for i in range(len(pen)):
    pen[i] = pygame.transform.scale(pen[i], (20, 20))
    recPen[i] = pen[i].get_rect()
    recPen[i].y = -1

##기타
clock = pygame.time.Clock()

##반복
while isActive:
    #화면 초기화
    SCREEN.fill((0,0,0))
    #이벤트
    eventProcess()
    #플레이어
    movePlayer()
    #학점
    moveGradeA()
    moveGradeB()
    moveGradeC()
    moveGradeF()
    #펜
    movePen()
    #충돌
    DetectionCrashPen()
    DetectionCrash()
    #text 업데이트
    screenText()
    #화면 업데이트
    pygame.display.flip()
    clock.tick(100)

