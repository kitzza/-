# 导入浏览器自动化模块
from selenium import webdriver
import datetime
import time

# 秒杀时间
target_time = "2022-10-17 16:50:00.00000000"

# 打开浏览器驱动
driver = webdriver.Chrome()
# 获取网页
driver.get('https://login.taobao.com/member/login.jhtml')
# 定位二维码登录标签
driver.find_element_by_class_name('icon-qrcode').click()
time.sleep(10) # 等待扫码登录
# 获取购物车网页
driver.get('https://cart.taobao.com/cart.htm?spm=a1z02.1.1997525049.1.jFX4ra&from=mini&ad_id=&am_id=&cm_id=&pm_id=1501036000a02c5c3739')
time.sleep(3)

# 点击全选标签
while True:
    try:
        if driver.find_element_by_id('J_SelectAll1'):
            driver.find_element_by_id('J_SelectAll1').click()
            print('已勾选全选标签')
            break
    except:
        print('未勾选')

# 点击结算标签
while True:
    # 当前时间
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print(current_time)
    if current_time >=target_time:
        while True:
            try:
                if driver.find_element_by_link_text('结 算'):
                    driver.find_element_by_link_text('结 算').click()
                    print('已锁定商品，等待结算！')
                    break
            except:
                pass
        time.sleep(1)
        # 点击提交订单
        while True:
            try:
                if driver.find_element_by_link_text('提交订单'):
                    driver.find_element_by_link_text('提交订单').click()
                    print('抢购成功，请尽快付款！')
            except:
                break
        time.sleep(0.01)