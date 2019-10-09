#!/usr/bin/python3
# vim: set encoding=utf-8
import time
from datetime import datetime
from datetime import timedelta

import pytest

from pages.calculator_page import CalculatorPage
from support.parking_cost import ParkingCost
from support.form_data import FormData


@pytest.mark.parametrize(
    "form_data",
    [
        FormData('Short-Term Parking', '2019-10-06', '00:00', '2019-10-07', '00:00', 0),
        FormData('Short-Term Parking', '2019-10-06', '00:00', '2019-10-07', '05:00', 100),
        FormData('Short-Term Parking', '2019-10-06', '00:00', '2019-10-07', '06:00', 5000),
    ],
)
def test_short_term_parking(browser, form_data: FormData):
    calc_page = CalculatorPage(browser)
    calc_page.open()
    calc_page.fill_calculator(form_data)
    calc_page.calculate_button().click()

    if form_data.delay > 0:
        assert "0" in calc_page.final_cost()
        time.sleep(form_data.delay/1000)

    parking_cost = ParkingCost()
    assert parking_cost.short_term_parking_cost(form_data) in calc_page.final_cost()
    # Todo: count duration and check for it
    # assert "1 Days, 0 Hours, 0 Minutes" in calc_page.final_cost()


@pytest.mark.parametrize(
    "form_data",
    [
        FormData('Valet Parking', '2019-10-06', '00:00', '2019-10-07', '00:00', 0),
        FormData('Valet Parking', '2019-10-06', '00:00', '2019-10-07', '05:00', 100),
        FormData('Valet Parking', '2019-10-06', '00:00', '2019-10-07', '06:00', 5000),
    ],
)
def test_valet_parking(browser, form_data: FormData):
    calc_page = CalculatorPage(browser)
    calc_page.open()
    calc_page.fill_calculator(form_data)
    calc_page.calculate_button().click()

    if form_data.delay > 0:
        assert "0" in calc_page.final_cost()
        time.sleep(form_data.delay/1000)

    parking_cost = ParkingCost()
    assert parking_cost.valet_parking_cost(form_data) in calc_page.final_cost()
    # Todo: count duration and check for it
    # assert "1 Days, 0 Hours, 0 Minutes" in calc_page.final_cost()
