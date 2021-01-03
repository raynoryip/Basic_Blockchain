#Frame reference: https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
#Author: Wailam Yip
#Student ID: s3598673

import tkinter as tk               
from tkinter import font  as tkfont 
from tkinter import ttk
from PIL import Image, ImageTk
import random
import datetime as date
import blockchain as bc
import time

public_ledger_A = []
public_ledger_A.append(bc.Block.create_genesis_block())
public_ledger_B = public_ledger_A.copy()
public_ledger_C = public_ledger_B.copy()
public_ledger_D = public_ledger_C.copy()
public_ledger_E = public_ledger_D.copy()

class SampleApp(tk.Tk):
     
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold")
        
        container = tk.Frame(self,  bg="black")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Main_Menu, Investment_Page, Look_up_a_ledger, Alternating_a_block, About_this_app, public_ledger, specific_ledger, Seed_Data, Replace):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label_1 = tk.Label (self, fg = 'white', bg = 'black',  font=('Chinyen',25),text = "BlockChain Investment System Simulation")         
        label_1.pack(side="top", fill="x", pady=30)

        button1 = tk.Button(self, text="Press here to Start",
                            command=lambda: controller.show_frame("Main_Menu"), height=2, width=30, font =('Chinyen', 12))
        button2 =tk.Button(self, text="Exit", command=quit, height=2, width=30, font =('Chinyen', 12))
        button1.pack(pady=10)
        button2.pack(pady=10)
        


class Main_Menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="BlockChain Investment System Simulation", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Investment Page",
                           command=lambda: controller.show_frame("Investment_Page"), height=2, width=30, font =('Chinyen', 12))
        button2 = tk.Button(self, text="Look up a ledger",
                           command=lambda: controller.show_frame("Look_up_a_ledger"), height=2, width=30, font =('Chinyen', 12))
        button3 = tk.Button(self, text="Someone try to alternate a block",
                                command=lambda: controller.show_frame("Alternating_a_block"), height=2, width=30, font =('Chinyen', 12))
        button4 = tk.Button(self, text="Seed Data",
                                command=lambda: controller.show_frame("Seed_Data"), height=2, width=30, font =('Chinyen', 12))             
        button5 = tk.Button(self, text="About this app",
                                 command=lambda: controller.show_frame("About_this_app"), height=2, width=30, font =('Chinyen', 12))     
        button6 = tk.Button(self, text="Exit",
                                 command=quit, height=2, width=30, font =('Chinyen', 12))        
        button1.pack(pady=10)
        button2.pack(pady=10)
        button3.pack(pady=10)
        button4.pack(pady=10)
        button5.pack(pady=10)

class Investment_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Investment Simulation", font=controller.title_font)
        label.pack()
        
        invest_1_text = "Amount: 100000000000\n Type: Government Debt \n Interest: 3% p.a. \n period: 12 months "
        invest_label1 =tk.Label (self, text=invest_1_text, bg="green", fg="white", font="none 12 bold")
        invest_label1.pack(pady=10)
        
        textlabel1 = tk.Label(self, text="Investor Name")
        textlabel1.pack(pady=2)
        textentry_name1 = tk.Entry(self, width=20, bg="white")
        textentry_name1.pack(pady=2)
        textlabel2 = tk.Label(self, text="Invest Amount")
        textlabel2.pack(pady=2)
        textentry_name2 = tk.Entry(self, width=20, bg="white")
        textentry_name2.pack(pady=2)        
        
        button_invest1 = ttk.Button(self, text="Invest!", width=6, command=lambda:Investment_Page.invest_submit(textentry_name1.get(), textentry_name2.get(), 0))
        button_invest1.pack(pady=2)
        
        
        invest_2_text = "Amount: 30000000000\n Type: Corporate Investment \n Interest: 2% p.a. \n period: 24 months "
        invest_label2 =tk.Label (self, text=invest_2_text, bg="green", fg="white", font="none 12 bold")
        invest_label2.pack(pady=10)
        
        textlabel1 = tk.Label(self, text="Investor Name")
        textlabel1.pack(pady=2)
        textentry_name3= tk.Entry(self, width=20, bg="white")
        textentry_name3.pack(pady=2)
        textlabel2 = tk.Label(self, text="Invest Amount")
        textlabel2.pack(pady=2)
        textentry_name4 = tk.Entry(self, width=20, bg="white")
        textentry_name4.pack(pady=2)           
        
        button_invest2 = ttk.Button(self, text="Invest!", width=6, command=lambda:Investment_Page.invest_submit(textentry_name3.get(), textentry_name4.get(), 1))
        button_invest2.pack(pady=2)        
        
        button1 = tk.Button(self, text="Print", command=lambda:Investment_Page.printing())
        button1.pack()
        
        back_button = tk.Button(self, text="Back to Menu",
                           command=lambda: controller.show_frame("Main_Menu"))
        back_button.pack()
    
    def printing():
        for block in public_ledger_A:
            print([block.getIndex(), block.gethash(), block.getdata(), block.getphash(), block.getTs()], end="")
        print("-------------------")
        for block in public_ledger_B:
            print([block.getIndex(), block.gethash(), block.getdata(), block.getphash(), block.getTs()], end="")
        
    def invest_submit(investor_name, amount, invest_type):
        invest_detail = [[100000000000, "Government Debt", 0.03, 12], [30000000000, "Corporate Investment", 0.02, 24]]
        detail = invest_detail[invest_type]
        block_detail = str(detail) + "-" + str((investor_name, amount))
        print((investor_name, amount,invest_type, detail, block_detail))
        public_ledger_A.append(bc.Block(len(public_ledger_A), date.datetime.now(), block_detail, public_ledger_A[len(
            public_ledger_A)-1].gethash()))
        public_ledger_B.append(bc.Block(len(public_ledger_B), date.datetime.now(), block_detail, public_ledger_A[len(
            public_ledger_B)-1].gethash()))
        public_ledger_C.append(bc.Block(len(public_ledger_C), date.datetime.now(), block_detail, public_ledger_A[len(
            public_ledger_C)-1].gethash()))
        public_ledger_D.append(bc.Block(len(public_ledger_D), date.datetime.now(), block_detail, public_ledger_A[len(
            public_ledger_D)-1].gethash()))
        public_ledger_E.append(bc.Block(len(public_ledger_E), date.datetime.now(), block_detail, public_ledger_A[len(
            public_ledger_E)-1].gethash()))        
        
    
