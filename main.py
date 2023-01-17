import tkinter
import customtkinter as ct
import hashlib
from PIL import Image, ImageTk
import socket
import random as rd 
import time
from tabulate import tabulate


def event_create():
    popup = ct.CTkToplevel(app)
    popup.title("Popup Window")
    lab = ct.CTkLabel(popup, text="Event has been created!")
    lab.pack()
    button = ct.CTkButton(popup, text="OK", command=popup.destroy)
    button.pack()

def show_student_page_back():
    global app, sidebar_frame, sidebar_frame2, current_label, student_tabs, challenge_tab
    global resume_score, video_score
    
    
    sidebar_frame = ct.CTkFrame(app, width=150, height=450, corner_radius=5)
    sidebar_frame.grid()
    sidebar_frame.grid(row=0, column=0, sticky="nsew")
    sidebar_frame.grid_propagate(False)
    
    sidebar_frame2 = ct.CTkFrame(app, width=150, height=150, corner_radius=5)
    sidebar_frame2.grid()
    sidebar_frame2.grid(row=1, column=0, sticky="nsew")
    sidebar_frame2.grid_propagate(False)
    
    game_label = ct.CTkLabel(sidebar_frame2, text = "Ongoing Games", font=ct.CTkFont(size=15, weight="bold"))
    game_label.grid(row=0, column=0)
    
    current_label = ct.CTkLabel(sidebar_frame2, text = "No current games", font=ct.CTkFont(size=12)) #if there then change this 
    current_label.grid(row=1, column=0, padx=20, pady=10)
    
    welcome_text = "Hi, " + "Jai Jindal" # create a function to get the user name
    wlabel1 = ct.CTkLabel(sidebar_frame, text=welcome_text, font=ct.CTkFont(size=20, weight="bold"), width=50, height=20)
    wlabel1.grid(row=0, column=0, pady=20, padx=10)
    
    leader_rank = ct.CTkLabel(sidebar_frame, text="Leaderboard Rank: #1", font=ct.CTkFont(size=12), width=50, height=20)
    league_tag = ct.CTkLabel(sidebar_frame, text="League: 2", font=ct.CTkFont(size=12), width=50, height=20)
    upload_resume = ct.CTkEntry(sidebar_frame, placeholder_text="Enter resume file")
    
    resume_score = ct.CTkLabel(sidebar_frame, text="Resume score: 0", font=ct.CTkFont(size=12), width=50, height=20)
    submit_resume= ct.CTkButton(sidebar_frame, text="Evaluate Resume", command=run_resume_model)
    upload_video = ct.CTkEntry(sidebar_frame, placeholder_text="Enter video file")
   
    video_score = ct.CTkLabel(sidebar_frame, text="Video score: 0", font=ct.CTkFont(size=12), width=50, height=20)
    submit_video = ct.CTkButton(sidebar_frame, text="Evaluate Video", command=run_video_model)
    
    leader_rank.grid(row=1, column=0, pady=(40,5), padx=10)
    league_tag.grid(row=2, column=0, pady=(0,30), padx=10)
    upload_resume.grid(row=3, column=0, pady=(5,5), padx=10)
    resume_score.grid(row=4, column=0, pady=(0,5), padx=10)
    submit_resume.grid(row=5, column=0, pady=(0,30), padx=10)
    upload_video.grid(row=6, column=0, pady=(5,5), padx=10)
    video_score.grid(row=7, column=0, pady=(0,5), padx=10)
    submit_video.grid(row=8, column=0, pady=(0,5), padx=10)
    
    
    student_tabs = ct.CTkTabview(app, width=240, height=450)
    student_tabs.grid(row=0, column=1, padx=(5, 0), sticky="nsew")
    student_tabs.add("Competitions")
    student_tabs.add("Leaderboards")
    
    registered_label = ct.CTkLabel(student_tabs.tab("Competitions"), text="Registered Competitions", font=ct.CTkFont(size=15, weight="bold"), width=50, height=20)
    registered_label.grid(row = 0, column = 0, padx = 10, pady = (20,5))
    ## create image
    
    image = Image.open("google.jpeg")
    image = image.resize((150,110)) 
    photo = ImageTk.PhotoImage(image)
    googlelabel = ct.CTkLabel(student_tabs.tab("Competitions"), text="", image=photo)
    googlelabel.grid(row=1, column=0, padx=10, pady=(5,20))
    
    upcoming_label = ct.CTkLabel(student_tabs.tab("Competitions"), text="Coming Soon                    ", font=ct.CTkFont(size=15, weight="bold"), width=50, height=20)
    upcoming_label.grid(row = 2, column = 0, padx = 10, pady = 5)
    
    image2 = Image.open("dysonimage.png")
    image2 = image2.resize((150,110)) 
    photo = ImageTk.PhotoImage(image2)
    googlelabel = ct.CTkLabel(student_tabs.tab("Competitions"), text="", image=photo)
    googlelabel.grid(row=3, column=0, padx=10, pady=5)
    ## create image
    
    challenge_tab = ct.CTkTabview(app, width=240, height=150)
    challenge_tab.grid(row=1, column=1, padx=(5,0), sticky="nsew")
    challenge_tab.add("Challenges")
    
    challenge_menu = ct.CTkComboBox(challenge_tab.tab("Challenges"), values=["DSA", "DSAI"])
    challenge_menu.grid(row=0, column=0, padx=40, pady=20)
    
    challenge_button = ct.CTkButton(challenge_tab.tab("Challenges"), text="Find Opponent", command=check)
    challenge_button.grid(row=1, column=0, padx=40)
    
    a= [('League1','emma', 102), ('League1','jake', 84), ('League1','michael', 77),('League2','rifah', 61), ('League2','sam', 59), ('League2','jalen', 41),('League3','olive', 30), ('League3','bobby', 14), ('League3','liz', 11), ('League3','amanda', 8)]
    
    leaderboard_tab = student_tabs.tab("Leaderboards")

    # Create leaderboard positions
    
    table = [["League", " Name", "Score"]]
    table.extend(a)

    # Create label to hold tabulate table
    leaderboard_label = ct.CTkLabel(leaderboard_tab, text=tabulate(table, headers="firstrow", tablefmt="grid"))
    leaderboard_label.grid(row=0, column=0, padx=10, pady=10)

    

