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
                    if arg_list[i-1]!=0:#0除算出ない場合
                        arg_list[i-2]=arg_list[i-2]/arg_list[i-1]#割る
                    else:#0除算の場合
                        print("注意!!\n0で除算されました")#警告を出す
                        arg_list[i-2]=0#0を返す（仕様）
                del arg_list[i-1]#空いたリスト2つを削除
                del arg_list[i-1]
                break
    print(arg_list[i-2])#計算結果を出力

pass_list = [4,1,2,"+",0,"/","*"]#逆ポーランド記法のリストを作成
calc(pass_list)#逆ポーランド記法を渡す

