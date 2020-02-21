from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.porters.vip/features/webdriver.html')
# 编写修改navigator.webdriver值的JavaScript代码
script = 'Object.defineProperty(navigator,"webdriver",{get:() => false,});'
# 运行JavaScript代码
driver.execute_script(script)

# 定位按钮并点击
driver.find_element_by_css_selector('.btn.btn-primary.btn-lg').click()
# 定位到文章内容元素
elements = driver.find_element_by_css_selector('#content')
time.sleep(1)
print(elements.text)
driver.close()









