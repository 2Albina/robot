#-*- coding: utf-8 -*
import robot
r = robot.rmap()
r.lm('task1-3')
def task():
    pass
    #------- пишите код здесь -----

    r.down(3)
    r.paint("red")
    r.right(4)
    r.up(3)
    r.paint()
    r.down(3)


    
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
