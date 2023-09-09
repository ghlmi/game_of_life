from os import system
import random , time


system("clear")


rowNumber = int(input("Please enter row number : "))
colNumber = int(input("Please enter col number : "))


system("clear")


#create World Function
world = list()
for row in range(rowNumber):
       world.append(list())
       for col in range(colNumber):
           cells = random.randint(0,1)
           world[row].append(cells)


#Create Next Gen World
NextGenWorld = list()
NextGenWorld = world


#Create Last Gen World
LastGenWorld = list()
LastGenWorld = world

#Compare Cells
def compareCells(i , j):



    

    row = i
    col = j

    cell = LastGenWorld[row][col]


    

    #First Row
    if row == 0 :
        #(0,0)
        if (col == 0):
            if cell == 1 :
                population = -1
                for ii in range(0,2):
                    for jj in range(0,2):
                        population += LastGenWorld[ii][jj]
                if population == 3 or population == 2 :
                    NextGenWorld[row][col] = 1
                else :
                    NextGenWorld[row][col] = 0

            #dead cell live in next Gen
            if cell == 0 :
                population = 0
                for ii in range(0,2):
                    for jj in range(0,2):
                        population += LastGenWorld[ii][jj]
                if population == 3 :
                    NextGenWorld[row][col] = 1



        #(0,Len Col)
        elif (col == len(world[i])-1):
            if cell == 1 :
                population = -1
                for ii in range(0,2):
                    for jj in range(0,2):
                        population += LastGenWorld[row+ii][col-jj]
                if population == 3 or population == 2 :
                    NextGenWorld[row][col] = 1
                else :
                    NextGenWorld[row][col] = 0


            #dead cell live in next Gen
            if cell == 0 :
                population = 0
                for ii in range(0,2):
                    for jj in range(0,2):
                        population += LastGenWorld[row+ii][col-jj]
                if population == 3 :
                    NextGenWorld[row][col] = 1

        else :
            if cell == 1:
                population = -1
                for ii in range(0,2):
                    for jj in range(-1,2):
                        population += LastGenWorld[row+ii][col+jj]
                if population == 3 or population == 2 :
                    NextGenWorld[row][col] = 1
                else :
                    NextGenWorld[row][col] = 0

            #dead cell live in next Gen
            if cell == 0 :
                population = 0
                for ii in range(0,2):
                    for jj in range(-1,2):
                        population += LastGenWorld[row+ii][col+jj]
                if population == 3 :
                    NextGenWorld[row][col] = 1

    #Last Row
    elif (row == len(world)-1) :



        #(Len Row,0)
        if (col == 0):
            if cell == 1 :
                population = -1
                for ii in range(0,2):
                    for jj in range(0,2):
                        population += LastGenWorld[row-ii][col+jj]
                if population == 3 or population == 2 :
                    NextGenWorld[row][col] = 1
                else :
                    NextGenWorld[row][col] = 0

            #dead cell live in next Gen
            if cell == 0 :
                population = 0
                for ii in range(0,2):
                    for jj in range(0,2):
                        population += LastGenWorld[row-ii][col+jj]
                if population == 3 :
                    NextGenWorld[row][col] = 1

            

        #(Len Row , Len Col)
        elif (col == len(world[i])-1):
            if cell == 1 :
                population = -1
                for ii in range(0,2):
                    for jj in range(0,2):
                        population += LastGenWorld[row-ii][col-jj]
                if population == 3 or population == 2 :
                    NextGenWorld[row][col] = 1
                else :
                    NextGenWorld[row][col] = 0

            #dead cell live in next Gen
            if cell == 0 :
                population = 0
                for ii in range(0,2):
                    for jj in range(0,2):
                        population += LastGenWorld[row-ii][col-jj]
                if population == 3 :
                    NextGenWorld[row][col] = 1

        else :
            if cell == 1:
                population = -1
                for ii in range(0,2):
                    for jj in range(-1,2):
                        population += LastGenWorld[row-ii][col+jj]
                if population == 3 or population == 2 :
                    NextGenWorld[row][col] = 1
                else :
                    NextGenWorld[row][col] = 0

            #dead cell live in next Gen
            if cell == 0 :
                population = 0
                for ii in range(0,2):
                    for jj in range(-1,2):
                        population += LastGenWorld[row-ii][col+jj]
                if population == 3 :
                    NextGenWorld[row][col] = 1

    #First Column
    elif col == 0 :
        if  row != 0  and row != len(world)-1:
            if cell == 1:
                population = -1
                for ii in range(-1,2):
                    for jj in range(0,2):
                        population += LastGenWorld[row+ii][col+jj]
                if population == 3 or population == 2 :
                    NextGenWorld[row][col] = 1
                else :
                    NextGenWorld[row][col] = 0

            #dead cell live in next Gen
            if cell == 0 :
                population = 0
                for ii in range(-1,2):
                    for jj in range(0,2):
                        population += LastGenWorld[row+ii][col+jj]
                if population == 3 :
                    NextGenWorld[row][col] = 1


    #Last Column
    elif col == len(world[row])-1 :
        if  row != 0  and row != len(world)-1:
            if cell == 1:
                population = -1
                for ii in range(-1,2):
                    for jj in range(0,2):
                        population += LastGenWorld[row+ii][col-jj]
                if population == 3 or population == 2 :
                    NextGenWorld[row][col] = 1
                else :
                    NextGenWorld[row][col] = 0

            #dead cell live in next Gen
            if cell == 0 :
                population = 0
                for ii in range(-1,2):
                    for jj in range(0,2):
                        population += LastGenWorld[row+ii][col-jj]
                if population == 3 :
                    NextGenWorld[row][col] = 1
    else :
        #live cell in current gen
        if cell == 1 :
            #Check population
            population = -1 
            for ii in range(i-1,i+2):
                for jj in range(j-1,j+2):
                    population += LastGenWorld[ii][jj]
            
            #Live in next Generation
            if population == 2 or population == 3 :
                NextGenWorld[row][col] = 1

            #Dead in next Generation
            else :
                NextGenWorld[row][col] =  0


        #dead cell in current gen
        if cell == 0 :
            #Check population
            population = 0
            for ii in range(i-1,i+2):
                for jj in range(j-1,j+2):
                    population += LastGenWorld[ii][jj]

            #Live in next Generation
            if population == 3 :
                NextGenWorld[row][col] = 1




while True :

    #Show Next Generations


    #nextGen
    for rows in range(0,len(world)):
        for cols in range(0,len(world[row])):
            compareCells(rows , cols);


    for i in NextGenWorld :
        for j in i :
            if j==1 :
                print("{:^3}".format("#"),end='')
            else :
                print("{:^3}".format(" "),end='')
        print("\n")  
    
    time.sleep(0.2)
    system("clear")



    
    LastGenWorld = NextGenWorld

    NextGenWorld = list()
    for row in range(rowNumber):
        NextGenWorld.append(list())
        for col in range(colNumber):
            cells = 0
            NextGenWorld[row].append(cells)

# end file
