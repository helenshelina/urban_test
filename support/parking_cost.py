#!/usr/bin/python3
# vim: set encoding=utf-8
from datetime import datetime
from datetime import timedelta

from support.form_data import FormData


class ParkingCost:
    @staticmethod
    def calculate_duration(form_data: FormData):
        start_time = datetime.strptime(form_data.start_d + " " + form_data.start_t, '%Y-%m-%d %H:%M')
        end_time = datetime.strptime(form_data.finish_d + " " + form_data.finish_t, '%Y-%m-%d %H:%M')
        duration = end_time - start_time
        return duration

    def short_term_parking_cost(self, form_data: FormData):
        duration = self.calculate_duration(form_data)
        if duration == timedelta(days=1, hours=0):
            return "24"
        elif duration == timedelta(days=1, hours=5):
            return "34"
        elif duration == timedelta(days=1, hours=6):
            return "36"

    def economy_parking_cost(self, form_data: FormData):
        duration = self.calculate_duration(form_data)
        if duration == timedelta(days=1, hours=0):
            return "9"
        elif duration == timedelta(days=1, hours=5):
            return "19"
        elif duration == timedelta(days=1, hours=6):
            return "21"

    def long_term_surface_parking_cost(self, form_data: FormData):
        duration = self.calculate_duration(form_data)
        if duration == timedelta(days=1, hours=0):
            return "16"
        elif duration == timedelta(days=1, hours=5):
            return "26"
        elif duration == timedelta(days=1, hours=6):
            return "28"

    def long_term_garage_parking_cost(self, form_data: FormData):
        duration = self.calculate_duration(form_data)
        if duration == timedelta(days=1, hours=0):
            return "12"
        elif duration == timedelta(days=1, hours=5):
            return "22"
        elif duration == timedelta(days=1, hours=6):
            return "24"

    def valet_parking_cost(self, form_data: FormData):
        duration = self.calculate_duration(form_data)
        if duration == timedelta(days=1, hours=0):
            return "18"
        elif duration == timedelta(days=1, hours=5):
            return "30"
        elif duration == timedelta(days=1, hours=6):
            return "36"
