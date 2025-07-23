# components/card_container.py

from nicegui import ui

def card_container(content_func):
    with ui.element('div').style(
        'display: flex; align-items: center; justify-content: center; min-height: 100vh; width: 100vw; background: #f7f8fa;'
    ):
        with ui.element('div').style(
            'background: #fff; max-width: 950px; width: 100%; '
            'padding: 38px 32px 28px 32px; '
            'box-shadow: 0px 8px 32px 0px rgba(0,0,0,0.09); border-radius: 20px; '
            'display: flex; flex-direction: column; align-items: stretch; gap: 20px;'
        ):
            content_func()
