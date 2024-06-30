import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 1 При всплывающих уведомления (В данном случае запрос для предоставление гео-локации)
# мы выключаем уведомления через настройки браузера
# 2
# 3 Инициализируем настройки браузера в переменную option = webdriver.ChromeOptions()
# 4 Далее добавляем настройку отключить уведомления в переменную option  option.add_argument('--disable-notifications')
# 5 и передаём Настройки при инициализации браузера  driver = webdriver.Chrome(service=service_obj, options=option)
# 6

service_obj = Service('C:\\WebDrivers\\Chrome 125.0.6422.78\\chromedriver.exe')
option = webdriver.ChromeOptions()
option.add_argument('--disable-notifications')

driver = webdriver.Chrome(service=service_obj, options=option)
driver.maximize_window()

driver.get('https://whatmylocation.com/')

time.sleep(15)
driver.quit()
