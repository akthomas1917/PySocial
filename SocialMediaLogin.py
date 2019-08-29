from selenium import webdriver

driver = webdriver.Chrome("/Users/aktho/Downloads/chromedriver")

###Instagram###
# username = 'akthomas19'
# password = 'instagram!!'
#
# url = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
#
# driver.get(url)
#
# driver.find_element_by_name('username').send_keys(username)
# driver.find_element_by_name('password').send_keys(password)
# driver.find_element_by_class_name('L3NKy').click()

###Twitter###
# username = 'akthomas19'
# password = 'twitter!'
#
# url = 'https://www.twitter.com/'
#
# driver.get(url)
#
# driver.find_element_by_name('session[username_or_email]').send_keys(username)
# driver.find_element_by_name('session[password]').send_keys(password)
# driver.find_element_by_class_name('EdgeButton--secondary').click()

###Facebook###
username = 'akthomas19@gmail.com'
password = 'woodlakefacebook17!'

url = 'https://www.facebook.com/'

driver.get(url)

driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_id('u_0_2').click()





