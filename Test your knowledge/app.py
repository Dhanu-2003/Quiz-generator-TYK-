from flask import Flask, render_template, request, jsonify
import example

app = Flask(__name__)

import mysql.connector as msc

myconn = msc.connect(host = '127.0.0.1',port = 3306,user='root',password='Dhanu@2003',database="TMK")

cursor = myconn.cursor()

top_sub = ["Maths","English","Genral Knowledge","Tamil","Biology","Chemistry",
           "Physics", "History","Economics","Civics","Geography","Computer",
           "Accountancy","Business","EVS","Physical Education","Information Practice","Applied Maths","Fine Arts"]

mail = ""
duration = ""
count = ""
title = ""
grade = ""
pos_mark = ""
neg_mark = ""
prac = ""


sub=""
mode=2

questions_list = []
opt_list= []
corr_list = []
selected_list = []
current_question = 0
review_que = []
leftover=''
total_correct = 0
total_wrong = 0
unattended = 0
ass=""
val = []
rem_tim = []
ass_lis=[]

@app.route('/')
def index():
    global mail,duration,pos_mark,neg_mark,prac,count,title,grade,questions_list,opt_list,corr_list,selected_list,current_question,review_que,val
    global total_correct,total_wrong,unattended,mode,ass_lis
    mail = ""
    duration = ""
    count = ""
    title = ""
    grade = ""
    pos_mark = ""
    neg_mark = ""
    prac = ""
    questions_list = []
    opt_list= []
    corr_list = []
    selected_list = []
    current_question = 0
    review_que = []
    total_correct = 0
    total_wrong = 0
    unattended = 0
    mode=2
    ass_lis=[]
    val=[]
    rem_tim = []
    return render_template("index.html",data = top_sub)

@app.route('/TMK/getname/<sub1>',methods=["POST","GET"])
def getname(sub1):
    global mail,duration,pos_mark,neg_mark,prac,count,title,grade,questions_list,opt_list,corr_list,selected_list,current_question,review_que,sub,ass_lis,val,rem_tim
    mail = ""
    duration = ""
    count = ""
    title = ""
    grade = ""
    pos_mark = ""
    neg_mark = ""
    prac = ""
    current_question = 0
    questions_list = []
    opt_list= []
    corr_list = []
    selected_list = []
    current_question = 0
    review_que = []
    sub=sub1
    ass_lis=[]
    val=[]
    rem_tim = []
    return render_template("page-2.html")

@app.route('/TMK/getdata', methods=["POST"])
def getdata():
    global mail
    mail = request.form.get("mail")
    return render_template("page-3.html")

@app.route('/TMK/getmarks', methods = ["POST"])
def getmarks():
    global duration,count,title,grade
    if mail=="":
        return index()
    duration = request.form.get("duration")
    title = request.form.get("title")
    grade = request.form.get("grade")
    count = request.form.get("count")
    for i in range(int(count)):
        selected_list.append(0)
        review_que.append(0)
 
    
    print(questions_list)
    print(duration, title, count, grade, type(duration))
    return render_template("page-4.html",data=[int(count)])

@app.route('/TMK/questions', methods = ['POST'])
def questions():
    global mail,duration,pos_mark,neg_mark,prac,count,title,grade,questions_list,opt_list,corr_list,selected_list,current_question,review_que,sub,val,rem_tim,ass_lis
    pos_mark = request.form.get("pos")
    neg_mark = request.form.get("neg")
    prac = request.form.get("prac")
    print(pos_mark,neg_mark,"================================")
    current_question = 0
    if(mail != ""and duration!=""and count!=""and title!=""and grade!=""and pos_mark!=""and neg_mark!=""and prac!=""):
        x = example.generate(int(count),sub,title,int(grade))
    else:
        mail = ""
        duration = ""
        count = ""
        title = ""
        grade = ""
        pos_mark = ""
        neg_mark = ""
        prac = ""
        questions_list = []
        opt_list= []
        corr_list = []
        selected_list = []
        current_question = 0
        sub=""
        review_que = []
        val=[]
        rem_tim = []
        ass_lis=[]
        return index()
    for i in x:
        print(i)
    questions_list = x[0]
    opt_list = x[1]
    corr_list = x[2]
    for i in range(int(count)):
        
        review_que.append('0')
        ass_lis.append("")
    if prac=="1":
        current_question = 0
        ass_lis[current_question] = example.getassistant(questions_list[current_question])
        return practice(curr_que = questions_list[0],cur_ans=opt_list[0],assist=ass_lis[current_question])
    return question()

