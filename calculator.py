def calc(arg_list):
    while len(arg_list)>1:
        for i in range(len(arg_list)):
            if isinstance(arg_list[i],str):
                if(arg_list[i]=='+'):
                    arg_list[i-2]+=arg_list[i-1]
                elif(arg_list[i]=='*'):
                    arg_list[i-2]*=arg_list[i-1]
                elif(arg_list[i]=='-'):
                    arg_list[i-2]-=arg_list[i-1]
                elif(arg_list[i]=='/'):
                    arg_list[i-2]=arg_list[i-2]/arg_list[i-1]
                del arg_list[i-1]
                del arg_list[i-1]
                break
    print(arg_list[i-2])


pass_list = [4,1,2,"+",2,"/","*"]
calc(pass_list)

