#!/usr/bin/python3
# vim: set encoding=utf-8
import time

import pytest

from pages.calculator_page import CalculatorPage
from support.parking_cost import ParkingCost
from support.form_data import FormData


# TODO: extract duration and count time for assertion
@pytest.mark.parametrize(
    "form_data",
    [
        FormData('Valet Parking', '2019-10-06', '00:00', '2019-10-07', '5:00', 0),
    ],
)
def test_calculate_1_and_half_days_parking(browser, form_data: FormData):
    park_cost = ParkingCost()
    park_cost.calculate_duration(form_data)
    calc_page = CalculatorPage(browser)
    calc_page.open()
    calc_page.fill_calculator(form_data)
    calc_page.calculate_button().click()
    assert "30.00" in calc_page.final_cost()
    assert "1 Days, 5 Hours, 0 Minutes" in calc_page.final_cost()


@pytest.mark.skip
def test_simple_calculate_parking(browser):
    calc_page = CalculatorPage(browser)
    calc_page.open()
    calc_page.select_lot('Valet Parking')
    calc_page.fill_start_date('2019-10-06')
    calc_page.fill_end_date('2019-10-07')
    calc_page.delay_time_radio_button(0).click()
    calc_page.calculate_button().click()
    parking_cost = ParkingCost()

    assert parking_cost.valet_parking_cost() in calc_page.final_cost()
    assert "1 Days, 0 Hours, 0 Minutes" in calc_page.final_cost()


@pytest.mark.skip
def test_delay_calculate_parking(browser):
    calc_page = CalculatorPage(browser)
    calc_page.open()
    calc_page.select_lot('Valet Parking')
    calc_page.fill_start_date('2019-10-06')
    calc_page.fill_end_date('2019-10-07')
    delay_time = 5000
    calc_page.delay_time_radio_button(delay_time).click()
    calc_page.calculate_button().click()
    parking_cost = ParkingCost()

    assert "0" in calc_page.final_cost()
    assert "" in calc_page.final_cost()

    time.sleep(delay_time/1000)
    assert parking_cost.valet_parking_cost() in calc_page.final_cost()
    assert "1 Days, 0 Hours, 0 Minutes" in calc_page.final_cost()

