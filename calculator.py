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
                break
    print(arg_list[i-2])#計算結果を出力
    return

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

def conv_RPN(rpn):#中間記法を逆ポーランド記法へ変換する
    pass
import sys#コマンドライン引数を受け取る
del sys.argv[0]#ファイル名削除
print(sys.argv)
for i in range(len(sys.argv)):#引数の型をただす
    sys.argv[i]=conv_ch_to_num(sys.argv[i])
print(sys.argv)

#pass_list = [4,1,2,"+",0,"/","*"]#逆ポーランド記法のリストを作成
#calc(pass_list)#逆ポーランド記法を渡す

