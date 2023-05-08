#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import json
import os
import click


def get_train(staff, dist, time, typ, file_name):
    """
    Запросить данные о поезде.
    """
    staff.append({
        "dist": dist,
        "time": time,
        "typ": typ,
    })
    with open(file_name, "w", encoding="utf-8") as fout:
        json.dump(staff, fout, ensure_ascii=False, indent=4)
    return staff


def display_trains(staff):
    """
    Отобразить список поездов.
    """
    # Проверить, что список поездов не пуст.
    if staff:
        # Заголовок таблицы.
        line = "+-{}-+-{}-+-{}-+-{}-+".format(
            "-" * 4,
            "-" * 30,
            "-" * 20,
            "-" * 15
        )
        print(line)
        print(
            "| {:^4} | {:^30} | {:^20} | {:^15} |".format(
                "No",
                "Пункт назначения",
                "время поезда",
                "Тип поезда"
            )
        )
        print(line)

        # Вывести данные о всех самолетах.
        for idx, train in enumerate(staff, 1):
            if isinstance(train, dict):
                print(
                    "| {:>4} | {:<30} | {:<20} | {:>15} |".format(
                        idx,
                        train.get('dist', ''),
                        train.get('time', 0),
                        train.get('typ', ''),
                    )
                )
            else:
                print("Error: Invalid train format.")

        print(line)

    else:
        print("Список поездов пуст")


def select_trains(staff, typ):
    """
    Выбрать поезда с заданным типом.
    """
    found = False
    for train in staff:
        if train.get('typ') == typ:
            found = True
            print(
                ' | {:<5} | {:<5} '.format(
                    train.get('dist', ''),
                    train.get('time', ''),
                )
            )

    if not found:
        print("Такого типа нет!")


def load_trains(file_name):
    with open(file_name, "r", encoding="utf-8") as fin:
        return json.load(fin)


@click.command()
@click.option("-c", "--command")
@click.argument('file_name')
@click.option("-n", "--name")
@click.option("-t", "--time")
@click.option("-p", "--typ")
def main(command, name, time, typ, file_name):
    """
    Главная функция программы.
    """
    if os.path.exists(file_name):
        staff = load_trains(file_name)
    else:
        staff = []
    if command == "add":
        get_train(staff, name, time, typ, file_name)
        click.secho('Данные добавлены')
    elif command == 'display':
        display_trains(staff)
    elif command == 'select':
        select_trains(staff, typ)


if __name__ == '__main__':
    main()
