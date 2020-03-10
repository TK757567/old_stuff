import random
snake_string = """
             ____                         
            / . .\\            
            \  ---<            
             \  /
   __________/ /
-=:___________/
"""


print("wlecome to python3!\n")
print(snake_string)
print("jan ken po game\n")
answer=["rock","paper","scissor"]
streak=0
robot_streak=0
human_streak=0
print("rock=0 , paper=1 , scissor=2 ")

while human_streak<3 or robot_streak<3:
    x=random.randint(0,2)
    robot=answer[x]
    human=int(input("enter your answer: "))
    if human<0 or human>2:
        print("enter ur answer correctly idiot")
        continue
    if answer[human]==robot:
        print(answer[human],robot+"\n")
        print("draw!hmmm not bad human\n")



    elif answer[human]=="rock" and robot=="paper":
        print(answer[human],robot+"\n")
        print("haha idoit\n")
        streak+=1
        robot_streak+=1


    elif answer[human]=="rock"and robot=="scissor":
        print(answer[human], robot+"\n")
        print("lucky human\n")
        streak+=1
        human_streak+=1


    elif answer[human]=="paper" and robot=="rock":
        print(answer[human], robot+"\n")
        print("lucky human\n")
        streak+=1
        human_streak+=1


    elif answer[human]=="paper" and robot=="scissor":
        print(answer[human], robot+"\n")
        print("hahaha idiot\n")
        streak+=1
        robot_streak+=1

    elif answer[human]=="scissor" and robot=="paper":
        print(answer[human], robot+"\n")
        print("lucky human\n")
        human_streak+=1
        streak+=1

    elif answer[human]=="scissor"and robot=="rock":
        print(answer[human], robot+"\n")
        print("hahaha idiot\n")
        robot_streak+=1
        streak+=1


    if human_streak==3 or robot_streak==3:
        break


print("human= {} , robot= {}".format(human_streak,robot_streak))
if robot_streak>human_streak:
    print("try harder")

elif human_streak>robot_streak:
    print("the human has a 200 iq")