def solution_submit():
    print("Solution submitted")
    time.sleep(10)
    ##raise alert
    show_student_page()
    
def back_to_student_page():
    global game_frame
    game_frame.destroy()
    show_student_page_back()

def game_submission_page():
    global app, sidebar_frame, sidebar_frame2, student_tabs, challenge_tab
    global game_frame, question
    sidebar_frame.destroy()
    sidebar_frame2.destroy()
    student_tabs.destroy()
    challenge_tab.destroy()
    
    question = "There is a question here"
  
    game_frame = ct.CTkFrame(app, width=400, height=600, corner_radius=5)
    game_frame.grid()
    game_frame.grid(row=0, column=0, sticky="nsew")
    game_frame.grid_propagate(False)
    print(question)
    
    q_statement = ct.CTkLabel(game_frame, text="Question:                                    ", font=ct.CTkFont(size=15, weight="bold"))
    q_statement.grid(row=0, column=0, padx=(0,0), pady=(40, 0))
    
    questionbox = ct.CTkTextbox(game_frame, width=250, height=100)
    questionbox.grid(row=1, column=0, padx=(50, 20), pady=(10, 20), sticky="nsew")
    questionbox.insert("0.0", question)
    
    q_statement = ct.CTkLabel(game_frame, text="Enter answer here:               ", font=ct.CTkFont(size=15, weight="bold"))
    q_statement.grid(row=2, column=0, padx=(0,0), pady=(0, 20))
    
    answerbox = ct.CTkTextbox(game_frame, width=250, height=200)
    answerbox.grid(row=3, column=0, padx=(50, 20), pady=(0, 20), sticky="nsew")
    
    submit_button = ct.CTkButton(game_frame, text="Submit", command=solution_submit)
    submit_button.grid(row=4, column=0, pady=(5,5))
    
    back_button = ct.CTkButton(game_frame, text="Back", command=back_to_student_page)
    back_button.grid(row=5, column=0 )
    
def run_resume_model():
    global resume_score
    time.sleep(1)
    x = rd.randint(60,90)
    resume_score.destroy()
    text = "Resume score: "+ str(x)
    resume_score = ct.CTkLabel(sidebar_frame, text=text, font=ct.CTkFont(size=12), width=50, height=20)
    resume_score.grid(row=4, column=0, pady=(0,5), padx=10)
    

def run_video_model():
    global video_score
    time.sleep(1)
    y = rd.randint(60,90)
    video_score.destroy()
    text = "Video score: "+ str(y)
    video_score = ct.CTkLabel(sidebar_frame, text=text, font=ct.CTkFont(size=12), width=50, height=20)
    video_score.grid(row=7, column=0, pady=(0,5), padx=10)
    
    
