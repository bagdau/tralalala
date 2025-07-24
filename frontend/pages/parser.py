# pages/parser.py
from nicegui import ui
import asyncio
from components.header import main_header
from components.card_container import card_container 

logs = [
    '[12:01:03] Подключение к источнику данных успешно.',
    '[12:01:05] Начат парсинг: Категория = Квартиры, Город = Шымкент.',
    '[12:01:10] Найдено 25 новых записей.',
    '[12:01:12] Запись #1 добавлена в базу данных.',
    '[12:01:13] Запись #2 добавлена в базу данных.'
]

def parser_page():
    def content():
        def inner_content():
            ui.label('Парсеры').style('font-size: 32px; font-weight: bold; margin-bottom: 16px;')

            with ui.row().style('gap: 32px; margin-bottom: 8px;'):
                with ui.column().style('flex: 1; gap: 18px; min-width: 200px;'):
                    ui.select(['Все', '10', '20', '50'], label='Выбор Количества').style('min-width: 170px')
                    ui.select(['Продажа', 'Аренда'], label='Тип объектов').style('min-width: 170px')
                with ui.column().style('flex: 1; gap: 18px; min-width: 200px;'):
                    ui.select(['Шымкент', 'Алматы', 'Астана'], label='Город').style('min-width: 170px')
                    ui.select(['Квартира', 'Дом', 'Офис'], label='Объекты').style('min-width: 170px')
                with ui.column().style('flex: 1; gap: 8px; min-width: 200px;'):
                    ui.select(['Актуальный', 'Архив'], label='Архив или Актуальный').style('min-width: 170px')
                    ui.label('Количество записей в источнике:').style('font-size: 15px; color: #888;')
                    ui.label('Количество записей в базе:').style('font-size: 15px; color: #888;')
                    ui.label('Количество страниц:').style('font-size: 15px; color: #888;')

            with ui.row().style('gap: 20px; justify-content: center; margin-bottom: 14px;'):
                ui.button('ПРОВЕРИТЬ СОЕДИНЕНИЕ', color='primary').style('min-width: 188px; font-size: 16px; font-weight: 500;')
                ui.button('ЗАПУСТИТЬ ПАРСЕР', color='green').style('min-width: 188px; font-size: 16px; font-weight: 500;')
                ui.button('ОСТАНОВИТЬ ПАРСЕР', color='red').style('min-width: 188px; font-size: 16px; font-weight: 500;')
                ui.button('ОЧИСТИТЬ ЛОГИ', color='pink').style('min-width: 188px; font-size: 16px; font-weight: 500;')

            ui.label('Логи парсера').style('font-weight: bold; font-size: 20px; margin-bottom: 12px; margin-top: 18px;')

            log_box = ui.markdown('```\n' + '\n'.join(logs) + '\n```') \
                .classes('bg-black text-white rounded-xl') \
                .style(
                    'font-size: 15px; width: 100%; max-width: 1200px; '
                    'font-family: "JetBrains Mono", monospace; white-space: pre-wrap; '
                    'max-height: 247px; overflow-y: auto; padding: 18px 26px;'
                )

            async def update_logs():
                for i in range(3):
                    await asyncio.sleep(3)
                    new_log = f'[12:01:{14 + i}] Новая запись #{i + 3} добавлена в базу данных.'
                    logs.append(new_log)
                    log_box.content = '```\n' + '\n'.join(logs) + '\n```'
                    log_box.update()
            asyncio.create_task(update_logs())

        card_container(inner_content)  # вот так вызываешь контейнер

    main_header(content)