#for loops repeat code for specific sequence 

for i in [1,3,5,6]:
    print(i)
    
range(0,10) # --> generate sequence numbers   form 0 to 10
range(0,5,1) # --> secuence number include 0, but not the 5  from 0 to 4 with iteration 1

for i in range(10):
    print("Cannot connect  to the destination")
    
time = 10
while  time <= 10:
    print(time)
    time= time + 2
 
 
 #Uses of <break> in the loops as for
computers = ["Asus", "Mac", "HP"];
for i in computers:
    if i == "Mac":
        break # break the (for) when find :"Mac" in the array 
    print(i)
    
    
letters = ["A","B","C","D","E","F","G","H","I"];
for word in letters:
    if word == "C":
        continue # the used of continue is for that if letter is equal a <"C"> the for continue wiht the iteration
    print(word)
    
#LOOP INFINITES, for stop this loops to be pressing  in the keyborad CTRL-C o CTRL-Z    


#Task 01

allow_list = ["192.168.243.140", "192.168.205.12", "192.168.151.162", "192.168.178.71", 
              "192.168.86.232", "192.168.3.24", "192.168.170.243", "192.168.119.173"]

ip_addresses = ["192.168.142.245", "192.168.109.50", "192.168.86.232", "192.168.131.147",
                "192.168.205.12", "192.168.200.48"]

for i in ip_addresses:
    if i in allow_list:
        print("IP address is allowed")
    else:
        print("IP address is not allowed")    
        break