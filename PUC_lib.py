# -*-coding:utf-8 -*-
from  ctypes import *
from PIL import ImageGrab
import sys
import time
import os
from PIL import ImageFilter
import pytesseract
import xlrd
from PIL import  Image
import math
import operator
from functools import reduce
class base_Test():
    def __int__(self):
        pass
    def return_Color(self,im,x,y):
        c=im.getpixel((x,y))
        if (125 < c[0] < 145) & (160 < c[1] < 180) & (20 < c[2] < 40):
            tmp = 'green'
        elif (70 < c[0] < 90) & (75 < c[1] < 85) & (80 < c[2] < 95):
            tmp = 'grey'
        elif (20 < c[0] < 35) & (110 < c[1] < 125) & (200 < c[2] < 215):
            tmp = 'blue'
        elif (200 < c[0] < 215) & (120 < c[1] < 135) & (20 < c[2] < 35):
            tmp = 'orange'
        elif (195 < c[0] < 205) & (15 < c[1] < 35) & (25 < c[2] < 45):
            tmp = 'red'
        elif (245 < c[0] < 255) & (245 < c[1] < 255) & (245 < c[2] < 255):
            tmp = "white"
        else:
            tmp = 'unkonwn'
        return tmp
    def cut_Image(self,x,y,m,n):
        x=int(x)
        y=int(y)
        w=int(x+m)
        l=int(y+n)
        im=ImageGrab.grab(bbox=(x, y, w,l))
        return im
    def return_Text(self,im,threshold=190):
        Lim = im.convert('L')
        table=[]
        #the for{} is used to binarizate the image
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        bim = Lim.point(table, "1")
        bim.show()
        text = pytesseract.image_to_string(bim)
        return text
    def excel_Pos(self,a,b,func=''):
        data=xlrd.open_workbook(r"C:\Python27\Lib\site-packages\auto_Test\config.xlsx")
        a=int(a)
        if 0<a<=5:
            b=int(b)
            sheet_pannel=data.sheet_by_index(0)
            tmp = sheet_pannel.col_values(0).index(func)
            width=sheet_pannel.cell(0,3).value
            height=sheet_pannel.cell(1,3).value
            pos=str(sheet_pannel.cell(tmp,1).value).split("-")
            tmp1=int(int(pos[0])+width*(a-1))
            tmp2=int(int(pos[1])+height*(b-1))
            #tmp1=str(tmp1)
            #tmp2=str(tmp2)
            pos_list=[str(tmp1),str(tmp2)]
            print pos_list
            return pos_list
        elif a<=0:
            sheet_button = data.sheet_by_index(1)
            tmp=sheet_button.col_values(0).index(b)
            pos_list=str(sheet_button.cell(tmp,1).value).split("-")
            print pos_list
            return pos_list
        else:
            pos_list=["Wrong Parameter"]
            return pos_list
            print "Wrong Parameter"
    def image_Rec(self,im1,im2):
        h1 = im1.histogram()
        h2 = im2.histogram()
        result = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
        return result

    #此段代码还没有写入总体设计需要注意
    def log_Read(self,log_Type,Plugin,time_start):
        if log_Type=="client":
            path=r"C:\Users\Administrator\AppData\Roaming\PUC\PUC_Client\Log\Client_Log"
        elif log_Type=="server":
            path=r"C:\ProgramData\PUC\PUC_Server\Log\Log"
        elif log_Type=="gataway":
            path=r"C:\ProgramData\PUC\PUC_Gateway\Log\Log"
        elif log_Type=="client_api":
            path=r"C:\Users\Administrator\AppData\Roaming\PUC\PUC_Client\Log\Client_API_Log"
        dirs=os.listdir(path)
        #com=Mytool.compare(1,2)

        def compare(x, y):
            stat_x = os.stat(path + "/" + x)
            stat_y = os.stat(path + "/" + y)
            if stat_x.st_ctime < stat_y.st_ctime:
                return -1
            elif stat_x.st_ctime > stat_y.st_ctime:
                return 1
            else:
                return 0
        dirs.sort(compare)
        log_Path=path+"/"+dirs[-1]
        plugin_Line=[]

        for line in open(log_Path):
            if Plugin in line:
                line = str(line)
                plugin_Line.append(line)
        print plugin_Line

        for i in range(len(plugin_Line)):
            tmpline=str(plugin_Line[i])[4:23]
            time_start=time.strptime(time_start, "%Y-%m-%d %H:%M:%S")
            print time_start
            timeArrary=time.strptime(tmpline,"%Y-%m-%d %H:%M:%S")
            if timeArrary>=time_start:
                fplugin_Log=plugin_Line[i:]
                return fplugin_Log
                break



