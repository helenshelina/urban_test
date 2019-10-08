#!/usr/bin/python3
# vim: set encoding=utf-8
from datetime import datetime

from support.form_data import FormData


class ParkingCost:
    @staticmethod
    def calculate_duration( form_data: FormData):
        start_time = datetime.strptime(form_data.start_d + " " + form_data.start_t, '%Y-%m-%d %H:%M')
        end_time = datetime.strptime(form_data.finish_d + " " + form_data.finish_t, '%Y-%m-%d %H:%M')
        duration = end_time - start_time
        return duration

    @staticmethod
    def short_term_parking_cost( duration) -> int:
        if duration == "1 day":
            return "18"
        elif duration == "1 day 5h":
            return "30"
        elif duration == "1 day 6h":
            return "36"
    # +12$ 1d 1h; 36$ - 1d 6h; 38$ - 1d 7h;

    @staticmethod
    def economy_parking_cost() -> int:
        return 7
    # +4$ 1d 1h; 21$ - 1d 6h

    @staticmethod
    def long_term_surface_parking_cost() -> int:
        return 16
    # +2$ 1d 1h; 28$ - 1d 6h

    @staticmethod
    def long_term_garrage_parking_cost() -> int:
        return 12
    # +2$ 1d 1h 24$ - 1d 6h

    @staticmethod
    def valet_parking_cost():
        return '18'
    # +12$ 1d 1h; 36$ - 1d 6h
