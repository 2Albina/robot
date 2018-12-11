#-*- coding: utf-8 -*
import robot
r = robot.rmap()
r.lm('task2-4')
r.sleep = 0.01
def task():
    pass
    #------- пишите код здесь -----
    def painting():
        r.right()
        r.paint()
        r.down()
        r.paint()
        r.down()
        r.paint()
        r.right()
        r.up()
        r.paint()
        r.left(2)
        r.paint()
        r.up()
    for k in range(5):
        for i in range(10):
            painting()
            if i < 9:
                r.right(4)
        r.left(36)
        if k < 4:
            r.down(4)
        
    #------- пишите код здесь -----
r.start(task)

#Отступ слева (tab) сохранять!
#r.help() - Список команд и краткие примеры

#r.right() - вправо
#r.right(3)- вправо на 3
#r.down() - вниз
#r.up() - вверх
#r.left() - влево
#r.paint() - закрасить  

#r.color() - закрашена ли клетка? 
#r.freeRight() - свободно ли справа? 
#r.freeLeft() - свободно ли слева?  
#r.freeUp() - свободно ли сверху? 
#r.freeDown() - свободно ли снизу?  

#r.wallRight() - стена ли справа? 
#r.wallLeft() - стена ли слева?  
#r.wallUp() - стена ли сверху? 
#r.wallDown() - стена ли снизу?  


#red - красный
#blue - синий
#yellow - желтый
#green - зеленый