def check():
    global sidebar_frame2, current_label
    current_label.destroy()
    view_game= ct.CTkButton(sidebar_frame2, text="View game", command=game_submission_page)
    view_game.grid(row=1, column=0, padx=2, pady=10)
    
    
def start_challenge():
    global sidebar_frame2
    
    if(question==""):
        HOST = "192.168.1.42"  # The server's hostname or IP address
        PORT = 2004  # The port used by the server

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            loop=0
            while(loop==0):
                question = s.recv(1024).decode("utf-8")
                if(question != ""):
                    loop+=1
            print(question)
            
            res_loop=0
            while(res_loop==0):
                result = s.recv(1024).decode("utf-8")
                if(result != ""):
                    res_loop+=1
            print(result)
            game_label = ct.CTkLabel(sidebar_frame2, text = "Ongoing Games", font=ct.CTkFont(size=10, weight="bold"))
            game_label.grid(row=0, column=0)
    else:
        print("Question already exists")
        
    #if question is there then raise error
    #if question is not there then run this entire code

def show_recruiter_page():
    global app
    
    sidebar_frame = ct.CTkFrame(app, width=150, height=200, corner_radius=5)
    sidebar_frame.grid()
    sidebar_frame.grid(row=0, column=0, sticky="nsew")
    sidebar_frame.grid_propagate(False)
    
    welcome_text = "Hi, " + "panchod" # create a function to get the user name
    wlabel1 = ct.CTkLabel(sidebar_frame, text=welcome_text, font=ct.CTkFont(size=20, weight="bold"), width=50, height=20)
    wlabel1.grid(row=0, column=0, pady=20, padx=10)
    
    company = ct.CTkLabel(sidebar_frame, text="Company: Apple", font=ct.CTkFont(size=12), width=50, height=20)
    companyid = ct.CTkLabel(sidebar_frame, text="Company ID: 30", font=ct.CTkFont(size=12), width=50, height=20)
    company.grid(row=1, column=0, pady=(40,5), padx=10)
    companyid.grid(row=2, column=0, pady=(0,30), padx=10)
    
    tabs = ct.CTkTabview(app, width=240, height=600)
    tabs.grid(row=0, column=1, padx=(5, 0), sticky="nsew")
    tabs.add("Create")
    tabs.add("Leaderboards")
    
    create_label = ct.CTkLabel(tabs.tab("Create"), text="Create a competition", font=ct.CTkFont(size=20, weight="bold"), width=50, height=20)
    cid = ct.CTkEntry(tabs.tab("Create"), placeholder_text="Company ID")
    challenge_name = ct.CTkEntry(tabs.tab("Create"), placeholder_text="Challeng Name")
    opento = ct.CTkComboBox(tabs.tab("Create"), values=["League 1", "League 2+", "League 3+"])
    duration = ct.CTkEntry(tabs.tab("Create"), placeholder_text="Duration")
    subject = ct.CTkComboBox(tabs.tab("Create"), values=["DSAI", "DSA"])
    remarks = ct.CTkTextbox(tabs.tab("Create"))
    create_button = ct.CTkButton(tabs.tab("Create"), text="Create Event", command=event_create)
    
    create_label.grid(row=0, column=0, padx=(10,0), pady=(10,5))
    cid.grid(row=1, column=0, padx=(10,0), pady=(10,5))
    challenge_name.grid(row=2, column=0, padx=(10,0), pady=(10,5))
    opento.grid(row=3, column=0, padx=(10,0), pady=(10,5))
    duration.grid(row=4, column=0, padx=(10,0), pady=(10,5))
    subject.grid(row=5, column=0, padx=(10,0), pady=(10,5))
    remarks.grid(row=6, column=0, padx=(10,0), pady=(10,5))
    remarks.insert("0.0","Remarks:")
    create_button.grid(row=7, column=0, padx=(10,0), pady=(10,5))
    
    a= [('League1','emma', 102), ('League1','jake', 84), ('League1','michael', 77),('League2','rifah', 61), ('League2','sam', 59), ('League2','jalen', 41),('League3','olive', 30), ('League3','bobby', 14), ('League3','liz', 11), ('League3','amanda', 8)]
    
    leaderboard_tab = tabs.tab("Leaderboards")

    # Create leaderboard positions
    
    table = [["League", " Name", "Score"]]
    table.extend(a)

    # Create label to hold tabulate table
    leaderboard_label = ct.CTkLabel(leaderboard_tab, text=tabulate(table, headers="firstrow", tablefmt="grid"))
    leaderboard_label.grid(row=0, column=0, padx=10, pady=10)
    

