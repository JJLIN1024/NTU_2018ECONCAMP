import csv
import random
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont
from PIL import ImageTk
from PIL import Image
import os
from operator import itemgetter
import pyautogui
path = os.getcwd()
# print(path) #/Users/jimmylin/Desktop/期末專題/img
os.chdir(path)

# country info
America=[[2, 2, 2, 2, 1.2],[1500, 1500, 1500, 1500, 0, 0],[3000, 2000, 500, 0]]
Russia=[[3, 1.7, 1.3, 2, 1.3],[2000, 1400, 1100, 1500, 0, 0],[3000, 2000, 500, 0]]
Aribic=[[1.8, 1.8, 1.2, 1.2, 1],[1800, 1800, 1200, 1200, 0, 0],[3000, 2000, 500, 0]]
China=[[2.2, 1.5, 2.1, 2.2, 0.8],[1500, 1400, 1800, 1300, 0, 0],[3000, 2000, 700, 0]]
hot_hot=[[1.5, 1.5, 2, 3, 1],[1300, 1200, 1800, 1700, 0, 0],[3000, 2000, 500, 0]]
England=[[1.8, 2, 2, 2.2, 1],[1300, 1800, 1600, 1300, 0, 0],[3000, 2000, 500, 0]]
uganda=[[1.3, 2.0, 1.2, 1.5, 1.1],[1300, 2000, 1200, 1500, 0, 50],[3000, 2000, 500, 0]]#有50汎合金
north_oh=[[2.3, 2, 1.8, 2, 1],[1500, 1300, 1200, 2000, 0, 0],[3000, 2000, 500, 0]]
Taiwan=[[1, 1, 3, 3, 1],[1100, 1300, 2000, 1600, 0, 0],[3000, 2000, 500, 0]]
Nan_gi=[[1.3, 1.7, 1.2, 1.8, 1],[1300, 1700, 1200, 1800, 50, 0],[3000, 2000, 500, 0]]
government=[[100000, 100000, 100000, 100000, 0, 0],[100000, 100000, 100000, 0]]

#建立集合所有國家資訊的list
all_player_info=[America, Russia, Aribic, China, hot_hot, England, uganda, north_oh, Taiwan, Nan_gi]
#建立集合所有國中文名稱的list
all_player_names=["美國", "俄羅斯", "沙漠之都",  "中國", "叢林之都", "英國", "烏干達", "海洋之都", "台灣", "南極"]

all_health = [1] * 10 # Health
education_list = [0] * 10

education_dict = {"0": "0", "1": "0.4", "2": "0.79", "3": "1.17", "4": "1.54", "5": "1.9", "6": "2.25", "7": "2.59", "8": "2.92", "9": "3.24",
"10": "3.55", "11": "3.85", "12": "4.14","13": "4.42", "14": "4.69", "15": "4.95", "16": "5.2", "17": "5.44", "18": "5.67", "19": "5.89",
"20": "6.1", "21": "6.3", "22": "6.49", "23": "6.67", "24": "6.84", "25": "7", "26": "7.15", "27": "7.29", "28": "7.42", "29": "7.54",
"30": "7.65", "31": "7.75", "32": "7.84", "33": "7.92", "34": "7.99", "35": "8.05", "36": "8.1", "37": "8.14", "38": "8.17", "39": "8.19",
"40": "8.2", "41": "8.2", "42": "8.19", "43": "8.17", "44": "8.14", "45": "8.1", "46": "8.05", "47": "7.99", "48": "7.92", "49": "7.84",
"50": "7.75", "51": "7.65", "52": "7.54", "53": "7.42", "54": "7.29", "55": "7.15", "56": "7", "57": "6.84", "58": "6.67", "59": "6.49",
"60": "6.3", "61": "6.1", "62": "5.89", "63": "5.67", "64": "5.44", "65": "5.2", "66": "4.95", "67": "4.69", "68": "4.42", "69": "4.14",
"70": "3.85", "71": "3.55", "72": "3.24", "73": "2.92", "74": "2.59", "75": "2.25", "76": "1.9", "77": "1.54", "78": "1.17", "79": "0.79",
"80": "0.4","81": "0"}
education_year = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],[0, 0, 0],                          #前面放基礎教育年限，中間放高等教育年限，最後放獨立研究機構年限
                  [0, 0, 0], [0, 0, 0],[0, 0, 0], [0, 0, 0],[0, 0, 0]]
education_list = [0] * 10
university = [0] * 10                                                                            #已蓋大學間數
attempt = [0] * 10                                                                               #因為戰爭會導致基礎教育建設失敗，要拿來看之前有沒有失敗過
invaded = [0] * 10
rank = []



