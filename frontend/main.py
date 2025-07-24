#!/usr/bin/env python3
from nicegui import app, ui
from pages.realty import realty_page
from pages.parser import parser_page
from pages.parsers_numbers import parsers_numbers


@ui.page('/')
def main():
    realty_page()
    

@ui.page('/parser')
def parser():
    parser_page()

@ui.page('/parsers_numbers')
def page_parsers_numbers():
    parsers_numbers()

ui.run()