@app.route('/TMK/question')
def question():
    global duration,pos_mark,neg_mark,prac,current_question,questions_list,opt_list
    if mail=="":
        return index()
    print("+++++++++++++",current_question,questions_list)
    print("\n\n\n")
    for i in range(len(questions_list)):
        print(questions_list[i])
        questions_list[i] = str(questions_list[i]).replace('"','').replace("'",'').replace("/",'')
        print("----------------------------")
    for i in range(len(opt_list)):
        print(opt_list[i])
        for j in range(len(opt_list[i])):
            opt_list[i][j] = str(opt_list[i][j]).replace('"','').replace("'",'').replace("/",'')
        print("----------------------------")
    
    print(prac,duration)
    print("\n\n\n")
  
    print(questions_list)
    print("----------------")
    print(opt_list)
    print("++++++++++++++++++++++++++++++++++++")
    return render_template("question.html",
                           data=[questions_list,opt_list,prac,duration,[i+1 for i in range(int(count))]])

@app.route('/TMK/prac/question/next/<marked>',methods=["POST","GET"])
def next(marked):
    global current_question,ass
    if mail=="":
        return index()
    print(questions_list[current_question])
    print(current_question)

    ans='0'
    if(duration==""):
        return index()
    
    if current_question+1!=int(count):
        selected_list[current_question] = marked
        current_question+=1
        if(ass_lis[current_question]==""):
            ass = example.getassistant(questions_list[current_question])
            ass_lis[current_question] = ass
        ass=ass_lis[current_question]
        if(selected_list[current_question]!="0"):
            if(chr(64+int(selected_list[current_question])).lower()==(corr_list[current_question].lower())):
                ans="1"
            else:
                ans='2'
                
        return practice(curr_que = questions_list[current_question],cur_ans=opt_list[current_question],assist=ass,ans=ans)
    return practice(curr_que = questions_list[current_question],cur_ans=opt_list[current_question],assist=ass,ans=ans)
    
@app.route('/TMK/prac/question')
def practice(curr_que,cur_ans,assist,ans='0'):
    global current_question
    if mail=="":
        return index()
    return render_template("prac.html",data=[curr_que,
                                             cur_ans,
                                             current_question,
                                             selected_list[current_question],
                                             current_question+1,
                                             ass_lis[current_question],
                                             ans,
                                             int(count)])


@app.route('/TMK/prac/question/prev/<marked>',methods=["POST","GET"])
def prev(marked):
    global current_question, questions_list,opt_list,ass
    if mail=="":
        return index()
    print(questions_list[current_question])
    print(current_question)
    print(marked)
    ans="0"
    if(duration==""):
        return index()
   
    if(current_question>=1):
        selected_list[current_question] = marked
        current_question-=1
        if(ass_lis[current_question]==""):
            ass = example.getassistant(questions_list[current_question])
            ass_lis[current_question] = ass
        ass=ass_lis[current_question]
        if(selected_list[current_question]!="0"):
            print(chr(64+int(selected_list[current_question])).lower(),(corr_list[current_question].lower()))
            if(chr(64+int(selected_list[current_question])).lower()==(corr_list[current_question].lower())):
                ans="1"
            else:
                ans='2'
                
        return practice(curr_que = questions_list[current_question],cur_ans=opt_list[current_question],assist=ass,ans=ans)
    return practice(curr_que = questions_list[current_question],cur_ans=opt_list[current_question],assist=ass,ans=ans)

