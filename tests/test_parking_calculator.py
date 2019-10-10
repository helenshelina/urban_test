#!/usr/bin/python3
# vim: set encoding=utf-8

import time

import pytest

from pages.calculator_page import CalculatorPage
from support.form_data import FormData
from support.parking_cost import ParkingCost


@pytest.mark.parametrize(
    "form_data, expected_cost_method, expected_duration",
    [
        (
            FormData(
                "Short-Term Parking", "2019-10-06", "00:00", "2019-10-07", "00:00", 0
            ),
            ParkingCost().short_term_parking_cost,
            "1 Days, 0 Hours, 0 Minutes",
        ),
        (
            FormData(
                "Short-Term Parking", "2019-10-06", "00:00", "2019-10-07", "05:00", 100
            ),
            ParkingCost().short_term_parking_cost,
            "1 Days, 5 Hours, 0 Minutes",
        ),
        (
            FormData(
                "Short-Term Parking", "2019-10-06", "00:00", "2019-10-07", "06:00", 5000
            ),
            ParkingCost().short_term_parking_cost,
            "1 Days, 6 Hours, 0 Minutes",
        ),
        (
            FormData("Valet Parking", "2019-10-06", "00:00", "2019-10-07", "00:00", 0),
            ParkingCost().valet_parking_cost,
            "1 Days, 0 Hours, 0 Minutes",
        ),
        (
            FormData(
                "Valet Parking", "2019-10-06", "00:00", "2019-10-07", "05:00", 100
            ),
            ParkingCost().valet_parking_cost,
            "1 Days, 5 Hours, 0 Minutes",
        ),
        (
            FormData(
                "Valet Parking", "2019-10-06", "00:00", "2019-10-07", "06:00", 5000
            ),
            ParkingCost().valet_parking_cost,
            "1 Days, 6 Hours, 0 Minutes",
        ),
        (
            FormData(
                "Economy Parking", "2019-10-06", "00:00", "2019-10-07", "00:00", 0
            ),
            ParkingCost().economy_parking_cost,
            "1 Days, 0 Hours, 0 Minutes",
        ),
        (
            FormData(
                "Economy Parking", "2019-10-06", "00:00", "2019-10-07", "05:00", 100
            ),
            ParkingCost().economy_parking_cost,
            "1 Days, 5 Hours, 0 Minutes",
        ),
        (
            FormData(
                "Economy Parking", "2019-10-06", "00:00", "2019-10-07", "06:00", 5000
            ),
            ParkingCost().economy_parking_cost,
            "1 Days, 6 Hours, 0 Minutes",
        ),
        (
            FormData(
                "Long-Term Surface Parking",
                "2019-10-06",
                "00:00",
                "2019-10-07",
                "00:00",
                0,
            ),
            ParkingCost().long_term_surface_parking_cost,
            "1 Days, 0 Hours, 0 Minutes",
        ),
        (
            FormData(
                "Long-Term Surface Parking",
                "2019-10-06",
                "00:00",
                "2019-10-07",
                "05:00",
                100,
            ),
            ParkingCost().long_term_surface_parking_cost,
            "1 Days, 5 Hours, 0 Minutes",
        ),
        (
            FormData(
                "Long-Term Surface Parking",
                "2019-10-06",
                "00:00",
                "2019-10-07",
                "06:00",
                5000,
            ),
            ParkingCost().long_term_surface_parking_cost,
            "1 Days, 6 Hours, 0 Minutes",
        ),
        (
            FormData(
                "Long-Term Garage Parking",
                "2019-10-06",
                "00:00",
                "2019-10-07",
                "00:00",
                0,
            ),
            ParkingCost().long_term_garage_parking_cost,
            "1 Days, 0 Hours, 0 Minutes",
        ),
        (
            FormData(
                "Long-Term Garage Parking",
                "2019-10-06",
                "00:00",
                "2019-10-07",
                "05:00",
                100,
            ),
            ParkingCost().long_term_garage_parking_cost,
            "1 Days, 5 Hours, 0 Minutes",
        ),
        (
            FormData(
                "Long-Term Garage Parking",
                "2019-10-06",
                "00:00",
                "2019-10-07",
                "06:00",
                5000,
            ),
            ParkingCost().long_term_garage_parking_cost,
            "1 Days, 6 Hours, 0 Minutes",
        ),
    ],
)
def test_calculate_parking_positive_flow(
    browser, form_data: FormData, expected_cost_method, expected_duration
):
    calc_page = CalculatorPage(browser)
    calc_page.open()
    calc_page.fill_calculator(form_data)
    calc_page.calculate_button().click()

    if form_data.delay > 0:
        assert "0" in calc_page.final_cost()
        time.sleep(form_data.delay / 1000)

    assert expected_cost_method(form_data) in calc_page.final_cost()

    assert expected_duration in calc_page.final_cost()


@pytest.mark.parametrize(
    "form_data, expected_cost, expected_duration",
    [
        (
            FormData("Valet Parking", "2019-10-32", "09:00", "2019-13-06", "30:00", 0),
            "1206.00",
            "66 Days, 21 Hours, 0 Minutes",
        ),
        (
            FormData("Valet Parking", "2019-10-32", "dd:00", "2019-13-06", "30:00", 0),
            "NaN ",
            "NaN Days, NaN Hours, NaN Minutes",
        ),
        (
            FormData("Valet Parking", "20----20-32", "09:00", "2019-13-06", "30:00", 0),
            "646596.00",
            "35921 Days, 21 Hours, 2.066666666666667 Minutes",
        ),
    ],
)
def test_calculate_parking_negative_flow(
    browser, form_data: FormData, expected_cost, expected_duration
):
    calc_page = CalculatorPage(browser)
    calc_page.open()
    calc_page.fill_calculator(form_data)
    calc_page.calculate_button().click()

    assert expected_cost in calc_page.final_cost()
    assert expected_duration in calc_page.final_cost()
