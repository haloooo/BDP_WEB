# * coding:utf-8 *
# Author    : Administrator
# Createtime: 7/12/2018
import time, sys, os

from BDP.common import check_result

sys.path.insert(0, os.getcwd())
from BDP.service.IR_sender.sender import send
from BDP.config import constants

def send_key(command, level=1,times=1):
    for i in range(0, times):
        send(command)
        sleep_level(level)

def init_focus_location():
    """
    初始化测试环境
    1.确保初始化焦点位于Disc栏
    """
    send_key("HOME")
    send_key('RIGHT', 1, 5)
    send_key('UP', 1, 5)
    send_key('LEFT', 1, 2)

def go_setup(type=True):
    """
    Home --> SetUp
    """
    send_key('UP', 1, 2)
    if type:
        send_key('RIGHT', 1, 5)
    else:
        send_key('RIGHT', 1, 2)
    send_key("ENTER")
    time.sleep(5)

def go_all_resetting():
    """
    SetUp --> Resetting --> Reset to Factory Default Settings --> All Settings
    """
    send_key("UP")
    send_key('ENTER', 1, 2)
    send_key("UP")
    send_key("ENTER")
    send_key("LEFT")
    send_key("ENTER", 2)
    #检查resetting操作是否完成
    # CheckResult.check_Resetting()
    #关闭reset成功画面
    send_key("ENTER")

def go_power_off():
    """
    Power Off
    """
    send_key("POWER", 2)

def go_power_on():
    """
    Power On
    """
    send_key("POWER", 3)

def go_finish_easySetup_step():
    """
    Finish Easy Setup Step
    """
    send_key("RIGHT", 1, 2)
    send_key("DOWN")
    send_key("ENTER")

def change_HDR_output():
    """
    Home --> Setup --> Screen Settings --> HDR Output
    """
    send_key("DOWN")
    send_key("ENTER")
    send_key("DOWN")
    send_key("ENTER")
    send_key("DOWN")
    send_key("ENTER")

def go_HDR_output():
    """
    Home --> Setup --> Screen Settings --> HDR Output
    """
    send_key("DOWN")
    send_key("ENTER")
    send_key("DOWN")

def go_home():
    """
    Home UI
    """
    send_key("HOME")

def go_system_setting():
    """
    Home UI --> Setup --> System Settings
    """
    send_key("UP", 1, 4)
    send_key("ENTER")
    time.sleep(4)

def change_OSD_language():
    """
    Home UI --> Setup --> System Settings --> OSD Language
    """
    send_key("ENTER")
    send_key("DOWN")
    send_key("ENTER")

def go_OSD_language():
    """
    Home UI --> Setup --> System Settings --> OSD Language
    """
    send_key("ENTER")

def go_device_name():
    """
    Home UI --> Setup --> System Settings --> Device Name
    """
    send_key('UP', 1, 3)
    send_key('ENTER')
    time.sleep(4)

def enter_device_name():
    """
    输入Device Name
    default : fff
    """
    send_key("GREEN", 1, 10)
    send_key("ENTER", 1, 6)

def save_device_name():
    """
    保存Device Name
    """
    send_key("YELLOW")

def go_network_setting():
    """
    Home UI --> Setup --> Network Setting
    """
    send_key("UP", 1, 3)
    send_key("ENTER")
    time.sleep(3)

def go_internet_settings():
    """
    Home UI --> Setup --> Internet Settings
    """
    send_key("ENTER")

def set_wired_setup():
    """设置有线网络"""
    send_key("UP")
    send_key("ENTER")
    send_key("RIGHT", 1, 2)
    send_key("ENTER", 2, 2)
    send_key("HOME")        #保存后返回主页

def go_right_wireless():
    """移动到正确的无线网络"""
    from BDP.common.check_result import check_pictures
    for i in range(0,19):
        if check_pictures('Wireless.png', False, 0.7, type='JP'):
            send_key("ENTER")
            time.sleep(3)
            break
        else:
            send_key("DOWN")


def set_wireless_setup():
    """设置无线网络"""
    send_key("DOWN")
    send_key("ENTER", 3)