@app.route('/TMK/prac/question/check/<marked>',methods=["POST","GET"])
def check(marked):
    global current_question, questions_list,opt_list,corr_list,ass
    print(questions_list[current_question])
    print(current_question)
    print(marked)
    if mail=="":
        return index()
    selected_list[current_question] = marked
    print(chr(64+int(selected_list[current_question])).lower(),(corr_list[current_question].lower()))
    if(chr(64+int(selected_list[current_question])).lower()==(corr_list[current_question].lower())):
        ans="1"
    else:
        ans='2'
    return practice(curr_que = questions_list[current_question],cur_ans=opt_list[current_question],assist=ass,ans=ans)

@app.route("/TMK/danalysis")
def danalysis():
    global total_correct,total_wrong,unattended,duration,leftover
    if mail=="":
        return index()
    return render_template("analysis.html",
                           data=[
                               int(count)-unattended,
                               unattended,
                               total_correct,
                               total_wrong,
                               total_correct*int(pos_mark),
                               total_wrong*int(neg_mark),
                               (total_correct*int(pos_mark)) - (total_wrong*int(neg_mark)),
                               int(duration)-leftover,
                               duration,
                               int(count)*int(pos_mark),
                               (int(count)-unattended)*int(neg_mark),
                               (int(count)-unattended)*int(pos_mark),
                               int(count)
                           ])

@app.route("/TMK/check_ans")
def check_ans():
    global current_question
    print(selected_list)
    print(opt_list)
    print(val)
    print(current_question)
    if mail=="":
        return index()
    curr_que = questions_list[current_question]
    cur_ans = opt_list[current_question]
    ans =val[current_question]
    assist=ass_lis[current_question]
    if(assist==""):
        ass_lis[current_question] = example.getassistant(questions_list[current_question])
    assist = ass_lis[current_question]
    
    return render_template("check_ans.html",data=[curr_que,
                                             cur_ans,
                                             current_question,
                                             selected_list[current_question],
                                             current_question+1,
                                             ass_lis[current_question],
                                             ans,
                                             int(count)])
@app.route("/TMK/next/check_ans")
def check_ans_next():
    global current_question,count
    if mail=="":
        return index()
    if((current_question)<int(count)):
        current_question += 1
   
    return  check_ans()
@app.route("/TMK/prev/check_ans")
def check_ans_prev():
    global current_question
    if mail=="":
        return index()
    if(current_question!=0):
        current_question -= 1
   
 
    
    return  check_ans()