def show_student_page():
    global app, sidebar_frame, sidebar_frame2, current_label, student_tabs, challenge_tab
    global resume_score, video_score
    
    
    sidebar_frame = ct.CTkFrame(app, width=150, height=450, corner_radius=5)
    sidebar_frame.grid()
    sidebar_frame.grid(row=0, column=0, sticky="nsew")
    sidebar_frame.grid_propagate(False)
    
    sidebar_frame2 = ct.CTkFrame(app, width=150, height=150, corner_radius=5)
    sidebar_frame2.grid()
    sidebar_frame2.grid(row=1, column=0, sticky="nsew")
    sidebar_frame2.grid_propagate(False)
    
    game_label = ct.CTkLabel(sidebar_frame2, text = "Ongoing Games", font=ct.CTkFont(size=15, weight="bold"))
    game_label.grid(row=0, column=0)
    
    current_label = ct.CTkLabel(sidebar_frame2, text = "No current games", font=ct.CTkFont(size=12)) #if there then change this 
    current_label.grid(row=1, column=0, padx=20, pady=10)
    
    welcome_text = "Hi, " + "Jai Jindal" # create a function to get the user name
    wlabel1 = ct.CTkLabel(sidebar_frame, text=welcome_text, font=ct.CTkFont(size=20, weight="bold"), width=50, height=20)
    wlabel1.grid(row=0, column=0, pady=20, padx=10)
    
    leader_rank = ct.CTkLabel(sidebar_frame, text="Leaderboard Rank: #1", font=ct.CTkFont(size=12), width=50, height=20)
    league_tag = ct.CTkLabel(sidebar_frame, text="League: 2", font=ct.CTkFont(size=12), width=50, height=20)
    upload_resume = ct.CTkEntry(sidebar_frame, placeholder_text="Enter resume file")
    
    resume_score = ct.CTkLabel(sidebar_frame, text="Resume score: 0", font=ct.CTkFont(size=12), width=50, height=20)
    submit_resume= ct.CTkButton(sidebar_frame, text="Evaluate Resume", command=run_resume_model)
    upload_video = ct.CTkEntry(sidebar_frame, placeholder_text="Enter video file")
   
    video_score = ct.CTkLabel(sidebar_frame, text="Video score: 0", font=ct.CTkFont(size=12), width=50, height=20)
    submit_video = ct.CTkButton(sidebar_frame, text="Evaluate Video", command=run_video_model)
    
    leader_rank.grid(row=1, column=0, pady=(40,5), padx=10)
    league_tag.grid(row=2, column=0, pady=(0,30), padx=10)
    upload_resume.grid(row=3, column=0, pady=(5,5), padx=10)
    resume_score.grid(row=4, column=0, pady=(0,5), padx=10)
    submit_resume.grid(row=5, column=0, pady=(0,30), padx=10)
    upload_video.grid(row=6, column=0, pady=(5,5), padx=10)
    video_score.grid(row=7, column=0, pady=(0,5), padx=10)
    submit_video.grid(row=8, column=0, pady=(0,5), padx=10)
    
    
    student_tabs = ct.CTkTabview(app, width=240, height=450)
    student_tabs.grid(row=0, column=1, padx=(5, 0), sticky="nsew")
    student_tabs.add("Competitions")
    student_tabs.add("Leaderboards")
    
    registered_label = ct.CTkLabel(student_tabs.tab("Competitions"), text="Registered Competitions", font=ct.CTkFont(size=15, weight="bold"), width=50, height=20)
    registered_label.grid(row = 0, column = 0, padx = 10, pady = (20,5))
    ## create image
    
    image = Image.open("google.jpeg")
    image = image.resize((150,110)) 
    photo = ImageTk.PhotoImage(image)
    googlelabel = ct.CTkLabel(student_tabs.tab("Competitions"), text="", image=photo)
    googlelabel.grid(row=1, column=0, padx=10, pady=(5,20))
    
    upcoming_label = ct.CTkLabel(student_tabs.tab("Competitions"), text="Coming Soon                    ", font=ct.CTkFont(size=15, weight="bold"), width=50, height=20)
    upcoming_label.grid(row = 2, column = 0, padx = 10, pady = 5)
    
    image2 = Image.open("dysonimage.png")
    image2 = image2.resize((150,110)) 
    photo = ImageTk.PhotoImage(image2)
    googlelabel = ct.CTkLabel(student_tabs.tab("Competitions"), text="", image=photo)
    googlelabel.grid(row=3, column=0, padx=10, pady=5)
    ## create image
    
    challenge_tab = ct.CTkTabview(app, width=240, height=150)
    challenge_tab.grid(row=1, column=1, padx=(5,0), sticky="nsew")
    challenge_tab.add("Challenges")
    
    challenge_menu = ct.CTkComboBox(challenge_tab.tab("Challenges"), values=["DSA", "DSAI"])
    challenge_menu.grid(row=0, column=0, padx=40, pady=20)
    
    challenge_button = ct.CTkButton(challenge_tab.tab("Challenges"), text="Find Opponent", command=check)
    challenge_button.grid(row=1, column=0, padx=40)
    
    a= [('League1','emma', 102), ('League1','jake', 84), ('League1','michael', 77),('League2','rifah', 61), ('League2','sam', 59), ('League2','jalen', 41),('League3','olive', 30), ('League3','bobby', 14), ('League3','liz', 11), ('League3','amanda', 8)]
    
    leaderboard_tab = student_tabs.tab("Leaderboards")

    # Create leaderboard positions
    
    table = [["League", " Name", "Score"]]
    table.extend(a)

    # Create label to hold tabulate table
    leaderboard_label = ct.CTkLabel(leaderboard_tab, text=tabulate(table, headers="firstrow", tablefmt="grid"))
    leaderboard_label.grid(row=0, column=0, padx=10, pady=10)