def set_different_mode(mode):
    """设置不同mode"""
    if(mode == 'Child Lock'):
        send_key("STOP", 0)
        send_key("HOME", 0)
        send_key("TOP_MENU")
    if(mode == 'Demo Mode'):
        send_key("STOP", 0)
        send_key("RETURN", 0)
        send_key("PAUSE", 0)
        send_key("SUBTITLE")
    if(mode == 'Services Mode'):
        send_key("STOP", 0)
        send_key("DISPLAY", 0)
        send_key("PAUSE", 0)
        send_key("UP", 1)

def go_usb_device():
    """进入USB device界面"""
    send_key('UP', 1, 2)
    send_key('LEFT', 1, 5)
    send_key("RIGHT")
    send_key("ENTER", 2)

def play_source(type):
    """播放资源文件"""
    if(type == 'video'):
        send_key("RIGHT")
        send_key("UP")
        send_key("ENTER", 2)
        # send_key("OPTIONS")
    if(type == 'music'):
        send_key("UP")
        send_key("ENTER", 2)
        # send_key("OPTIONS")
    if(type == 'photo'):
        send_key("UP")
        send_key("RIGHT")
        send_key("ENTER", 2)
        # send_key("OPTIONS")

def change_catetory():
    """修改catetory"""
    sleep_level(2)
    send_key('LEFT')
    send_key('DOWN')
    send_key('ENTER')

def register_as_favorite():
    """设置为Favorite"""
    send_key("OPTIONS")

def go_diff_icon(type):
    """进入不同类型界面"""
    sleep_level(1)
    if(type == 'disc'):
        send_key('ENTER', 2)
    if(type == 'media server'):
        send_key('LEFT', 1, 2)
        send_key('ENTER')
    if(type == 'screen mirroring'):
        send_key('RIGHT', 1, 3)
        send_key('ENTER')
        time.sleep(5)
    if(type == 'bivl app'):
        send_key("DOWN")
        send_key('ENTER', 2)
    if(type == 'USB'):
        send_key('RIGHT')

def config_wireless_setup():
    """配置无线"""
    sleep_level(1)
    send_key('ENTER')
    send_key('RED')
    send_key('LEFT', 1, 3)
    send_key('ENTER', 1, 8)
    send_key('RIGHT', 1, 9)
    send_key('DOWN', 1, 2)
    send_key('ENTER', 3)
    send_key('ENTER')
    # 配置完成后进入HOME界面
    send_key('HOME')

def restart_power():
    """重启电源"""
    send_key('RESTART', 2, 2)
    send_key('POWER')

def go_digital_concert_hall():
    """
    进入Digital Concert Hall界面
    进行多次点击以确保进入界面
    """
    send_key('UP')
    send_key('LEFT', 1, 5)
    send_key('DOWN', 1, 2)
    send_key('RIGHT', 1, 2)
    send_key('ENTER', 3)

def quit_play_back(type):
    """退出播放"""
    if type == 'video':
        send_key('STOP')
    if type == 'music':
        send_key('RETURN')
    if type == 'photo':
        send_key('OPTIONS')
        send_key('RETURN', 1, 2)

def finish_initial_settings():
    """确保退出easy display settings界面"""
    from BDP.common.check_result import check_pictures
    flag = check_pictures('EasyDisplaySettings.png')
    if flag:
        send_key('RIGHT', 1, 2)
        send_key('DOWN')
        send_key('ENTER')

def pressKey():
    send_key('ENTER', 2)
    send_key('FAVORITE', 2)

def sleep_level(level):
    """设置不同休眠等级"""
    lv0 = constants.configs['time']['lv0']
    lv1 = constants.configs['time']['lv1']
    lv2 = constants.configs['time']['lv2']
    lv3 = constants.configs['time']['lv3']
    lv4 = constants.configs['time']['lv4']
    if level == 0:
        time.sleep(lv0)
    if level == 1:
        time.sleep(lv1)
    if level == 2:
        time.sleep(lv2)
    if level == 3:
        time.sleep(lv3)
    if level == 4:
        time.sleep(lv4)

def check_USB(type):
    """检查是否正确的插入优盘"""
    send_key("HOME")
    go_diff_icon('USB')
    if not check_result.check_pictures('USB_device.png', type=type):
        return False
    else:
        return True

if __name__ == '__main__':
    go_right_wireless()