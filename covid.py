from pygame import *
from random import *
from math import *
from pandas import Series as s
from numpy import random as rn
from tkinter import *
from PIL import ImageTk, Image

#colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = (192, 192, 192)
yellow = (255, 255, 102)
light_blue = (173,216,230)
sky_blue = (135,206,235)
beige = (207, 185, 151)
rc = 135
gc = 206
bc = 235
w = 455



#variables
run = False
r=10
xy_pos=[]
num=0
tot=0
dig = 1
stop = 0
positive_rate = 17.88
used = positive_rate/100
death_rate = 7.344
recover_rate = 89.72
people_num = 100
days=1
color = sky_blue
death = 100348416
poplation = 1366400000
tot_dead = round(death * people_num /poplation)
v = 1
rate = round(2414/v)
cycles = 0
pause = False
rep = False

#lists
x_l=list(range(10,w-9))
y_l=list(range(10,w-9))
people=list(range(people_num))
infected_start=randint(0, people_num-1)
infected_people=[]
infected_people_color = [beige for i in range(people_num)]
tot_prob = [0 for i in range(10000)]
dead = []
recovered = []
date = [[i,0] for i in people]
direction=[-1,1]
#create the starting position
def valid(x,y,xy_pos):
    for k in xy_pos:
        if sqrt(pow(k[0]-x,2)+pow(k[1]-y,2)) <20:
            return False
    return True
def create(xy_pos,x_l,y_l):
    for i in people:
        j = 0
        while j == 0:
            x, y = choice(x_l), choice(y_l)
            if (x, y) not in xy_pos and valid(x,y,xy_pos):

                xy_pos.append((x, y))
                j = 1
            else:
                pass

create(xy_pos,x_l,y_l)

#movement of poeple
x_c = [choice(direction) for i in people]
y_c = [choice(direction) for l in people]
vx = []
vy = []
def vel(v):
    global  vx, vy
    vx = [v*x_c[i] for i in people]
    vy = [v*y_c[i] for i in people]
vel(v)

#infected
infected_people.append(infected_start)
infected_people_color[infected_start] = red
date[infected_start][1] = 1
def infected():
    global  infected_people, days, date
    for k in infected_people:
        if infected_people_color[k] == black:
            pass
        else:
            if date[k][1] >=3:
                for j in people:
                    if j in infected_people:
                        pass
                    else:
                        if xy_pos[j][0] in range(xy_pos[k][0]-12, xy_pos[k][0]+13) and xy_pos[j][1] in range(xy_pos[k][1]-12, xy_pos[k][1]+13) :
                            if rn.choice([0, 1], p=[1 - used, used]):
                                infected_people.append(j)
                                date.append((j, 1))
                                infected_people_color[j] = red

    return False
#death
def dead_people():
    global infected_people, dead, people, date
    for i in infected_people:
        if date[i][1] >= 5:
            if rn.choice([0, 1], p=[1 - death_rate/100, death_rate/100]) == 1:
                dead.append(i)
                infected_people.remove(i)
                infected_people_color[i] = black

#recovered
def recovered_people():
    global infected_people, recovered, people, date
    for i in infected_people:
        if date[i][1] >= 14:
            if rn.choice([0, 1], p=[1 - recover_rate / 100, recover_rate / 100]) == 1:
                recovered.append(i)
                infected_people.remove(i)
                infected_people_color[i] = green
#check
def check():
    global xy_pos, infected_people
    for (i, j) in xy_pos:
        if i not in range(10, w-10):
            i = randint(10, w-10)
        if j not in range(10, w-10):
            j = randint(10, w-10)
    if len(infected_people) == 0:
        infected_people.append(randint(0, people_num))