def rec_button_function():
    global tabview_1, rec_pass
    password = student_pass.get()
    encrypt = hashlib.sha256(password.encode()).hexdigest()
    tabview_1.destroy()
    show_recruiter_page()

def student_button_function():
    global tabview_1, student_pass
    password = student_pass.get()
    encrypt = hashlib.sha256(password.encode()).hexdigest()
    tabview_1.destroy()
    show_student_page()

ct.set_appearance_mode("dark")  # Modes: system (default), light, dark
ct.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = ct.CTk()
app.geometry("400x600")
#app.resizable(False, False)


tabview_1 = ct.CTkTabview(app, width=320, height=500)
tabview_1.grid(row=1, column=1, padx=(40, 0), pady=(40, 0), sticky="nsew")
tabview_1.add("Students")
tabview_1.add("Recruiter")

logoimage = Image.open("logo.jpg")
logoimage = logoimage.resize((150,110)) 
photo = ImageTk.PhotoImage(logoimage)

logolabel = ct.CTkLabel(tabview_1.tab("Students"), text="", image=photo)
logolabel.grid(row=0, column=1, padx=10, pady=(40, 20))

logolabel = ct.CTkLabel(tabview_1.tab("Recruiter"), text="", image=photo)
logolabel.grid(row=0, column=1, padx=10, pady=(40, 20))

student_label = ct.CTkLabel(tabview_1.tab("Students"), text="Student Login", font=ct.CTkFont(size=20, weight="bold"))
student_label.grid(row=1, column=1, padx=10, pady=10)
recruiter_label = ct.CTkLabel(tabview_1.tab("Recruiter"), text="Recruiter Login", font=ct.CTkFont(size=20, weight="bold"))
recruiter_label.grid(row=1, column=1, padx=10, pady=10)

student_user = ct.CTkEntry(tabview_1.tab("Students"), placeholder_text="Enter Username")
student_pass = ct.CTkEntry(tabview_1.tab("Students"), placeholder_text="Enter Password", show="*")
rec_user = ct.CTkEntry(tabview_1.tab("Recruiter"), placeholder_text="Enter Username")
rec_pass = ct.CTkEntry(tabview_1.tab("Recruiter"), placeholder_text="Enter Password", show="*")

student_user.grid(row=2, column=1, padx=80, pady=(0, 10))
student_pass.grid(row=3, column=1, padx=80, pady=(0, 10))
rec_user.grid(row=2, column=1, padx=80, pady=(0, 10))
rec_pass.grid(row=3, column=1, padx=80, pady=(0, 10))

student_button = ct.CTkButton(tabview_1.tab("Students"), text="Log In", command=student_button_function)
rec_button = ct.CTkButton(tabview_1.tab("Recruiter"), text="Log In", command=rec_button_function)

student_button.grid(row=4, column =1, padx=80, pady=10)
rec_button.grid(row=4, column =1, padx=80, pady=10)

question=""

app.mainloop()