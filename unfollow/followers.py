from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox()
driver.get("https://instagram.com")
userinfo = "YOUR_USERNAME"
passinfo = "YOUR_PASSWORD"
takipciler = []
takipettigim = []
time.sleep(5)
login_user = driver.find_element_by_name("username")
login_pass = driver.find_element_by_name("password")
login_button = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")

login_user.send_keys(userinfo)
login_pass.send_keys(passinfo)
login_button.click()
time.sleep(5)
home = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[1]/a/div/div/img")
home.click()
time.sleep(5)
notnow = driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
notnow.click()
time.sleep(5)
profile = driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div/div[2]/div[1]/div/div/a")
profile.click()
time.sleep(5)

followerlist = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
followerlist.click()

time.sleep(5)


jscommand = """ 
followers2 = document.querySelector(".isgrP");
followers2.scrollTo(0, followers2.scrollHeight);
var lenOfPage = followers2.scrollHeight;
return lenOfPage;
"""

lenOfPage = driver.execute_script(jscommand)
match = False
while(match == False):
    lastCount = lenOfPage
    time.sleep(2)
    lenOfPage = driver.execute_script(jscommand)
    if lastCount == lenOfPage:
        match = True
time.sleep(5)
followers = driver.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")

for takipci in followers:
    takipciler.append(takipci.text)
with open("followers.txt","w",encoding = "UTF-8") as file:
    for follower in takipciler:
        file.write(follower + "\n")


