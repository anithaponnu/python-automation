from selenium.webdriver.chrome.service import Service

service = Service(log_path="chromedriver.log")
driver = webdriver.Chrome(service=service, options=options)