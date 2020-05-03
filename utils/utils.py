import os
import signal
import subprocess
from time import sleep

import allure
import pymysql
import requests
from appium.webdriver.webdriver import WebDriver


def attach(driver: WebDriver, name):
    '''
    截图并保存到allure报告上
    '''
    temp_name = "xx.png"
    name = "步骤--" + repr(name)  # 强制转换为字符串
    driver.get_screenshot_as_file(temp_name)
    allure.attach.file(temp_name, attachment_type=allure.attachment_type.PNG, name=name)
    os.remove(temp_name)


def cookies():
    '''
    维护一个cookies的方法， 增加， 更新
    根据具体项目维护方法
    :return:
    '''
    r = requests.request()
    pass


def recordvideo(func):
    '''
    实现运行录屏的方法
    '''
    project_root = os.path.abspath(os.path.dirname(__file__))
    video_path = os.path.join(project_root, "video")

    start_cmd = "adb shell screenrecord --bugreport /data/local/tmp/{name}.mp4".format(name=func.__name__)
    # pull_cmd = "adb pull /data/local/tmp/{name}.mp4 {video_path}".format(name=func.__name__,video_path=video_path)
    pull_cmd = "adb pull /data/local/tmp/{name}.mp4 ./".format(name=func.__name__)
    clear_cmd = "adb shell rm /data/local/tmp/{name}.mp4".format(name=func.__name__)

    def record(*args, **kwargs):
        # 启动录屏 adb shell screenrecord --bugreport --time-limit 20 /data/local/tmp/用例名.mp4
        # os.system("adb shell screenrecord --bugreport /data/local/tmp/{name}.mp4".format(name=repr(func)))
        P = subprocess.Popen(start_cmd, shell=True)
        # 运行用例
        func(*args, **kwargs)
        # 停止录制
        os.kill(P.pid, signal.CTRL_C_EVENT)
        # 拉取视频 adb pull /data/local/tmp/用例名.mp4  ./
        P = subprocess.Popen(pull_cmd, shell=True, encoding="utf-8")
        # print("清理录制")
        # P = subprocess.Popen(clear_cmd, shell=True)

    return record


class Mysql():
    '''
    mysql的连接
    ip = "127.0.0.1"
    username = "root"
    password = "mysql"
    db = "test_db"
    db = Mysql().connect(ip, username, password, db)
    db.execute("create table test_one (`id` int auto_increment not null primary key, `name` varchar(30) not null);")
    '''

    def connect(self, ip, username, password, db):
        self.cursor = pymysql.connect(ip, username, password, db).cursor()
        return self.cursor

    def preset_data(self):
        '''
        前置准备数据
        :return:
        '''
        pass

    def post_data(self):
        '''
        后置清理数据
        :return:
        '''
        pass


class Redis():
    '''
    redis相关的操作
    '''

    def connect(self):
        pass

    def disconnect(self):
        pass

    def read(self):
        pass

    def insert(self):
        pass

    def delete(self):
        pass

# if __name__ == '__main__':
#     ip = "127.0.0.1"
#     username = "root"
#     password = "mysql"
#     db = "test_db"
#     db = Mysql().connect(ip, username, password, db)
#     db.execute("create table test_one (`id` int auto_increment not null primary key, `name` varchar(30) not null);")
#     db.close()