class Mytool():
    def __int__(self):
        pass
    def Find_Item_on_Tree(self):
        bT=base_Test()
        tmpxy=bT.excel_Pos(0,"resource_tree_top")
        #print tmpxy
        tmpmn=bT.excel_Pos(0,"resource_tree_bottom")
        #print tmpmn
        tmpl=int(tmpmn[1])-int(tmpxy[1])
        tmpim=bT.cut_Image(tmpxy[0],tmpxy[1],270,tmpl)#180 should be change
        #tmpim.show()
        for i in range(1,tmpl):
            tmpc=bT.return_Color(tmpim,3,i)
            tmploc=260
            if tmpc=="grey":
                #tmploc=1
                tmploc=tmploc+i
                #tmploc=str(tmploc)
                print tmploc
                break
        return tmploc

    def cut_Panel_Number(self,x,y):
        bT=base_Test()
        tmp1xy=bT.excel_Pos(x,y,"cnumber")
        tmp2xy=bT.excel_Pos(x,y,"cnumber2")
        tmpim=bT.cut_Image(tmp1xy[0],tmp1xy[1],tmp2xy[0]-tmp1xy[0],tmp2xy[1]-tmp1xy[1])
        #tmpim.show()
        text=bT.return_Text(tmpim)
        print text
        return text
    def image_Comparsion_Panel(self,x,y,func):
        bT=base_Test()
        tmp1xy=bT.excel_Pos(x,y,"lstate")
        tmp2xy=bT.excel_Pos(x,y,"lstate1")
        tmpim = bT.cut_Image(tmp1xy[0], tmp1xy[1], tmp2xy[0] - tmp1xy[0], tmp2xy[1] - tmp1xy[1])
        tmpim1=Image.open(func+".png")
        result=bT.image_Rec(tmpim,tmpim1)
        print result
        return result
    def return_Postion(self,x,y,func):
        func=str(func)
        pos=base_Test().excel_Pos(x,y,func)
        return pos
    def dgna_Pos(self,a,func):
        data = xlrd.open_workbook(r"C:\Python27\Lib\site-packages\auto_Test\config.xlsx")
        sheet_dgna = data.sheet_by_index(1)
        a=int(a)
        if a<=0:
            tmp = sheet_dgna.col_values(0).index(func)
            poslist = str(sheet_dgna.cell(tmp, 1).value).split("-")
            print poslist
            return poslist
        else:
            tmp = sheet_dgna.col_values(0).index(func)
            pos=str(sheet_dgna.cell(tmp, 1).value).split("-")
            tmp2 = int(int(pos[1]) + 31* (a - 1))
            poslist = [str(pos[0]), str(tmp2)]
            print poslist
            return poslist


    def return_Dgna_Input(self):
        bT = base_Test()
        Top_left_concer = bT.excel_Pos(0, "dgna_input_left")
        Lower_right_corner = bT.excel_Pos(0, "dgna_input_right")
        a = int(Top_left_concer[0])
        b = int(Top_left_concer[1])
        c = int(Lower_right_corner[0])
        d = int(Lower_right_corner[1])
        print a,b,c,d
        im = bT.cut_Image(0, 0, 1920, 1080)
        for i in range(b, d):
            for x in range(a, c):
                print x,i
                color = bT.return_Color(im, x, i)
                if color == "white":
                    c_list = [x, i]
                    print c_list
                    return c_list
                    break
                #else:
                 #   print "The element can not founded"

    def search_Pos(self, a, func):
        data = xlrd.open_workbook(r"d:\Python27\Lib\site-packages\auto_Test\config.xlsx")
        sheet_pos = data.sheet_by_index(1)
        tmp = sheet_pos.col_values(0).index(func)
        poslist = str(sheet_pos.cell(tmp, 1).value).split("-")
        a = int(a)
        if a <= 1:
            print
            poslist
            return poslist
        else:
            if "dgna" in func:
                tmp2 = int(int(poslist[1]) + 30 * (a - 1))
            elif "cross" in func:
                tmp2 = int(int(poslist[1]) + 28 * (a - 1))
            pos = [str(poslist[0]), str(tmp2)]
            print pos
            return pos




        #for i in range(len(Pl))
                #print(line)
                #print plugin_Line
        #print log_File
#\d\d\d\d\-\d\d\-\d\d\\s+\d\d:\d\d:\d\d\\s+\d\d\d
a=Mytool().log_Read("client","[PUCClient][debug]","2018-06-29 15:29:21")
test.push






#im=Image.open("55.jpg")
#text=base_Test().return_Text(im,85)
#print text
#time.sleep(3)
#tmpim=base_Test().cut_Image(0,250,220,605)
#a=base_Test().return_Color(tmpim,3,9)
#print a
#Mytool().cut_Panel_Number(1,1)
#a=Mytool().return_Postion(1,1,"cnumber")
#print a
#time.sleep(2)
#a=Mytool().return_Dgna()





