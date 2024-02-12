# open file text with python

## READ
with open("loguin-file.txt","r") as file:
    file_text = file.read()
print(file_text.split()) # this form the data is covert to lists

##WRITE
with open("file_example.csv", "a") as file:
    file.write("I am learning python")

# convert string to list
"HELLO".split # [H,E,L,L,O]


#Algorithm for reviewing users that is block for more 3 attempts
def loguin_check(loguin_list,current_user):
    counter = 0
    for i in loguin_list:
        if i == current_user:
            counter = counter + 1
    
    if counter >= 3 :
        return "You user is blocked"        
    else:
        return "You can log in"
    
    
# Algotihm activity

def check_ip(list_ip,list_remove):
    list_adress = list_ip.split()
    for i in list_remove:
        for j in list_adress:
            if i == j:
                list_ip.remove(j)
    list_adress = " ".join(list_adress)                
    return list_adress


if 5> 10:
    print("Hello")
el    
                
    
