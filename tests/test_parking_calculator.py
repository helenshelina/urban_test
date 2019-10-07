#!/usr/bin/python3
# vim: set encoding=utf-8

from pages.calculator_page import CalculatorPage
from support.parking_cost import ParkingCost


def test_simple_calculate_parking(browser):
    calc_page = CalculatorPage(browser)
    calc_page.open()
    calc_page.select_lot('Valet Parking')
    calc_page.fill_start_date('2019-10-06')
    calc_page.fill_end_date('2019-10-07')
    calc_page.choose_delay_time(0)
    calc_page.calculate()
    parking_cost = ParkingCost()

    assert parking_cost.valet_parking_cost() in calc_page.final_cost()
    assert "1 Days, 0 Hours, 0 Minutes" in calc_page.final_cost()


def test_calculate_1_and_half_days_parking(browser):
    calc_page = CalculatorPage(browser)
    calc_page.open()
    calc_page.select_lot('Valet Parking')
    calc_page.fill_start_date('2019-10-06')
    calc_page.fill_start_time('00:00')
    calc_page.fill_end_date('2019-10-07')
    calc_page.fill_end_time('5:00')
    calc_page.choose_delay_time(0)
    calc_page.calculate()
    assert "30.00" in calc_page.final_cost()
    assert "1 Days, 5 Hours, 0 Minutes" in calc_page.final_cost()
