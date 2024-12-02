import os.path
import re
import pyperclip3
#import pyautogui
import time
import tarfile
import py_compile
class 打包文件():
    def __init__(self):
        self.主文件夹=r'E:\mechanical-calculation-4\发布程序文件'
        return
    def 获取文件夹(self):
        filename=os.listdir(self.主文件夹)
        list=filename
        n = len(list)
        bek = []
        for i in range(n):
            if "." in list[i]:
                bek.append(i)
        list = [list[i] for i in range(n) if (i not in bek)]
        #list.remove('python')
        list.remove('bat文件')
        list.remove('数据文件');list.remove('打包输出程序')
        print(list)
        #print(filename)
        '''for filename in os.listdir(self.主文件夹):
            print(filename)'''
        return list
    def 打开文件夹返回文件列表(self,文件夹):
        文件夹路径=self.主文件夹+'/'+文件夹
        文件列表=os.listdir(文件夹路径)
        list=文件列表
        n = len(list)
        bek = []
        for i in range(n):
            if ".pyc" in list[i]:
                bek.append(i)
        list = [list[i] for i in range(n) if (i not in bek)]
        n = len(list)
        bek = []
        for i in range(n):
            if ".py" in list[i]:
                bek.append(i)
        list = [list[i] for i in range(n) if (i in bek)]
        #list.remove('主界面.py');list.remove('开始界面.py');list.remove('绘图对比界面.py');
        文件列表=list
        print(文件列表)
        return 文件列表
    def 读取代码(self,主文件路径,文件路径):
        文件路径 = self.主文件夹 + '\\' + 主文件路径+ '\\' +文件路径
        f = open(文件路径,encoding="utf-8")
        代码文件=f.read()
        f.close()
        return 代码文件
    def 读取txt文件到剪切板(self,文件路径):
        return
    '''def 浏览器处理(self,代码文件):
        pyperclip.copy(代码文件)
        pyautogui.PAUSE = 2
        pyautogui.click(210, 552, button='left')
        pyautogui.hotkey('ctrl', 'a')  # 复制信息
        pyautogui.hotkey('ctrl', 'v')  # 粘贴信息
        time.sleep(2)
        pyautogui.click(105,263, button='left')
        pyautogui.click(91, 307, button='left')
        time.sleep(2)
        pyautogui.click(1412,528, button='left')
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        代码文件=string = pyperclip.paste()
        return 代码文件'''
    def 写入py(self,代码文件,主文件路径,文件路径):
        文件路径 = self.主文件夹 + '\\' + 主文件路径 + '\\' + 文件路径
        f = open(文件路径,'w',encoding="utf-8")
        代码文件 = f.write(代码文件)
        f.close()
        return
    def 分别打包程序(self):
        return
    def 上传到ftp(self):
        return
    def 处理打包程序(self):
        文件夹列表1=self.获取文件夹()
        for i in range(len(文件夹列表1)):
            文件列表=self.打开文件夹返回文件列表(文件夹列表1[i])
            for j in range(len(文件列表)):
                #代码=self.读取代码(文件夹列表1[i],文件列表[j])
                #self.读取txt文件到剪切板(文件列表[j])
                #转换代码=self.浏览器处理(代码)
                #self.写入py(转换代码,文件夹列表1[i],文件列表[j])
                self.pyc处理(文件夹列表1[i],文件列表[j])
        return
    def 压缩为tar(self):
        return
    def pyc处理(self,主文件路径,文件名称):
        #启动文件=['主界面.py','开始界面.py','绘图对比界面.py']
        启动文件 = []
        文件路径 = self.主文件夹 + '\\' + 主文件路径 + '\\' + 文件名称
        文件名称提取=re.findall(r'(.+?)\.',文件名称)
        print(str(文件名称提取[0]))
        输出文件和路径=self.主文件夹 + '\\' + 主文件路径+'\\'+str(文件名称提取[0])+'.pyc'
        py_compile.compile(文件路径,输出文件和路径)
        if (文件名称 in 启动文件):
            print("存在")
        else:
            os.remove(文件路径)
        return

if __name__ == '__main__':
    测试=打包文件()
    '''文件夹列表=测试.获取文件夹()
    测试.打开文件夹返回文件列表(文件夹列表[0])
    代码=测试.读取代码(文件夹列表[0],'fn计算.py')
    #转换代码=测试.浏览器处理(代码)
    #测试.写入py(转换代码,文件夹列表[0],'fn界面程序.py')
    测试.pyc处理(文件夹列表[0],'fn计算.py')'''
    测试.处理打包程序()
