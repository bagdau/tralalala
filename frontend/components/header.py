from nicegui import ui

ui.add_head_html('<link rel="stylesheet" href="static/main.css">')

def main_header(content_func):
    with ui.header().style(
        'background: #332a26;'
        'height: 100px;'
        'opacity: 1;'
        'display: flex;'
        'justify-content: center;'  
    ):

        with ui.element('div').style(
            'max-width: 1200px;'     
            'width: 100%;'          
            'padding-left: 20px;'
            'padding-right: 20px;'
            'display: flex;'
            'align-items: center;'
            'gap: 29px;'
            'box-sizing: border-box;'
        ):
            ui.image('static/img/logo.png').style(
                'width: 132px; height: 100px; object-fit: contain; margin-right: 16px;'
            )
            
            with ui.row().style('gap: 29px;'):
                ui.button('Недвижимости', on_click=lambda: ui.navigate.to('/'), color='success')  # синий
                ui.button('Парсер', on_click=lambda: ui.navigate.to('/parser'), color='success')  # серый
                ui.button('Парсер номеров', on_click=lambda: ui.navigate.to('/parsers_numbers'), color='success')  # зеленый
                ui.button('Выйти', on_click=lambda: print('Logout'), color='success')  # красный


    with ui.column().style(
        'background: #fff; border-radius: 12px; margin-top: 12px;'
        'padding-left: 32px; padding-right: 32px; padding-top: 16px; padding-bottom: 16px;'
    ):
        content_func()
