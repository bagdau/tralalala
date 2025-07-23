from nicegui import ui
from components.layout import main_layout
from components.card_container import card_container

class State:
    def __init__(self):
        self.archive = 'Нет'
        self.region = 'Все'
        self.owner_type = 'Все'
        self.estate_type = 'Продажа'
        self.object_type = 'Все'
        self.rooms = 'Любое'

state = State()


def realty_page():
    def content():
        ui.label('Недвижимость').style(
            'font-size: 36px; font-weight: bold; margin-bottom: 32px; text-align: center;'
        )

        # Первая строка фильтров (по центру)
        with ui.row().classes('gap-4 items-end').style('justify-content: center; width: 100%;'):
            with ui.column().classes('gap-1'):
                ui.label('Поиск по (Архив):').style('font-size: 16px;')
                ui.radio(['Да', 'Нет'], value=state.archive).bind_value(state, 'archive').classes('inline')
            with ui.column().classes('gap-1'):
                ui.label('Район:').style('font-size: 16px;')
                ui.select(['Все', 'Центр', 'Спальный'], value=state.region).bind_value(state, 'region').style('min-width:130px')
            with ui.column().classes('gap-1'):
                ui.label('Адрес:').style('font-size: 16px;')
                ui.input().props('placeholder="Введите адрес"').style('min-width:180px')
            with ui.column().classes('gap-1'):
                ui.label('Тип владельца:').style('font-size: 16px;')
                ui.select(['Все', 'Физ. лицо', 'Компания'], value=state.owner_type).bind_value(state, 'owner_type').style('min-width:150px')
            with ui.column().classes('gap-1'):
                ui.label('Тип недвижимости:').style('font-size: 16px;')
                ui.select(['Продажа', 'Аренда'], value=state.estate_type).bind_value(state, 'estate_type').style('min-width:130px')
            with ui.column().classes('gap-1'):
                ui.label('Выбор объектов:').style('font-size: 16px;')
                ui.select(['Все', 'Квартира', 'Дом'], value=state.object_type).bind_value(state, 'object_type').style('min-width:130px')

        # Вторая строка фильтров (по центру)
        with ui.row().classes('gap-4 items-end').style('justify-content: center; width: 100%; margin-top: 10px;'):
            with ui.column().classes('gap-1'):
                ui.label('Цена:').style('font-size: 16px;')
                with ui.row().classes('gap-2'):
                    ui.input().props('placeholder="Минимальная" type="number"').style('width: 130px')
                    ui.input().props('placeholder="Максимальная" type="number"').style('width: 130px')
            with ui.column().classes('gap-1'):
                ui.label('Комнатность:').style('font-size: 16px;')
                with ui.row().classes('gap-2'):
                    ui.select(['Любое', '1', '2', '3', '4+'], value=state.rooms).bind_value(state, 'rooms').style('width: 110px')
                    ui.select(['Любое', '1', '2', '3', '4+']).style('width: 110px')
            with ui.column().classes('gap-1'):
                ui.label('Площадь:').style('font-size: 16px;')
                with ui.row().classes('gap-2'):
                    ui.input().props('placeholder="Минимальная" type="number"').style('width: 130px')
                    ui.input().props('placeholder="Максимальная" type="number"').style('width: 130px')
            with ui.column().classes('gap-1'):
                ui.label('Этажность:').style('font-size: 16px;')
                with ui.row().classes('gap-2'):
                    ui.input().props('placeholder="Минимальный" type="number"').style('width: 130px')
                    ui.input().props('placeholder="Максимальный" type="number"').style('width: 130px')

        # Кнопка по центру
        with ui.row().style('justify-content: center; width: 100%; margin-top: 16px;'):
            ui.button('ПРИМЕНИТЬ ФИЛЬТР', color='primary').style('min-width: 200px; font-size: 18px;')

        # Таблица
        columns = [
            {'name': 'id', 'label': 'id'},
            {'name': 'object', 'label': 'Объект'},
            {'name': 'area', 'label': 'Площадь'},
            {'name': 'floor', 'label': 'Этаж'},
            {'name': 'price', 'label': 'Цена'},
            {'name': 'year', 'label': 'Год'},
            {'name': 'phone', 'label': 'Телефон'},
            {'name': 'added', 'label': 'Дата добавления'},
            {'name': 'details', 'label': 'Подробнее'},
        ]
        rows = []  # подставь свои данные
        ui.table(columns=columns, rows=rows, row_key='id').style('width: 100%; margin-top: 32px; font-size: 17px;')

    # Специальный большой card-контейнер только для этой страницы:
    def big_card(inner):
        with ui.element('div').style(
            'display: flex; align-items: center; justify-content: center; min-height: 100vh; width: 100vw; background: #f7f8fa;'
        ):
            with ui.element('div').style(
                'background: #fff; max-width: 1200px; width: 100%; '
                'padding: 48px 44px 40px 44px; '
                'font-size: 18px; '  # применится ко всем вложенным элементам!
                'box-shadow: 0px 8px 32px 0px rgba(0,0,0,0.09); border-radius: 26px; '
                'display: flex; flex-direction: column; align-items: center; gap: 28px;'
            ):
                inner()

    main_layout(lambda: big_card(content))