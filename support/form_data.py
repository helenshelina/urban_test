#!/usr/bin/python3
# vim: set encoding=utf-8


class FormData:
    def __init__(self, lot: str, start_d: str, start_t: str, finish_d: str, finish_t: str, delay: int):
        self.__lot = lot
        self.__start_d = start_d
        self.__start_t = start_t
        self.__finish_d = finish_d
        self.__finish_t = finish_t
        self.__delay = delay

    @property
    def lot(self) -> str:
        return self.__lot

    @property
    def start_d(self) -> str:
        return self.__start_d

    @property
    def start_t(self) -> str:
        return self.__start_t

    @property
    def finish_d(self) -> str:
        return self.__finish_d

    @property
    def finish_t(self) -> str:
        return self.__finish_t

    @property
    def delay(self) -> int:
        return self.__delay

