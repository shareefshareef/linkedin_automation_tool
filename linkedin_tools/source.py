from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import logging




class Alinkedin():
    def __init__(self, email="#enteremail or password", password="#type password"):
        self.credentials = {
            'email': email,
            'password': password,
            'url': 'https://www.linkedin.com/login'
        }
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        

    def login(self):
        try:
            logging.info(f"Logging into account: {self.credentials['email']}")
            self.browser.get(self.credentials['url'])
            username = self.browser.find_element(By.ID, "username")
            username.clear()
            username.send_keys(self.credentials['email'])
            sleep(1)
            password = self.browser.find_element(By.ID, "password")
            password.clear()
            password.send_keys(self.credentials['password'])
            sleep(1)
            submit_button = self.browser.find_element(By.CLASS_NAME, "btn__primary--large")
            submit_button.click()
            logging.info("Login successful.")
            sleep(5)
        except Exception as e:
            logging.error(f"Error during login: {e}")

    def update_summary(self, summary_text, summary_link, login=True):
        try:
            if login:
                self.login()
            logging.info("Updating profile summary...")
            self.browser.get(summary_link)
            text_box = self.browser.find_element(By.TAG_NAME, "textarea")
            text_box.clear()
            text_box.send_keys(summary_text)
            sleep(1)
            save_button = self.browser.find_element(By.XPATH, "//span[text() = 'Save']")
            save_button.click()
            sleep(2)
            logging.info("Profile summary updated.")
        except Exception as e:
            logging.error(f"Error updating profile summary: {e}")

    def post_tweet(self, url, post="hello .", login=True):
        try:
            if login:
                self.login()
            sleep(3)
            pformat = post.split("\n")
            logging.info("Started posting tweet.")
            logging.info(f"Post content: {pformat[0]}")
            self.browser.get(url)
            sleep(2)
            click_on_text_area = self.browser.find_element(By.CSS_SELECTOR, "div.ql-editor.ql-blank")
            sleep(2)
            click_on_text_area.send_keys(post)
            sleep(2)
            click_on_post = self.browser.find_element(By.XPATH, "//span[text() = 'Post']").click()
            sleep(2)
            logging.info("Tweet posted.")
        except Exception as e:
            logging.error(f"Error posting tweet: {e}")

    def post_poll(self, url, poll, login=True):
        try:
            if login:
                self.login()
            a, b, c, d = poll['options']
            logging.info("Started posting poll.")
            self.browser.get(url)
            sleep(3)
            plusym = self.browser.find_element(By.XPATH, "//button[@aria-label='More']")
            sleep(2)
            plusym.click()
            sleep(3)
            create_poll_button = self.browser.find_element(By.XPATH, "//button[@aria-label='Create a poll']")
            sleep(1)
            create_poll_button.click()
            sleep(5)
            poll_question_textarea = self.browser.find_element(By.XPATH, "//textarea[@placeholder='E.g., How do you commute to work?']")
            sleep(1)
            poll_question_textarea.send_keys(poll['question'])
            sleep(2)
            
            poll_option_input = self.browser.find_element(By.ID, "poll-option-1")
            sleep(1)
            poll_option_input.send_keys(a)
            sleep(2)

            poll_option_input = self.browser.find_element(By.ID, "poll-option-2")
            sleep(1)
            poll_option_input.send_keys(b)
            sleep(2)

            add_option_button = self.browser.find_element(By.XPATH, "//button[span[text()='Add option']]")
            sleep(1)
            add_option_button.click()
            sleep(2)

            poll_option_input = self.browser.find_element(By.ID, "poll-option-3")
            sleep(1)
            poll_option_input.send_keys(c)
            sleep(2)

            add_option_button = self.browser.find_element(By.XPATH, "//button[span[text()='Add option']]")
            sleep(1)
            add_option_button.click()
            sleep(2)

            poll_option_input = self.browser.find_element(By.ID, "poll-option-4")
            sleep(1)
            poll_option_input.send_keys(d)
            sleep(2)

            done_button = self.browser.find_element(By.XPATH, "//button[@aria-label='Done']")
            sleep(1)
            done_button.click()

            sleep(3)
            element = self.browser.find_element(By.XPATH, "//button[contains(@class, 'share-actions__primary-action') and contains(@class, 'artdeco-button--primary')]")
            sleep(1)
            element.click()
            sleep(5)
            logging.info("Poll posted.")
        except Exception as e:
            logging.error(f"Error posting poll: {e}")
            
    def quit_driver(self):
        logging.info("Quitting the browser.")
        self.browser.quit()
    

        




