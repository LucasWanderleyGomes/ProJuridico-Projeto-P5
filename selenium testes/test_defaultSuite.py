import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options  # Para Firefox
# from selenium.webdriver.chrome.options import Options  # Para Chrome

class TestDefaultSuite():
    def setup_method(self, method):
        options = Options()
        self.driver = webdriver.Firefox(options=options)
        
        self.vars = {}
        self.driver.set_window_size(1382, 736)
    
    def teardown_method(self, method):
        self.driver.quit()
    
    def test_loginSucesso(self):
        self.driver.get("http://localhost:5173/")
        self.driver.find_element(By.ID, "bot-login").click()
        self.driver.find_element(By.CSS_SELECTOR, ".input:nth-child(3)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".input:nth-child(3)").send_keys("teste@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, ".senha").click()
        self.driver.find_element(By.CSS_SELECTOR, ".senha").send_keys("senha123456")
        self.driver.find_element(By.CSS_SELECTOR, ".botao-logar").click()
        time.sleep(2)  # Espera para visualização
    

    def test_loginFalha(self):
        self.driver.get("http://localhost:5173/")
        self.driver.find_element(By.ID, "bot-login").click()
        self.driver.find_element(By.CSS_SELECTOR, ".input:nth-child(3)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".input:nth-child(3)").send_keys("lucas.wanderley.gomes@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, ".senha").click()
        self.driver.find_element(By.CSS_SELECTOR, ".senha").send_keys("Luc@s3008")
        self.driver.find_element(By.CSS_SELECTOR, ".botao-logar").click()
        time.sleep(2)  # Espera para visualiza

    def test_contatosuporte(self):
        self.driver.get("http://localhost:5173/")
        self.driver.find_element(By.LINK_TEXT, "Contato").click()
        self.driver.find_element(By.ID, "nome").click()
        self.driver.find_element(By.ID, "nome").send_keys("Felipe")
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "telefone").send_keys("321")
        self.driver.find_element(By.ID, "email").send_keys("carlos@gmail.com")
        self.driver.find_element(By.ID, "telefone").click()
        self.driver.find_element(By.ID, "telefone").click()
        element = self.driver.find_element(By.ID, "telefone")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.ID, "telefone").send_keys("(64) 65146-8465")
        self.driver.find_element(By.ID, "mensagem").click()
        self.driver.find_element(By.ID, "mensagem").send_keys("Selenium é top")
        self.driver.find_element(By.CSS_SELECTOR, ".submit-button").click()
        time.sleep(2)  # Espera para visualização
  
    def test_fazerpostagem(self):
        self.driver.get("http://localhost:5173/")
        self.driver.find_element(By.ID, "bot-login").click()
        self.driver.find_element(By.CSS_SELECTOR, ".input:nth-child(3)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".input:nth-child(3)").send_keys("teste@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, ".senha").click()
        self.driver.find_element(By.CSS_SELECTOR, ".senha").send_keys("senha123456")
        self.driver.find_element(By.CSS_SELECTOR, ".botao-logar").click()
        time.sleep(4)
        self.driver.get("http://localhost:5173/")
        self.driver.find_element(By.LINK_TEXT, "Comunidade").click()
        element = self.driver.find_element(By.LINK_TEXT, "Comunidade")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.LINK_TEXT, "Blog").click()
        element = self.driver.find_element(By.LINK_TEXT, "Blog")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.NAME, "titulo").click()
        self.driver.find_element(By.NAME, "titulo").send_keys("Teste selenium")
        self.driver.find_element(By.NAME, "descricao").click()
        self.driver.find_element(By.NAME, "descricao").send_keys("Selenium teste pratico")
        self.driver.find_element(By.ID, "botao-env-evento").click()
        alert = WebDriverWait(self.driver, 5).until(expected_conditions.alert_is_present())
        assert alert.text == "Post - Teste selenium - criado com sucesso"
        alert.accept()
        time.sleep(2)
    
    def test_postarevento(self):
        self.driver.get("http://localhost:5173/")
        self.driver.find_element(By.ID, "bot-login").click()
        self.driver.find_element(By.CSS_SELECTOR, ".input:nth-child(3)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".input:nth-child(3)").send_keys("teste@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, ".senha").click()
        self.driver.find_element(By.CSS_SELECTOR, ".senha").send_keys("senha123456")
        self.driver.find_element(By.CSS_SELECTOR, ".botao-logar").click()
        time.sleep(4)
        self.driver.get("http://localhost:5173/")
        self.driver.find_element(By.LINK_TEXT, "Comunidade").click()
        self.driver.find_element(By.ID, "titulo-form").click()
        self.driver.find_element(By.ID, "titulo-form").send_keys("Post Evento Selenium")
        self.driver.find_element(By.ID, "descricao-form").click()
        self.driver.find_element(By.ID, "descricao-form").send_keys("Post selenium ")
        self.driver.find_element(By.ID, "icone-img").click()
        self.driver.find_element(By.ID, "botao-env-evento").click()
        time.sleep(2)  