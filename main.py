from tkinter import *
app = Tk()
app.title('COVIDx')
app.minsize(500,400)
app.config(bg="#1b1464")
app.iconbitmap('icon.ico')

def ree():
    label.pack()

def b_gov():
    asking_u_g.config(text='Create or login?\n')
    b_help_about.destroy()
    button_user.destroy()
    button_gov.destroy()
    wannaCreate.pack()
    wannaLogin.pack()

def Wcreate():
    asking_u_g.config(text='enter your email and password to create an account\n')
    wannaCreate.destroy()
    wannaLogin.destroy()
    title_email.pack()
    box_email.pack()
    title_pass.pack()
    box_pass.pack()
    b1_create.pack()
    L_invalid.pack()

ctrs={'mohp.gov.eg':'Egypt','hhs.gov':'USA'}
def creating():
    global ctrs
    # for making a file and read it
    ml_gv_old = open('emails_gov.txt', 'r').read()
    ml_gv_new = open('emails_gov.txt', 'w')
    email = box_email.get()
    login_domain=str(email).split('@')[1]

    if '@' and '.' not in list(email):
        L_invalid.config(text='enter a valid email')
        return
    if login_domain not in ctrs.keys():
        L_invalid.config(text='enter a gov acc')
        return
    password = box_pass.get()
    chk1 = chk2 = chk3 = chk4 = True
    if len(password) >= 6:
        chk1 = False
    for i in list(password):
        if i.islower():
            chk2 = False
        if i.isupper():
            chk3 = False
        if i.isnumeric():
            chk4 = False

    print(password, len(password), chk1 or chk2 or chk3 or chk4)

    if chk1 or chk2 or chk3 or chk4:
        L_invalid.config(text='password must be at least 6 chrs and have UPPER, lower and numbers')
        return

    L_invalid.config(text='donnnnnnnnnnnnnnne')
    ml_gv_new.write(f'{ml_gv_old}\n{email} ::: {password}')



def Wlogin():
    wannaCreate.destroy()
    wannaLogin.destroy()
    title_email.pack()
    box_email.pack()
    title_pass.pack()
    box_pass.pack()
    b1_login.pack()
    L_invalid.pack()

def after_login():
    print('aaa')
    title_email.destroy()
    box_email.destroy()
    title_pass.destroy()
    box_pass.destroy()
    b1_login.destroy()
    L_invalid.destroy()
    b_go_cretae.destroy()
    L_invalid.destroy()
    asking_u_g.destroy()
    welcome_email.pack()
    print(save_email)
    n_cases.pack()
    bn_cases.pack()
    n_deaths.pack()
    bn_deaths.pack()
    n_rec.pack()
    bn_rec.pack()
    n_vac.pack()
    bn_vac.pack()
    b_submit.pack()

save_email=' '
save_country=' '
def logging():
    global save_email,save_country
    file1= open('emails_gov.txt', 'r')
    ml_gv= file1.read().split('\n')
    ml_gv[0] = '00 ::: 00'
    for i in range(len(ml_gv)):
        ml_gv[i] = ml_gv[i].split(' ::: ')
        # print(ml_gv[i])
        # print(dict(ml_gv))
    dict_gov=dict(ml_gv)
    users = list(dict_gov.keys())
    usersPass = list(dict_gov.values())

    login_email = box_email.get()
    login_pass = box_pass.get()
    login_domain=str(login_email).split('@')[1]
    ctrs={'mohp.gov.eg':'Egypt','hhs.gov':'USA'}
    if login_email in users and login_pass == dict_gov[login_email]:
        L_invalid.config(text='esta')
        save_email=str(login_email)
        save_country=ctrs[login_domain]
        after_login()
    else:
        L_invalid.config(text='there is no account like this')
        b_go_cretae.pack()
        file1.close()


def symptoms_calc():
   var_all=var1.get()+var2.get()+var3.get()+var4.get()+var5.get()+var6.get()+var7.get()+var8.get()
   Label(app, text=f'you are  {var_all / 0.08}% likely to have coronavirus. ',bg='#1b1464',fg='#00ffc5').grid(row=12, sticky=W)

