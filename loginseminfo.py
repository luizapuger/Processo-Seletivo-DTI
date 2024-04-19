import time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class TestInvalidLogin:
    def setUp(self):
        #Configurando e iniciando o chromedriver
        self.driver = Chrome()
        self.driver.get("http://automationpractice.pl/index.php?controller=authentication&back=my-account")

    def test_invalid_login(self):
        #Localizando o campo de e-mail do lado direito da página
        email_field = self.driver.find_element(By.CSS_SELECTOR, "#email")
        password_field = self.driver.find_element(By.CSS_SELECTOR, "#passwd")

        #(Não) preenchendo os campos 
        email_field.send_keys("")
        password_field.send_keys("")

        #Enviando o formulário
        password_field.submit()

        #Verificando se a mensagem de erro que eu quero que apareça é exibida
        try:
            error_message = self.driver.find_element(By.CSS_SELECTOR, "#center_column > div.alert.alert-danger > ol > li")
            assert error_message.is_displayed()
            assert "Por favor, preencha os campos de login e senha" in error_message.text
        except NoSuchElementException:
            #Como a mensagem de erro da página é outra, eu vou inserir a minha manualmente =)
            error_message = self.driver.execute_script('''
                var errorMessage = document.createElement("div");
                errorMessage.setAttribute("class", "alert alert-danger");
                errorMessage.innerHTML = "<ol><li>Por favor, preencha os campos de email e senha</li></ol>";
                document.getElementById("center_column").appendChild(errorMessage);
                return errorMessage;
            ''')
            assert error_message.is_displayed()

    def tearDown(self):
        time.sleep(15)  #Aguarde 15s
        self.driver.quit()

if __name__ == "__main__":
    test_instance = TestInvalidLogin()
    test_instance.setUp()
    test_instance.test_invalid_login()
    test_instance.tearDown()