@app.route("/TMK/analysis", methods = ['POST'])
def anaysis():
    global total_correct,total_wrong,unattended,duration,selected_list,leftover,unattended,mail,sub,val
    val=[]
    if mail=="" or sub=="":
        return index()
    count=len(questions_list)
    l=[]
    for i in range(int(count)):
        temp = request.form.get("optans"+str(i+1))
        l.append(chr(64+int(temp)))
        selected_list[i] = temp
        print(mail,'\n',sub,'\n',questions_list[i],'\n',''.join(opt_list[i]),'\n',selected_list,'\n',corr_list)
        cursor.execute("insert into solved values('{}','{}','{}','{}','{}','{}')".format(mail,sub,questions_list[i].replace("'",'"'),'$'.join(opt_list[i]),chr(int(selected_list[i])+64),str(corr_list[i])))
        myconn.commit()
    for i in range(int(count)):
        
        if l[i]=="@":
            unattended+=1
          
        elif l[i].lower() == corr_list[i].lower():
            total_correct+=1
        else:
            total_wrong+=1
        val.append(ord(corr_list[i].upper())-64)

    print(unattended)
    print(total_correct)
    print(total_wrong)
    leftover = int(request.form.get("timeleft-1"))
    data= [int(count),
           unattended,
           total_correct,
           total_wrong,
           int(total_correct)*int(pos_mark),
           int(total_wrong)*int(neg_mark),
           (int(count)-int(unattended))*int(pos_mark),
           (int(count)-int(unattended))*int(neg_mark),
           int(count)*int(pos_mark),
           duration,
           leftover]
    rank1 = round((int(total_correct)/int(count))*100,2)
    strdata = ''.join([str(data[i])+"$" for i in range(len(data))])
    if mail!="":
        cursor.execute("select data1 from history where subject='{}' && mail_id='{}'".format(sub.lower(),mail.lower()))
        dta = list(cursor.fetchall())
        cursor.execute("select percentage from stu_rank where subject='{}' && mail_id='{}'".format(sub,mail))
        dta1 = list(cursor.fetchall())
        print(dta,dta1)
        if dta==[]:
            query = "insert into history values('{}','{}','{}')".format(mail.lower(),sub.lower(),strdata.lower())
            cursor.execute(query)
            myconn.commit()
        else:
            temp1=dta[0][-1]
            pre_data = list(map(int,temp1[0:len(temp1)-1:].split("$")))
            for i in range(len(data)):
                pre_data[i]+=int(data[i])
            strdata = [str(pre_data[i])+"$" for i in range(len(pre_data))]
            query = "update history set data1='{}' where subject='{}' && mail_id='{}';".format(''.join(strdata).lower(),sub.lower(),mail.lower())
            cursor.execute(query)
            myconn.commit()
        if dta1==[]:
            query1 = "insert into stu_rank values('{}','{}','{}')".format(mail.lower(),sub.lower(),rank1)
            cursor.execute(query1)
            myconn.commit()
        else:
            temp2 = round((float(dta1[0][-1])+rank1)/2,2)
            query2 = "update stu_rank set percentage='{}' where subject='{}' && mail_id='{}';".format(temp2,sub.lower(),mail.lower())
            cursor.execute(query2)
            myconn.commit()

    cursor.reset()
            
    # Process js_list as needed
    return render_template("analysis.html",
                           data=[
                               int(count)-unattended,
                               unattended,
                               total_correct,
                               total_wrong,
                               total_correct*int(pos_mark),
                               total_wrong*int(neg_mark),
                               (total_correct*int(pos_mark)) - (total_wrong*int(neg_mark)),
                               int(duration)-leftover,
                               duration,
                               int(count)*int(pos_mark),
                               (int(count)-unattended)*int(neg_mark),
                               (int(count)-unattended)*int(pos_mark),
                               int(count)
                           ])



@app.route('/TMK/his_exe')
def his():
    global mode,mail
    if mail=="":
        return index()
    cursor.execute("select subject from history where mail_id='{}'".format(mail))
    d1 = set(cursor.fetchall())
    cursor.reset()
    return render_template("his_exe.html",data=[list(i)[0] for i in d1])
@app.route('/TMK/his/que/<sub1>',methods=['post','get'])
def his_seq(sub1):
    global sub
    if mail=="":
        return index()
    sub = sub1
    return canalysis()


@app.route("/TMK/canalysis")
def canalysis():
    global total_correct,total_wrong,unattended,duration,leftover,sub,mail,mode
    if mail=="":
        return index()
    cursor.execute("select data1 from history where subject='{}' && mail_id='{}'".format(sub,mail))
    data1 = cursor.fetchall()[0][-1]
    temp_data = list(map(int,data1[0:len(data1)-1:].split("$")))
    """ data= [int(count),
           unattended,
           total_correct,
           total_wrong,
           int(total_correct)*int(pos_mark),
           int(total_wrong)*int(neg_mark),
           (int(count)-int(unattended))*int(pos_mark),
           (int(count)-int(unattended))*int(neg_mark),
           int(count)*int(pos_mark),
           duration,
           leftover] """
    return render_template("cana.html",
                           data=[
                               temp_data[0]-temp_data[1],
                               temp_data[1],
                               temp_data[2],
                               temp_data[3],
                               temp_data[4],
                               temp_data[5],
                               temp_data[4] - temp_data[5],
                               temp_data[9]-temp_data[10],
                               temp_data[9],
                               temp_data[8],
                               temp_data[7],
                               temp_data[6],
                               temp_data[0],
                               mode
                           ])



