# Import the Python SDK
import google.generativeai as genai
# Used to securely store your API key


genai.configure(api_key="YOUR_API_KEY")
total = 0
model = genai.GenerativeModel('gemini-pro')
def getassistant(question):
    response = model.generate_content("Generate a way to solve the question {}. Don't tell the answer".format(question))
    try:
        return response.text.replace("`",'').replace("**",'').replace("***",'')
    except:
        getassistant(question)
def generate(count,sub,tit,gra):
    global total
    total = int(count)
    question = []
    answer = []
    sub_ans = []
    corr_ans = []
    while(count>0):
        response = model.generate_content("Generate {} mcq with 4 options on the subject {} title{} for grade {} with seperate answers key".format(10,sub,tit,gra))
        q_count=0
        sub_ans = []
        dquestion = []
        danswer = []
        sub_ans = []
        dcorr_ans = []
    
        data = response.text.split("\n")
        ans_sec = 0

        for i in data:
            print(i)
            print("____________________________")
        for i in range(len(data)):
            data[i] = data[i].replace("\n","")
            data[i] = data[i].replace("*","")
            
            data[i] = data[i].strip()
        for i in data:
            if "answer" in i.lower():
                ans_sec = 1
                danswer.append(sub_ans)
            elif ans_sec and i!="":
                for j in i:               
                    if j.isalpha():
                        dcorr_ans.append(j)
                        break
            elif i!="":
                if q_count%5==1:
                    if sub_ans!=[]:
                        danswer.append(sub_ans)
                        sub_ans = []
                    dquestion.append(' '.join(i.split()[1::]))
                    """ print("----------------Question------------")
                    print(i,q_count)
                    print("----------------------------------------") """
                elif q_count!=0:
                    sub_ans.append(' '.join(i.split()[1::]))
                q_count+=1
        if len(danswer)==len(dquestion) and len(dquestion)==len(dcorr_ans) and len(dquestion)!=0:
            answer.extend(danswer)
            corr_ans.extend(dcorr_ans)
            question.extend(dquestion)
            print(len(answer),len(question),len(corr_ans))
            print(question)
            print("_____________________")
            print(answer)
            print("____________________")
            print(corr_ans)
            print("__________________________")

            print()
            count-=10
        else:
            print("Invalid Response Trying again....")
            print(len(answer), len(question), len(corr_ans))
            print(answer)
            print(question)
            print(corr_ans)
            dquestion = []
            danswer = []
            sub_ans = []
            dcorr_ans = []
    return [question[0:total],answer[0:total],corr_ans[0:total]]
       

    
        
""" 
print(data) """