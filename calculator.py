#-----------------------------------------------------------------------------#
def calc(arg_list):#逆ポーランド記法を受け取り，計算結果を返すメソッド
    while len(arg_list)>1:#リストがただ一つの数値となった場合計算を終了する
        for i in range(len(arg_list)):#リストの個数分
            if isinstance(arg_list[i],str):#文字列すなわち演算子ならば
                if arg_list[i]=='+':#足し算ならば
                    arg_list[i-2]+=arg_list[i-1]#足す
                elif arg_list[i]=='*':
                    arg_list[i-2]*=arg_list[i-1]
                elif arg_list[i]=='-':
                    arg_list[i-2]-=arg_list[i-1]
                elif arg_list[i]=='/':
                    if arg_list[i-1]!=0:#0除算でない場合
                        arg_list[i-2]=arg_list[i-2]/arg_list[i-1]#割る
                    else:#0除算の場合
                        print("注意!!\n0で除算されました")#警告を出す
                        arg_list[i-2]=0#0を返す（仕様）
                del arg_list[i-1]#空いたリスト2つを削除
                del arg_list[i-1]
                print(arg_list)
                break
    print(arg_list[i-2])#計算結果を出力
    return
#-----------------------------------------------------------------------------------#
def conv_ch_to_num(ch):#文字列を数値に変換可能か確認する
    comma=0
    if ch.rfind(".")!=-1:#"."を含むかどうか
        comma=len(ch)-ch.rfind(".")-1#コンマの場所を記憶
        ch=ch.replace(".","")#isdigitは小数に対応していないので一時的にコンマを削除
    if ch.isdigit():#数値かどうか
        ch = int(ch)/(10**(comma))#数値なら小数を直す
        return ch
    else :
        return ch
#------------------------------------------------------------------------------------#
def conv_RPN(rpn):#中間記法を逆ポーランド記法へ変換する
    nest = 0
    maxnest=0
    remove_list = []
    rpn_nest = []
    for i in range(len(rpn)):
        if rpn[i]=='(':
            nest+=1
            rpn_nest.append(-2)
            remove_list.append(i)
        elif rpn[i]==')':
            nest-=1
            rpn_nest.append(-2)
            remove_list.append(i)
        elif rpn[i]== '*' or rpn[i]=='/':
            rpn_nest.append(2*nest+2)
            if 2*nest+2>maxnest:
                maxnest=2*nest+2
        elif rpn[i]== '+' or rpn[i]=='-':
            rpn_nest.append(2*nest+1)
            if 2*nest+1>maxnest:
                maxnest=2*nest+1
        else :
            rpn_nest.append(0)
    print(rpn_nest)
    print("最大深さ："+str(maxnest))
#---*---*---*---*---*---*---*---*---*---*---*---*---*---*---*---*---*---*---*---*#
    for i in range(len(remove_list)):#括弧の部分を削除
        del rpn[remove_list[i]-i]
        del rpn_nest[remove_list[i]-i]
    for i in range(maxnest):
        search_nest=maxnest-i
        search_index=0
        while search_index<len(rpn):
            if rpn_nest[search_index]==search_nest:
                index=search_index+1
                while index<len(rpn):
                    if rpn_nest[index]>0:
                        rpn_nest.insert(index,rpn_nest[search_index]*-1)
                        del rpn_nest[search_index]
                        rpn.insert(index,rpn[search_index])
                        del rpn[search_index]
                        print(rpn_nest)
                        print(rpn)
                        break
                    if index==len(rpn)-1:
                        rpn_nest.append(rpn_nest[search_index]*-1)
                        del rpn_nest[search_index]
                        rpn.append(rpn[search_index])
                        del rpn[search_index]
                        print(rpn_nest)
                        print(rpn)
                        break
                    index+=1
            search_index+=1

    print(rpn_nest)
    print(rpn)
    return rpn

#------------------------------(メイン)--------------------------------------#
#import sys#コマンドライン引数を受け取る
#del sys.argv[0]#ファイル名削除
#print(sys.argv)
while 1:
    print("半角スペース区切りで計算式を入力\n括弧付き計算可能\n[end]で終了")
    input_list = ""
    input_list = input()
    input_list = input_list.split()
    if input_list[0] == "end":
        break
    print(input_list)
    for i in range(len(input_list)):#引数の型をただす
        input_list[i]=conv_ch_to_num(input_list[i])
    print()
    calc(conv_RPN(input_list))


