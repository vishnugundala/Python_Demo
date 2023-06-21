from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# configure webdriver
options = Options()
options.headless = True  # hide GUI
options.add_argument("--window-size=1920,1080")  # set window size to native GUI size
options.add_argument("start-maximized")  # ensure window is full-screen

links = ["https://www.amazon.in/Apple-iPhone-14-512GB-Blue/dp/B0BDJH3V3Q/ref=sr_1_17?crid=T6EHI5O60LFH&keywords=iphone+14&qid=1684750621&sprefix=i%2Caps%2C271&sr=8-17",
         ,"https://www.amazon.in/Apple-iPhone-Plus-128GB-Starlight/dp/B0BDJFTGK6/ref=sr_1_18?crid=T6EHI5O60LFH&keywords=iphone%2B14&qid=1684750621&sprefix=i%2Caps%2C271&sr=8-18&th=1"]
driver = webdriver.Chrome(options=options)
prodcut_title_list = []
for i links:

driver.get("https://www.amazon.in/Apple-iPhone-14-128GB-Purple/dp/B0BDJ213TX/ref=sr_1_4?crid=T6EHI5O60LFH&keywords=iphone%2B14&qid=1684748930&sprefix=i%2Caps%2C271&sr=8-4&th=1")
product_xpath = '//*[@id="productTitle"]'
element = driver.find_element(By.XPATH, product_xpath)
print(element.text)
prodcut_title_list.append(element.text)

element = driver.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]')

print(element.text)

import pandas as pd
df = pd.DataFrame(prodcut_title_list,sellling,columns= ["prodcu_list",sellling,mrp,stoarge])
df.to_excel("sample_data.xlsx")