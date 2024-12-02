# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 18:00:36 2022

@author: lizhuang
"""
from ftplib import FTP
from ftplib import error_perm

class FTP_OP():
    def __init__(self,host, username, password, port):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        
    def ftp_connect(self):
        self.ftp = FTP()
        self.ftp.encoding = 'UTF-8' # 适应中文编码
        try:
            self.ftp.set_debuglevel(2) # 调试级别
            self.ftp.connect(self.host, self.port)
            self.ftp.login(self.username, self.password)
            self.ftp.set_pasv(False) # 设置被动模式
        except error_perm:
            print('[ERROR]: user authentication failed.')
            return -1
        except Exception as e:
            print('[ERROR]: ftp connect failed. %s'%e)
            return -1
        print('***ftp success connected.***')
    
    def download_file(self, ftp_file, local_file):
        # 从ftp服务器上下载文件到本地
        # ftp_file: 远端要下载的文件
        # local_file: 保存到本地文件
        bufsize = 1024
        with open(local_file, 'wb') as f:
            self.ftp.retrbinary("RETR %s"%ftp_file, f.write, bufsize)
            
    def upload_file(self, ftp_file, local_file):
        # 上传本地文件至ftp服务器
        # ftp_file:保存至ftp的文件名
        # local_file：本地文件
        bufsize = 1024
        with open(local_file, 'rb') as f:
            self.ftp.storbinary("STOR %s"%ftp_file, f, bufsize)
            
    def ftp_quit(self):
        # 退出ftp
        self.ftp.quit()
        
if __name__ == '__main__':
    ftp1 =FTP_OP("8.130.16.246", 'lizhuang', 'lizhuang2511', 21)
    ftp1.ftp_connect()
    
    ftp_filename = '/程序更新/主界面.tar'
    local_filename = '../主界面.tar'
    
    # 下载文件至本地
    ftp1.download_file(ftp_filename, local_filename)
    # 上传本机文件至ftp服务器
    #ftp.upload_file('/abc_upload.jpg', local_filenaem)
    
    ftp1.ftp_quit()
 