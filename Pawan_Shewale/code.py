# --------------
##File path for the file 
file_path 



#Code starts here

def read_file(path):
    file=open(path,'r')
    sentence=file.readline()
    return sentence
    file.close()

sample_message=read_file(file_path)
print(sample_message)


# --------------
#Code starts here
message_1=read_file(file_path_1)
message_2=read_file(file_path_2)

print(message_1)
print(message_2)
print(type(message_1))

def fuse_msg(message_a,message_b):
    quotient=int(message_b)//int(message_a)
    return str(quotient)

secret_msg_1=fuse_msg(message_1,message_2)

print(secret_msg_1)





# --------------
#Code starts here
message_3=read_file(file_path_3)

print(message_3)

def substitute_msg(message_c):
    if message_c=='Red':
        sub='Army General'
    elif message_c=='Green':
        sub='Data Scientist'
    elif message_c=='Blue':
        sub='Marine Biologist'
    else:
        print("Message is not in Red,Green and Blue")
    return sub

secret_msg_2=substitute_msg(message_3)

print(secret_msg_2)





# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

#Code starts here
message_4=read_file(file_path_4)
message_5=read_file(file_path_5)

print(message_4)
print(message_5)
c_list=[]
def compare_msg(message_d,message_e):
    a_list=message_d.split()
    b_list=message_e.split()
    print(a_list)
    print(b_list)
    print(len(a_list))

    for i in range(1,len(a_list)):
        if (a_list[i]) not in b_list:
            c_list.append(a_list[i])
    print(c_list)  
    final_msg=" ".join(c_list)
    return final_msg

secret_msg_3=compare_msg(message_4,message_5)
print(secret_msg_3)




# --------------
#Code starts here
message_6=read_file(file_path_6)
print(message_6)
def extract_msg(message_f):
    a_list=message_f.split()
    even_word= lambda x: ((len(x))%2==0)
    b_list=filter(even_word,a_list)
    final_msg=" ".join(b_list)
    return final_msg

secret_msg_4=extract_msg(message_6)
print(secret_msg_4)



# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]


final_path= user_data_dir + '/secret_message.txt'

#Code starts here
secret_msg=" ".join(message_parts)
print(secret_msg)
def write_file(secret_msg,path):
    file_new=open(path,"a+")
    file_new.write(secret_msg)
    file_new.close
    #return file_new

write_file(secret_msg,final_path)
print(secret_msg)



