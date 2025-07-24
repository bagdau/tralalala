from nicegui import ui
from components.header import main_header
from components.card_container import card_container


class State:
    def __init__(self):
        self.archive = 'Нет'
        self.region = 'Все'
        self.owner_type = 'Все'
        self.estate_type = 'Продажа'
        self.object_type = 'Все'
        self.rooms = 'Любое'
        self.page = 1

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

        # Вторая строка фильтров
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

        # ---- ДАННЫЕ-ТАБЛИЦА ----
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
        # ---- ВРЕМЕННАЯ ЗАГЛУШКА С ДАННЫМИ ----
        all_rows = [

            {
                'id': i,
                'object': f'Квартира №{i}',
                'area': f'{40 + i*2} м²',
                'floor': str(i % 9 + 1),
                'price': f'{10_000_000 + i*222_000} ₸',
                'year': 2000 + (i % 20),
                'phone': f'8(707)000-0{i:03d}',
                'added': f'2024-07-{(i % 30) + 1:02d}',
                'details': 'Подробнее'
            }
            for i in range(1, 36)
        ]       
        PAGE_SIZE = 7
        total_pages = (len(all_rows) - 1) // PAGE_SIZE + 1

        def get_rows_for_page(page):
            start = (page - 1) * PAGE_SIZE
            end = start + PAGE_SIZE
            return all_rows[start:end]

        def update_table():
            table.rows = get_rows_for_page(state.page)
            page_label.text = f'Страница {state.page} из {total_pages}'

        table = ui.table(
            columns=columns,
            rows=get_rows_for_page(state.page),
            row_key='id'
        ).style('width: 100%; margin-top: 32px; font-size: 17px;')

        # --- ПАГИНАЦИЯ под таблицей ---
        with ui.row().style('justify-content: center; margin-top: 18px; margin-bottom: 12px;'):
            prev_btn = ui.button('', icon='chevron_left', color='primary', 
                                 on_click=lambda: go_page(-1)).props('flat').style('min-width: 42px')
            page_label = ui.label(f'Страница {state.page} из {total_pages}').style('font-size: 16px; padding: 0 14px; font-weight: 500; color: #333;')
            next_btn = ui.button('', icon='chevron_right', color='primary', 
                                 on_click=lambda: go_page(1)).props('flat').style('min-width: 42px')

        def go_page(delta):
            new_page = state.page + delta
            if 1 <= new_page <= total_pages:
                state.page = new_page
                update_table()

        update_table()  # начальная отрисовка

    # card-контейнер
    def big_card(inner):
        with ui.element('div').style(
            'display: flex; align-items: center; justify-content: center; min-height: 100vh; width: 100vw; background: #f7f8fa;'
        ):
            with ui.element('div').style(
                'background: #fff; max-width: 1200px; width: 100%; '
                'padding: 48px 44px 40px 44px; '
                'font-size: 18px; '  
                'box-shadow: 0px 8px 32px 0px rgba(0,0,0,0.09); border-radius: 26px; '
                'display: flex; flex-direction: column; align-items: center; gap: 28px;'
            ):
                inner()

    main_header(lambda: big_card(content))

# --- для локального запуска ---
if __name__ == "__main__":
    realty_page()
    ui.run()