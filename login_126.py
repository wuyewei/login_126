'''
如何判断元素是否在iframe上？
    1.定位到元素后，切换到firepath界面
    2.看firebug工具左上角，如果显示Top Window说明没有iframe
    3.如果显示iframe#xxx这样的，说明在iframe上，#后面就是它的id
'''
from selenium import webdriver

web = webdriver.Chrome()
url = 'https://mail.126.com'
web.get(url)
# web.implicitly_wait(10)
# 定位账号登录
el_1 = web.find_element_by_id('switchAccountLogin')
# 点击并跳转到登录页面
el_1.click()
web.implicitly_wait(10)
# 定位iframe
iframe = web.find_element_by_tag_name('iframe')  # switch_to.default_content() 跳回最外层页面
# 进入iframe
web.switch_to.frame(iframe)                      # switch_to.parent_frame() 跳回上层页面
# 定位输入邮箱账号的输入框
el_2 = web.find_element_by_name('email')
el_2.clear()
el_2.send_keys('*******') # 输入邮箱账号
# web.implicitly_wait(10)
# 定位密码输入框
el_3 = web.find_element_by_name('password')
el_3.send_keys('*******') # 输入密码

# web.implicitly_wait(10)
# 定位登录按钮
el_4 = web.find_element_by_id('dologin')
el_4.click()

web.implicitly_wait(10)
# 判断登录是否成功
el_5 = web.find_element_by_id('spnUid')
if el_5.text == '*******': # 输入邮箱账号
    print('登陆成功')
else:
    print('登录失败')
# 获取有几封未读邮件
el_6 = web.find_element_by_xpath('// *[ @ id = "_mail_component_128_128"]')
print(el_6.get_attribute('title'))
# 定位收件箱按钮
el_7 = web.find_element_by_xpath('//*[@id="_mail_component_32_32"]/span[2]')
el_7.click()
# web.implicitly_wait(10)
# 打印所有的邮件信息
el = web.find_elements_by_xpath('/html/body/div[2]/div[1]/div[2]/div/div[1]/div/div[4]/div')
for i in el:
    print(i.get_attribute('aria-label'))