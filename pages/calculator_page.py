#!/usr/bin/python3
# vim: set encoding=utf-8

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

from support.form_data import FormData


class CalculatorPage:
    URL = "https://storage.googleapis.com/urban-qa-testing/parkcalcTestHarness.html"

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get(self.URL)

    def select_lot(self, lot: str):
        lots = Select(self.browser.find_element_by_id("Lot"))
        lots.select_by_visible_text(lot)

    @staticmethod
    def _fill_in(element: WebElement, text: str):
        element.clear()
        element.send_keys(text)

    def fill_start_date(self, date: str):
        start_date = self.browser.find_element_by_id("EntryDate")
        self._fill_in(start_date, date)

    def fill_start_time(self, time: str):
        start_time = self.browser.find_element_by_id("EntryTime")
        self._fill_in(start_time, time)

    def fill_end_date(self, date: str):
        end_date = self.browser.find_element_by_id("ExitDate")
        self._fill_in(end_date, date)

    def fill_end_time(self, time: str):
        end_time = self.browser.find_element_by_id("ExitTime")
        self._fill_in(end_time, time)

    def delay_time_radio_button(self, time: int) -> WebElement:
        return self.browser.find_element_by_css_selector(
            f"form.BodyCopy > input[value='{time}']"
        )

    def calculate_button(self) -> WebElement:
        return self.browser.find_element_by_id("calculate")

    def final_cost(self) -> str:
        return self.browser.find_element_by_id("cost").text

    def fill_calculator(self, form_data: FormData) -> str:
        self.select_lot(form_data.lot)
        self.fill_start_date(form_data.start_d)
        self.fill_start_time(form_data.start_t)
        self.fill_end_date(form_data.finish_d)
        self.fill_end_time(form_data.finish_t)
        self.delay_time_radio_button(form_data.delay).click()
