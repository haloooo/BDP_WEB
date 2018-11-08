# * coding:utf-8 *
# Author    : Administrator
# Createtime: 7/12/2018
import os
import configparser

configs = {
    'reportLocation':{
        'dirname' : r"D:\test\evidence\log\TestScript"    #日志输出路径
    },
    'time':{                                                   #睡眠时间等级(秒)
        'lv0':1,
        'lv1':2,
        'lv2':15,
        'lv3':30,
        'lv4':60
    },
    'PicturePath':{
        'root':'',                                             #总体对比图路径
        'part':''                                              #局部对比图路径
    },
}
conf = configparser.ConfigParser()
dirname = os.path.dirname(os.getcwd())
dirname_ = os.path.join(os.getcwd(),"BDP")
config_file_path = os.path.join(dirname_, "config\\Autotest_config.ini")
print(config_file_path)
conf.read(config_file_path)
camera_id = conf.get("TestSetting", "camera_id")
output_resolution = conf.get('TestSetting', 'output_resolution')
temp_dir = conf.get('TestSetting', 'temp_dir')
log_dir = conf.get('TestSetting', 'log_dir')

# camera_id = 0
# output_resolution = '1080p'
# temp_dir = r'd:\temp'
# log_dir = r'D:\test\evidence\log\TestScript'


# tar_path = r'D:\Pictures'
tar_path = os.path.join(dirname_, "pictures")
ratio = 0.9
flag = True





if __name__ == '__main__':
    print (tar_path)