class Look_up_a_ledger(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Ledger Record - The Blockchain", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        button1 = tk.Button(self, text="Look up a public ledger",
                                command=lambda: controller.show_frame("public_ledger"), height=2, width=30, font =('Chinyen', 12))        
        button1.pack(pady=10)
        
        button2 = tk.Button(self, text="Look up specific ledger",
                                command=lambda: controller.show_frame("specific_ledger"), height=2, width=30, font =('Chinyen', 12))        
        button2.pack(pady=10)        
        
        back_button = tk.Button(self, text="Back to Menu",
                                command=lambda: controller.show_frame("Main_Menu"))
        back_button.pack(pady=10)
        
class public_ledger(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Public Ledger Record", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        button1 = tk.Button(self, text="Public Ledger A",
                                command=lambda: public_ledger.display_ledger(self, "A"), height=2, width=30, font =('Chinyen', 12))        
        button1.pack(pady=10)
    
        button2 = tk.Button(self, text="Public Ledger B",
                                command=lambda: public_ledger.display_ledger(self, "B"), height=2, width=30, font =('Chinyen', 12))        
        button2.pack(pady=10)            
        
        button3 = tk.Button(self, text="Public Ledger C",
                                command=lambda: public_ledger.display_ledger(self, "C"), height=2, width=30, font =('Chinyen', 12))        
        button3.pack(pady=10)
    
        button4 = tk.Button(self, text="Public Ledger D",
                                command=lambda: public_ledger.display_ledger(self, "D"), height=2, width=30, font =('Chinyen', 12))        
        button4.pack(pady=10)            
        
        button5 = tk.Button(self, text="Public Ledger E",
                                command=lambda: public_ledger.display_ledger(self, "E"), height=2, width=30, font =('Chinyen', 12))        
        button5.pack(pady=10)   
        
        back_button = tk.Button(self, text="Back to Menu",
                                command=lambda: controller.show_frame("Main_Menu"))
        back_button.pack()
        
    def display_ledger(frame, option):
        window = tk.Toplevel(frame)
        if option == "A":
            for i in range(len(public_ledger_A)):
                block_index = public_ledger_A[i].getIndex()
                block_hash = public_ledger_A[i].gethash()
                block_data = public_ledger_A[i].getdata()
                block_time = public_ledger_A[i].getTs()
                cont = "block Index: {}\n Hash: {}, Data: {}, Timestamp: {}".format(block_index, block_hash, block_data, block_time)
                
                label = tk.Label(window, text=cont)
                label.pack()
                    
        elif option == "B":
            for i in range(len(public_ledger_B)):
                block_index = public_ledger_B[i].getIndex()
                block_hash = public_ledger_B[i].gethash()
                block_data = public_ledger_B[i].getdata()
                block_time = public_ledger_B[i].getTs()
                cont = "block Index: {}\n Hash: {}, Data: {}, Timestamp: {}".format(block_index, block_hash, block_data, block_time)
                
                label = tk.Label(window, text=cont)
                label.pack()
                
        elif option == "C":
            for i in range(len(public_ledger_C)):
                block_index = public_ledger_C[i].getIndex()
                block_hash = public_ledger_C[i].gethash()
                block_data = public_ledger_C[i].getdata()
                block_time = public_ledger_C[i].getTs()
                cont = "block Index: {}\n Hash: {}, Data: {}, Timestamp: {}".format(block_index, block_hash, block_data, block_time)
                
                label = tk.Label(window, text=cont)
                label.pack()                
               
        elif option == "D":
            for i in range(len(public_ledger_D)):
                block_index = public_ledger_D[i].getIndex()
                block_hash = public_ledger_D[i].gethash()
                block_data = public_ledger_D[i].getdata()
                block_time = public_ledger_D[i].getTs()
                cont = "block Index: {}\n Hash: {}, Data: {}, Timestamp: {}".format(block_index, block_hash, block_data, block_time)
                
                label = tk.Label(window, text=cont)
                label.pack()
                    
        elif option == "E":
            for i in range(len(public_ledger_E)):
                block_index = public_ledger_E[i].getIndex()
                block_hash = public_ledger_E[i].gethash()
                block_data = public_ledger_E[i].getdata()
                block_time = public_ledger_E[i].getTs()
                cont = "block Index: {}\n Hash: {}, Data: {}, Timestamp: {}".format(block_index, block_hash, block_data, block_time)
                
                label = tk.Label(window, text=cont)
                label.pack()            
    
