from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Inicializa o chromedriver
driver = webdriver.Chrome()

#Acessa a página de login
driver.get('http://automationpractice.pl/index.php?controller=authentication&back=my-account')

#Clica no link "Esqueceu sua senha?"
link_esqueci_senha = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Forgot your password?")))
link_esqueci_senha.click()

#Imprime uma mensagem no terminal
print("Você clicou em 'Forgot your password?' e foi redirecionado para outra página.")

#Fechando
driver.quit()
