from selenium import webdriver
from time import sleep

start=2079
end=10000
errcount = 0
def login(browser):
    browser.get("https://www.baifubao.com/user/0/login/0")
    browser.maximize_window()

    sleep(2)

    browser.find_element_by_id("TANGRAM__PSP_4__sms_btn_back").click()
    browser.find_element_by_name("userName").clear()
    browser.find_element_by_name("userName").send_keys('三淼服装')
    # browser.find_element_by_name("userName").send_keys('sep555@qq.com')
    sleep(2)
    browser.find_element_by_name("password").clear()
    browser.find_element_by_name("password").send_keys('!@sanmiao90')
    # browser.find_element_by_name("password").send_keys('Song19870919')
    sleep(5)
    browser.find_element_by_id("TANGRAM__PSP_4__submit").click()

browser = webdriver.Firefox()
login(browser)

for phonevarint in range(start,end):
    for errcount in range(0,5):
        phonevar = "186"+str(phonevarint).zfill(4)+"0056"
        print("正在测试:"+phonevar)
        sleep(15)
        browser.get("https://www.baifubao.com/wireless/0/transfer/0/wap/0/start/0?username="+phonevar)
        sleep(15)

        if(browser.page_source.find('系统正忙')>0):
            print("系统出错，目前号码: "+phonevar)
        else:
            break
        
    print("检查错误："+str(errcount)+"次")
    if errcount == 4:
        print("系统出错次数达到 %d 次，正在退出" % errcount)
        break

    if(browser.page_source.find('不支持给自己转账')>0):
        print("找到号码："+phonevar)
        break

    # if phonevarint % 20 == 0:
    #     print("达到次数，正在等待。。。")
    #     sleep(3600)
    if phonevarint == (start + 80):
        print("达到次数上限，退出。。。当前号码： " + phonevar)
        break

# browser.close()