class specific_ledger(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Search for a specific block", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        textlabel1 = tk.Label(self, text="Please enter a name")
        textlabel1.pack(pady=2)        
        textentry_name1 = tk.Entry(self, width=20, bg="white")
        textentry_name1.pack(pady=2)        
        
        button1 = ttk.Button(self, text="search", width=6, command=lambda:specific_ledger.Search(self, textentry_name1.get()))
        button1.pack(pady=2)          
        
        back_button = tk.Button(self, text="Back to Menu",
                                command=lambda: controller.show_frame("Main_Menu"))
        back_button.pack()

    def Search(frame,name):
        
        window = tk.Toplevel(frame)
        name = name.lower()
        #theoretically all list should return same value, unless someone make changes to it
        resultA = specific_ledger.lookup(name, public_ledger_A)
        resultB = specific_ledger.lookup(name, public_ledger_B)
        resultC = specific_ledger.lookup(name, public_ledger_C)
        resultD = specific_ledger.lookup(name, public_ledger_D)
        resultE = specific_ledger.lookup(name, public_ledger_E)
        
        if len(resultA) > 0:
            label = tk.Label(window, text="---------------------[In Ledger A]------------------------")
            label.pack()               
            for index in range(len(public_ledger_A)):
                if public_ledger_A[index].getIndex() in resultA:
                    block_index = public_ledger_A[index].getIndex()
                    block_hash = public_ledger_A[index].gethash()
                    block_data = public_ledger_A[index].getdata()
                    block_time = public_ledger_A[index].getTs()
                    cont = "block Index: {}\n Hash: {}, Data: {}, Timestamp: {}".format(block_index, block_hash, block_data, block_time)
                    
                    label = tk.Label(window, text=cont)
                    label.pack()            
        else:
            label = tk.Label(window, text="Ledge A, not found")
            label.pack()
    
        if len(resultB) > 0:
            label = tk.Label(window, text="---------------------[In Ledger B]------------------------")
            label.pack()           
            for index in range(len(public_ledger_B)):
                if public_ledger_B[index].getIndex() in resultB:
                    block_index = public_ledger_B[index].getIndex()
                    block_hash = public_ledger_B[index].gethash()
                    block_data = public_ledger_B[index].getdata()
                    block_time = public_ledger_B[index].getTs()
                    cont = "block Index: {}\n Hash: {}, Data: {}, Timestamp: {}".format(block_index, block_hash, block_data, block_time)
                        
                    label = tk.Label(window, text=cont)
                    label.pack()            
        else:
            label = tk.Label(window, text="Ledge B, not found")   
            label.pack()
        
        if len(resultC) > 0:
            label = tk.Label(window, text="---------------------[In Ledger C]------------------------")
            label.pack()                   
            for index in range(len(public_ledger_C)):
                if public_ledger_C[index].getIndex() in resultC:
                    block_index = public_ledger_C[index].getIndex()
                    block_hash = public_ledger_C[index].gethash()
                    block_data = public_ledger_C[index].getdata()
                    block_time = public_ledger_C[index].getTs()
                    cont = "block Index: {}\n Hash: {}, Data: {}, Timestamp: {}".format(block_index, block_hash, block_data, block_time)
                            
                    label = tk.Label(window, text=cont)
                    label.pack()            
        else:
            label = tk.Label(window, text="Ledge C, not found")       
            label.pack()
        
        if len(resultD) > 0:
            label = tk.Label(window, text="---------------------[In Ledger D]------------------------")
            label.pack()                   
            for index in range(len(public_ledger_D)):
                if public_ledger_D[index].getIndex() in resultD:
                    block_index = public_ledger_D[index].getIndex()
                    block_hash = public_ledger_D[index].gethash()
                    block_data = public_ledger_D[index].getdata()
                    block_time = public_ledger_D[index].getTs()
                    cont = "block Index: {}\n Hash: {}, Data: {}, Timestamp: {}".format(block_index, block_hash, block_data, block_time)
                            
                    label = tk.Label(window, text=cont)
                    label.pack()            
        else:
            label = tk.Label(window, text="Ledge D, not found")   
            label.pack()
        
        if len(resultE) > 0:
            label = tk.Label(window, text="---------------------[In Ledger E]------------------------")
            label.pack()                   
            for index in range(len(public_ledger_E)):
                if public_ledger_E[index].getIndex() in resultE:
                    block_index = public_ledger_E[index].getIndex()
                    block_hash = public_ledger_E[index].gethash()
                    block_data = public_ledger_E[index].getdata()
                    block_time = public_ledger_E[index].getTs()
                    cont = "block Index: {}\n Hash: {}, Data: {}, Timestamp: {}".format(block_index, block_hash, block_data, block_time)
                                
                    label = tk.Label(window, text=cont)
                    label.pack()            
        else:
            label = tk.Label(window, text="Ledge E, not found")   
            label.pack()
        
        
    def lookup(needle, ledger):
        print(needle)
        target_block = []
        for block in ledger:
            if(block.getIndex()>0):
                data = block.getdata()
                name = data.split("-")[1].split(",")[0].lower()
                print(name)
                if needle in name:
                    target_block.append(block.getIndex())
        
        print(target_block)   
        return target_block
                

class Seed_Data(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        Seed_Data.load_seed()
        
        label = tk.Label(self, text="Seeding Successful", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        back_button = tk.Button(self, text="Back to Menu",
                                command=lambda: controller.show_frame("Main_Menu"))
        back_button.pack()
        
    def load_seed():
        invest_detail = [[100000000000, "Government Debt", 0.03, 12], [30000000000, "Corporate Investment", 0.02, 24]]
        names = ["Juliane Hutt", "Millard Rakow", "Maryam Borders", "Michaele Walton", "Willis Edsall", "Barb Lamar", "Maira Bryd", "Senaida Paris" 
                "Hanna Womack", "Irvin Holen", "Layne Richmond", "Hedwig Brunette", "Anastacia Derrow", "Ivan Smitherman", "Evia Vice", "Mercedez Rader",
                "Loriann Tesch"]
        
        for i in range(10):
            seed_1= []
            seed_1 = invest_detail[int(2*random.random())]
            block_detail = str(seed_1) + "-" + str((names[int(16*random.random())], int(1000*random.random())))
            public_ledger_A.append(bc.Block(len(public_ledger_A), date.datetime.now(), block_detail, public_ledger_A[len(public_ledger_A)-1].gethash()))
            public_ledger_B.append(bc.Block(len(public_ledger_B), date.datetime.now(), block_detail, public_ledger_A[len(public_ledger_B)-1].gethash()))
            public_ledger_C.append(bc.Block(len(public_ledger_C), date.datetime.now(), block_detail, public_ledger_A[len(public_ledger_C)-1].gethash()))
            public_ledger_D.append(bc.Block(len(public_ledger_D), date.datetime.now(), block_detail, public_ledger_A[len(public_ledger_D)-1].gethash()))
            public_ledger_E.append(bc.Block(len(public_ledger_E), date.datetime.now(), block_detail, public_ledger_A[len(public_ledger_E)-1].gethash()))
        
class Alternating_a_block(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Integrity", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        button1 = tk.Button(self, text="Try Hacker", command=lambda:controller.show_frame("Replace"), height=2, width=30, font =('Chinyen', 12))
        button1.pack(pady=10)        
        
        button2 = tk.Button(self, text="Check integrity", command=lambda:Alternating_a_block.integrity(self), height=2, width=30, font =('Chinyen', 12))
        button2.pack(pady=10)    
        
        back_button = tk.Button(self, text="Back to Menu",
                                command=lambda: controller.show_frame("Main_Menu"))
        back_button.pack(pady=10)    
        
    def integrity(frame):
        window = tk.Toplevel(frame)
        
        label = tk.Label(window, text="We will now compare Ledger A with other ledgers to see if they are the same\n")
        label.pack(side="top", fill="x", pady=10)       
        label2= tk.Label(window, text="If they have no difference, the screen won't display anything\n")
        label2.pack(side="top", fill="x", pady=10)   
        
        A_difference_B = [block_A for block_A, block_B in zip(public_ledger_A, public_ledger_B) if block_A.gethash() != block_B.gethash() ]
        A_difference_C = [block_A for block_A, block_C in zip(public_ledger_A, public_ledger_C) if block_A.gethash() != block_C.gethash() ]
        
        label = tk.Label(window, text="---------------------[Ledge A and Ledger B Difference]------------------------")
        label.pack() 
        for block in A_difference_B:
            block_index = block.getIndex()
            block_hash = block.gethash()
            block_data = block.getdata()
            block_time = block.getTs()
            cont = "block Index: {}\n Hash: {}, Data: {}, Timestamp: {}".format(block_index, block_hash, block_data, block_time)
                
            label1 = tk.Label(window, text=cont)
            label1.pack()                  
        
        label = tk.Label(window, text="---------------------[Ledge A and Ledger C Difference]------------------------")
        label.pack()           
        for block in A_difference_C:                 
            block_index = block.getIndex()
            block_hash = block.gethash()
            block_data = block.getdata()
            block_time = block.getTs()
            cont = "block Index: {}\n Hash: {}, Data: {}, Timestamp: {}".format(block_index, block_hash, block_data, block_time)
                    
            label1 = tk.Label(window, text=cont)
            label1.pack()            
        
class Replace(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Someone try to replace a block", height=2, width=30, font =('Chinyen', 12))
        label.pack(side="top", fill="x", pady=10)
        label2 = tk.Label(self, text="To make life easier, hacker could only modify Ledger A", height=2, width=30, font =('Chinyen', 12))
        label2.pack(side="top", fill="x", pady=10)
        
        textlabel1 = tk.Label(self, text="Please enter a block Index from 1 to {}".format(len(
            public_ledger_A)))
        textlabel1.pack(pady=2)        
        textentry_name1 = tk.Entry(self, width=20, bg="white")
        textentry_name1.pack(pady=2)        
        
        textlabel2 = tk.Label(self, text="hacking content")
        textlabel2.pack(pady=2)        
        textentry_name2 = tk.Entry(self, width=20, bg="white")
        textentry_name2.pack(pady=2)          
    
        button1 = ttk.Button(self, text="Modify this block", width=6, command=lambda:Replace.modification(self, textentry_name1.get(), textentry_name2.get()))
        button1.pack(pady=2)             
            
        back_button = tk.Button(self, text="Back to Previous Page",
                                command=lambda: controller.show_frame("Alternating_a_block"))
        back_button.pack(pady=10)
        
    def modification(frame, hack_block_index, hack_block_content):
        
        window = tk.Toplevel(frame)
        
        label = tk.Label(window, text="modification Successful", height=2, width=30, font =('Chinyen', 12))
        label.pack(side="top", fill="x", pady=10)        
        
        hacker_block = bc.Block(hack_block_index, date.datetime.now(
            ), hack_block_content, public_ledger_A[len(public_ledger_A)-1].gethash())        
        
        hack_block_index = int(hack_block_index)
        
        print(type(hack_block_index))
        print(hack_block_content)
        
        for index in range(len(public_ledger_A)):
            print(public_ledger_A[index].getIndex())
            if public_ledger_A[index].getIndex() == hack_block_index:
                public_ledger_A[index] = hacker_block
                break
            
class About_this_app(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        cont = "This app is a p2p online investment system simulation, user can investment any amount to any investment product.\n"
        cont2 = "We use Blockchain system to secure the integrity of the transactions,\n you can look the chain to see your record or public record\n"
        cont3 = "Author: Wailam Yip\n"
        cont4 = "Student ID: s3598673\n"
        main_cont = cont + cont2+ cont3+cont4
        
        label = tk.Label(self, text=main_cont, font=controller.title_font, bg="Green")
        label.pack(side="top", fill="x", pady=10)
        
        
        back_button = tk.Button(self, text="Back to Menu",
                                command=lambda: controller.show_frame("Main_Menu"))
        back_button.pack()    

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()