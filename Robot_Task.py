def matrix(x,y):
    row1=[0,0,0,0,0]
    row2=[0,0,0,0,0]
    row3=[0,0,0,0,0]
    row4=[0,0,0,0,0]
    row5=[0,0,0,0,0]
    matrix=[row1,row2,row3,row4,row5]
    rownum=int(x)
    columnum=int(y)
    sele_row=matrix[rownum-1]
    sele_row[columnum-1]='x'
    print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n")





def move_robot(command):
    global x , y    
    
    direction = command[0].upper() 
    steps = int(command[1:])       
    if direction == 'N':
        if 1 < x:
            x -=1
            
    elif direction == 'S':
        if  x<rows:
            x +=1
            
    elif direction == 'E':
        if y<=cols:
            y +=1
    elif direction == 'W':
        if y >0:
            y -= 1
    
                             
    
    else:
        print("Invalid direction! Use N, S, E, or W.")
        
    print(f"Robot moved to {command} :({x}, {y})")
    matrix(x,y)
    
rows = 5
cols = 5

x = 3
y = 3

print(f"Robot starting at ")
matrix(x,y)

while 1:
    move_robot(input('Input only N1,E2,S3,W4 Move the Robot  :'))

    
    

