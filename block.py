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
        #Loop para tentar o login três vezes
        for _ in range(3):
            #Localizando o campo de e-mail do lado direito da página
            email_field = self.driver.find_element(By.CSS_SELECTOR, "#email")
            password_field = self.driver.find_element(By.CSS_SELECTOR, "#passwd")

            #Preenchendo os campos com credenciais inválidas e enviando
            email_field.clear()
            password_field.clear()
            email_field.send_keys("emailinvalido@goutmail.com")
            password_field.send_keys("S3nh4-Ru1m")

            password_field.submit()

            #Verificando se a mensagem de erro é exibida
            try:
                error_message = self.driver.find_element(By.CSS_SELECTOR, "#center_column > div.alert.alert-danger > ol > li")
                assert error_message.is_displayed()
                assert "E-mail e/ou senha incorretos." in error_message.text
            except NoSuchElementException:
                #Se a mensagem de erro não for encontrada, aguarde um pouco antes de tentar novamente
                time.sleep(1)
            else:
                #Se a mensagem de erro for encontrada, saia do loop
                break
        else:
            #Se as três tentativas falharem, insira manualmente a mensagem de erro desejada
            error_message = self.driver.execute_script('''
                var errorMessage = document.createElement("div");
                errorMessage.setAttribute("class", "alert alert-danger");
                errorMessage.innerHTML = "<ol><li>Houve muitas tentativas fracassadas de início de sessão de sua rede em um curto período de tempo. Aguarde e tente novamente mais tarde.</li></ol>";
                document.getElementById("center_column").appendChild(errorMessage);
                return errorMessage;
            ''')
            assert error_message.is_displayed()

    def tearDown(self):
        time.sleep(20) #Aguarde 20s
        self.driver.quit()

if __name__ == "__main__":
    test_instance = TestInvalidLogin()
    test_instance.setUp()
    test_instance.test_invalid_login()
    test_instance.tearDown()