def saving_data():
    id1.get()


def user_symptoms():
    welcome.destroy()
    asking_u_g.destroy()
    button_user.destroy()
    button_gov.destroy()
    b_help_about.destroy()
    Label(app, text="Enter your name",bg='#1b1464',fg='#00ffc5').grid(row=0, sticky=W)
    name1.grid(row=0, sticky=E)
    Label(app, text="your national ID",bg='#1b1464',fg='#00ffc5').grid(row=1, sticky=W)
    id1.grid(row=1, sticky=E)
    Label(app, text="\nCheck the symptoms you have",bg='#1b1464',fg='#00ffc5').grid(row=2, sticky=W)
    Checkbutton(app, text="fever", variable=var1,bg='#1b1464',fg='#00ffc5').grid(row=3, sticky=W)
    Checkbutton(app, text="dry cough", variable=var2,bg='#1b1464',fg='#00ffc5').grid(row=4, sticky=W)
    Checkbutton(app, text="tiredness", variable=var3,bg='#1b1464',fg='#00ffc5').grid(row=5, sticky=W)
    Checkbutton(app, text="aches and pains", variable=var4,bg='#1b1464',fg='#00ffc5').grid(row=6, sticky=W)
    Checkbutton(app, text="loss of taste or smell", variable=var5,bg='#1b1464',fg='#00ffc5').grid(row=7, sticky=W)
    Checkbutton(app, text="sore throat", variable=var6,bg='#1b1464',fg='#00ffc5').grid(row=8, sticky=W)
    Checkbutton(app, text="chest pain or pressure", variable=var7,bg='#1b1464',fg='#00ffc5').grid(row=9, sticky=W)
    Checkbutton(app, text="difficulty breathing or shortness of breath", variable=var8,bg='#1b1464',fg='#00ffc5').grid(row=10, sticky=W)
    Button(app, text='how likely I have corona?', command=symptoms_calc,bg='#00ffc5').grid(row=11, sticky=W, pady=4)
    Button(app, text=' recommend some medicine', command=rec_med,bg='#00ffc5').grid(row=13, sticky=W, pady=4)
    Button(app, text='save my data', command=saving_data, bg='#00ffc5').grid(row=15, sticky=W, pady=4)

def rec_med():
    global var1,var2,var6,var3,var7,var8,var4,var5
    med=[]
    if var1.get()==1 or var3.get()==1:
        med.append('Paracetamol')
    if var2.get()==1 or var5.get()==1:
        med.append('benzonatate')
    if var4.get()==1 or var6.get()==1:
        med.append('Acetaminophen')
    if var7.get() == 1:
        med.append('Nitroglycerin ')
    if var8.get() == 1:
        med.append('Ativan')
    medT=''
    if len(med)==0:
        medT='you are a healthy person'
    else:
        for i in range(len(med)):
            if i == len(med)-1:
                medT += f'and {med[i]}'
            else:
                medT+=f'{med[i]}, '
    you_get=Label(app, text='',bg='#1b1464',fg='#00ffc5')
    you_get.grid(row=14, sticky=W)
    if len(med)==0:
        you_get.config(text=f'{medT}')
    else:
        you_get.config(text=f'you have to get {medT}')
    print(med,medT)

