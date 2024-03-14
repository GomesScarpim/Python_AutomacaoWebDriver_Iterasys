# 1 - Bibliotecas
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# 2 - Classe (Opcional)
class Teste_Produtos():

    # 2.1 Atributos
    url = "https://www.saucedemo.com"              # endereço do site alvo

    # 2.2 Funções e Métodos
    def setup_method(self, method):                # método de inicialização dos testes
        self.driver = webdriver.Chrome()           # instancia o objeto do Selenium WebDriver como Chrome
        self.driver.implicitly_wait(10)            # define o tempo de espera padrão por elementos em 10 segundos

    def teardown_method(self, method):             # método de finalização dos testes
        self.driver.quit()                         # encerra / destrói o objeto do Selenium WebDriver da memória

    def test_selecionar_produto(self):             # método de teste
        self.driver.get(self.url)                  # abre o navegador
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")             # escreve no campo user-name
        self.driver.find_element(By.NAME, "password").send_keys("secret_sauce")             # escreve a senha
        self.driver.find_element(By.CSS_SELECTOR, "input.submit-button.btn_action").click()   # clique no botão de login

        # transição de página

        assert self.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"  # confirma se está escrito Products no elemento
        assert self.driver.find_element(By.ID, "item_4_title_link").text == "Sauce Labs Backpack" # confirma se é a mochila
        # confirma o preço da mochila
        assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(1) .inventory_item_price").text == (
            "$29.99" 
        )

