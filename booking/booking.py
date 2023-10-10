
from selenium import webdriver
from selenium.webdriver.common.by import By

import os
import booking.constants as const
import booking.booking_filtration as bf


class Booking(webdriver.Chrome):
    def __init__(self, driver_path = const.DRIVER_PATH , teardown=False):
        self.driver_path = driver_path
        self.teardown=teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()

        self.implicitly_wait(15)
        self.maximize_window()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
    
    def land_first_page(self):
        self.get(const.BASE_URL)
        
    def change_currency(self, currency):
        currency_element=self.find_element(By.ID,'button[data-tooltip-text]="Choose your currency')
        currency_element.click()
        selected_currency_element = self.find_element(By.CSS_SELECTOR, f'a[data-modal-header-async-url-param*="selected_currency={currency}"]')

    def select_place_to_go(self,place_to_go):
        search_field=self.find_element(By.ID,'ss')
        search_field.clear()
        search_field.send_keys(place_to_go)

        first_result=self.find_element(By.CSS_SELECTOR,'li[data-i="0]')
        first_result.click()
    
    def select_data_to_go(self,check_in , check_out ):
        check_in=self.find_element(By.CSS_SELECTOR,f'td[data-date="{check_in}"]')
        check_in.click()

        check_out=self.find_element(By.CSS_SELECTOR,f'td[data-date="{check_in}"]')
        check_out.click()
    
    def select_adults(self,count):
        selection_element=self.find_element(By.ID , ' xp__guests__toggle')
        selection_element.click()

        while True:
            decrease_adult_element=self.find_element(By.CSS_SELECTOR , 'button[aria-label="Decrease number of Adults"]')
            decrease_adult_element.click()

            adults_value_element=self.find_element(By.ID , 'group_adults')
            adults_value=adults_value_element.get_attribute()

            if int(adults_value) == 1:
                break

        increase_button_element=self.find_element(By.CSS_SELECTOR , 'button[aria-label="Increase number of Adults"]')

        for i in range(count-1):
            increase_button_element.click()
    
    def click_search(self):
        search_button=self.find_element(By.CSS_SELECTOR , 'button[type="sumbit"]')
        search_button.click()

    def appply_filtration(self):
        filtration=bf.BookingFiltration(driver=self)