class SampleApp(tk.Tk):
    #initialization
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # tk.Tk.iconbitmap(self, default='Pixelpress-Pirates-Flag-Jolly-Roger.ico')
        # tk.Tk.wm_title(self, "NTU_Econ_game")

        self.minsize(width=1100, height=600)
        self.maxsize(width=1100, height=600)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        #有製作任何新的頁面就加進這個for loop 裡面
        for F in (StartPage, PageOne,USA, RUSSIA, DESERT, CHINA, FOREST, UK, UGANDA, OCEAN, TAIWAN, POLE, PageThree, SubPage,Produce, Investment, Trade, Health, War, Conscription , Reconnoitre, Education, EndPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

loopnum = 0
#虛擬使用者共9個
#btn mutiple command
#記錄選擇國家的變數
def record_countryNum(num):
    global t
    t = num
    print('t',t)

#在button mutiple command 裡面負責轉換page
def showNextFrame(self,page):
    self.controller.show_frame(page)

#開始頁面
class StartPage(tk.Frame):
    #initialization
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        f1 = tkfont.Font(family = 'STLiti', size = 72, weight = "bold")
        label = tk.Label(self, text = "NTU ECON Game", font = f1, fg = "#a2cffe")
        label.pack(side = "top", pady = 100)
        f1 = ttk.Style()
        f1.configure('my.TButton', font=('Bahnschrift SemiBold SemiConden', 24))
        self.btn1 = ttk.Button(self, text = "Start Game", width = 15, style = "my.TButton",
                                  command = lambda: controller.show_frame("PageOne"))
        self.btn1.place(x = 425, y = 350)
def human():
    global rank
    rank = []
    for i in range(10):
        country = all_player_info[i]                                        #決定國家

        asset = country[2][0] + (country[1][0] + country[1][1] + country[1][2] + country[1][3]) * 0.8      #總資產 = 黃金 + (石油 + 金屬礦 + 糧食 + 木頭)  * 0.8
        education = education_year[i][0] + education_year[i][1] + education_year[i][2]                     #教育 = 基礎教育年限 + 高等教育年限 + 獨立研究機構年限
        if education == 0:                                                  #如果都沒有教育，以1年計
            education = 1
        health = 1                                                          #人均壽命演算法待補
        HDI = asset * education * health                                    #ＨＤＩ＝（總資產＊教育年數＊人均預期壽命）
        data = []                                                           #各國資料
        data.append(i)
        data.append(HDI)
        rank.append(data)

    rank = sorted(rank, key=lambda s: s[1], reverse=True)
    check_num = []
    for i in range(10):
        if 0 <= i <= 2:
            all_player_info[rank[i][0]][2][1] += 100
        elif 3 <= i <= 5:
            all_player_info[rank[i][0]][2][1] += 150
        elif 6 <= i <= 9:
            all_player_info[rank[i][0]][2][1] += 200
        # print(rank[i][0], all_player_info[rank[i][0]][2][1])
        check_num.append(rank[i][0])
    print("人民已加")

def redistribution():
    asset_old = []
    asset_old_number=[]
    asset_new = [0] * 10
    change = []
    for i in range(10):
        if i != 6 and i != 9:
            asset_old.append(sum(all_player_info[i][1]) * 0.8 + all_player_info[i][2][0])
            asset_old_number.append(i)
        else:
            asset_old.append((all_player_info[i][1][0] + all_player_info[i][1][1] + all_player_info[i][1][2] + all_player_info[i][1][3]) * 0.8 + all_player_info[i][2][0])
            asset_old_number.append(i)
    asset_final=list(zip(asset_old,asset_old_number))
    print("asset_final", asset_final)
    asset_final=sorted(asset_final, key=itemgetter(0))
    print("asset_final", asset_final)

    rank_redistribution=[]
    for i in range(len(asset_final)):
        rank_redistribution.append(asset_final[i][1])
    print('rank_redistribution',rank_redistribution)

    # rank_redistribution = [1, 2, 0, 9, 8, 7, 6, 5, 4, 3] #由小到大
    # print(rank_redistribution)
    poverty_line = asset_old[rank_redistribution[9]] // 8.7
    print("poverty_line is: {:.0f}".format(poverty_line))

    for t in range(10):
        try:
            if asset_old[rank_redistribution[t]] < poverty_line:
                asset_new[rank_redistribution[t]] = asset_old[rank_redistribution[t]] + asset_old[rank_redistribution[9]] // 3
                change.append(rank_redistribution[t])
            elif asset_old[rank_redistribution[t]] >= poverty_line:
                asset_new[rank_redistribution[t]] = asset_old[rank_redistribution[t]]
        except:
            pass
    print("change", change)
    print("asset_new", asset_new)

    for m in change:
        index = rank_redistribution[m + 1]
        if asset_new[m] > asset_new[index]:
            asset_new[m] = asset_new[index]
        elif asset_new[m] <= asset_new[index]:
            pass
    print("asset_new after check", asset_new)

def gift():                                            #待輸入天數函數
    global loopnum
    print("回合", loopnum)
    for i in range(10):
        if loopnum % 3 == 0 and loopnum != 0:
            country = all_player_info[i]
            country[1][0] += 1000 * country[0][0]
            country[1][1] += 1000 * country[0][1]
            country[1][2] += 1000 * country[0][2]
            country[1][3] += 1000 * country[0][3]
            if i == 0:
                print("\n天降中...")
        all_player_info[i][2][0] += 750
    print("\n天降函數已跑完")

def NextRound(self, page1, time, page2):
    gift()
    human()
    redistribution()
    continue_proceess1()
    global loopnum
    global p
    global I
    global T
    global E
    global W
    global R
    global H
    p = 0
    I = 0
    T = 0
    E = 0
    W = 0
    R = 0
    H = 0
    self.controller.show_frame(page1)
    self.after(time, showNextFrame(self,page2))

    loopnum += 1
    print(loopnum)
    if loopnum == 12:

        self.controller.show_frame('EndPage')
        gameoverRanking()
        print('遊戲結束')

def rankFinal():
    global all_health

    rank_final = []
    for i in range(len(all_player_info)):
        country = all_player_info[i]              #決定國家

        asset = country[2][0] + (country[1][0] + country[1][1] + country[1][2] + country[1][3]) * 0.8      #總資產 = 黃金 + (石油 + 金屬礦 + 糧食 + 木頭)  * 0.8
        education = education_year[i][0] + education_year[i][1] + education_year[i][2]                     #教育 = 基礎教育年限 + 高等教育年限 + 獨立研究機構年限
        if education == 0:                 #如果都沒有教育，以1年計
            education = 1
        health = all_health[i]
        HDI = asset * education * health     #ＨＤＩ＝（總資產＊教育年數＊人均預期壽命）

        # print(all_player_names[i], HDI)
        data = []                                   #各國資料
        data.append(all_player_names[i])
        data.append(str(HDI))
        rank_final.append(data)

        for k in range(len(rank_final)):
            rank_final[k][1] = float(rank_final[k][1])

    # print('rank_final', rank_final)
    rank_final = sorted(rank_final, key= itemgetter(1), reverse = True)    #由大到小排名，若HDI相同，先出現的先輸出
    # print('rank_final', rank_final)

    rankstr = ''
    for i in range(len(rank_final)):
        if i == 0:
            rankstr += '\n'
            rankstr += '國家  HDI分數'
            rankstr += '\n'
            rankstr += '\n'
            rankstr += rank_final[i][0]
            rankstr += ','
            rankstr += str(rank_final[i][1])
        else:
            rankstr += '\n'
            rankstr += rank_final[i][0]
            rankstr += ','
            rankstr += str(rank_final[i][1])


    f4 = tkfont.Font(size=15)
    qq = tk.Toplevel()  # Opens new window
    qq.title('Rankinfo')
    qq.geometry('400x300')  # Makes the window a certain size
    qqlbl = tk.Label(qq, text= rankstr, font = f4)
    qqlbl.pack()
    qqbtn = tk.Button(qq, text= 'ok', command = lambda: qq.destroy())
    qqbtn.pack()

def gameoverRanking():

    global rankstr
    rank_final = []
    for i in range(len(all_player_info)):
        country = all_player_info[i]              #決定國家

        asset = country[2][0] + (country[1][0] + country[1][1] + country[1][2] + country[1][3]) * 0.8      #總資產 = 黃金 + (石油 + 金屬礦 + 糧食 + 木頭)  * 0.8
        education = education_year[i][0] + education_year[i][1] + education_year[i][2]                     #教育 = 基礎教育年限 + 高等教育年限 + 獨立研究機構年限
        if education == 0:                 #如果都沒有教育，以1年計
            education = 1
        health = all_health[i]
        HDI = asset * education * health     #ＨＤＩ＝（總資產＊教育年數＊人均預期壽命）

        # print(all_player_names[i], HDI)
        data = []                                   #各國資料
        data.append(all_player_names[i])
        data.append(str(HDI))
        rank_final.append(data)

        for k in range(len(rank_final)):
            rank_final[k][1] = float(rank_final[k][1])

    # print('rank_final', rank_final)
    rank_final = sorted(rank_final, key= itemgetter(1), reverse = True)    #由大到小排名，若HDI相同，先出現的先輸出
    # print('rank_final', rank_final)

    rankstrfianl = ''
    for i in range(len(rank_final)):
        if i == 0:

            rankstrfianl += 'King of the world '
            rankstrfianl += ': '
            rankstrfianl += rank_final[i][0]
            rankstrfianl += ','
            rankstrfianl += str(rank_final[i][1])
        else:
            rankstrfianl += '\n'
            rankstrfianl += rank_final[i][0]
            rankstrfianl += ','
            rankstrfianl += str(rank_final[i][1])

    qq = tk.Toplevel()
    qq.geometry("400x300")
    f4 = tkfont.Font(size = 20)
    qqlabel = tk.Label(qq, text = rankstrfianl, font = f4)
    qqlabel.pack()
    qqbtn = ttk.Button(qq, text = 'ok', command = lambda: qq.destroy())
    qqbtn.pack()


class EndPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        f3 = tkfont.Font(size=100)
        label = tk.Label(self, text="Game Over", font=f3)
        label.pack(side="top", fill="x", pady=10)
        f4 = tkfont.Font(size=15)

#第一頁
class PageOne(tk.Frame):
    #initialization
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #以下是各個國家的圖片
        image_USA = Image.open("/Users/jimmylin/Desktop/期末專題/img/usa.png")
        image_USA = image_USA.resize((150, 100), Image.ANTIALIAS)
        self.image_USA = ImageTk.PhotoImage(image_USA)

        image_RUSSIA = Image.open("/Users/jimmylin/Desktop/期末專題/img/russia.png")
        image_RUSSIA = image_RUSSIA.resize((150, 100), Image.ANTIALIAS)
        self.image_RUSSIA = ImageTk.PhotoImage(image_RUSSIA)

        image_DESERT = Image.open("/Users/jimmylin/Desktop/期末專題/img/desert.png")
        image_DESERT = image_DESERT.resize((150, 100), Image.ANTIALIAS)
        self.image_DESERT = ImageTk.PhotoImage(image_DESERT)

        image_CHINA = Image.open("/Users/jimmylin/Desktop/期末專題/img/china.png")
        image_CHINA = image_CHINA.resize((150, 100), Image.ANTIALIAS)
        self.image_CHINA = ImageTk.PhotoImage(image_CHINA)

        image_FOREST = Image.open("/Users/jimmylin/Desktop/期末專題/img/forest.png")
        image_FOREST = image_FOREST.resize((150, 100), Image.ANTIALIAS)
        self.image_FOREST = ImageTk.PhotoImage(image_FOREST)

        image_UK = Image.open("/Users/jimmylin/Desktop/期末專題/img/uk.png")
        image_UK = image_UK.resize((150, 100), Image.ANTIALIAS)
        self.image_UK = ImageTk.PhotoImage(image_UK)

        image_UGANDA = Image.open("/Users/jimmylin/Desktop/期末專題/img/uganda.png")
        image_UGANDA = image_UGANDA.resize((150, 100), Image.ANTIALIAS)
        self.image_UGANDA = ImageTk.PhotoImage(image_UGANDA)

        image_OCEAN = Image.open("/Users/jimmylin/Desktop/期末專題/img/ocean.png")
        image_OCEAN = image_OCEAN.resize((150, 100), Image.ANTIALIAS)
        self.image_OCEAN = ImageTk.PhotoImage(image_OCEAN)

        image_TAIWAN = Image.open("/Users/jimmylin/Desktop/期末專題/img/taiwan.png")
        image_TAIWAN = image_TAIWAN.resize((150, 100), Image.ANTIALIAS)
        self.image_TAIWAN = ImageTk.PhotoImage(image_TAIWAN)

        image_POLE = Image.open("/Users/jimmylin/Desktop/期末專題/img/south_pole.png")
        image_POLE = image_POLE.resize((150, 100), Image.ANTIALIAS)
        self.image_POLE = ImageTk.PhotoImage(image_POLE)

        #以下是各個國家的button
        #用lambda 函數避免出現error
        USA_btn = ttk.Button(self, image = self.image_USA,
                        command=lambda:controller.show_frame("USA"))
        USA_btn.place(x = 75, y = 150)

        RUSSIA_btn = ttk.Button(self, image = self.image_RUSSIA,
                            command = lambda: controller.show_frame("RUSSIA"))
        RUSSIA_btn.place(x = 275, y = 150)

        DESERT_btn = ttk.Button(self, image = self.image_DESERT,
                            command = lambda: controller.show_frame("DESERT"))
        DESERT_btn.place(x = 475, y = 150)

        CHINA_btn = ttk.Button(self, image = self.image_CHINA,
                            command = lambda: controller.show_frame("CHINA"))
        CHINA_btn.place(x = 675, y = 150)

        FOREST_btn = ttk.Button(self, image = self.image_FOREST,
                            command = lambda: controller.show_frame("FOREST"))
        FOREST_btn.place(x = 875, y = 150)

        UK_btn = ttk.Button(self, image = self.image_UK,
                        command = lambda: controller.show_frame("UK"))
        UK_btn.place(x = 75, y = 350)

        UGANDA_btn = ttk.Button(self, image = self.image_UGANDA,
                            command = lambda: controller.show_frame("UGANDA"))
        UGANDA_btn.place(x = 275, y = 350)

        OCEAN_btn = ttk.Button(self, image = self.image_OCEAN,
                            command = lambda: controller.show_frame("OCEAN"))
        OCEAN_btn.place(x = 475, y = 350)

        TAIWAN_btn = ttk.Button(self, image = self.image_TAIWAN,
                            command = lambda: controller.show_frame("TAIWAN"))
        TAIWAN_btn.place(x = 675, y = 350)

        POLE_btn = ttk.Button(self, image = self.image_POLE,
                            command = lambda: controller.show_frame("POLE"))
        POLE_btn.place(x = 875, y = 350)

        # USA_btn = ttk.Button(self, text='USA', command=lambda: controller.show_frame("USA"))
        # USA_btn.place(x=75, y=150)

        # RUSSIA_btn = ttk.Button(self, text='RUSSIA', command=lambda: controller.show_frame("RUSSIA"))
        # RUSSIA_btn.place(x=275, y=150)

        # DESERT_btn = ttk.Button(self, text='DESERT', command=lambda: controller.show_frame("DESERT"))
        # DESERT_btn.place(x=475, y=150)

        # CHINA_btn = ttk.Button(self, text='CHINA', command=lambda: controller.show_frame("CHINA"))
        # CHINA_btn.place(x=675, y=150)

        # FOREST_btn = ttk.Button(self, text='FOREST', command=lambda: controller.show_frame("FOREST"))
        # FOREST_btn.place(x=875, y=150)

        # UK_btn = ttk.Button(self, text='UK', command=lambda: controller.show_frame("UK"))
        # UK_btn.place(x=75, y=350)

        # UGANDA_btn = ttk.Button(self, text='UGANDA', command=lambda: controller.show_frame("UGANDA"))
        # UGANDA_btn.place(x=275, y=350)

        # OCEAN_btn = ttk.Button(self, text='OCEAN', command=lambda: controller.show_frame("OCEAN"))
        # OCEAN_btn.place(x=475, y=350)

        # TAIWAN_btn = ttk.Button(self, text='TAIWAN', command=lambda: controller.show_frame("TAIWAN"))
        # TAIWAN_btn.place(x=675, y=350)

        # POLE_btn = ttk.Button(self, text='POLE', command=lambda: controller.show_frame("POLE"))
        # POLE_btn.place(x=875, y=350)

        #label
        format = tkfont.Font(size = 48, family = "AR DESTINE")
        label = tk.Label(self, text = "Choice a Country", font = format)
        label.pack(side = "top", fill = "x", pady = 30)



#印出國家完整的資訊(處理國家屬性)
class USA(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        format_1 = tkfont.Font(size = 36, family = "Calibri")
        format_2 = tkfont.Font(size = 18, family = "微軟正黑體")
        format_3 = tkfont.Font(size = 14, family = "微軟正黑體")
        label = tk.Label(self, text = "United States of America", font = format_1)
        label.pack(side = "top", fill = "x", pady = 10)

        info = tk.Label(self, text = "國家特色 :", font = format_2)
        info.place(x = 10, y = 85)

        info = tk.Label(self, text = "\t此國乃謂世界的金融中心，其強勢文化影響著眾多國家，在國內有的是能力極佳外交主動人才，", font = format_3)
        info.place(x = 10, y = 125)

        info = tk.Label(self, text = "\t具有靈活的外交手段，且具有強大優勢武力和高聳圍牆，能抵禦各國的攻擊。", font = format_3)
        info.place(x = 10, y = 150)

        info = tk.Label(self, text = "角色特色 :", font = format_2)
        info.place(x = 10, y = 175)

        info = tk.Label(self, text = "\t小川驕傲、好色、好鬥、愛出風頭、執行能力強，對於自己的面子很重視，絕對不承認自己的錯誤，", font = format_3)
        info.place(x = 10, y = 215)

        info = tk.Label(self, text = "\t商人治國就是喜歡的就是利益交換，注重的是最終結果，至於手段，方便就好。", font = format_3)
        info.place(x = 10, y = 245)

        label = tk.Label(self, text = "初始資源量 :", font = format_2)
        label.place(x = 10, y = 280)

        word = tk.Label(self, text = "\t石油: 1500單位\t金礦: 1500單位\t糧食: 1500單位\t木頭: 1500單位", font = format_3)
        word.place(x = 10, y = 320)

        word = tk.Label(self, text = "\t黃金: 3000單位\t人民: 2000人\t士兵: 500人", font = format_3)
        word.place(x = 10, y = 360)

        label = tk.Label(self, text = "生產倍率 :", font = format_2)
        label.place(x = 10, y = 400)

        word = tk.Label(self, text = "\t石油:  1.5  \t金礦:  1.5  \t糧食:  1.5  \t木頭:  1.5", font = format_3)
        word.place(x = 10, y = 450)

        f1 = ttk.Style()
        f1.configure('my.TButton', font=('AR CENA', 16))
        back = ttk.Button(self, text = "Back", style = "my.TButton", width = 10,
                            command = lambda: controller.show_frame("PageOne"))
        back.place(x = 375, y = 500)

        #command =  lambda: [showNextFrame(self, 'PageThree'), record_loopNum(0)])
        #這裡是mutiple command
        #用[]來讓一個btn執行多個function
        #showNextFrame()使轉換頁面
        #record_loopNum()是記錄選擇國家的變數t是多少
        confirm = ttk.Button(self, text = "Confirm", style = "my.TButton", width = 10,
                            command =  lambda: [showNextFrame(self, 'PageThree'), record_countryNum(0)])
        confirm.place(x = 575, y = 500)

#以下是剩下9個國家的class
#結構都是ㄧ樣的就不打註解了
class RUSSIA(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        format_1 = tkfont.Font(size = 48, family = "Calibri")
        format_2 = tkfont.Font(size = 18, family = "微軟正黑體")
        format_3 = tkfont.Font(size = 14, family = "微軟正黑體")
        label = tk.Label(self, text = "Russia", font = format_1)
        label.pack(side = "top", fill = "x", pady = 10)

        info = tk.Label(self, text = "國家特色 :", font = format_2)
        info.place(x = 10, y = 85)

        info = tk.Label(self, text = "\t身為戰鬥名族，具有頑強抵抗的毅力，寧為玉碎不為瓦全，善於透過焦土政策讓敵軍進攻時得不到資源。", font = format_3)
        info.place(x = 10, y = 125)

        info = tk.Label(self, text = "角色特色 :", font = format_2)
        info.place(x = 10, y = 175)

        info = tk.Label(self, text = "\t小普處在國家權力的核心，作風十分強硬，深受人民的愛戴，是一名強而有力的領導者。", font = format_3)
        info.place(x = 10, y = 205)

        label = tk.Label(self, text = "初始資源量 :", font = format_2)
        label.place(x = 10, y = 280)

        word = tk.Label(self, text = "\t石油: 2000單位\t金礦: 1400單位\t糧食: 1100單位\t木頭: 1500單位", font = format_3)
        word.place(x = 10, y = 320)

        word = tk.Label(self, text = "\t黃金: 3000單位\t人民: 2000人\t士兵: 500人", font = format_3)
        word.place(x = 10, y = 360)

        label = tk.Label(self, text = "生產倍率 :", font = format_2)
        label.place(x = 10, y = 400)

        word = tk.Label(self, text = "\t石油:  2.0  \t金礦:  1.4  \t糧食:  1.1  \t木頭:  1.5", font = format_3)
        word.place(x = 10, y = 450)

        f1 = ttk.Style()
        f1.configure('my.TButton', font=('AR CENA', 16))
        back = ttk.Button(self, text = "Back", style = "my.TButton", width = 10,
                            command = lambda: controller.show_frame("PageOne"))
        back.place(x = 375, y = 500)

        confirm = ttk.Button(self, text = "Confirm", style = "my.TButton", width = 10,
                            command =  lambda: [showNextFrame(self, 'PageThree'), record_countryNum(1)])
        confirm.place(x = 575, y = 500)

class DESERT(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        format_1 = tkfont.Font(size = 36, family = "微軟正黑體")
        format_2 = tkfont.Font(size = 18, family = "微軟正黑體")
        format_3 = tkfont.Font(size = 14, family = "微軟正黑體")
        label = tk.Label(self, text = "沙 漠 之 都", font = format_1)
        label.pack(side = "top", fill = "x", pady = 10)

        info = tk.Label(self, text = "國家特色 :", font = format_2)
        info.place(x = 10, y = 85)

        info = tk.Label(self, text = "\t曾經因為戰亂而造成家破人亡的地區，宗教的出現癒合了國家的分裂，於是成為醫療技術很高的地區。", font = format_3)
        info.place(x = 10, y = 125)

        info = tk.Label(self, text = "角色特色 :", font = format_2)
        info.place(x = 10, y = 175)

        info = tk.Label(self, text = "\t小穆身為宗教領袖，受到當地教徒的尊敬，能化解人民之間的衝突。", font = format_3)
        info.place(x = 10, y = 215)

        label = tk.Label(self, text = "初始資源量 :", font = format_2)
        label.place(x = 10, y = 280)

        word = tk.Label(self, text = "\t石油: 1800單位\t金礦: 1800單位\t糧食: 1200單位\t木頭: 1200單位", font = format_3)
        word.place(x = 10, y = 320)

        word = tk.Label(self, text = "\t黃金: 3000單位\t人民: 2000人\t士兵: 500人", font = format_3)
        word.place(x = 10, y = 360)

        label = tk.Label(self, text = "生產倍率 :", font = format_2)
        label.place(x = 10, y = 400)

        word = tk.Label(self, text = "\t石油:  1.8  \t金礦:  1.8  \t糧食:  1.2  \t木頭:  1.2", font = format_3)
        word.place(x = 10, y = 450)

        f1 = ttk.Style()
        f1.configure('my.TButton', font=('AR CENA', 16))
        back = ttk.Button(self, text = "Back", style = "my.TButton", width = 10,
                            command = lambda: controller.show_frame("PageOne"))
        back.place(x = 375, y = 500)

        confirm = ttk.Button(self, text = "Confirm", style = "my.TButton", width = 10,
                            command =  lambda: [showNextFrame(self, 'PageThree'), record_countryNum(2)])
        confirm.place(x = 575, y = 500)

class CHINA(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        format_1 = tkfont.Font(size = 36, family = "Calibri")
        format_2 = tkfont.Font(size = 18, family = "微軟正黑體")
        format_3 = tkfont.Font(size = 14, family = "微軟正黑體")
        label = tk.Label(self, text = "People Republic of China", font = format_1)
        label.pack(side = "top", fill = "x", pady = 10)

        info = tk.Label(self, text = "國家特色 :", font = format_2)
        info.place(x = 10, y = 85)

        info = tk.Label(self, text = "\t高度封閉的共產國家，政府透過高壓的手段箝制人民的言論自由，使得外界不易取得內部資訊。", font = format_3)
        info.place(x = 10, y = 125)

        info = tk.Label(self, text = "角色特色 :", font = format_2)
        info.place(x = 10, y = 175)

        info = tk.Label(self, text = "\t習維尼外表可愛，喜歡寫詩，喜歡做不可能的事，禁止所有低端吃包子。", font = format_3)
        info.place(x = 10, y = 215)

        label = tk.Label(self, text = "初始資源量 :", font = format_2)
        label.place(x = 10, y = 280)

        word = tk.Label(self, text = "\t石油: 1500單位\t金礦: 1400單位\t糧食: 1800單位\t木頭: 1300單位", font = format_3)
        word.place(x = 10, y = 320)

        word = tk.Label(self, text = "\t黃金: 3000單位\t人民: 2000人\t士兵: 500人", font = format_3)
        word.place(x = 10, y = 360)

        label = tk.Label(self, text = "生產倍率 :", font = format_2)
        label.place(x = 10, y = 400)

        word = tk.Label(self, text = "\t石油:  1.5  \t金礦:  1.4  \t糧食:  1.8  \t木頭:  1.3", font = format_3)
        word.place(x = 10, y = 450)

        f1 = ttk.Style()
        f1.configure('my.TButton', font=('AR CENA', 16))
        back = ttk.Button(self, text = "Back", style = "my.TButton", width = 10,
                            command = lambda: controller.show_frame("PageOne"))
        back.place(x = 375, y = 500)

        confirm = ttk.Button(self, text = "Confirm", style = "my.TButton", width = 10,
                            command =  lambda: [showNextFrame(self, 'PageThree'), record_countryNum(3)])
        confirm.place(x = 575, y = 500)

class FOREST(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        format_1 = tkfont.Font(size = 36, family = "微軟正黑體")
        format_2 = tkfont.Font(size = 18, family = "微軟正黑體")
        format_3 = tkfont.Font(size = 14, family = "微軟正黑體")
        label = tk.Label(self, text = "雨 林 之 都", font = format_1)
        label.pack(side = "top", fill = "x", pady = 10)

        info = tk.Label(self, text = "國家特色 :", font = format_2)
        info.place(x = 10, y = 85)

        info = tk.Label(self, text = "\t身處物產豐饒之地，糧食不虞匱乏，有大片森林當作屏障，善於游擊戰，使敵軍進攻不易。", font = format_3)
        info.place(x = 10, y = 125)

        info = tk.Label(self, text = "角色特色 :", font = format_2)
        info.place(x = 10, y = 175)

        info = tk.Label(self, text = "\t泰山飛簷走壁、靈活、八塊腹肌、超強核心肌群、有龐大動物大軍為其盟友。", font = format_3)
        info.place(x = 10, y = 215)

        label = tk.Label(self, text = "初始資源量 :", font = format_2)
        label.place(x = 10, y = 280)

        word = tk.Label(self, text = "\t石油: 1300單位\t金礦: 1200單位\t糧食: 1800單位\t木頭: 1700單位", font = format_3)
        word.place(x = 10, y = 320)

        word = tk.Label(self, text = "\t黃金: 3000單位\t人民: 2000人\t士兵: 500人", font = format_3)
        word.place(x = 10, y = 360)

        label = tk.Label(self, text = "生產倍率 :", font = format_2)
        label.place(x = 10, y = 400)

        word = tk.Label(self, text = "\t石油:  1.3  \t金礦:  1.2  \t糧食:  1.8  \t木頭:  1.7", font = format_3)
        word.place(x = 10, y = 450)

        f1 = ttk.Style()
        f1.configure('my.TButton', font=('AR CENA', 16))
        back = ttk.Button(self, text = "Back", style = "my.TButton", width = 10,
                            command = lambda: controller.show_frame("PageOne"))
        back.place(x = 375, y = 500)

        confirm = ttk.Button(self, text = "Confirm", style = "my.TButton", width = 10,
                            command =  lambda: [showNextFrame(self, 'PageThree'), record_countryNum(4)])
        confirm.place(x = 575, y = 500)

class UK(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        format_1 = tkfont.Font(size = 36, family = "Calibri")
        format_2 = tkfont.Font(size = 18, family = "微軟正黑體")
        format_3 = tkfont.Font(size = 14, family = "微軟正黑體")
        label = tk.Label(self, text = "United Kingdom", font = format_1)
        label.pack(side = "top", fill = "x", pady = 10)

        info = tk.Label(self, text = "國家特色 :", font = format_2)
        info.place(x = 10, y = 85)

        info = tk.Label(self, text = "\t科技進步，疆域廣大，戰鬥謀略極強，善於在夜晚的時候給予敵軍措手不及的突襲。", font = format_3)
        info.place(x = 10, y = 125)

        info = tk.Label(self, text = "角色特色 :", font = format_2)
        info.place(x = 10, y = 175)

        info = tk.Label(self, text = "\t小伊莉，女王在英國人心目中，是國家團結的象徵。而她的端正品行，往往是為全體國民，樹立個人行為操守的典範。", font = format_3)
        info.place(x = 10, y = 215)

        label = tk.Label(self, text = "初始資源量 :", font = format_2)
        label.place(x = 10, y = 280)

        word = tk.Label(self, text = "\t石油: 1300單位\t金礦: 1800單位\t糧食: 1600單位\t木頭: 1300單位", font = format_3)
        word.place(x = 10, y = 320)

        word = tk.Label(self, text = "\t黃金: 3000單位\t人民: 2000人\t士兵: 500人", font = format_3)
        word.place(x = 10, y = 360)

        label = tk.Label(self, text = "生產倍率 :", font = format_2)
        label.place(x = 10, y = 400)

        word = tk.Label(self, text = "\t石油:  1.3  \t金礦:  1.8  \t糧食:  1.6  \t木頭:  1.3", font = format_3)
        word.place(x = 10, y = 450)

        f1 = ttk.Style()
        f1.configure('my.TButton', font=('AR CENA', 16))
        back = ttk.Button(self, text = "Back", style = "my.TButton", width = 10,
                            command = lambda: controller.show_frame("PageOne"))
        back.place(x = 375, y = 500)

        confirm = ttk.Button(self, text = "Confirm", style = "my.TButton", width = 10,
                            command =  lambda: [showNextFrame(self, 'PageThree'), record_countryNum(5)])
        confirm.place(x = 575, y = 500)

class UGANDA(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        format_1 = tkfont.Font(size = 36, family = "Calibri")
        format_2 = tkfont.Font(size = 18, family = "微軟正黑體")
        format_3 = tkfont.Font(size = 14, family = "微軟正黑體")
        label = tk.Label(self, text = "Uganda", font = format_1)
        label.pack(side = "top", fill = "x", pady = 10)

        info = tk.Label(self, text = "國家特色 :", font = format_2)
        info.place(x = 10, y = 85)

        info = tk.Label(self, text = "\t生活在森林裡的狩獵民族，有敏銳的洞察能力，能夠在戰鬥時取得先機，先發制人。", font = format_3)
        info.place(x = 10, y = 125)

        info = tk.Label(self, text = "角色特色 :", font = format_2)
        info.place(x = 10, y = 175)

        info = tk.Label(self, text = "\t黑豹，過人的力量、速度、耐力和靈敏反應，是一名優秀的獵人、專精於野外定向追蹤。", font = format_3)
        info.place(x = 10, y = 215)

        label = tk.Label(self, text = "初始資源量 :", font = format_2)
        label.place(x = 10, y = 280)

        word = tk.Label(self, text = "\t石油: 1300單位\t金礦: 2000單位\t糧食: 1200單位\t木頭: 1500單位", font = format_3)
        word.place(x = 10, y = 320)

        word = tk.Label(self, text = "\t黃金: 3000單位\t人民: 2000人\t士兵: 500人", font = format_3)
        word.place(x = 10, y = 360)

        label = tk.Label(self, text = "生產倍率 :", font = format_2)
        label.place(x = 10, y = 400)

        word = tk.Label(self, text = "\t石油:  1.3  \t金礦:  2.0  \t糧食:  1.2  \t木頭:  1.5", font = format_3)
        word.place(x = 10, y = 450)

        f1 = ttk.Style()
        f1.configure('my.TButton', font=('AR CENA', 16))
        back = ttk.Button(self, text = "Back", style = "my.TButton", width = 10,
                            command = lambda: controller.show_frame("PageOne"))
        back.place(x = 375, y = 500)

        confirm = ttk.Button(self, text = "Confirm", style = "my.TButton", width = 10,
                            command =  lambda: [showNextFrame(self, 'PageThree'), record_countryNum(6)])
        confirm.place(x = 575, y = 500)

class OCEAN(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        format_1 = tkfont.Font(size = 36, family = "微軟正黑體")
        format_2 = tkfont.Font(size = 18, family = "微軟正黑體")
        format_3 = tkfont.Font(size = 14, family = "微軟正黑體")
        label = tk.Label(self, text = "海 洋 之 都", font = format_1)
        label.pack(side = "top", fill = "x", pady = 10)

        info = tk.Label(self, text = "國家特色 :", font = format_2)
        info.place(x = 10, y = 85)

        info = tk.Label(self, text = "\t氣候環境較為嚴峻，因此造就出人民堅強的性格，不畏懼困難的挑戰。", font = format_3)
        info.place(x = 10, y = 125)

        info = tk.Label(self, text = "角色特色 :", font = format_2)
        info.place(x = 10, y = 175)

        info = tk.Label(self, text = "\t小嗝嗝·阿倫德斯·哈德克三世，身處險峻惡劣的氣候之下，性格野蠻霸道，為海上的強權，以搶奪他國資源來當作生存機會。", font = format_3)
        info.place(x = 10, y = 215)

        label = tk.Label(self, text = "初始資源量 :", font = format_2)
        label.place(x = 10, y = 280)

        word = tk.Label(self, text = "\t石油: 1500單位\t金礦: 1300單位\t糧食: 1200單位\t木頭: 2000單位", font = format_3)
        word.place(x = 10, y = 320)

        word = tk.Label(self, text = "\t黃金: 3000單位\t人民: 2000人\t士兵: 500人", font = format_3)
        word.place(x = 10, y = 360)

        label = tk.Label(self, text = "生產倍率 :", font = format_2)
        label.place(x = 10, y = 400)

        word = tk.Label(self, text = "\t石油:  1.5  \t金礦:  1.3  \t糧食:  1.2  \t木頭:  2.0", font = format_3)
        word.place(x = 10, y = 450)

        f1 = ttk.Style()
        f1.configure('my.TButton', font=('AR CENA', 16))
        back = ttk.Button(self, text = "Back", style = "my.TButton", width = 10,
                            command = lambda: controller.show_frame("PageOne"))
        back.place(x = 375, y = 500)

        confirm = ttk.Button(self, text = "Confirm", style = "my.TButton", width = 10,
                            command =  lambda: [showNextFrame(self, 'PageThree'), record_countryNum(7)])
        confirm.place(x = 575, y = 500)

class TAIWAN(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        format_1 = tkfont.Font(size = 36, family = "Calibri")
        format_2 = tkfont.Font(size = 18, family = "微軟正黑體")
        format_3 = tkfont.Font(size = 14, family = "微軟正黑體")
        label = tk.Label(self, text = "Taiwan", font = format_1)
        label.pack(side = "top", fill = "x", pady = 10)

        info = tk.Label(self, text = "國家特色 :", font = format_2)
        info.place(x = 10, y = 85)

        info = tk.Label(self, text = "\t由資本家及財閥掌握的國家，勞工權利低落，雖然勞工遭受雇主的無情剝削，但卻也因此造就了繁榮的經濟。", font = format_3)
        info.place(x = 10, y = 125)

        info = tk.Label(self, text = "角色特色 :", font = format_2)
        info.place(x = 10, y = 175)

        info = tk.Label(self, text = "\t慣老闆，習慣對員工提出各種要求，要求員工辛苦工作，為公司賣命", font = format_3)
        info.place(x = 10, y = 215)

        label = tk.Label(self, text = "初始資源量 :", font = format_2)
        label.place(x = 10, y = 280)

        word = tk.Label(self, text = "\t石油: 1100單位\t金礦: 1300單位\t糧食: 2000單位\t木頭: 1600單位", font = format_3)
        word.place(x = 10, y = 320)

        word = tk.Label(self, text = "\t黃金: 3000單位\t人民: 2000人\t士兵: 500人", font = format_3)
        word.place(x = 10, y = 360)

        label = tk.Label(self, text = "生產倍率 :", font = format_2)
        label.place(x = 10, y = 400)

        word = tk.Label(self, text = "\t石油:  1.1  \t金礦:  1.3  \t糧食:  2.0  \t木頭:  1.6", font = format_3)
        word.place(x = 10, y = 450)

        f1 = ttk.Style()
        f1.configure('my.TButton', font=('AR CENA', 16))
        back = ttk.Button(self, text = "Back", style = "my.TButton", width = 10,
                            command = lambda: controller.show_frame("PageOne"))
        back.place(x = 375, y = 500)

        confirm = ttk.Button(self, text = "Confirm", style = "my.TButton", width = 10,
                            command =  lambda: [showNextFrame(self, 'PageThree'), record_countryNum(8)])
        confirm.place(x = 575, y = 500)

class POLE(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        format_1 = tkfont.Font(size = 36, family = "Calibri")
        format_2 = tkfont.Font(size = 18, family = "微軟正黑體")
        format_3 = tkfont.Font(size = 14, family = "微軟正黑體")
        label = tk.Label(self, text = "Antarctic", font = format_1)
        label.pack(side = "top", fill = "x", pady = 10)

        info = tk.Label(self, text = "國家特色 :", font = format_2)
        info.place(x = 10, y = 85)

        info = tk.Label(self, text = "\t冰天雪地的半封閉經濟體。", font = format_3)
        info.place(x = 10, y = 125)

        info = tk.Label(self, text = "角色特色 :", font = format_2)
        info.place(x = 10, y = 175)

        info = tk.Label(self, text = "\t企鵝王，天生好動，管不住自己的腳，是一隻毛很多、快樂的企鵝（happy feet）。", font = format_3)
        info.place(x = 10, y = 215)

        label = tk.Label(self, text = "初始資源量 :", font = format_2)
        label.place(x = 10, y = 280)

        word = tk.Label(self, text = "\t石油: 1300單位\t金礦: 1700單位\t糧食: 1200單位\t木頭: 1800單位", font = format_3)
        word.place(x = 10, y = 320)

        word = tk.Label(self, text = "\t黃金: 3000單位\t人民: 2000人\t士兵: 500人", font = format_3)
        word.place(x = 10, y = 360)

        label = tk.Label(self, text = "生產倍率 :", font = format_2)
        label.place(x = 10, y = 400)

        word = tk.Label(self, text = "\t石油:  1.3  \t金礦:  1.7  \t糧食:  1.2  \t木頭:  1.8", font = format_3)
        word.place(x = 10, y = 450)

        f1 = ttk.Style()
        f1.configure('my.TButton', font=('AR CENA', 16))
        back = ttk.Button(self, text = "Back", style = "my.TButton", width = 10,
                            command = lambda: controller.show_frame("PageOne"))
        back.place(x = 375, y = 500)

        confirm = ttk.Button(self, text = "Confirm", style = "my.TButton", width = 10,
                            command =  lambda: [showNextFrame(self, 'PageThree'), record_countryNum(9)])
        confirm.place(x = 575, y = 500)


#各個行動的頁面
class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        f3 = tkfont.Font(size = 28, family = "微軟細正體")
        label = tk.Label(self, text = "行動頁面", font = f3)
        label.pack(side = "top", fill = "x", pady = 10)

        #各個行動的btn
        f1 = ttk.Style()
        f1.configure('my.TButton', font=('AR CENA', 16))
        button_info = ttk.Button(self, text="Country Info", style = "my.TButton", width = 15,
                                    command=lambda:show_resource_info(t))
        button_info.place(x = 100, y = 100)

        button_produce = ttk.Button(self, text="Produce", style = "my.TButton", width = 15,
                                    command=lambda: controller.show_frame("Produce"))
        button_produce.place(x = 100, y = 200)

        button_Investment = ttk.Button(self, text="Investment", style = "my.TButton", width = 15,
                                    command=lambda: controller.show_frame("Investment"))
        button_Investment.place(x = 100, y = 300)

        button_Trade = ttk.Button(self, text="Trade", style = "my.TButton", width = 15,
                                    command=lambda: controller.show_frame("Trade"))
        button_Trade.place(x = 100, y = 400)

        button_NextRound = ttk.Button(self, text="Next Round", style = "my.TButton", width = 15,
                                    command=lambda: NextRound(self,'SubPage',1000, 'PageThree'))
        button_NextRound.place(x = 350, y = 500)


        button_Rank = ttk.Button(self, text = "Rank", style = "my.TButton", width = 15,
                                    command=lambda: rankFinal())
        button_Rank.place(x = 350, y = 100)

        button_Education = ttk.Button(self, text="Education", style = "my.TButton", width = 15,
                                    command=lambda: controller.show_frame("Education"))
        button_Education.place(x = 350, y = 200)

        button_Reconnoitre = ttk.Button(self, text="Reconnoitre", style = "my.TButton", width = 15,
                                        command=lambda: controller.show_frame("Reconnoitre"))
        button_Reconnoitre.place(x = 350, y = 300)

        button_War = ttk.Button(self, text="War", style = "my.TButton", width = 15,
                                        command=lambda: controller.show_frame("War"))
        button_War.place(x = 350, y = 400)

        button_War = ttk.Button(self, text="Conscription", style = "my.TButton", width = 15,
                                        command=lambda: controller.show_frame("Conscription"))
        button_War.place(x = 100, y = 500)

        button_Health = ttk.Button(self, text = "Health", style = "my.TButton", width = 15,
                                    command=lambda: controller.show_frame("Health"))
        button_Health.place(x = 600, y = 100)

        image_fun = Image.open("/Users/jimmylin/Desktop/期末專題/img/p1_jump.png")
        self.image_fun = ImageTk.PhotoImage(image_fun)
        labelimg = tk.Label(self, image = self.image_fun)
        labelimg.place(x = 600, y = 300)

        image_fun1 = Image.open("/Users/jimmylin/Desktop/期末專題/img/p1_jump.png")
        self.image_fun1 = ImageTk.PhotoImage(image_fun1)
        labelimg1 = tk.Label(self, image = self.image_fun1)
        labelimg1.place(x = 650, y = 200)

        image_fun2 = Image.open("/Users/jimmylin/Desktop/期末專題/img/p1_jump.png")
        self.image_fun2 = ImageTk.PhotoImage(image_fun2)
        labelimg2 = tk.Label(self, image = self.image_fun2)
        labelimg2.place(x = 750, y = 150)

        image_fun3 = Image.open("/Users/jimmylin/Desktop/期末專題/img/p1_jump.png")
        image_fun3 = image_fun3.resize((250, 250), Image.ANTIALIAS)
        self.image_fun3 = ImageTk.PhotoImage(image_fun3)
        labelimg3 = tk.Label(self, image = self.image_fun3)
        labelimg3.place(x = 750, y = 300)


class SubPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        f3 = tkfont.Font(size=28)
        label = tk.Label(self, text="Sub Page", font=f3)
        label.pack(side="top", fill="x", pady=10)

#這兩個func 是class produce 裡面大量用到的所以寫成function
#簡單來說就是使用者在entry中輸入 檢查後跳出一個新視窗告訴使用者訊息或者進行下一步
def wrong_input():
    r = tk.Toplevel()  # Opens new window
    r.title('wrong input')
    r.geometry('150x50')  # Makes the window a certain size
    rlbl = tk.Label(r, text='輸入錯誤，請重新輸入')
    rlbl.pack()  # Pack is like .grid(), just different
    rbtn = tk.Button(r, text = 'ok', command = lambda: r.destroy())
    rbtn.pack()

#這個func 是global 的 當你需要顯示國家資訊的時候就可以用
#info page就是用這個func 建立的
def show_resource_info(t):
    line = "{}的資源倍率和資源存量\n".format(all_player_names[t])+'\n'+"石油   資源存量: {} 資源倍率: {:.1f}".format(str(all_player_info[t][1][0]), all_player_info[t][0][0])+'\n'+"金屬   資源存量: {} 資源倍率: {:.1f}".format(str(all_player_info[t][1][1]), all_player_info[t][0][1])+'\n'+"糧食   資源存量: {} 資源倍率: {:.1f}".format(str(all_player_info[t][1][2]), all_player_info[t][0][2])+'\n'+'武器倍率: {}'.format(all_player_info[t][0][4])+'\n'+"木頭   資源存量: {} 資源倍率: {:.1f}".format(str(all_player_info[t][1][3]), all_player_info[t][0][3])+'\n'+"企鵝毛 資源存量: {}".format(str(all_player_info[t][1][4])+'\n'+"汎合金 資源存量: {}".format(str(all_player_info[t][1][5]))+'\n\n'+'黃金存量：{}'.format(all_player_info[t][2][0])+'\n'+'人民數量：{}'.format(all_player_info[t][2][1])+'\n'+'士兵數量:{}'.format(all_player_info[t][2][2])+'\n'+'機器人數量:{}'.format(all_player_info[t][2][3]))

    r = tk.Toplevel()  # Opens new window
    r.title('info')
    r.geometry('600x400')  # Makes the window a certain size
    f2 = tkfont.Font(size = 16, family = "標楷體")
    rlbl = tk.Label(r, text = line, font = f2)
    rlbl.pack()  # Pack is like .grid(), just different
    rbtn = ttk.Button(r, text = 'OK', command = lambda: r.destroy())
    rbtn.place(x = 260, y = 325)

#以下是各個行動的code
#基本上都沒什麼改動 都是原本你們寫的code
#但是在檢查輸入的部分有改動 因為不需要那麼麻煩的try except
#只要檢查是不是對的就好 對了才下一步 錯了就跳出錯誤訊息視窗即可
#還有每個原本的print statement都改成label 或者是新視窗來顯示
#
def Conscription_wrong_input(line):
    qq = tk.Toplevel()
    qq.geometry("400x300")
    qqlabel = tk.Label(qq, text =line)
    qqlabel.pack()
    qqbtn = ttk.Button(qq, text = 'ok', command = lambda: qq.destroy())
    qqbtn.pack()

#conscription
class Conscription(tk.Frame):

    global all_player_info


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        f3 = tkfont.Font(size=28)
        label = tk.Label(self, text="Conscription Page", font=f3)
        label.pack(side="top", fill="x", pady=10)

        checkbtn = ttk.Button(self, text = 'conscription', command = lambda: self.check())
        checkbtn.pack()

        returnbtn = ttk.Button(self, text = 'back', command = lambda: controller.show_frame("PageThree"))
        returnbtn.pack()

        image_fun3 = Image.open("/Users/jimmylin/Desktop/期末專題/img/shawn.png")
        image_fun3 = image_fun3.resize((400, 400), Image.ANTIALIAS)
        self.image_fun3 = ImageTk.PhotoImage(image_fun3)
        labelimg3 = tk.Label(self, image = self.image_fun3)
        labelimg3.place(x = 300, y = 150)



    # 先判斷現在的資訊，再提供選項給玩家
    # 條件（士兵>500或是機器人>1且人民>0）皆不符合，不可以操作conscription function
    def check(self):

        global all_player_info

        if all_player_info[t][2][3] == 0 and all_player_info[t][2][2] <= 500 and all_player_info[t][2][1] == 0:
            print('fail1')

            Conscription_wrong_input('抱歉，您至少需要1名人民或1個機器人或500士兵來進行操作，\n 請等待下回合天降過後再次嘗試')
            return

        else:
            print('success')

            qq = tk.Toplevel()
            qq.geometry("400x300")
            qqlabel = tk.Label(qq, text = '進行徵兵或退役')
            qqlabel.pack()

            qqbtn = ttk.Button(qq, text = '徵兵', command = lambda: Conscription.expandman())
            qqbtn.pack()

            qqbtn2 = ttk.Button(qq, text = '退役', command = lambda: Conscription.retiredman())
            qqbtn2.pack()

            qqbtn3 = ttk.Button(qq, text = '結束', command = lambda: qq.destroy())
            qqbtn3.pack()

    # 如果玩家選擇要進行徵兵
    @staticmethod
    def expandman():

        for u in range(10):
            if u != t:
                if all_player_info[u][2][1] == 0:
                    continue
              # 如果人口數=0，就沒有人可以進行徵兵，所以排除這個選項
                    # Conscription_wrong_input('{}的人口數為0，無法徵兵'.format(all_player_names[u]))
                else:
                    maxq = 100 * (all_player_info[u][2][1] // 100)  # 能徵兵的最大值（人民）
                    if maxq > all_player_info[u][2][0]:
                        maxq = 100 * (all_player_info[u][2][0] // 100)  # 能徵兵的最大值（黃金）
                    maxqq = maxq // 100
                    qlist = []
                    for k in range(maxqq + 1):
                        qlist.append(k*100)

                    quantity = random.sample(qlist, k = 1) # delete
                    quantity = int(quantity[0])

                    all_player_info[u][2][0] -= quantity  # 減去花費黃金
                    all_player_info[u][2][1] -= quantity  # 減少人民
                    all_player_info[u][2][2] += quantity  # 增加士兵

                    # Conscription_wrong_input('{}花費{}黃金，徵兵{}個人，現有{}個士兵'.format(all_player_names[u], quantity, quantity, all_player_info[u][2][2]))




        if all_player_info[t][2][1] == 0:
              # 如果人口數=0，就沒有人可以進行徵兵，所以排除這個選項
            Conscription_wrong_input('您的人口數為0，無法徵兵')
            return

        maxq = 100 * (all_player_info[t][2][1] // 100)  # 能徵兵的最大值（人民）
        if maxq > all_player_info[t][2][0]:
            maxq = 100 * (all_player_info[t][2][0] // 100)  # 能徵兵的最大值（黃金）

        print('maxq',maxq)
        # 選單（以100為單位，直到maxq的士兵人數）
        maxqq = maxq // 100
        maxq_list = []
        for q in range(maxqq+1):
            maxq_list.append(100*q)
        print('maxq_list',maxq_list)
        qq = tk.Toplevel()
        qq.geometry("400x300")
        qqlabel = tk.Label(qq, text = '您已選擇進行徵兵，請輸入要徵兵的人數')
        qqlabel.pack()

        qq.expandman_num = tk.IntVar()
        qqentry = ttk.Combobox(qq, width=12, textvariable = qq.expandman_num)
        qqentry['values'] = maxq_list
        # qqentry.current(0)
        qqentry.pack()

        qqbtn = ttk.Button(qq, text = 'ok', command = lambda: [Conscription.expandman2(qq.expandman_num.get()),qq.destroy()])
        qqbtn.pack()

    @staticmethod
    def expandman2(qnumget):

        quantity =  qnumget # delete

        all_player_info[t][2][0] -= quantity  # 減去花費黃金
        all_player_info[t][2][1] -= quantity  # 減少人民
        all_player_info[t][2][2] += quantity  # 增加士兵

        Conscription_wrong_input('您花費{}黃金，徵兵{}個人，現有{}個士兵'.format(quantity, quantity, all_player_info[t][2][2]))
        return

    # 如果玩家選擇要進行退役
    @staticmethod
    def retiredman():

        #虛擬
        for u in range(10):
            if u != t:
                if all_player_info[u][2][3] == 0 and all_player_info[u][2][2] <= 500:
                    return # 如果進行退役就會使士兵數小於500（沒有機器人時），所以排除選項1
                    # Conscription_wrong_input('{}僅有{}個士兵，無法退役'.format(all_player_names[u], all_player_info[u][2][2]))
                else:
                    if all_player_info[u][2][3] > 0:  # 能退役的最大值
                        maxq = 100 * (all_player_info[u][2][2] // 100)
                    else:
                        maxq = 100 * ((all_player_info[u][2][2] - 500) // 100)

                    # 選單（以100為單位，直到maxq的士兵人數）
                    maxqq = maxq // 100
                    maxq_list = []
                    for q in range(maxqq+1):
                        maxq_list.append(100*q)

                    rq = random.sample(maxq_list, k = 1)
                    rq = int(rq[0])
                    quantity = qnumget  # delete

                    all_player_info[u][2][1] += quantity  # 增加人民
                    all_player_info[u][2][2] -= quantity  # 減少士兵

                    # Conscription_wrong_input('{}已退役{}個兵，現有{}個士兵'.format(all_player_names[u], quantity, all_player_info[u][2][2]))



        if all_player_info[t][2][3] == 0 and all_player_info[t][2][2] <= 500:  # 如果進行退役就會使士兵數小於500（沒有機器人時），所以排除選項1
            Conscription_wrong_input('您僅有{}個士兵，無法退役'.format(all_player_info[t][2][2]))
            return


        if all_player_info[t][2][3] > 0:  # 能退役的最大值
            maxq = 100 * (all_player_info[t][2][2] // 100)
        else:
            maxq = 100 * ((all_player_info[t][2][2] - 500) // 100)

        # 選單（以100為單位，直到maxq的士兵人數）
        maxqq = maxq // 100
        maxq_list = []
        for q in range(maxqq+1):
            maxq_list.append(100*q)

        qq = tk.Toplevel()
        qq.geometry("400x300")
        qqlabel = tk.Label(qq, text = '您已選擇進行退役，請輸入要退役的人數')
        qqlabel.pack()

        qq.retiredman_num = tk.IntVar()
        qqentry = ttk.Combobox(qq, width=12, textvariable = qq.retiredman_num)
        qqentry['values'] = maxq_list
        # qqentry.current(0)
        qqentry.pack()

        qqbtn = ttk.Button(qq, text = 'ok', command = lambda: [Conscription.retiredman2(qq.retiredman_num.get()),qq.destroy()])
        qqbtn.pack()

    @staticmethod
    def retiredman2(qnumget):

        quantity = qnumget  # delete

        all_player_info[t][2][1] += quantity  # 增加人民
        all_player_info[t][2][2] -= quantity  # 減少士兵

        Conscription_wrong_input('您已退役{}個兵，現有{}個士兵'.format(quantity, all_player_info[t][2][2]))
        return

#Produce 頁面
def record_produce_time():
    global p
    print('pb',p)
    p += 1
    print('pa',p)


class Produce(tk.Frame):
    global p
    p = 0
    # 國家資訊會用到
    global all_player_info

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        f1 = tkfont.Font(size=36, family = "Bahnschrift SemiBold Condensed")
        f2 = tkfont.Font(size=22, family = "標楷體")
        label = tk.Label(self, text = "Produce", font=f1)
        label.pack(side="top", fill="x", pady=10)

        line = "規則說明:\t\t\t\t\t\t\t\t\n一、每回合最多生產四次(不限單項資源生產幾次)\t\t\t\n 二、生產的單位根據那項資源倍率所決定(1000 * 次數 * 該項倍率)\t  \n三、生產一次資源會消耗200個人民，若人民太少則無法生產\t\t"

        label2 = tk.Label(self, text=line, font=f2)
        label2.pack(side="top", fill="x", pady=10)

        self.oilcheck = tk.IntVar()
        self.produce_oil_checkButton = ttk.Checkbutton(self, text='石油', variable=self.oilcheck, onvalue=1, offvalue=0, state='mormal')
        self.produce_oil_checkButton.place(x=300, y=250)

        self.produceTime_oil = tk.IntVar()
        self.oilChosen = ttk.Combobox(self, width = 18, textvariable = self.produceTime_oil)
        self.oilChosen['values'] = (1, 2, 3, 4)
        self.oilChosen.place(x=300, y=270)
        self.oilChosen.current(0)


        self.metalcheck = tk.IntVar()
        self.produce_metal_checkButton = ttk.Checkbutton(self, width=10, text='金屬', variable=self.metalcheck, onvalue=1, offvalue=0, state='mormal')
        self.produce_metal_checkButton.place(x=300, y=370)

        self.produceTime_metal = tk.IntVar()
        self.metalChosen = ttk.Combobox(self, width=18, textvariable = self.produceTime_metal)
        self.metalChosen['values'] = (1, 2, 3, 4)
        self.metalChosen.place(x=300, y=390)
        self.metalChosen.current(0)


        self.foodcheck = tk.IntVar()
        self.produce_food_checkButton = ttk.Checkbutton(self, width=10, text='糧食', variable=self.foodcheck, onvalue=1, offvalue=0, state='mormal')
        self.produce_food_checkButton.place(x=600, y=250)

        self.produceTime_food = tk.IntVar()
        self.foodChosen = ttk.Combobox(self, width=18, textvariable = self.produceTime_food)
        self.foodChosen['values'] = (1, 2, 3, 4)
        self.foodChosen.place(x=600, y=270)
        self.foodChosen.current(0)


        self.woodcheck = tk.IntVar()
        self.produce_wood_checkButton = ttk.Checkbutton(self, width=10, text='木頭', variable=self.woodcheck, onvalue=1, offvalue=0, state='mormal')
        self.produce_wood_checkButton.place(x=600, y=370)

        self.produceTime_wood = tk.IntVar()
        self.woodChosen = ttk.Combobox(self, width=18, textvariable = self.produceTime_wood)
        self.woodChosen['values'] = (1, 2, 3, 4)
        self.woodChosen.place(x=600, y=390)
        self.woodChosen.current(0)

        f1 = ttk.Style()
        f1.configure('my.TButton', font=('AR CENA', 16))
        button = ttk.Button(self, text="ok", style = "my.TButton", width = 10,
                            command=self.produce_checkinput)
        button.place(x=400, y=475)

        button2 = ttk.Button(self, text="結束生產", style = "my.TButton", width = 10,
                             command=lambda: [controller.show_frame("PageThree")])
        button2.place(x=575, y=475)

    def RandomPlayer(self, u):
        # produce
        # 需要生產的東西和次數 （1~4個整數）

        produce_thing_list = []
        produce_thing_quantity = random.randint(1, 4)
        for i in range(produce_thing_quantity):
            produce_thing = random.randint(1, 4)
            produce_thing_list.append(produce_thing)

        produce_thing_list = sorted(set(produce_thing_list))
        # print('p', produce_thing_list)

        # 1 2 3 4
        len2list = [[1, 1], [1, 2], [1, 3], [2, 2]]
        len3list = [[1, 1, 1], [1, 1, 2]]
        # 1 1 1 1

        produce_time_list = []

        if len(produce_thing_list) == 1:
            produce_time = random.randint(1, 4)
            produce_time_list.append(produce_time)
        if len(produce_thing_list) == 2:
            produce_time = random.sample(len2list, k=1)
            random.shuffle(produce_time)
            produce_time_list = (produce_time[0])
        if len(produce_thing_list) == 3:
            produce_time = random.sample(len3list, k=1)
            random.shuffle(produce_time)
            produce_time_list = (produce_time[0])
        if len(produce_thing_list) == 4:
            produce_time_list = [1, 1, 1, 1]

        print('pp', produce_time_list)

        Produce.produce_random_part(produce_thing_list, produce_time_list, u)


    #phase two
    def produce_checkinput(self):


        global p

        if p >= 1:
            line = '生產次數已用完'
            qq = tk.Tk()  # Opens new window
            qq.title('opps!')
            qq.geometry('400x300')  # Makes the window a certain size
            qqlbl = tk.Label(qq, text=line)
            qqlbl.pack()
            qq.btn = tk.Button('ok', command = lambda: qq.destroy())
            qq.mainloop()
            return

        global all_player_info
        global produce_check
        global produce_dictionary
        global produce_time

        max_count = 0
        if self.oilcheck.get() == 1 :
            max_count += self.produceTime_oil.get()
        if self.metalcheck.get() == 1 :
            max_count +=self.produceTime_metal.get()
        if self.foodcheck.get() == 1 :
            max_count +=self.produceTime_food.get()
        if self.woodcheck.get() == 1 :
            max_count +=self.produceTime_wood.get()

        if max_count > 4:
            print('超出生產次數上限')
        else:
            produce_check = []
            produce_time = []
            max_count = 0
            if self.oilcheck.get() == 1 :
                produce_check.append(0)
                produce_time.append(self.produceTime_oil.get())
            if self.metalcheck.get() == 1 :
                produce_check.append(1)
                produce_time.append(self.produceTime_metal.get())
            if self.foodcheck.get() == 1 :
                produce_check.append(2)
                produce_time.append(self.produceTime_food.get())
            if self.woodcheck.get() == 1 :
                produce_check.append(3)
                produce_time.append(self.produceTime_wood.get())
        print('produce_check', produce_check)

        produce_dictionary = {"0": "石油", "1": "金礦", "2": "糧食", "3": "木頭"}

        produce_list = list(set(produce_check))  # 處理輸入重複的問題
        produce_list.sort()

        answer = ''  # 告訴使用者他輸入想要生產的資源

        for i in range(len(produce_list)):
            if i == 0:
                answer += "你要生產的東西為" + '\n' + produce_dictionary[str(produce_list[i])]
            else:
                answer += "\n" + produce_dictionary[str(produce_list[i])]
        if answer != '':
            qq = tk.Toplevel()  # Opens new window
            qq.title('answer')
            qq.geometry('400x300')  # Makes the window a certain size
            qqlbl = tk.Label(qq, text=answer)
            qqlbl.pack()
            qq.btn = ttk.Button(qq, text="ok",
                                command=lambda: [qq.destroy(), Produce.produce_part3(produce_list, produce_time)])
            qq.btn.pack()

        if self.oilcheck.get() == 0 and self.metalcheck.get() == 0 and self.foodcheck.get()== 0 and self.woodcheck.get() == 0 :
            pass
        else:
            for u in range(10):
                if u != t:
                    self.RandomPlayer(u)
                else:
                    continue

        #一樣把這部分處理完的結果return
        #produce_part3 會用到
        print('produce_list',produce_list, 'produce_time',produce_time)
        return (produce_list, produce_time)

    @staticmethod
    def produce_part3(produce_list, produce_time):

        global all_player_info

        #  一樣這裡才get
        b = produce_time

        for i in range(len(produce_list)):
            produce_list[i] = int(produce_list[i])
         # 檢查各資源輸入次數是否正確以及累加資源

        if len(produce_list) != len(b):
            wrong_input()

        elif len(produce_list) == len(b):

            test = 0
            # for i in range(len(b)):
            #     test += int(b[i])
            #     cost_pop = test * 200

            if test <= 4:
                messagestr = ''
                for i in range(len(b)):
                    old = all_player_info[t][1][produce_list[i]]
                    all_player_info[t][1][produce_list[i]] += int(1000 * all_player_info[t][0][produce_list[i]] * int(b[i]))
                    # print(all_player_info[t][1][produce_list[i]])
                    new = all_player_info[t][1][produce_list[i]]
                    gap = new - old

                    message = "你的{}增加{:.0f}單位，{}生產後擁有{:.0f}單位".format(produce_dictionary[str(produce_list[i])], gap, produce_dictionary[str(produce_list[i])], all_player_info[t][1][produce_list[i]])
                    if i == 0:
                        messagestr += message
                    else:
                        messagestr += '\n' + message

                # all_player_info[t][2][1] = all_player_info[t][2][1] - cost_pop

                #記錄生產次數 進入下一回合後才再次更新
                record_produce_time()

                # 顯示結果
                r = tk.Toplevel()  # Opens new window
                r.title('生產成功')
                r.geometry("%dx%d%+d%+d" % (400, 200, 500, 250))
                rlbl = tk.Label(r, text = messagestr)

                # all_player_info[t][2][1] = all_player_info[t][2][1] - cost_pop

                rlbl.pack()  # Pack is like .grid(), just different
                rbtn = tk.Button(r, text = 'ok', command = lambda: r.destroy())
                rbtn.pack()

            elif test > 4:

                r = tk.Toplevel()  # Opens new window
                r.title('wrong input')
                r.geometry('150x50')  # Makes the window a certain size
                rlbl = tk.Label(r, text='生產次數超過4次，請重新輸入')
                rlbl.pack()  # Pack is like .grid(), just different
                rbtn = tk.Button(r, text = 'ok', command = lambda: r.destroy())
                rbtn.pack()

            # elif all_player_info[t][2][1] < cost_pop:

            #     r = tk.Toplevel()  # Opens new window
            #     r.title('wrong input')
            #     r.geometry('150x50')  # Makes the window a certain size
            #     rlbl = tk.Label(r, text="人民不足，請重新嘗試，你現在只有{}個人民".format(all_player_info[t][2][1]))
            #     rlbl.pack()  # Pack is like .grid(), just different
            #     rbtn = tk.Button(r, text = 'ok', command = lambda: r.destroy())
            #     rbtn.pack()

            else:
                wrong_input()

    @staticmethod
    def produce_random_part(produce_list, produce_time, u):

        print('u', u)
        global all_player_info
        t = u

        b = produce_time

        for i in range(len(produce_list)):
            produce_list[i] = int(produce_list[i])
         # 檢查各資源輸入次數是否正確以及累加資源

        if len(produce_list) != len(b):
            wrong_input()

        elif len(produce_list) == len(b):
            test = 0
            for i in range(len(b)):
                test += int(b[i])
                cost_pop = test * 200

            if test <= 4 and all_player_info[t][2][1] >= cost_pop:
                messagestr = ''
                for i in range(len(b)):
                    old = all_player_info[t][1][produce_list[i]]
                    all_player_info[t][1][produce_list[i]] += int(1000 * all_player_info[t][0][produce_list[i]] * int(b[i]))
                    # print(all_player_info[t][1][produce_list[i]])
                    new = all_player_info[t][1][produce_list[i]]
                    gap = new - old

                    print('test',t, i)
                    try:
                        message = "{}的{}增加{:.0f}單位，{}生產後擁有{:.0f}單位".format(all_player_names[t],produce_dictionary[str(produce_list[i])], gap, produce_dictionary[str(produce_list[i])], all_player_info[t][1][produce_list[i]])
                        if i == 0:
                            messagestr += message
                        else:
                            messagestr += '\n' + message
                    except Exception as e:
                        print(t, i)
                        print(e)

                all_player_info[t][2][1] = all_player_info[t][2][1] - cost_pop


                # 顯示結果
                # r = tk.Toplevel()  # Opens new window
                # r.title('生產成功')
                # r.geometry("%dx%d%+d%+d" % (400, 200, 500, 250))
                # rlbl = tk.Label(r, text=messagestr)

                # all_player_info[t][2][1] = all_player_info[t][2][1] - cost_pop

                # rlbl.pack()  # Pack is like .grid(), just different
                # rbtn = tk.Button(r, text = 'ok', command = lambda: r.destroy())
                # rbtn.pack()

            elif test > 4:
                return
                # r = tk.Toplevel()  # Opens new window
                # r.title('wrong input')
                # r.geometry('150x50')  # Makes the window a certain size
                # rlbl = tk.Label(r, text='生產次數超過4次，請重新輸入')
                # rlbl.pack()  # Pack is like .grid(), just different
                # rbtn = tk.Button(r, text = 'ok', command = lambda: r.destroy())
                # rbtn.pack()

            elif all_player_info[t][2][1] < cost_pop:
                return
                # r = tk.Toplevel()  # Opens new window
                # r.title('wrong input')
                # r.geometry('150x50')  # Makes the window a certain size
                # rlbl = tk.Label(r, text="人民不足，請重新嘗試，你現在只有{}個人民".format(all_player_info[t][2][1]))
                # rlbl.pack()  # Pack is like .grid(), just different
                # rbtn = tk.Button(r, text = 'ok', command = lambda: r.destroy())
                # rbtn.pack()

            else:
                return




def record_invest_time():
    global I
    print('ib', I)
    I += 1
    print('ia', I)

def not_enough_resource():
    r = tk.Toplevel() # Opens new window
    r.title('not enough resource')
    r.geometry('150x50')  # Makes the window a certain size
    rlbl = tk.Label(r, text='資源不足以投資')
    rlbl.pack()  # Pack is like .grid(), just different
    rbtn = ttk.Button(r, text = 'ok', command = lambda: r.destroy())
    rbtn.pack()

#投資頁面
class Investment(tk.Frame):
    global I # 生產次數
    I = 0
    global all_player_info
    global all_invest_info
    global all_invest_names

    all_invest_info = ["Oilfield", "Ironworks", "Farm", "Sawmill", "Military", "Robot"]
    all_invest_names =["油田", "煉鐵廠", "農田", "伐木場", "軍營", "機器人"]

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        f1 = tkfont.Font(size = 36, family = "Bahnschrift SemiBold Condensed")
        f2 = tkfont.Font(size = 22, family = "標楷體")
        label = tk.Label(self, text="Investment", font=f1)
        label.pack(side="top", fill="x", pady=10)

        line = '\n'+"投 資 項 目\t   效   果  \t\t消     耗\t"+'\n'+"  油    田      石油倍率(r) + 0.2   石油1000 其三基礎各200"+'\n'+"  煉 鐵 廠      金屬倍率(r) + 0.2   金屬1000 其三基礎各200"+'\n'+"  農    田      糧食倍率(r) + 0.2   糧食1000 其三基礎各200"+'\n'+"  伐 木 場      木頭倍率(r) + 0.2   木頭1000 其三基礎各200"+'\n'+"  軍    營      武器倍率(r) + 0.5   基礎四各1000   汎合金1"+'\n'+"  機 器 人      永 久 人 民 + 500   基礎四各1000   企鵝毛1\n\n請選擇投資項目: \t\t\t\t\t"

        label2 = tk.Label(self, text=line, font=f2)
        label2.pack(side="top", fill="x")

        self.investnum = tk.StringVar()
        self.investChosen = ttk.Combobox(self, width=18, textvariable = self.investnum)
        self.investChosen['values'] = ['油田','煉鐵廠','農田','伐木場','軍營','機器人']
        self.investChosen.place(x=400, y=355)
        self.investChosen.current(0)

        f1 = ttk.Style()
        f1.configure('my.TButton', font=('AR CENA', 16))
        button = ttk.Button(self, text="OK", style = "my.TButton", width = 12,
                            command= lambda: self.investmentProcess())
        button.place(x=400, y=500)

        button2 = ttk.Button(self, text="結束投資", style = "my.TButton", width = 12,
                             command=lambda: controller.show_frame("PageThree"))
        button2.place(x=600, y=500)

    def invest_random_player(self, u):
        invest_info = random.randint(0, 5)
        Investment.investmentFinal_random_player(invest_info, u)

    def investmentProcess(self):
        global I
        global all_player_info


        if I > 4:
            r = tk.Toplevel() # Opens new window
            r.title('oops!')
            r.geometry('150x50')  # Makes the window a certain size
            rlbl = tk.Label(r, text="投資次數已達到上限")
            rlbl.pack()  # Pack is like .grid(), just different
            rbtn = tk.Button(r, text = 'ok', command = lambda: r.destroy())

            return
        # 虛擬使用者的啟動 必須放在上方check 條件之下
        for u in range(10):
            if u != t:
                print('u', u, 't', t)
                self.invest_random_player(u)
            else:
                continue
        investthing_list = ['油田','煉鐵廠','農田','伐木場','軍營','機器人']
        invest_info_2 = investthing_list.index(self.investnum.get())

        line = "\n投資" + str(all_invest_names[invest_info_2])

        r = r = tk.Toplevel()  # Opens new pop up window
        r.title('investmentProcess')
        r.geometry('200x200')  # Makes the window a certain size
        rlbl = tk.Label(r, text=line)
        rlbl.pack()  # Pack is like .grid(), just different
        rbtn = ttk.Button(r, text = 'continue', command = [Investment.investmentFinal(invest_info_2), r.destroy()])
        rbtn.pack()

        return (invest_info_2)

    @staticmethod
    def investmentFinal(invest_info_2):

        global all_player_info
        global I

        invest = invest_info_2
        print('invest', invest)
        if invest == 0:

            #如果投資油田
            all_player_info[t][1][0] -= 1000                                             #資源消耗
            all_player_info[t][1][1] -= 200
            all_player_info[t][1][2] -= 200
            all_player_info[t][1][3] -= 200
            lack = "n"
                # print(all_player_info[t])
            for i in range(4):
                if all_player_info[t][1][i] < 0:                                         #如果資源不足
                    lack = "y"
                    done = "n"
                    break
                else:
                    done = "y"

            if lack == "y":
                all_player_info[t][1][0] += 1000                                         #還他資源
                all_player_info[t][1][1] += 200
                all_player_info[t][1][2] += 200
                all_player_info[t][1][3] += 200
                not_enough_resource()
                show_resource_info(t)
                                            #然後給他看他有的資源
            elif done == "y":
                all_player_info[t][0][0] += 0.2
                record_invest_time()
                show_resource_info(t)

        elif invest == 1:
            print('in')
            all_player_info[t][1][0] -= 200
            all_player_info[t][1][1] -= 1000
            all_player_info[t][1][2] -= 200
            all_player_info[t][1][3] -= 200
            lack = "n"
                # print(all_player_info[t])
            for i in range(4):
                if all_player_info[t][1][i] < 0:
                    lack = "y"
                    done = "n"
                    break
                else:
                    done = "y"

            if lack == "y":
                all_player_info[t][1][0] += 200
                all_player_info[t][1][1] += 1000
                all_player_info[t][1][2] += 200
                all_player_info[t][1][3] += 200
                not_enough_resource()
                show_resource_info(t)

            elif done == "y":
                all_player_info[t][0][1] += 0.2
                record_invest_time()
                show_resource_info(t)


        elif invest == 2:
            all_player_info[t][1][0] -= 200
            all_player_info[t][1][1] -= 200
            all_player_info[t][1][2] -= 1000
            all_player_info[t][1][3] -= 200
            lack = "n"
                # print(all_player_info[t])
            for i in range(4):
                if all_player_info[t][1][i] < 0:
                    lack = "y"
                    done = "n"
                    break
                else:
                    done = "y"

            if lack == "y":
                all_player_info[t][1][0] += 200
                all_player_info[t][1][1] += 200
                all_player_info[t][1][2] += 1000
                all_player_info[t][1][3] += 200
                not_enough_resource()
                show_resource_info(t)

            elif done == "y":
                all_player_info[t][0][2] += 0.2
                record_invest_time()
                show_resource_info(t)


        elif invest == 3:
            all_player_info[t][1][0] -= 200
            all_player_info[t][1][1] -= 200
            all_player_info[t][1][2] -= 200
            all_player_info[t][1][3] -= 1000
            lack = "n"
                # print(all_player_info[t])
            for i in range(4):
                if all_player_info[t][1][i] < 0:
                    lack = "y"
                    done = "n"
                    break
                else:
                    done = "y"

            if lack == "y":
                all_player_info[t][1][0] += 200
                all_player_info[t][1][1] += 200
                all_player_info[t][1][2] += 200
                all_player_info[t][1][3] += 1000
                not_enough_resource()
                show_resource_info(t)

            elif done == "y":
                all_player_info[t][0][3] += 0.2
                record_invest_time()
                show_resource_info(t)

        elif invest == 5:
            print('pan')
            all_player_info[t][1][0] -= 1000
            all_player_info[t][1][1] -= 1000
            all_player_info[t][1][2] -= 1000
            all_player_info[t][1][3] -= 1000
            all_player_info[t][1][4] -= 1
            lack = "n"
                # print(all_player_info[t])
            for i in range(5):
                if all_player_info[t][1][i] < 0:
                    print('i',i)
                    lack = "y"
                    done = "n"
                    break
                else:
                    done = "y"

            if lack == "y":
                all_player_info[t][1][0] += 1000
                all_player_info[t][1][1] += 1000
                all_player_info[t][1][2] += 1000
                all_player_info[t][1][3] += 1000
                all_player_info[t][1][4] += 1
                not_enough_resource()
                show_resource_info(t)

            elif done == "y":
                all_player_info[t][2][3] += 500
                record_invest_time()
                show_resource_info(t)

        elif invest == 4:
            all_player_info[t][1][0] -= 1000
            all_player_info[t][1][1] -= 1000
            all_player_info[t][1][2] -= 1000
            all_player_info[t][1][3] -= 1000
            all_player_info[t][1][5] -= 1
            lack = "n"
                # print(all_player_info[t])
            for i in range(6):
                if all_player_info[t][1][i] < 0:
                    lack = "y"
                    done = "n"
                    break
                else:
                    done = "y"
            if lack == "y":
                all_player_info[t][1][0] += 1000
                all_player_info[t][1][1] += 1000
                all_player_info[t][1][2] += 1000
                all_player_info[t][1][3] += 1000
                all_player_info[t][1][5] += 1
                not_enough_resource()
                show_resource_info(t)

            elif done == "y":
                all_player_info[t][0][4] += 0.5
                record_invest_time()
                show_resource_info(t)
        else:
            not_enough_resource()
            # print("time", time)
            #
    @staticmethod
    def investmentFinal_random_player(invest_info, u):

        t = u
        print('final t',t)
        global all_player_info
        global I

        invest = invest_info
        if invest == 0:

            #如果投資油田
            all_player_info[t][1][0] -= 1000                                             #資源消耗
            all_player_info[t][1][1] -= 200
            all_player_info[t][1][2] -= 200
            all_player_info[t][1][3] -= 200
            lack = "n"
                # print(all_player_info[t])
            for i in range(4):
                if all_player_info[t][1][i] < 0:                                         #如果資源不足
                    lack = "y"
                    done = "n"
                    break
                else:
                    done = "y"

            if lack == "y":
                all_player_info[t][1][0] += 1000                                         #還他資源
                all_player_info[t][1][1] += 200
                all_player_info[t][1][2] += 200
                all_player_info[t][1][3] += 200
                # not_enough_resource()
                # show_resource_info(t)
                                            #然後給他看他有的資源
            elif done == "y":
                all_player_info[t][0][0] += 0.2
                # record_invest_time()
                # show_resource_info(t)

        elif invest == 1:
            all_player_info[t][1][0] -= 200
            all_player_info[t][1][1] -= 1000
            all_player_info[t][1][2] -= 200
            all_player_info[t][1][3] -= 200
            lack = "n"
                # print(all_player_info[t])
            for i in range(4):
                if all_player_info[t][1][i] < 0:
                    lack = "y"
                    done = "n"
                    break
                else:
                    done = "y"

            if lack == "y":
                all_player_info[t][1][0] += 200
                all_player_info[t][1][1] += 1000
                all_player_info[t][1][2] += 200
                all_player_info[t][1][3] += 200
                # not_enough_resource()
                # show_resource_info(t)

            elif done == "y":
                all_player_info[t][0][1] += 0.2
                # record_invest_time()
                # show_resource_info(t)


        elif invest == 2:
            all_player_info[t][1][0] -= 200
            all_player_info[t][1][1] -= 200
            all_player_info[t][1][2] -= 1000
            all_player_info[t][1][3] -= 200
            lack = "n"
                # print(all_player_info[t])
            for i in range(4):
                if all_player_info[t][1][i] < 0:
                    lack = "y"
                    done = "n"
                    break
                else:
                    done = "y"

            if lack == "y":
                all_player_info[t][1][0] += 200
                all_player_info[t][1][1] += 200
                all_player_info[t][1][2] += 1000
                all_player_info[t][1][3] += 200
                # not_enough_resource()
                # show_resource_info(t)

            elif done == "y":
                all_player_info[t][0][2] += 0.2
                # record_invest_time()
                # show_resource_info(t)


        elif invest == 3:
            all_player_info[t][1][0] -= 200
            all_player_info[t][1][1] -= 200
            all_player_info[t][1][2] -= 200
            all_player_info[t][1][3] -= 1000
            lack = "n"
                # print(all_player_info[t])
            for i in range(4):
                if all_player_info[t][1][i] < 0:
                    lack = "y"
                    done = "n"
                    break
                else:
                    done = "y"

            if lack == "y":
                all_player_info[t][1][0] += 200
                all_player_info[t][1][1] += 200
                all_player_info[t][1][2] += 200
                all_player_info[t][1][3] += 1000
                # not_enough_resource()
                # show_resource_info(t)

            elif done == "y":
                all_player_info[t][0][3] += 0.2
                # record_invest_time()
                # show_resource_info(t)

        elif invest == 4:
            all_player_info[t][1][0] -= 1000
            all_player_info[t][1][1] -= 1000
            all_player_info[t][1][2] -= 1000
            all_player_info[t][1][3] -= 1000
            all_player_info[t][1][5] -= 1
            lack = "n"
                # print(all_player_info[t])
            for i in range(5):
                if all_player_info[t][1][i] < 0:
                    lack = "y"
                    done = "n"
                    break
                else:
                    done = "y"

            if lack == "y":
                all_player_info[t][1][0] += 1000
                all_player_info[t][1][1] += 1000
                all_player_info[t][1][2] += 1000
                all_player_info[t][1][3] += 1000
                all_player_info[t][1][5] += 1
                # not_enough_resource()
                # show_resource_info(t)

            elif done == "y":
                all_player_info[t][0][4] += 0.5
                # record_invest_time()
                # show_resource_info(t)

        elif invest == 5:
            all_player_info[t][1][0] -= 1000
            all_player_info[t][1][1] -= 1000
            all_player_info[t][1][2] -= 1000
            all_player_info[t][1][3] -= 1000
            all_player_info[t][1][4] -= 1
            lack = "n"
                # print(all_player_info[t])
            for i in range(6):
                if all_player_info[t][1][i] < 0:
                    print('lll')
                    print(all_player_info[t][1][i], i)
                    lack = "y"
                    done = "n"
                    break
                else:
                    done = "y"
            if lack == "y":
                all_player_info[t][1][0] += 1000
                all_player_info[t][1][1] += 1000
                all_player_info[t][1][2] += 1000
                all_player_info[t][1][3] += 1000
                all_player_info[t][1][4] += 1
                # not_enough_resource()
                # show_resource_info(t)

            elif done == "y":
                print('sussss')
                all_player_info[t][2][4] += 500
                # record_invest_time()
                # show_resource_info(t)
        else:
            return
            # not_enough_resource()

#Trade 頁面
class Trade(tk.Frame):
    global t

    global all_player_info
    global T
    T = 0
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        f3 = tkfont.Font(size=22)
        label = tk.Label(self, text="Trade", font=f3)
        label.pack(side="top", fill="x", pady=10)

        global t

        line ='以下是商品 :石油, 金屬, 糧食, 木頭, 企鵝毛, 汎合金，\n 請選擇想要與之交易的小隊 和想要用於交易之商品'

        label2 = tk.Label(self, text=line, font=f3)
        label2.pack(side="top", fill="x", pady=10)

        line3 = '請選擇想要透過交易獲得之商品'
        label3 = tk.Label(self, text=line3, font=f3)
        label3.place(x = 300, y = 350)

        # country_list = ["美國", "俄羅斯", "沙漠之都", "中國", "熱帶栽培", "英國", "烏干達", "海洋之都", "台灣", "南極"]
        # my_country = country_list[t]

        self.allcountryname = ["美國", "俄羅斯", "沙漠之都", "中國", "熱帶栽培", "英國", "烏干達", "海洋之都", "台灣", "南極"]
        # self.allcountryname.pop(my_country)
        self.allgoodsname = ['石油', '金屬', '糧食', '木頭', '企鵝毛', '汎合金']

        self.tradenum = tk.StringVar()
        self.tradenumChosen = ttk.Combobox(self, width=12, textvariable = self.tradenum)
        self.tradenumChosen['values'] = self.allcountryname
        self.tradenumChosen.place(x=300, y=150)
        self.tradenumChosen.current(0)

        self.tradegoods = tk.StringVar()
        self.tradegoodsChosen = ttk.Combobox(self, width=12, textvariable = self.tradegoods)
        self.tradegoodsChosen['values'] = ['石油', '金屬', '糧食', '木頭', '企鵝毛', '汎合金']
        self.tradegoodsChosen.place(x=500, y=150)
        self.tradegoodsChosen.current(0)

        self.offergoods = tk.StringVar()
        self.offergoodsChosen = ttk.Combobox(self, width=12, textvariable = self.offergoods)
        self.offergoodsChosen['values'] = ['石油', '金屬', '糧食', '木頭', '企鵝毛', '汎合金']
        self.offergoodsChosen.place(x=500, y=400)
        self.offergoodsChosen.current(0)

        button = ttk.Button(self, text="ok",
                            command= lambda:self.Tradeinfocheck())
        button.place(x=600, y=500)

        button2 = ttk.Button(self, text="結束交易",
                             command=lambda: controller.show_frame("PageThree"))
        button2.place(x=700, y=500)


    def tradeRandom_player(self, u):
        u = u
        # Trade
        while True:

            trade_num = random.randint(0, 9)
            num_list = [0, 1, 2, 3, 4, 5]
            trade_goods_num, trade_goods_others_num = random.sample(num_list, k=2)

            trade_goods_num_q = random.randint(0, all_player_info[t][1][trade_goods_num])

            trade_goods_others_num_q = random.randint(0, all_player_info[t][1][trade_goods_others_num])

            if trade_goods_others_num_q == 0 or trade_goods_num_q == 0:
                continue
            # 南極條款
            if trade_goods_others_num == 4 or trade_goods_others_num == 5:
                if trade_goods_others_num_q // trade_goods_num_q < 20:
                    continue
                else:
                    break
            else:
                if trade_goods_others_num_q // trade_goods_num_q > 1.5:
                    continue
                else:
                    break
        print(trade_goods_num, trade_goods_others_num)
        print(trade_goods_num_q, trade_goods_others_num_q)

        Trade.TradeProcess3_random_player(trade_num, trade_goods_num, trade_goods_others_num,trade_goods_num_q, trade_goods_others_num_q, u)

    def Tradeinfocheck(self):
        global T

        if T > 0:
            qq = tk.Toplevel()  # Opens new window
            qq.title('process')
            qq.geometry('400x300')  # Makes the window a certain size
            qqlbl = tk.Label(qq, text='交易次數已用完')
            qqlbl.pack()
            qqbtn = tk.Button(qq, text= 'ok', command = lambda: qq.destroy())
            qqbtn.pack()
            return

        global trade_num
        global good_num_self
        global good_num_other

        trade_num = self.allcountryname.index(self.tradenum.get())
        good_num_self = self.allgoodsname.index(self.tradegoods.get())
        good_num_other = self.allgoodsname.index(self.offergoods.get())

        if trade_num == t:
            wrong_input()
        if not 0 <= trade_num <= 9:
            wrong_input()
        if not 0 <= good_num_self <= 5:
            wrong_input()
        if not 0 <= good_num_other <= 5:
            wrong_input()
        else:
            Trade.TradeProcess2(self,trade_num ,good_num_self)


    def TradeProcess2(self,trade_num ,good_num_self):

        qq = tk.Tk()  # Opens new window
        qq.title('process')
        qq.geometry('400x300')  # Makes the window a certain size
        qqlbl = tk.Label(qq, text='請輸入數量：')
        qqlbl.place(x = 25, y = 50)

        qq.label2 = tk.Label(qq, text = '提供商品')
        qq.label2.place(x = 50, y = 100)
        qq.label3 = tk.Label(qq, text = '獲得商品')
        qq.label3.place(x = 50, y = 150)

        trade_entry = tk.Entry(qq)
        trade_entry.place(x = 150, y = 100)

        offer_entry = tk.Entry(qq)
        offer_entry.place(x = 150, y = 150)

        qq.btn = ttk.Button(qq, text = 'ok',command = lambda: [Trade.TradeProcess3(trade_entry.get(), offer_entry.get()), qq.destroy()])
        qq.btn.place(x = 200, y = 250)


        for u in range(10):
            if u != t:
                self.tradeRandom_player(u)
            else:
                continue

    @staticmethod
    def TradeProcess3(x, y):

        good_num_self_q = int(x)
        good_num_other_q = int(y)

        if all_player_info[t][1][good_num_self] < good_num_self_q:
            qq = tk.Toplevel() # Opens new window
            qq.title('process')
            qq.geometry('400x300')  # Makes the window a certain size
            qqlbl = tk.Label(qq, text='貴國資源不足以用於交易')
            qqlbl.pack()
            qqbtn = ttk.Button(qq, text = 'ok', command = lambda: qq.destroy())
            qqbtn.pack()

        elif all_player_info[trade_num][1][good_num_other] < good_num_other_q:
            qq = tk.Toplevel()  # Opens new window
            qq.title('process')
            qq.geometry('400x300')  # Makes the window a certain size
            qqlbl = tk.Label(qq, text='交易對象該資源不足以用於交易')
            qqlbl.pack()
            qqbtn = ttk.Button(qq, text = 'ok', command = lambda: qq.destroy())
            qqbtn.pack()
        else:
            trade(t, trade_num, good_num_self, good_num_self_q, good_num_other,
                good_num_other_q)

    @staticmethod
    def TradeProcess3_random_player(trade_num, trade_goods_num,trade_goods_others_num,trade_goods_num_q, trade_goods_others_num_q, u):
        t = u
        trade_num = trade_num
        good_num_self = trade_goods_num
        good_num_self_q = trade_goods_num_q
        good_num_other = trade_goods_others_num
        good_num_other_q = trade_goods_others_num_q

        if all_player_info[t][1][good_num_self] < good_num_self_q:
            return
            # qq = tk.Toplevel()  # Opens new window
            # qq.title('process')
            # qq.geometry('400x300')  # Makes the window a certain size
            # qqlbl = tk.Label(qq, text='貴國資源不足以用於交易')
            # qqlbl.pack()
            # qqbtn = ttk.Button(qq, text = 'ok', command = lambda: qq.destroy())
            # qqbtn.pack()

        elif all_player_info[trade_num][1][good_num_other] < good_num_other_q:
            return
            # qq = tk.Toplevel()  # Opens new window
            # qq.title('process')
            # qq.geometry('400x300')  # Makes the window a certain size
            # qqlbl = tk.Label(qq, text='交易對象該資源不足以用於交易')
            # qqlbl.pack()
            # qqbtn = ttk.Button(qq, text = 'ok', command = lambda: qq.destroy())
            # qqbtn.pack()

        else:
            trade_random(t, trade_num, good_num_self, good_num_self_q, good_num_other, good_num_other_q)


        # qq = tk.Tk()  # Opens new window
        # qq.title('process')
        # qq.geometry('400x300')  # Makes the window a certain size
        # qqlbl = tk.Label(qq, text = '交易過程' )
        # qqlbl.pack()

        # allgoodsname = ['石油', '金屬', '糧食', '木頭', '企鵝毛', '汎合金']

        # line = '{}和{}交易，以{} {}單位換取{} {}單位'.format(all_player_names[t], all_player_names[trade_num],
        # allgoodsname[good_num_self], good_num_self_q, allgoodsname[good_num_other] ,good_num_other_q)


        # qqlbl2 = tk.Label(qq, text = line)
        # qqlbl2.pack()

        # qqbtn = ttk.Button(qq, text = 'ok', command = lambda: qq.destroy())
        # qqbtn.pack()

def trade_random(player1,player2,good1,num1,good2,num2):

    global T
    T += 1
    #小隊一
    all_player_info[player1][1][good1]-=num1 #export good1
    all_player_info[player1][1][good2]+=num2 #import good2
    #小隊

    all_player_info[player2][1][good1]+=num1 #import good1
    all_player_info[player2][1][good2]-=num2  #export good2
    # line = '以下是{}再交易後的資源數量：'.format(all_player_names[player1])+"石油數量:{} 金屬數量:{} \n 糧食數量:{} 木頭數量:{} \n 企鵝毛數量:{}, 汎合金數量:{}".format(all_player_info[player1][1][0], all_player_info[player1][1][1], all_player_info[player1][1][2], all_player_info[player1][1][3], all_player_info[player1][1][4], all_player_info[player1][1][5])

    # qq = tk.Tk()  # Opens new window
    # qq.title('process')
    # qq.geometry('400x300')  # Makes the window a certain size
    # qqlbl = tk.Label(qq, text=line)
    # qqlbl.pack()
    # qqbtn = ttk.Button(qq, text = 'ok', command = lambda: qq.destroy())
    # qqbtn.pack()
def trade(player1,player2,good1,num1,good2,num2):

    global T
    T += 1
    #小隊一
    all_player_info[player1][1][good1]-=num1 #export good1
    all_player_info[player1][1][good2]+=num2 #import good2
    #小隊

    all_player_info[player2][1][good1]+=num1 #import good1
    all_player_info[player2][1][good2]-=num2  #export good2
    line = '以下是{}再交易後的資源數量：'.format(all_player_names[player1])+"石油數量:{} 金屬數量:{} \n 糧食數量:{} 木頭數量:{} \n 企鵝毛數量:{}, 汎合金數量:{}".format(all_player_info[player1][1][0], all_player_info[player1][1][1], all_player_info[player1][1][2], all_player_info[player1][1][3], all_player_info[player1][1][4], all_player_info[player1][1][5])

    qq = tk.Tk()  # Opens new window
    qq.title('process')
    qq.geometry('400x300')  # Makes the window a certain size
    qqlbl = tk.Label(qq, text=line)
    qqlbl.pack()
    qqbtn = ttk.Button(qq, text = 'ok', command = lambda: qq.destroy())
    qqbtn.pack()


class Health(tk.Frame):
    global all_player_info

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        f3 = tkfont.Font(size=22)
        label = tk.Label(self, text="Health", font=f3)
        label.pack(side="top", fill="x", pady=10)

        line ='你今天有睡飽6小時嗎 >< ? 有就勾 沒有就不勾'

        label2 = tk.Label(self, text=line, font=f3)
        label2.pack(side="top", fill="x", pady=10)

        image_fun3 = Image.open("/Users/jimmylin/Desktop/期末專題/img/trump.png")
        image_fun3 = image_fun3.resize((400, 400), Image.ANTIALIAS)
        self.image_fun3 = ImageTk.PhotoImage(image_fun3)
        labelimg3 = tk.Label(self, image = self.image_fun3)
        labelimg3.place(x = 300, y = 150)

        self.health_check = tk.IntVar()
        self.health_check_checkButton = ttk.Checkbutton(self, text='請勾選', variable=self.health_check, onvalue=1, offvalue=0, state='mormal')
        self.health_check_checkButton.place(x=700, y=100)


        button = ttk.Button(self, text="ok",
                            command= lambda:Health.HealthFinal(self.health_check))
        button.place(x=600, y=400)

        button2 = ttk.Button(self, text="結束",
                             command=lambda: controller.show_frame("PageThree"))
        button2.place(x=700, y=400)


    # def show_rank_info():
    #     line = "以下是各國排名" + rankFinal[0][0] + rankFinal[0][1] + rankFinal[1][0] + rankFinal[0][1] + rankFinal[2][0] + rankFinal[2][1] + rankFinal[3][0] + rankFinal[3][1] + rankFinal[4][0] + rankFinal[4][1] + rankFinal[5][0] + rankFinal[5][1] + rankFinal[6][0] + rankFinal[6][1] + rankFinal[7][0] + rankFinal[7][1] + rankFinal[8][0] + rankFinal[8][1] + rankFinal[9][0] + rank[9][1]

    #     r = tk.Tk()  # Opens new window
    #     r.title('info')
    #     r.geometry('600x400')  # Makes the window a certain size
    #     rlbl = tk.Label(r, text=line)
    #     rlbl.pack()  # Pack is like .grid(), just different
    #     r.mainloop()

    @staticmethod
    def HealthFinal(Health_info):

        Health_info = int(Health_info.get())

        rank_info = Health_info
        if rank_info == 0:
            all_health[t] -= 0.1

        loop_counter_before = 1
        loop_counter = 0
        if loop_counter == loop_counter_before + 1:
            all_health += [0.1] * 10
            loop_counter_before = loop_counter
        if Health_info == 1:
            line2 = '休息是為了底更多的霸閣'
        if Health_info == 0:
            line2 = 'ＺＺＺＺＺＺＺ～～～'

        qq = tk.Toplevel()  # Opens new window
        qq.title('Rankinfo')
        qq.geometry('400x300')  # Makes the window a certain size
        qqlbl = tk.Label(qq, text= line2)
        qqlbl.pack()
        qqbtn = tk.Button(qq, text= 'ok', command = lambda: qq.destroy())
        qqbtn.pack()

        # return(rank)  #一個兩層的list，用HDI由大到小排名 [國家名, HDI]
#這兩個func 是class produce 裡面大量用到的所以寫成function
#簡單來說就是使用者在entry中輸入 檢查後跳出一個新視窗告訴使用者訊息或者進行下一步
class Reconnoitre(tk.Frame):

    global R
    R = 0
    global all_player_info

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        f3 = tkfont.Font(size=22)
        label = tk.Label(self, text="Reconnoitre", font=f3)
        label.pack(side="top", fill="x", pady=10)

        line = '您可選擇任一國家的任一資訊，將會花費您50黃金及50人民'

        label2 = tk.Label(self, text=line, font=f3)
        label2.pack(side="top", fill="x", pady=10)

        button = ttk.Button(self, text="ok", command=self.Reconnoitre_process)
        button.place(x=200, y=400)

        button2 = ttk.Button(self, text="結束偵察", command=lambda: controller.show_frame("PageThree"))
        button2.place(x=400, y=400)

        image_fun3 = Image.open("/Users/jimmylin/Desktop/期末專題/img/recon.png")
        image_fun3 = image_fun3.resize((400, 400), Image.ANTIALIAS)
        self.image_fun3 = ImageTk.PhotoImage(image_fun3)
        labelimg3 = tk.Label(self, image = self.image_fun3)
        labelimg3.place(x = 600, y = 150)

    def Reconnoitre_process(self):

        if R > 0:
            qq = tk.Toplevel()  # Opens new window
            qq.title('process')
            qq.geometry('400x300')  # Makes the window a certain size
            qqlbl = tk.Label(qq, text='徵查次數已用完')
            qqlbl.pack()
            qqbtn = tk.Button(qq, text= 'ok', command = lambda: qq.destroy())
            qqbtn.pack()
            return

        global all_player_info
        global all_player_names

        a = tk.Toplevel()
        a.geometry('500x400')
        a.title('徵兵')

        if all_player_info[t][2][0] <= 50 or all_player_info[t][2][1] <= 50:
            if all_player_info[t][2][0] <= 50:
                line = '黃金不足，無法進行偵察'
            else:
                line = '人口不足，無法進行偵察'
            f3 = tkfont.Font(size=22)
            label3 = tk.Label(a, text=line, font=f3)
            label3.pack(side="top", fill="x", pady=10)
            back = ttk.Button(a, text="返回", command=lambda: a.destroy())
            back.place(x=250, y=75)
        else:
            la1 = tk.Label(a, text="請選擇欲偵察對象：")
            la1.place(x = 50, y = 120)
            la2 = tk.Label(a, text="請選擇欲偵察資訊：")
            la2.place(x = 200, y = 120)

            def clickMe():
                global choice
                who = all_player_names.index(name.get())
                choice = ['石油', '金屬', '糧食', '木頭', '企鵝毛', '汎合金', '黃金', '人口', '士兵', '機器人']
                what = choice.index(info.get())
                if what in [0, 1, 2, 3, 4, 5]:
                    i = 1
                    j = what
                else:
                    i = 2
                    j = what - 6

                messenger = '{}的{}數量為{}'.format(all_player_names[who], choice[what], all_player_info[who][i][j])  # 印出資訊
                r = tk.Tk()
                r.title('偵察成功')
                r.geometry('400x100')
                rlbl = tk.Label(r, text=messenger)
                rlbl.pack()

                all_player_info[t][2][0] -= 50  # 減少黃金
                all_player_info[t][2][1] -= 50  # 減少人口
                global R
                R += 1
                show_resource_info(t)
                back = ttk.Button(r, text="返回", command=lambda: [r.destroy(), a.destroy()])
                back.place(x=250, y=75)

            # 按钮
            action = ttk.Button(a, text="OK", command=clickMe)
            action.place(x = 350, y = 150)

            listcountry = ["美國", "俄羅斯", "沙漠之都",  "中國", "叢林之都", "英國", "烏干達", "海洋之都", "台灣", "南極"]
            listcountry.pop(t)

            # 下拉列表
            name = tk.StringVar()
            nameChosen = ttk.Combobox(a, width=12, textvariable=name)
            nameChosen['values'] = (listcountry)
            nameChosen.place(x = 50, y = 150)
            nameChosen.current(0)

            # 下拉列表
            info = tk.StringVar()
            infoChosen = ttk.Combobox(a, width=12, textvariable=info)
            infoChosen['values'] = ('石油', '金屬', '糧食', '木頭', '企鵝毛', '汎合金', '黃金', '人口', '士兵', '機器人')
            infoChosen.place(x = 200, y = 150)
            infoChosen.current(0)
            a.mainloop()

class Education(tk.Frame):
    global all_player_info

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        f3 = tkfont.Font(size = 22)
        label = tk.Label(self, text = "Education", font = f3)
        label.pack(side = "top", fill = "x", pady = 10)
        button = ttk.Button(self, text = "繼續進行教育", command = lambda: self.education_info())
        button.place(x = 450, y = 100)

        button2 = ttk.Button(self, text = "結束教育",
                             command = lambda: controller.show_frame("PageThree"))
        button2.place(x = 600, y = 100)

        image_fun3 = Image.open("/Users/jimmylin/Desktop/期末專題/img/steve.png")
        image_fun3 = image_fun3.resize((400, 400), Image.ANTIALIAS)
        self.image_fun3 = ImageTk.PhotoImage(image_fun3)
        labelimg3 = tk.Label(self, image = self.image_fun3)
        labelimg3.place(x = 325, y = 150)

    def education_info(self):
        #randomPlayer
        for u in range(10):
            if u != t:
                if education_year[u][0] == 0 and attempt[u] == 0:
                    continueP = random.random()
                    if continueP > 0.1:
                        print('1',all_player_names[u])
                        education_proceess1_random(u)
                    else:
                        continue

                elif education_year[u][0] == 0 and attempt[u] == 1:

                    continueP = random.random()
                    if continueP > 0.2:
                        print('2',all_player_names[u])
                        education_proceess2_random(u)
                    else:
                        continue

                elif education_year[u][0] == 2 and university[u] < 5:

                    continueP = random.random()
                    if continueP > 0.35:
                        print('3',all_player_names[u])
                        education_proceess3_random(u)
                    else:
                        continue

                elif education_year[u][0] == 2 and 5 <= university[u] <= 41:

                    continueP = random.random()
                    if continueP > 0.2:
                        print('4',all_player_names[u])
                        education_proceess4_random(u)
                    else:
                        continue

                elif education_year[u][0] == 2 and university[u] >= 42:

                    continueP = random.random()
                    if continueP > 0.1:
                        print('5',all_player_names[u])
                        education_proceess5_random(u)
                    else:
                        continue

        if education_year[t][0] == 0 and attempt[t] == 0:
            global root
            root = tk.Tk()
            root.title("Education")
            root.geometry("500x150")
            info = tk.Label(root, text = "您目前只能進行基礎教育，所需花費1000黃金，\n如果這回合有人攻打你，就會失敗")
            info.place(x = 20, y = 50)
            button1 = ttk.Button(root, text = "繼續", command = education_proceess1)
            button1.place(x = 150, y = 100)
            button2 = ttk.Button(root, text = "返回", command = root.destroy)
            button2.place(x = 250, y = 100)

        elif education_year[t][0] == 0 and attempt[t] == 1:
            root = tk.Tk()
            root.title("Education")
            root.geometry("500x150")
            info = tk.Label(root, text = "第二次建設基礎教育一定會成功，\n但需花費500黃金")
            info.place(x = 20, y = 50)
            button1 = ttk.Button(root, text = "繼續", command = education_proceess2)
            button1.place(x = 150, y = 100)
            button2 = ttk.Button(root, text = "返回", command = root.destroy)
            button2.place(x = 250, y = 100)

        elif education_year[t][0] == 2 and university[t] < 5:
            root = tk.Tk()
            root.title("Education")
            root.geometry("500x150")
            info = tk.Label(root, text = "現在可以開始建設大學，建設每間大學\n費用為50黃金，每回合上限為10間")
            info.place(x = 20, y = 50)
            button1 = ttk.Button(root, text = "繼續", command = education_proceess3)
            button1.place(x = 150, y = 100)
            button2 = ttk.Button(root, text = "返回", command = root.destroy)
            button2.place(x = 250, y = 100)

        elif education_year[t][0] == 2 and 5 <= university[t] <= 41:
            root = tk.Tk()
            root.title("Education")
            root.geometry("500x150")
            info1 = tk.Label(root, text = "現在可以開始建設大學和獨立研究機構，\n建設每間大學費用為50黃金，每回合上限為10間，")
            info1.place(x = 10, y = 50)
            info2 = tk.Label(root, text = "建設每間獨立研究機構費用為250黃金，\n國家每擁有五間大學就能建設一間獨立研究機構。")
            info2.place(x = 10, y = 70)
            button1 = ttk.Button(root, text = "繼續", command = education_proceess4)
            button1.place(x = 150, y = 100)
            button2 = ttk.Button(root, text = "返回", command = root.destroy)
            button2.place(x = 250, y = 100)

        elif education_year[t][0] == 2 and university[t] >= 42:
            root = tk.Tk()
            root.title("Education")
            root.geometry("500x150")
            info1 = tk.Label(root, text = "你一定覺得很奇怪，為什麼多蓋大學後\n高等教育年限為什麼卻減少了，")
            info1.place(x = 10, y = 20)
            info2 = tk.Label(root, text = "很簡單的經濟學原理: 邊際效益遞減")
            info2.place(x = 10, y = 40)
            info3 = tk.Label(root, text = "你選擇拆除大學，試試看最大值是\n幾間大學吧~一間大學拆除費用為10黃金")
            info3.place(x = 10, y = 60)
            button1 = ttk.Button(root, text = "繼續", command = education_proceess5)
            button1.place(x = 150, y = 100)
            button2 = ttk.Button(root, text = "返回", command = root.destroy)
            button2.place(x = 250, y = 100)

def education_proceess1():
    global education_list
    if all_player_info[t][2][0] < 1000:
        edu = tk.Tk()
        edu.title("Education")
        edu.geometry("500x150")
        info = tk.Label(edu, text = "黃金不夠，請下回合再來")
        info.place(x = 20, y = 50)
        button = ttk.Button(edu, text = "返回", command = lambda: [edu.destroy(), root.destroy()])
        button.place(x = 200, y = 100)

    else:
        all_player_info[t][2][0] -= 1000
        education_list[t] = 1
        edu = tk.Tk()
        edu.title("Education")
        edu.geometry("500x150")
        info = tk.Label(edu, text = "建設基礎教育中，請待回合結束再確認")
        info.place(x = 20, y = 50)
        button = ttk.Button(edu, text = "返回", command = lambda: [edu.destroy(), root.destroy()])
        button.place(x = 200, y = 100)

def education_proceess2():
    if all_player_info[t][2][0] < 500:
        edu = tk.Tk()
        edu.title("Education")
        edu.geometry("500x150")
        info = tk.Label(edu, text = "黃金不夠，請下回合再來")
        info.place(x = 20, y = 50)
        button = ttk.Button(edu, text = "返回", command = lambda: [edu.destroy(), root.destroy()])
        button.place(x = 200, y = 100)

    else:
        all_player_info[t][2][0] -= 500
        education_year[t][0] = 2
        edu = tk.Tk()
        edu.title("Education")
        edu.geometry("500x150")
        info = tk.Label(edu, text = "建設基礎教育成功，基礎教育年限變為{}年".format(education_year[t][0]))
        info.place(x = 20, y = 50)
        button = ttk.Button(edu, text = "返回", command = lambda: [edu.destroy(), root.destroy()])
        button.place(x = 200, y = 100)

def education_proceess3():
    if all_player_info[t][2][0] < 50:
        edu = tk.Tk()
        edu.title("Education")
        edu.geometry("500x150")
        info = tk.Label(edu, text = "黃金不夠，請下回合再來")
        info.place(x = 20, y = 50)
        button = ttk.Button(edu, text = "返回", command = lambda: [edu.destroy(), root.destroy()])
        button.place(x = 200, y = 100)

    else:
        edu = tk.Tk()
        edu.title("Education")
        edu.geometry("500x150")
        edu_num = tk.IntVar()
        edu_box = ttk.Combobox(edu, width = 14, textvariable = edu_num)
        edu_box["value"] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        edu_box.place(x = 80, y = 50)
        edu_box.current(0)

        info = tk.Label(edu, text = "選擇要建設的大學間數")
        info.place(x = 77, y = 25)

        button = ttk.Button(edu, text = "OK", command = lambda: get_num())
        button.place(x = 250, y = 50)

    def get_num():
        global university_num
        university_num = edu_box.get()
        try:
            university_num = int(university_num)
            if 0 <= university_num <= 10 and all_player_info[t][2][0] >= university_num * 50:
                university[t] += university_num                                       #更新現在已蓋的大學數量
                old = float(education_year[t][1])                                     #蓋大學前的高等教育年限
                education_year[t][1] = float(education_dict[str(university[t])])      #更新高等教育的年限
                new = float(education_year[t][1])                                     #蓋大學後的高等教育年限
                gap = new - old                                                       #蓋大學前後的差距
                all_player_info[t][2][0] -= university_num * 50                       #扣掉黃金
                message = tk.Tk()
                message.title("Success")
                message.geometry("500x150")
                info1 = tk.Label(message,  text = "您花費了{}黃金，建設{}所大學".format(university_num * 50, university_num))
                info1.place(x = 20, y = 50)
                info2 = tk.Label(message,  text = "高等教育年限為{}年，變動了{:.2f}年".format(education_year[t][1], gap))
                info2.place(x = 20, y = 70)
                button = ttk.Button(message, text = "返回", command = lambda: [edu.destroy(), message.destroy(), root.destroy()])
                button.place(x = 200, y = 100)

            else:
                message = tk.Tk()
                message.title("Warning")
                message.geometry("500x150")
                info = tk.Label(message,  text = "數字輸入錯誤，請重新輸入")
                info.place(x = 20, y = 50)
                button = ttk.Button(message, text = "返回", command = lambda: message.destroy())
                button.place(x = 200, y = 100)

        except:
                message = tk.Tk()
                message.title("Warning")
                message.geometry("500x150")
                info = tk.Label(message,  text = "輸入並非數字，請重新輸入")
                info.place(x = 20, y = 50)
                button = ttk.Button(message, text = "返回", command = lambda: message.destroy())
                button.place(x = 200, y = 100)

def education_proceess4():
    if all_player_info[t][2][0] < 50:
        edu = tk.Tk()
        edu.title("Education")
        edu.geometry("500x150")
        info = tk.Label(edu, text = "黃金不夠，請下回合再來")
        info.place(x = 20, y = 50)
        button = ttk.Button(edu, text = "返回", command = lambda: [edu.destroy(), root.destroy()])
        button.place(x = 200, y = 100)

    else:
        edu = tk.Tk()
        edu.title("Education")
        edu.geometry("500x150")
        edu_num1 = tk.IntVar()
        edu_box1 = ttk.Combobox(edu, width = 14, textvariable = edu_num1)
        edu_box1["value"] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        edu_box1.place(x = 50, y = 55)
        edu_box1.current(0)
        edu_num2 = tk.IntVar()
        edu_box2 = ttk.Combobox(edu, width = 14, textvariable = edu_num2)
        edu_box2["value"] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        edu_box2.place(x = 200, y = 55)
        edu_box2.current(0)

        info1 = tk.Label(edu, text = "選擇要建設的大學間數")
        info1.place(x = 47, y = 30)

        info2 = tk.Label(edu, text = "選擇要建設的獨立研究機構間數")
        info2.place(x = 197, y = 30)

        button = ttk.Button(edu, text = "OK", command = lambda: get_num())
        button.place(x = 375, y = 55)

    def get_num():
        global university_num
        university_num = edu_box1.get()
        research_num = edu_box2.get()
        try:
            university_num = int(university_num)
            research_num = int(research_num)
            if 0 <= university_num <= 10 and all_player_info[t][2][0] >= university_num * 50 + research_num * 250 and 0 <= research_num <= 10 and university[t]//5 >= research_num:
                university[t] += university_num
                education_year[t][1] = float(education_dict[str(university[t])])
                education_year[t][2] += research_num
                all_player_info[t][2][0] -= (university_num * 50 + int(research_num * 250))
                message = tk.Tk()
                message.title("Success")
                message.geometry("500x150")
                info1 = tk.Label(message,  text ="您花費了{}黃金，建設{}所大學和{}所獨立研究機構".format(university_num * 50 + research_num * 250, university_num, research_num))
                info1.place(x = 20, y = 50)
                info2 = tk.Label(message,  text = "高等教育年限為{:.2f}年，研究機構年限為{}年".format(education_year[t][1], education_year[t][2]))
                info2.place(x = 20, y = 70)
                button = ttk.Button(message, text = "返回", command = lambda: [edu.destroy(), message.destroy(), root.destroy()])
                button.place(x = 200, y = 100)

            else:
                message = tk.Tk()
                message.title("Warning")
                message.geometry("500x150")
                info = tk.Label(message,  text = "數字輸入錯誤，請重新輸入")
                info.place(x = 20, y = 50)
                button = ttk.Button(message, text = "返回", command = lambda: message.destroy())
                button.place(x = 200, y = 100)

        except:
                message = tk.Tk()
                message.title("Warning")
                message.geometry("500x150")
                info = tk.Label(message,  text = "輸入並非數字，請重新輸入")
                info.place(x = 20, y = 50)
                button = ttk.Button(message, text = "返回", command = lambda: message.destroy())
                button.place(x = 200, y = 100)

def education_proceess5():
    if all_player_info[t][2][0] < 10:
        edu = tk.Tk()
        edu.title("Education")
        edu.geometry("500x150")
        info = tk.Label(edu, text = "黃金不夠，請下回合再來")
        info.place(x = 20, y = 50)
        button = ttk.Button(edu, text = "返回", command = lambda: [edu.destroy(), root.destroy()])
        button.place(x = 200, y = 100)

    else:
        edu = tk.Tk()
        edu.title("Education")
        edu.geometry("500x150")
        edu_num1 = tk.IntVar()
        edu_box1 = ttk.Combobox(edu, width = 14, textvariable = edu_num1)
        edu_box1["value"] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        edu_box1.place(x = 50, y = 55)
        edu_box1.current(0)
        edu_num2 = tk.IntVar()
        edu_box2 = ttk.Combobox(edu, width = 14, textvariable = edu_num2)
        edu_box2["value"] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        edu_box2.place(x = 200, y = 55)
        edu_box2.current(0)

        info1 = tk.Label(edu, text = "選擇要拆除的大學間數")
        info1.place(x = 47, y = 30)

        info2 = tk.Label(edu, text = "選擇要建設的獨立研究機構間數")
        info2.place(x = 197, y = 30)

        button = ttk.Button(edu, text = "OK", command = lambda: get_num())
        button.place(x = 375, y = 55)

    def get_num():
        global university_num
        university_num = edu_box1.get()
        research_num = edu_box2.get()
        try:
            university_num = int(university_num)
            research_num = int(research_num)
            if 0 <= university_num <= 10 and all_player_info[t][2][0] >= 10 * university_num:
                if 0 <= int(education_year[t][2]) + research_num <= university[t] //5 and university_num * 10 + research_num * 250 <= all_player_info[t][2][0]:
                    university[t] += university_num
                    education_year[t][1] = float(education_dict[str(university[t])])
                    education_year[t][2] += research_num
                    all_player_info[t][2][0] -= (university_num * 50 + int(research_num * 250))
                    message = tk.Tk()
                    message.title("Success")
                    message.geometry("500x150")
                    info1 = tk.Label(message,  text ="您花費了{}黃金，拆除{}所大學和{}所獨立研究機構".format(university_num * 50 + research_num * 250, university_num, research_num))
                    info1.place(x = 20, y = 50)
                    info2 = tk.Label(message,  text = "高等教育年限為{:.2f}年，研究機構年限為{}年".format(education_year[t][1], education_year[t][2]))
                    info2.place(x = 20, y = 70)
                    button = ttk.Button(message, text = "返回", command = lambda: [edu.destroy(), message.destroy(), root.destroy()])
                    button.place(x = 200, y = 100)

            else:
                message = tk.Tk()
                message.title("Warning")
                message.geometry("500x150")
                info = tk.Label(message,  text = "數字輸入錯誤，請重新輸入")
                info.place(x = 20, y = 50)
                button = ttk.Button(message, text = "返回", command = lambda: message.destroy())
                button.place(x = 200, y = 100)

        except:
                message = tk.Tk()
                message.title("Warning")
                message.geometry("500x150")
                info = tk.Label(message,  text = "輸入並非數字，請重新輸入")
                info.place(x = 20, y = 50)
                button = ttk.Button(message, text = "返回", command = lambda: message.destroy())
                button.place(x = 200, y = 100)

def continue_proceess1():
    for i in range(10):
        if education_list[i] != 0:
            if invaded[i] == 0:
                if i == t:
                    message = tk.Toplevel()
                    message.title("Success")
                    message.geometry("500x150")
                    info = tk.Label(message,  text = "{}，基礎教育成功!!".format(all_player_names[i]))
                    info.place(x = 20, y = 50)
                    button = ttk.Button(message, text = "返回", command = lambda: message.destroy())
                    button.place(x = 200, y = 100)
                    education_year[i][0] += 2
                    education_list[i] = 0
                else:
                    education_year[i][0] += 2
                    education_list[i] = 0
            else:
                if i == t:
                    message = tk.Toplevel()
                    message.title("Failed")
                    message.geometry("500x150")
                    info = tk.Label(message,  text = "{}基礎教育失敗，因為有{}個國家攻擊你".format(all_player_names[i],invaded[i]))
                    info.place(x = 20, y = 50)
                    button = ttk.Button(message, text = "返回", command = lambda: message.destroy())
                    button.place(x = 200, y = 100)
                else:
                    pass
        else:
            pass

def education_proceess1_random(u):
    u = u
    global education_list
    if all_player_info[u][2][0] < 1000:
        return

    else:
        all_player_info[u][2][0] -= 1000
        education_list[u] = 1
        print(all_player_names[u],'succeed')

def education_proceess2_random(u):
    u = u
    if all_player_info[u][2][0] < 500:
        return

    else:
        all_player_info[u][2][0] -= 500
        education_year[u][0] = 2

def education_proceess3_random(u):
    u = u
    if all_player_info[u][2][0] < 50:
        return

    else:

        edu_num = random.randint(1, 10)
        print(all_player_names[u] , edu_num, '大學')

        global university_num
        university_num = edu_num
        try:
            university_num = int(university_num)
            if 0 <= university_num <= 10 and all_player_info[u][2][0] >= university_num * 50:

                university[u] += university_num                                       #更新現在已蓋的大學數量
                old = float(education_year[u][1])                                     #蓋大學前的高等教育年限
                education_year[u][1] = float(education_dict[str(university[u])])      #更新高等教育的年限
                new = float(education_year[u][1])                                     #蓋大學後的高等教育年限
                gap = new - old                                                       #蓋大學前後的差距
                all_player_info[u][2][0] -= university_num * 50                       #扣掉黃金
                print('in', 'gap',gap)
            else:
                print('fail')
        except:
                print('fail')

def education_proceess4_random(u):
    u = u
    if all_player_info[u][2][0] < 50:
        return

    else:
        edu_num = random.randint(1, 10)
        edu_num2 = random.randint(1, 10)
        print(all_player_names[u] , edu_num,edu_num2, '大學研究朵')

        u = u
        global university_num
        university_num = edu_num
        research_num = edu_num2
        try:
            university_num = int(university_num)
            research_num = int(research_num)
            if 0 <= university_num <= 10 and all_player_info[u][2][0] >= university_num * 50 + research_num * 250 and 0 <= research_num <= 10 and university[u]//5 >= research_num:
                university[u] += university_num
                education_year[u][1] = float(education_dict[str(university[u])])
                education_year[u][2] += research_num
                all_player_info[u][2][0] -= (university_num * 50 + int(research_num * 250))

            else:
                print('fail')

        except:
                print('fail')

def education_proceess5_random(u):
    u = u
    if all_player_info[u][2][0] < 10:
        return

    else:
        edu_num = random.randint(1, 10)
        edu_num2 = random.randint(1, 10)
        print(all_player_names[u] , edu_num,edu_num2, '大學研究朵2')

        u = u
        global university_num
        university_num = edu_num
        research_num = edu_num2
        try:
            university_num = int(university_num)
            research_num = int(research_num)
            if 0 <= university_num <= 10 and all_player_info[u][2][0] >= 10 * university_num:
                if 0 <= int(education_year[u][2]) + research_num <= university[u] //5 and university_num * 10 + research_num * 250 <= all_player_info[u][2][0]:
                    university[u] += university_num
                    education_year[u][1] = float(education_dict[str(university[u])])
                    education_year[u][2] += research_num
                    all_player_info[u][2][0] -= (university_num * 50 + int(research_num * 250))

            else:
                print('fail')

        except:
            print('fail')

class War(tk.Frame):
    # 測試用
    global all_player_info
    global all_player_names

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        f3 = tkfont.Font(size=22)
        label = tk.Label(self, text="War", font=f3)
        label.pack(side="top", fill="x", pady=10)

        """image_fun3 = Image.open("/Users/jimmylin/Desktop/期末專題/img/war1.png")
        image_fun3 = image_fun3.resize((300, 300), Image.ANTIALIAS)
        self.image_fun3 = ImageTk.PhotoImage(image_fun3)
        labelimg3 = tk.Label(self, image = self.image_fun3)
        labelimg3.place(x = 400, y = 150)"""

        line = '戰爭開打了！'

        label2 = tk.Label(self, text=line, font=f3)
        label2.pack(side="top", fill="x", pady=10)

        button = ttk.Button(self, text="ok", command=lambda: self.prepare(), state='normal')
        button.place(x=400, y=400)

        button2 = ttk.Button(self, text="結束戰爭", command=lambda: [controller.show_frame("PageThree")])
        button2.place(x=600, y=400)

    def prepare(self):
        temp = []  # 用來暫存至今尚未分配的兵力狀況，用來判斷攻擊某國時是否用到士兵
        for i in range(10):
            temp0 = [all_player_info[i][2][2], all_player_info[i][2][3]]
            temp.append(temp0)
        print('temp', temp)
        self.random_data(temp)

        self.pre_war(temp)

    def random_data(self, temp):
        global fight, distribution, arrange
        fight = [[], [], [], [], [], [], [], [], [], []]  # 用來存欲攻擊的對象
        distribution = [[], [], [], [], [], [], [], [], [], []]  # 用來存各個國家輸入對國家的兵力分配
        arrange = [[0]] * 10  # 用來存各個國家輸入對士兵的兵力分配

        for i in range(10):
            sum = all_player_info[i][2][2] + all_player_info[i][2][3]
            if sum < 500:
                fight[i].append(100)
            else:
                fight_country_p = 0
                fight_p = random.uniform(0, 1)
                # print(fight_p)

                if fight_p >= 0.5:
                    if sum >= 500:
                        fight_country_p = random.randint(1, 1)
                    if sum >= 1000:
                        fight_country_p = random.randint(1, 2)
                    if sum >= 1500:
                        fight_country_p = random.randint(1, 3)
                    # print(fight_country_p)
                    country_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                    del country_list[i]

                    country_list_1 = random.sample(country_list, k=fight_country_p)
                    country_list_1 = sorted(country_list_1)
                    for k in range(len(country_list_1)):
                        fight[i].append(country_list_1[k])
                else:
                    fight[i].append(100)

        for k in range(len(fight)):

            all_army = all_player_info[k][2][2] + all_player_info[k][2][3]

            if fight[k] == [100]:
                distribution[k].append(all_army)
            else:

                addsoilder_p = random.uniform(0, 1)

                if len(fight[k]) == 1:
                    addsoilder = addsoilder_p * (all_army - 500)
                    h = int(addsoilder // 100)
                    distribution[k].append(500 + h * 100)
                    distribution[k].append(all_army - (500 + h * 100))

                elif len(fight[k]) == 2:
                    addsoilder = addsoilder_p * (all_army - 1000)
                    h = int(addsoilder // 100)

                    while True:
                        addsoilder_p2 = random.uniform(0, addsoilder_p)
                        if addsoilder_p + addsoilder_p2 <= 1:
                            break

                    addsoilder2 = addsoilder_p2 * (all_army - 1000)
                    h2 = int(addsoilder2 // 100)

                    print('2', addsoilder_p, addsoilder_p2)

                    distribution[k].append(500 + h * 100)
                    distribution[k].append(500 + h2 * 100)
                    distribution[k].append(all_army - 1000 - (h * 100) - (h2 * 100))

                elif len(fight[k]) == 3:
                    addsoilder = addsoilder_p * (all_army - 1500)
                    while True:
                        addsoilder_p2 = random.uniform(0, addsoilder_p)
                        addsoilder_p3 = random.uniform(0, addsoilder_p2)
                        if addsoilder_p + addsoilder_p2 + addsoilder_p3 <= 1:
                            break

                    addsoilder2 = addsoilder_p2 * (all_army - 1500)
                    addsoilder3 = addsoilder_p3 * (all_army - 1500)

                    h = int(addsoilder // 100)
                    h2 = int(addsoilder2 // 100)
                    h3 = int(addsoilder3 // 100)

                    print('3', addsoilder_p, addsoilder_p2, addsoilder_p3)
                    distribution[k].append(500 + h * 100)
                    distribution[k].append(500 + h2 * 100)
                    distribution[k].append(500 + h3 * 100)
                    distribution[k].append(all_army - 1500 - (h * 100) - (h2 * 100) - (h3 * 100))

        cc = 0
        for i in range(10):
            type_s = []
            type_r = []
            if fight[i] != [100]:
                for j in range(len(fight[i])):
                    # 判斷派兵情況，以機器人為優先
                    if temp[i][1] > 0:  # 有機器人
                        if temp[i][1] >= int(distribution[i][j]):  # 有足夠機器人
                            if temp[i][1] % int(distribution[i][j]) == 0:  # 只需要機器人
                                type_s.append(0)
                                type_r.append(int(distribution[i][j]))
                                temp[i][1] -= int(distribution[i][j])
                            else:  # 皆要
                                type_s.append(int(distribution[i][j]) - (500 * (int(distribution[i][j]) // 500)))
                                temp[i][0] -= (int(distribution[i][j]) - (500 * (int(distribution[i][j]) // 500)))
                                type_r.append(500 * (int(distribution[i][j]) // 500))
                                temp[i][1] -= (500 * (int(distribution[i][j]) // 500))
                        else:  # 沒有足夠機器人
                            type_s.append(int(distribution[i][j]) - temp[i][1])
                            temp[i][0] -= (int(distribution[i][j]) - temp[i][1])
                            type_r.append(temp[i][1])
                            temp[i][1] = 0
                    else:  # 沒有機器人
                        type_s.append(int(distribution[i][j]))
                        temp[i][0] -= int(distribution[i][j])
                        type_r.append(0)
                    cc += 1

            type_s.append(temp[i][0])
            type_r.append(temp[i][1])
            arrange[i] = type_s  # 將士兵分派情況存入arrange，用作戰爭後士兵減損的數據

        print('fight', fight)
        print('distribution', distribution)
        print('arrange', arrange)


    """def pre_war(self, temp):
        global fight, distribution, arrange
        fight = [[2, 3, 5], [5, 9], [1], [4, 9], [0], [1, 7], [8], [6], [100], [100]]
        distribution = [[800, 500, 800, 400], [500, 500, 200], [700, 600], [500, 500, 0], [500, 700], [500, 500, 100], [800, 700], [500, 300],
                    [700], [500]]
        arrange = [[800, 500, 800, 400], [0, 500, 200], [700, 600], [0, 0, 0], [500, 700], [0, 0, 100], [300, 200], [500, 300], [700], [0]]
        self.tostart()
        return"""

    def pre_war(self, temp):
        sum = all_player_info[t][2][2] + all_player_info[t][2][3]  # 總兵力
        maxq = sum // 500  # 能攻擊的國家數的最大值
        if maxq >= 9:
            maxq = 9

        a = tk.Toplevel()
        a.geometry('600x400')
        a.title('選擇攻擊對象')

        line = "您現在有{}兵力，最多可以攻擊{}個國家".format(sum, maxq)
        la1 = tk.Label(a, text=line)
        la1.place(x=50, y=50)

        # 選單（多選的方式、排除自己、加上不攻擊）
        la1 = tk.Label(a, text="請選擇要攻擊的國家:")
        la1.place(x=50, y=80)

        country0 = tk.IntVar()
        if t == 0 or maxq == 0:
            country0Chosen = ttk.Checkbutton(a, width=10, text='美國', variable=country0, onvalue=1, offvalue=0,
                                             command=lambda: check(), state='disabled')
        else:
            country0Chosen = ttk.Checkbutton(a, width=10, text='美國', variable=country0, onvalue=1, offvalue=0,
                                             command=lambda: check(), state='normal')
        country0Chosen.place(x=50, y=100)

        country1 = tk.IntVar()
        if t == 1 or maxq == 0:
            country1Chosen = ttk.Checkbutton(a, width=10, text='俄羅斯', variable=country1, onvalue=1, offvalue=0,
                                             command=lambda: check(), state='disabled')
        else:
            country1Chosen = ttk.Checkbutton(a, width=10, text='俄羅斯', variable=country1, onvalue=1, offvalue=0,
                                             command=lambda: check(), state='normal')
        country1Chosen.place(x=300, y=100)

        country2 = tk.IntVar()
        if t == 2 or maxq == 0:
            country2Chosen = ttk.Checkbutton(a, width=10, text='沙漠之都', variable=country2, onvalue=1, offvalue=0,
                                             command=lambda: check(), state='disabled')
        else:
            country2Chosen = ttk.Checkbutton(a, width=10, text='沙漠之都', variable=country2, onvalue=1, offvalue=0,
                                             command=lambda: check(), state='normal')
        country2Chosen.place(x=50, y=140)

        country3 = tk.IntVar()
        if t == 3 or maxq == 0:
            country3Chosen = ttk.Checkbutton(a, width=10, text='中國', variable=country3, onvalue=1, offvalue=0,
                                             command=lambda: check(), state='disabled')
        else:
            country3Chosen = ttk.Checkbutton(a, width=10, text='中國', variable=country3, onvalue=1, offvalue=0,
                                             command=lambda: check(), state='normal')
        country3Chosen.place(x=300, y=140)

        country4 = tk.IntVar()
        if t == 4 or maxq == 0:
            country4Chosen = ttk.Checkbutton(a, width=10, text='叢林之都', variable=country4, onvalue=1, offvalue=0,
                                             command=lambda: check(), state='disabled')
        else:
            country4Chosen = ttk.Checkbutton(a, width=10, text='叢林之都', variable=country4, onvalue=1, offvalue=0,
                                             command=lambda: check(), state='normal')
        country4Chosen.place(x=50, y=180)

        country5 = tk.IntVar()
        if t == 5 or maxq == 0:
            country5Chosen = ttk.Checkbutton(a, width=10, text='英國', variable=country5, onvalue=1, offvalue=0,
                                             command=lambda: check(), state='disabled')
        else:
            country5Chosen = ttk.Checkbutton(a, width=10, text='英國', variable=country5, onvalue=1, offvalue=0,
                                             command=lambda: check(), state='normal')
        country5Chosen.place(x=300, y=180)

        country6 = tk.IntVar()
        if t == 6 or maxq == 0:
            country6Chosen = ttk.Checkbutton(a, width=10, text='烏干達', variable=country6, onvalue=1, offvalue=0,
                                             command=lambda: check(), state='disabled')
        else:
            country6Chosen = ttk.Checkbutton(a, width=10, text='烏干達', variable=country6, onvalue=1, offvalue=0,
                                             command=lambda: check(), state='normal')
        country6Chosen.place(x=50, y=220)

        country7 = tk.IntVar()
        if t == 7 or maxq == 0:
            country7Chosen = ttk.Checkbutton(a, width=10, text='海洋之都', variable=country7, onvalue=1, offvalue=0,
                                             command=lambda: check(), state='disabled')
        else:
            country7Chosen = ttk.Checkbutton(a, width=10, text='海洋之都', variable=country7, onvalue=1, offvalue=0,
                                             command=lambda: check(), state='normal')
        country7Chosen.place(x=300, y=220)

        country8 = tk.IntVar()
        if t == 8 or maxq == 0:
            country8Chosen = ttk.Checkbutton(a, width=10, text='台灣', variable=country8, onvalue=1, offvalue=0,
                                             command=lambda: check(), state='disabled')
        else:
            country8Chosen = ttk.Checkbutton(a, width=10, text='台灣', variable=country8, onvalue=1, offvalue=0,
                                             command=lambda: check(), state='normal')
        country8Chosen.place(x=50, y=260)

        country9 = tk.IntVar()
        if t == 9 or maxq == 0:
            country9Chosen = ttk.Checkbutton(a, width=10, text='南極', variable=country9, onvalue=1, offvalue=0,
                                             command=lambda: check(), state='disabled')
        else:
            country9Chosen = ttk.Checkbutton(a, width=10, text='南極', variable=country9, onvalue=1, offvalue=0,
                                             command=lambda: check(), state='normal')
        country9Chosen.place(x=300, y=260)

        button = ttk.Button(a, text="ok", command=lambda: selected_country())
        button.place(x=450, y=260)

        def check():
            n = country0.get() + country1.get() + country2.get() + country3.get() + country4.get() + country5.get() + country6.get() + country7.get() + country8.get() + country9.get()
            if n == maxq:
                country0Chosen.configure(state='disabled')
                country1Chosen.configure(state='disabled')
                country2Chosen.configure(state='disabled')
                country3Chosen.configure(state='disabled')
                country4Chosen.configure(state='disabled')
                country5Chosen.configure(state='disabled')
                country6Chosen.configure(state='disabled')
                country7Chosen.configure(state='disabled')
                country8Chosen.configure(state='disabled')
                country9Chosen.configure(state='disabled')

        def selected_country():
            country = []
            if country0.get() == 1:
                country.append(0)
            if country1.get() == 1:
                country.append(1)
            if country2.get() == 1:
                country.append(2)
            if country3.get() == 1:
                country.append(3)
            if country4.get() == 1:
                country.append(4)
            if country5.get() == 1:
                country.append(5)
            if country6.get() == 1:
                country.append(6)
            if country7.get() == 1:
                country.append(7)
            if country8.get() == 1:
                country.append(8)
            if country9.get() == 1:
                country.append(9)
            country = sorted(country)

            # 選擇國家(編號)存入temporary
            global temporary
            temporary = []
            if len(country) == 0:
                temporary = [100]  # 如果不攻擊
                fight[t] = temporary
                distribution[t] = [sum]  # 將所有兵力拿去守城
                arrange[t] = [temp[t][0]]
            else:
                for i in range(len(country)):
                    temporary.append(int(country[i]))
                fight[t] = temporary
            assign()

        global total, dis_list
        dis_list = []  # 用來暫存兵力分配，之後再append進distribution之中
        total = 0

        def assign():
            # 輸入兵力分配  至少500 （攻擊數個選單 用選擇的方式 顯示到maxq個)
            global temporary, total
            maxp = sum
            if temporary != [100]:
                def create(mmax = maxp - (len(temporary)- 1) * 500, n = 0):
                    b = tk.Toplevel()
                    b.geometry("%dx%d%+d%+d" % (600, 400, 100, 100))
                    b.title('分配兵力')
                    line = "您現在擁有的兵力為{}，要攻擊的國家如下，請分配您的兵力".format(sum)
                    la = tk.Label(b, text=line)
                    la.place(x=50, y=50)

                    la1 = tk.Label(b, width=10, text=all_player_names[temporary[n]]+ ':')
                    la1.place(x=50, y=90)
                    k = mmax //100 + 1
                    scope = []
                    for i in range(5, k):
                        scope.append(i * 100)
                    la11 = tk.Listbox(b)
                    for i in range(len(scope)):
                        la11.insert(i + 1, scope[i])
                    la11.place(x=100, y=120)
                    la11.select_set(0)

                    b1 = tk.Button(b, text='選擇', width=15, height=2, command=lambda: selection())
                    b1.place(x=100, y=350)

                    def selection():
                        global total, k
                        how = la11.get(la11.curselection())
                        dis_list.append(how)
                        print('dis_list', dis_list)
                        total += how
                        if len(dis_list) == len(temporary):
                            # dis_list.reverse()
                            b.destroy()
                            a.destroy()
                            show()
                        else:
                            pyautogui.click(696, 521)
                        return

                    b2 = tk.Button(b, width=10, height=2, command=lambda: [minus(n), b.destroy()])
                    b2.place(x=587, y=390)
                create()

                def minus(n):
                    mmax = 500 + maxp - (len(temporary) - n - 1) * 500 - total
                    print(total, mmax)
                    n += 1
                    pyautogui.moveTo(277, 493)
                    create(mmax, n)
            else:
                show()
                a.destroy()

        def show():
            global total, dis_list
            type_s = []  # 用來暫存對各個攻擊對象的士兵數量
            type_r = []  # 用來暫存對各個攻擊對象的機器人數量
            out = ''
            cc = 0

            c = tk.Tk()
            c.geometry('600x400')
            c.title('兵力配置')
            la1 = tk.Label(c, text="您在此局的兵力配置如下：")
            la1.place(x=50, y=50)

            if temporary != [100]:
                for j in range(len(fight[t])):
                    # 判斷派兵情況，以機器人為優先
                    if temp[t][1] > 0:  # 有機器人
                        if temp[t][1] >= int(dis_list[j]):  # 有足夠機器人
                            if temp[t][1] % int(dis_list[j]) == 0:  # 只需要機器人
                                type_s.append(0)
                                type_r.append(int(dis_list[j]))
                                temp[t][1] -= int(dis_list[j])
                            else:  # 皆要
                                type_s.append(int(dis_list[j]) - (500 * (int(dis_list[j]) // 500)))
                                temp[t][0] -= (int(dis_list[j]) - (500 * (int(dis_list[j]) // 500)))
                                type_r.append(500 * (int(dis_list[j]) // 500))
                                temp[t][1] -= (500 * (int(dis_list[j]) // 500))
                        else:  # 沒有足夠機器人
                            type_s.append(int(dis_list[j]) - temp[t][1])
                            temp[t][0] -= (int(dis_list[j]) - temp[t][1])
                            type_r.append(temp[t][1])
                            temp[t][1] = 0
                    else:  # 沒有機器人
                        type_s.append(int(dis_list[j]))
                        temp[t][0] -= int(dis_list[j])
                        type_r.append(0)
                    cc += 1
                    out += '攻打'
                    out += all_player_names[fight[t][j]]
                    out += ':'
                    out += str(dis_list[j])
                    out += '  '
                    if cc % 3 == 0:
                        out += '\n'

            out += '守城：'
            out += str(sum - total)
            type_s.append(sum - total)
            type_r.append(temp[t][1])
            print(type_s)
            arrange[t] = type_s  # 將士兵分派情況存入arrange，用作戰爭後士兵減損的數據

            dis_list.append(int(sum - total))
            distribution[t] = dis_list

            la2 = tk.Label(c, text=out)
            la2.place(x=50, y=100)

            button = ttk.Button(c, text="進入戰場", command=lambda: [c.destroy(), self.tostart()])
            button.place(x=450, y=260)

            print('fight', fight)
            print('distribution', distribution)
            print('arrange', arrange)

    def war_rank(self):
        asset_old = []  # asset_old放調整前的總資產
        asset_old_number = []  # asset_old_number放編號  #change放有進行調整的編號
        for i in range(10):
            z = i
            if i != 6 and i != 9:
                asset_old.append(sum(all_player_info[i][1]) * 0.8 + all_player_info[z][2][0])
                asset_old_number.append(i)
            else:
                asset_old.append((all_player_info[z][1][0] + all_player_info[z][1][1] + all_player_info[z][1][2] +
                                  all_player_info[z][1][3]) * 0.8 + all_player_info[z][2][0])
                asset_old_number.append(i)
        global rank_of_war
        rank_of_war = []  # rank_redistribution放小隊總資產依照由小到大所排出的編號
        asset_test = zip(asset_old, asset_old_number)  # 將小隊編號和總資產和在一起
        asset_test = sorted(asset_test, key=itemgetter(0))  # 由小到大排序
        for i in range(len(asset_test)):  # 產出rank_redistribution
            rank_of_war.append(asset_test[i][1])
        print(all_player_names)
        print('RANK', rank_of_war)
        return rank_of_war

    def tostart(self):
        global protected, block
        protected = []
        rank = self.war_rank()  # 由窮到富為攻擊順序
        for z in range(10):
            me = rank[z]
            block = 0
            self.warzone(z, me)
        self.warending()

    def warending(self):
        de = tk.Toplevel()
        de.geometry("%dx%d%+d%+d" % (800, 600, 500, 250))
        de.title('戰爭結束')
        f3 = tkfont.Font(size=32)
        lab = tk.Label(de, font=f3, text='戰爭結束了')
        lab.pack()
        bu = ttk.Button(de, text="ok", width=10, command=lambda: de.destroy())
        bu.pack()

    # 戰爭
    def warzone(self, z, me):
        global invaded, amm
        invaded = [0] * 10
        amm = [0, 0]

        def showframe(i):

            def afterwar():
                ratio = ['石油倍率', '金屬倍率', '糧食倍率', '木頭倍率', '武器倍率']
                resources = ['石油', '金屬', '糧食', '木頭']

                if win == me and win == t:
                    blank = 160
                    la4 = tk.Label(d, text='{}可以奪取{}一項資源倍率，請選擇：'.format(all_player_names[win], all_player_names[lose]))
                    la4.place(x=80, y=110)
                    print('oil,metal,food,wood,武器倍率 （各物資的倍率） oil,metal,food,wood,企鵝毛,汎合金（各物資的數量）gold,opulation,soilder,永久人民')
                    print('###before', all_player_info[me])

                    def click():
                        ratio = ['石油倍率', '金屬倍率', '糧食倍率', '木頭倍率', '武器倍率']
                        seize_ratio = ratio.index(seize.get())
                        action.configure(state='disabled')
                        amount = 0.2
                        amm[0] = seize_ratio
                        if seize_ratio in [0, 1, 2, 3, 4]:
                            if all_player_info[lose][0][seize_ratio] < 0.2:
                                amount = all_player_info[lose][0][seize_ratio]
                            line = '您已選擇奪取{}{}'.format(ratio[seize_ratio], amount)
                            print('您已選擇奪取{}{}'.format(ratio[seize_ratio], amount))
                            la5 = tk.Label(d, bg='gray', text=line)
                            la5.place(x=80, y=160)
                            all_player_info[win][0][seize_ratio] += amount
                            all_player_info[lose][0][seize_ratio] -= amount

                    seize = tk.StringVar()
                    seizeChosen = ttk.Combobox(d, width=12, textvariable=seize)
                    seizeChosen['values'] = ('石油倍率', '金屬倍率', '糧食倍率', '木頭倍率', '武器倍率')
                    seizeChosen.place(x=80, y=130)
                    seizeChosen.current(0)

                    action = ttk.Button(d, text="OK", command=click)
                    action.place(x=250, y=130)

                    resources = ['石油', '金屬', '糧食', '木頭']
                    la6 = tk.Label(d, text='{}可以選擇奪取{}一項資源50%，其餘200(1+r)，請選擇：'.format(all_player_names[win],
                                                                                      all_player_names[lose]))
                    la6.place(x=80, y=190)

                    def click1():
                        resources = ['石油', '金屬', '糧食', '木頭']
                        seize_resources = resources.index(seize1.get())
                        amm[1] = seize_resources
                        action1.configure(state='disabled')
                        line = '您已選擇奪取' + resources[seize_resources] + '50%'
                        all_player_info[win][1][seize_resources] += int(all_player_info[lose][1][seize_resources] * 0.5)
                        all_player_info[lose][1][seize_resources] = int(all_player_info[lose][1][seize_resources] * 0.5)

                        c = 0
                        for i in range(4):
                            print('您已選擇奪取{}50%'.format(resources[seize_resources]), end=' ')
                            if i != seize_resources:  # 其餘200(1+r)，不足就歸零
                                if all_player_info[lose][1][i] >= int(200 * (1 + all_player_info[lose][0][i])):
                                    print('{}{}'.format(resources[i], int(200 * (1 + all_player_info[lose][0][i]))), end=' ')
                                    line += resources[i] + str(int(200 * (1 + all_player_info[lose][0][i])))
                                    all_player_info[win][1][i] += int(200 * (1 + all_player_info[lose][0][i]))
                                    all_player_info[lose][1][i] -= int(200 * (1 + all_player_info[lose][0][i]))
                                else:
                                    print('{}{}'.format(resources[i], all_player_info[lose][1][i]), end=' ')
                                    line += resources[i] + str(all_player_info[lose][1][i])
                                    all_player_info[win][1][i] += all_player_info[lose][1][i]
                                    all_player_info[lose][1][i] = 0
                                la7 = tk.Label(d, bg='gray', text=line)
                                la7.place(x=80, y=240)
                                c += 1
                            if c == 3:
                                print('')
                                break
                        print('###after', all_player_info[me])

                    seize1 = tk.StringVar()
                    seize1Chosen = ttk.Combobox(d, width=12, textvariable=seize1)
                    seize1Chosen['values'] = ('石油', '金屬', '糧食', '木頭')
                    seize1Chosen.place(x=80, y=210)
                    seize1Chosen.current(0)

                    action1 = ttk.Button(d, text="OK", command=click1)
                    action1.place(x=250, y=210)
                else:
                    blank = 110
                    amm[0] = int(random.choice([0, 1, 2, 3, 4]))
                    amm[1] = int(random.choice([0, 1, 2, 3]))

                    print(amm)
                    print('oil,metal,food,wood,武器倍率 （各物資的倍率） oil,metal,food,wood,企鵝毛,汎合金（各物資的數量）gold,opulation,soilder,永久人民')
                    print('before1', all_player_info[me])
                    amount = 0.2
                    if all_player_info[lose][0][amm[0]] < 0.2:
                        amount = all_player_info[lose][0][amm[0]]
                    print('您已選擇奪取{}{}'.format(ratio[amm[0]], amount))
                    all_player_info[win][0][amm[0]] += amount
                    all_player_info[lose][0][amm[0]] -= amount

                    all_player_info[win][1][amm[1]] += int(all_player_info[lose][1][amm[1]] * 0.5)
                    all_player_info[lose][1][amm[1]] = int(all_player_info[lose][1][amm[1]] * 0.5)

                    c = 0
                    for i in range(4):
                        print('您已選擇奪取{}50%'.format(resources[amm[1]]), end=' ')
                        if i != amm[1]:  # 其餘200(1+r)，不足就歸零
                            if all_player_info[lose][1][i] >= int(200 * (1 + all_player_info[lose][0][i])):
                                print('{}{}'.format(resources[i], int(200 * (1 + all_player_info[lose][0][i]))), end=' ')
                                all_player_info[win][1][i] += int(200 * (1 + all_player_info[lose][0][i]))
                                all_player_info[lose][1][i] -= int(200 * (1 + all_player_info[lose][0][i]))
                            else:
                                print('{}{}'.format(resources[i], all_player_info[lose][1][i]), end=' ')
                                all_player_info[win][1][i] += all_player_info[lose][1][i]
                                all_player_info[lose][1][i] = 0
                            c += 1
                        if c == 3:
                            print('')
                            break
                    print('after1', all_player_info[me])

                    """amount = 0.2
                    if all_player_info[lose][0][amm[0]] < 0.2:
                        amount = all_player_info[lose][0][amm[0]]
                    line = '您已選擇奪取{}{}'.format(ratio[amm[0]], amount)
                    la5 = tk.Label(d, bg='gray', text=line)
                    la5.place(x=80, y=blank)

                    line = '您已選擇奪取' + resources[amm[1]] + '50%'
                    c = 0
                    for i in range(4):
                        if i != amm[1]:  # 其餘200(1+r)，不足就歸零
                            if all_player_info[lose][1][i] >= int(200 * (1 + all_player_info[lose][0][i])):
                                line += resources[i] + str(int(200 * (1 + all_player_info[lose][0][i])))
                            else:
                                line += resources[i] + str(all_player_info[lose][1][i])
                            la7 = tk.Label(d, bg='gray', text=line)
                            la7.place(x=80, y=blank + 30)
                            c += 1
                        if c == 3:
                            break"""

                amount = 0.2
                if all_player_info[lose][0][amm[0]] < 0.2:
                    amount = all_player_info[lose][0][amm[0]]
                if lose == u and lose == t:
                    line = '您已被奪取{}{}'.format(ratio[amm[0]], amount)
                    la5 = tk.Label(d2, bg='gray', text=line)
                    la5.place(x=80, y=110)

                line = '您已被奪取' + resources[amm[1]] + '50%'
                c = 0
                for i in range(4):
                    if i != amm[1]:  # 其餘200(1+r)，不足就歸零
                        if all_player_info[lose][1][i] >= int(200 * (1 + all_player_info[lose][0][i])):
                            line += resources[i] + str(int(200 * (1 + all_player_info[lose][0][i])))
                        else:
                            line += resources[i] + str(all_player_info[lose][1][i])
                        if lose == u and lose == t:
                            la7 = tk.Label(d2, bg='gray', text=line)
                            la7.place(x=80, y=140)
                        c += 1
                    if c == 3:
                        break

            u = fight[me][i]
            global protected
            if me == t:
                d = tk.Toplevel()
                d.geometry("%dx%d%+d%+d" % (800, 600, 500, 250))
                d.title('戰場-攻擊方')
                la = tk.Label(d, text='{}.{}'.format(z, all_player_names[me]))
                la.place(x=50, y=50)
            if u == t:
                d2 = tk.Toplevel()
                d2.geometry("%dx%d%+d%+d" % (800, 600, 500, 250))
                d2.title('戰場-守城方')
                la = tk.Label(d2, text='{}.{}'.format(z, all_player_names[u]))
                la.place(x=50, y=50)

            if u in protected:
                if me == t:
                    la1 = tk.Label(d, text='你選擇攻打{}: {}在防護罩底下，攻擊無效'.format(all_player_names[u], all_player_names[u], all_player_names[u]))
                    la1.place(x=50, y=80)
                    bu = ttk.Button(d, text="結束", command=lambda: d.destroy())
                    bu.place(x=350, y=110)
                if u == t:
                    la1 = tk.Label(d2, text='被{}攻打，但因為你在防護罩下，攻擊無效'.format(all_player_names[me]))
                    la1.place(x=50, y=80)
                    bu = ttk.Button(d2, text="結束", command=lambda: d2.destroy())
                    bu.place(x=350, y=110)
                print('{}回合，{}打{}，{}在防護罩下'.format(z, all_player_names[me], all_player_names[u], all_player_names[u]))
                i += 1
            else:
                strength_me = distribution[me][i] * float(all_player_info[me][0][4])  # 計算己方武力值
                strength_u = distribution[u][-1] * float(all_player_info[u][0][4])  # 計算對方武力值
                print('{}的武力:{}, {}的武力:{}'.format(all_player_names[me], strength_me, all_player_names[u], strength_u))
                invaded[u] += 1  # 如果遭受攻擊，就＋１

                if strength_me == strength_u:  # 武力值相同的情況
                    if me == t:
                        la2 = tk.Label(d, text='你選擇攻打{}: 兩國武力值皆為{}，此回合和局'.format(all_player_names[u], int(strength_me)))
                        la2.place(x=50, y=80)
                        bu = ttk.Button(d, text="結束", command=lambda: d.destroy())
                        bu.place(x=350, y=110)
                    if u == t:
                        la2 = tk.Label(d2, text='被{}攻打: 兩國武力值皆為{}，此回合和局'.format(all_player_names[me], int(strength_me)))
                        la2.place(x=50, y=80)
                        bu = ttk.Button(d2, text="結束", command=lambda: d2.destroy())
                        bu.place(x=350, y=110)
                    print('{}回合，{}{}和局'.format(z, all_player_names[me], all_player_names[u]))

                    all_player_info[me][2][2] -= int(float(arrange[me][i]) * 0.1)
                    all_player_info[u][2][2] -= int(float(arrange[u][-1]) * 0.1)
                    arrange[u][-1] -= int(float(arrange[u][-1]) * 0.1)
                    i += 1

                else:  # 判斷輸贏
                    global win, lose
                    if strength_me > strength_u:  # 攻擊方win
                        win = me
                        lose = u
                        if me == t:
                            la3 = tk.Label(d, text='你選擇攻打{}，此回合你贏得勝利'.format(all_player_names[lose]))
                            la3.place(x=50, y=80)
                        if u == t:
                            la4 = tk.Label(d2, text='被{}攻打，此回合你守城失敗'.format(all_player_names[win]))
                            la4.place(x=50, y=80)

                        all_player_info[me][2][2] -= int(float(arrange[me][i]) * 0.1)
                        all_player_info[u][2][2] -= int(float(arrange[u][-1]) * 0.3)
                        distribution[u][-1] -= int(float(arrange[u][-1]) * 0.3)
                        arrange[u][-1] -= int(float(arrange[u][-1]) * 0.3)

                        afterwar()
                        if me == t:
                            bu = ttk.Button(d, text="結束", command=lambda: d.destroy())
                            bu.place(x=350, y=270)
                        if u == t:
                            bu = ttk.Button(d2, text="結束", command=lambda: d2.destroy())
                            bu.place(x=350, y=170)

                    else:  # 守城方win
                        win = u
                        lose = me

                        if win == t:
                            la3 = tk.Label(d2, text='被{}攻打，此回合你守城成功'.format(all_player_names[lose]))
                            la3.place(x=50, y=80)
                            bu = ttk.Button(d2, text="結束", command=lambda: d2.destroy())
                            bu.place(x=350, y=110)
                        if lose == t:
                            la4 = tk.Label(d, text='你選擇攻打{}，此回合你鎩羽而歸'.format(all_player_names[win]))
                            la4.place(x=50, y=80)
                            bu = ttk.Button(d, text="結束", command=lambda: d.destroy())
                            bu.place(x=350, y=110)

                        all_player_info[u][2][2] -= int(float(arrange[u][-1]) * 0.1)
                        all_player_info[me][2][2] -= int(float(arrange[me][i]) * 0.3)
                        distribution[u][-1] -= int(float(arrange[u][-1]) * 0.1)
                        arrange[u][-1] -= int(float(arrange[u][-1]) * 0.1)

                    print('{}回合，{}攻擊{}, {}贏{}輸'.format(z, all_player_names[me], all_player_names[u],
                                                            all_player_names[win], all_player_names[lose]))

                    if lose not in protected:  # 將輸家append進保護罩之中
                        protected.append(lose)
                    i += 1

            ifnextround(i)

        def ifnextround(i):
            if i == len(fight[me]):
                return
            else:
                showframe(i)

        if fight[me] == [100]:  # 如果玩家先前選擇不攻擊
            if me == t:
                d0 = tk.Toplevel()
                d0.geometry("%dx%d%+d%+d" % (800, 600, 500, 250))
                d0.title('戰場-攻擊方')
                la = tk.Label(d0, text='{}.{}'.format(z, all_player_names[me]))
                la.place(x=50, y=50)

                la1 = tk.Label(d0, text='在此戰爭中，你選擇不攻擊任何國家')
                la1.place(x=50, y=80)
                bu = ttk.Button(d0, text="結束", command=lambda: d0.destroy())
                bu.place(x=350, y=110)

            print('{}回合，{}，沒有戰爭發生'.format(z, all_player_names[me]))
            return
        else:
            showframe(0)




if __name__ == "__main__":
    app = SampleApp()
    app.title("NTU ECON Game")
    app.mainloop()