@app.route('/TMK/rank/<sub1>',methods=["POST","GET"])
def rank(sub1):
    global sub,mode
    sub=sub1
    mode=2
    return render_template("get_mail.html")


@app.route('/TMK/your_rank')
def your_rank():
    global mail,sub
    if mail=="":
        return index()
    print(sub)
    cursor.execute("select mail_id,percentage from stu_rank where subject='{}'".format(sub))
    dump = {}
    for i in cursor:
        dump[i[0]] = i[1]
    datatemp = sorted(dump,key=lambda x:round(float(dump[x]),2),reverse=True)
    senddata = []
    mydata = []
    counttemp=1
    print(dump)
    for i in datatemp:
        if i.lower()!=mail.lower():
            senddata.append([counttemp,i,dump[i],sub])
        else:
            mydata = [counttemp,i,dump[i],sub]
        counttemp+=1
    print([senddata,mydata])
    return render_template("rank1.html",data=[senddata,mydata])



@app.route('/TMK/gm/<m>',methods=["POST","GET"])
def get_mail(m):
    global mode,ass_lis
    ass_lis=[]
    mode = int(m)
    return render_template("get_mail.html")
@app.route("/TMK/show",methods=["post"])
def show():
    global mode,mail
    mail=request.form.get("mail")
    print(mail)
    print(mode)
    if mode==0:
        return se()
    elif mode==1:
        return his()
    else:
        return your_rank()


@app.route('/TMK/solved_exe')
def se():
    global mail
    if mail=="":
        return index()
    cursor.execute("select subject from solved where mail_id='{}'".format(mail))
    d1 = set(cursor.fetchall())
    cursor.reset()

    return render_template("solved_example.html",data=[list(i)[0] for i in d1])
@app.route('/TMK/se/que/<sub1>',methods=['post','get'])
def seq(sub1):
    global sub
    sub = sub1
    return  seq1()
@app.route('/TMK/se/que')
def seq1():
    global sub,opt_list,questions_list,corr_list,selected_list,current_question,count,mail
    if mail=="":
        return index()
    current_question=0
    opt_list,questions_list,corr_list,selected_list=[],[],[],[]
    if sub=="":
        return index()
    cursor.execute("select question,option1,opted,answer from solved where subject='{}' && mail_id='{}'".format(sub,mail))
    d1 = [list(i) for i in cursor.fetchall()]
    count = len(d1)
    dup = []
    for i in range(count):
        d1[i].append(i+1)
        questions_list.append(d1[i][0])
        opt_list.append(d1[i][1])
        corr_list.append(ord(d1[i][3].upper())-64)
        selected_list.append(ord(d1[i][2].upper())-64)
        ass_lis.append("")
        
    cursor.reset()
    print(d1)
    return render_template("solved_exe_que.html",data = d1)

@app.route("/TMK/check_ans/<opt>",methods=["post","get"])
def check_ans1(opt):
    global current_question,count
    if mail=="":
        return index()
    current_question = int(opt)
    curr_que = questions_list[current_question]
    cur_ans = list(opt_list[current_question].split("$"))
    ans = corr_list[current_question]
    if ass_lis[current_question]=="":
        ass_lis[current_question] = example.getassistant(questions_list[current_question])
    assist = ass_lis[current_question]
    return render_template("sol_exe_check_ans.html",data=[curr_que,
                                             cur_ans,
                                             current_question,
                                             selected_list[current_question],
                                             current_question+1,
                                             ass_lis[current_question],
                                             ans,
                                             int(count)])

@app.route("/TMK/se/que/next")
def se_next():
    global current_question,count
    if mail=="":
        return index()
    if(current_question<count+1):
        current_question+=1
    print(current_question)
    return seq(current_question)
@app.route("/TMK/se/que/prev")
def se_prev():
    global current_question
    if(current_question>1):
        current_question-=1
    return seq(current_question)
    


    
""" 
    print(optd.split(","))
 
 
    return render_template("analysis.html") """
   



if __name__=='__main__':
    app.run(debug=True)
