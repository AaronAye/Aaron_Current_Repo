from pages.base_page import Page
from selenium.webdriver.common.by import By
class MainPage(Page):
    def open_main(self):
        self.driver.get('https://target.com/')

    def click_search_bar(self):
        self.driver.find_element(By.ID,'search').send_keys('SkinnyPop')
        self.driver.find_element(By.XPATH, value="//button[@data-test='@web/Search/SearchButton']").click()