canvas = Canvas(app, width=190, height=140)
img = PhotoImage(file="phelo0.png")
def help_about():
    asking_u_g.destroy()
    button_user.destroy()
    button_gov.destroy()
    b_help_about.destroy()
    Label(app, text="This program is programed by\nMoustafa Ashmawy & Phelopater Ramsis\n", font='Arial 15',bg='#1b1464',fg='#00ffc5').pack()
    canvas.pack()
    canvas.create_image(0, 0, anchor=NW, image=img)
    Label(app, text="Thanks to Dr. Moh Sameer\nSpecial thanks to Dr. Gamal Zayed", font='Arial 15',bg='#1b1464', fg='#00ffc5').pack()
    Label(app, text="\nThis is how to use the program", font='Arial 15',bg='#1b1464', fg='#00ffc5').pack()
    Label(app, text='''Using GUI, we created a simple interface for the user, even if was for the government 
of the user. Anyone who starts to start our program will face a tab which asks him/her if he/she
is a government or a user, then the user or government starts to log in or create an 
account:
A) if government: they will update numbers of new cases, death, doses, treated 
people, and date and start to arrange them with specific timeline.
B) if the user: he will choose his symptoms, and will gain a lot of information like how 
% precent he/she has corona, the recommended medicines, and near hospitals with 
their contact.
C) that information even it was inserted from each government or the user. Both of 
them will be used in producing statistics.
''', font='Arial 11',bg='#1b1464',fg='#00ffc5').pack()



def submitting():
    data_old=open('data.txt','r').read()
    data=open('data.txt','w')
    data.write(f'{data_old}\n{bn_cases.get()} : {bn_deaths.get()} : {bn_rec.get()} : {bn_vac.get()}')
    data.close()
    label.pack()



#ree
label=Label(app, text='saved')
#user or gov
welcome = Label(app, text="Welcome in COVIDx program\n",font='Arial 20 bold',bg='#1b1464',fg='#00ffc5')
asking_u_g=Label(app, text="\nAre you a government or a user?\n",font='Arial 14',bg='#1b1464',fg='#00ffc5')
button_gov= Button(text='gov',command=b_gov,height=2,width=10,font='Arial 12',bg='#00ffc5')
button_user= Button(text='user',command=user_symptoms,height=2,width=10,font='Arial 12',bg='#00ffc5')
b_help_about= Button(text='about or help',command=help_about,height=2,width=13,font='Arial 10',bg='#ec008c')
welcome.pack()
asking_u_g.pack()
button_gov.pack()
button_user.pack()
b_help_about.pack(side=BOTTOM)
#gov
wannaCreate = Button(text='create', command=Wcreate,bg='#00ffc5')
wannaLogin = Button(text='login', command=Wlogin,bg='#00ffc5')
#wcreate
title_email = Label(text='email',bg='#1b1464',fg='#00ffc5')
title_pass = Label(text='password',bg='#1b1464',fg='#00ffc5')
box_email = Entry(bg='#1b1464',fg='#ec008c')
box_pass = Entry(bg='#1b1464',fg='#ec008c')
#creating
L_invalid=Label(text=' ',bg='#1b1464',fg='#00ffc5')
b1_create= Button(text='create', command=creating,bg='#00ffc5')
#logging
b1_login= Button(text='login', command=logging,bg='#00ffc5')
#go_create
b_go_cretae=Button(text='create new account', command=creating,bg='#00ffc5')
#Symptoms_calc
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
name1=Entry(bg='#1b1464',fg='#ec008c')
id1=Entry(bg='#1b1464',fg='#ec008c')
#help_out


#after_login
welcome_email=Label(app, text=f"\nWelcome #name#{save_email.split('@')[0]} from #ctr#{save_country}\n",font='Arial 14',bg='#1b1464',fg='#00ffc5')
n_cases = Label(text='new cases',bg='#1b1464',fg='#00ffc5')
bn_cases = Entry(bg='#1b1464',fg='#ec008c')
n_deaths = Label(text='new deaths',bg='#1b1464',fg='#00ffc5')
bn_deaths = Entry(bg='#1b1464',fg='#ec008c')
n_rec = Label(text='new recoveries',bg='#1b1464',fg='#00ffc5')
bn_rec = Entry(bg='#1b1464',fg='#ec008c')
n_vac = Label(text='new vaccinated',bg='#1b1464',fg='#00ffc5')
bn_vac = Entry(bg='#1b1464',fg='#ec008c')
b_submit= Button(text='submit data',command=submitting,height=2,width=10,font='Arial 12',bg='#00ffc5')







app.mainloop()





