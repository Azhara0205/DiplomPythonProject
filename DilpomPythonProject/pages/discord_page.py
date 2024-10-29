from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class DiscordPage:
    def __init__(self, driver):
        self.driver = driver
        self.message_input_locator = (By.XPATH, "//*[@id='app-mount']/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[3]/main/form/div/div[1]/div[1]/div/div[3]")  # Локатор поля ввода сообщения

    def send_message(self, message):
        message_input = self.driver.find_element(*self.message_input_locator)
        message_input.send_keys(message + Keys.ENTER)

    def delete_message(self, message_id):
        pass

    def edit_message(self, message_id, new_content):
        pass

    def add_reaction(self, message_id, emoji):
        pass

    def remove_reaction(self, message_id, emoji):
        pass