#reort
def report():
    root = Tk()
    root.geometry('300x300')
    root.title('REPORT')
    root.configure(bg = 'black')
    l_days = Label(root, text='DAYS : %s' % (days), font=('Ariel Bold', 20)).pack()
    l_inf = Label(root, text='INFECTED : %s' % (len(infected_people)), font=('Ariel Bold', 20)).pack()
    l_died = Label(root, text='DIED : %s' % (len(dead)), font=('Ariel Bold', 20)).pack()
    l_rec = Label(root, text='RECOVERED : %s' % (len(recovered)), font=('Ariel Bold', 20)).pack()
    l_notinf = Label(root, text='NON INFECTED : %s' % (people_num - len(infected_people)), font=('Ariel Bold', 20)).pack()
    root.mainloop()

#starting screen
def simulation():
    global run,  gui
    run= True
    gui.destroy()
gui = Tk()
gui.configure(bg='black')
gui.title('COVID Vs INDIA')
gui.iconbitmap(r'D:\projects\imp_projects\covid_simulator\icon.ico')
gui.geometry('550x550')
for i in range(11):
    for j in range(14):
        label = Label(gui, text='  ', fg='black', bg='black').grid(row=i, column=j)
img = ImageTk.PhotoImage(Image.open(r'D:\projects\imp_projects\covid_simulator\sars-cov-19_up.jpg'))
panel = Label(gui, image=img, bg='black')
panel.grid(row=8, column=15)
label1 = Label(gui, text='COVID Vs INDIA', font=('Ariel Bold', 20), fg='white', bg='black').grid(row=12, column=15)
start_bt = Button(gui, text='START', font=('Ariel Bold', 15), bg='red', fg='white', command=simulation).grid(row=13,
                                                                                                           column=15)

gui.mainloop()


#simulation


init()
img_start = image.load(r'D:\projects\imp_projects\covid_simulator\pause_play64.png')
img_stop = image.load(r'D:\projects\imp_projects\covid_simulator\stop64.png')
img_rep = image.load(r'D:\projects\imp_projects\covid_simulator\report64.png')
window=display.set_mode((w, w+80))
window.fill(sky_blue)
display.set_caption("COVID SIMULATOR!")


while run:

    for i in event.get():
        if i.type == QUIT:
            run = False
        if i.type == MOUSEBUTTONDOWN:
            if 100 <= mouse.get_pos()[0] <= 164 and w+16 <= mouse.get_pos()[1] <= w + 80:
                pause = not(pause)
            if 200 <= mouse.get_pos()[0] <= 264 and w+16 <= mouse.get_pos()[1] <= w + 80:
                run = False
            if pause:
                if 300 <= mouse.get_pos()[0] <= 364 and w+16 <= mouse.get_pos()[1] <= w + 80:
                    rep = not (rep)
                    time.wait(3)
                    report()
                    rep = not(rep)
    window.fill(color)

    #time.wait(10)
    for j in people:
        xc = xy_pos[j][0]
        yc = xy_pos[j][1]
        draw.circle(window, infected_people_color[j], (xc,yc), r)
        draw.circle(window, black, (xc,yc),r,1)
        draw.line(window, black, (0,w), (w,w), 2)




        if not(pause):
            if xy_pos[j][0] == 10 or xy_pos[j][0] == w - 10:
                vx[j] = -vx[j]
            if xy_pos[j][1] == 10 or xy_pos[j][1] == w - 10:
                vy[j] = -vy[j]
            xy_pos[j] = (xc + vx[j], yc - vy[j])

    if not (pause):
        check()
        dig += 1
        if dig%250 == 0:
            shuffle(vx)
            shuffle(vy)

        recovered_people()
        dead_people()

        cycles += 1
        infected()
        if cycles % rate == 0:
            days += 1
            for k in infected_people:
                date[k][1] += 1

    font_t = font.Font('freesansbold.ttf', 32)
    text = font_t.render('%s' % (days), False, black)
    if not(rep):
        window.blit(img_start, (100, w + 16))
        window.blit(img_stop, (200, w + 16))
    if pause:
        window.blit(img_rep, (300, w + 16))

    window.blit(text, (0, w+10))
    display.update()

