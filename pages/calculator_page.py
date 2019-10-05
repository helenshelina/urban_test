#!/usr/bin/python3
# vim: set encoding=utf-8

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select


class CalculatorPage:
    URL = 'https://storage.googleapis.com/urban-qa-testing/parkcalcTestHarness.html'

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get(self.URL)

    def select_lot(self, lot: str):
        lots = Select(self.browser.find_element_by_id('Lot'))
        lots.select_by_visible_text(lot)

    def _fill_in(self, element: WebElement, text: str):
        element.clear()
        element.send_keys(text)

    def fill_start_date(self, date: str):
        start_date = self.browser.find_element_by_id('EntryDate')
        self._fill_in(start_date, date)

    def fill_start_time(self, time: str):
        start_time = self.browser.find_element_by_id('EntryTime')
        self._fill_in(start_time, time)

    def fill_end_date(self, date: str):
        end_date = self.browser.find_element_by_id('ExitDate')
        self._fill_in(end_date, date)

    def fill_end_time(self, time: str):
        end_time = self.browser.find_element_by_id('ExitTime')
        self._fill_in(end_time, time)

    def choose_delay_time(self, time: int):
        response_delay = self.browser.find_element_by_css_selector(f"form.BodyCopy > input[value='{time}']")
        response_delay.click()

    def calculate(self):
        calculate_button = self.browser.find_element_by_id('calculate')
        calculate_button.click()

    def final_cost(self) -> str:
        return self.browser.find_element_by_id('cost').text
