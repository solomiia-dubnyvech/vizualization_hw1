import pandas as pd


def load_data():
    data = pd.read_csv('data_lab1.csv').loc[:, ['Year', 'J-D']]
    data.loc[:, 'J-D'] += 0.2
    return data


def get_marked_years_bold():
    return [2016]


def get_marked_years_right_align():
    return [1904, 1998]


def get_marked_years_left_align():
    return [1944, 2014, 2015, 2017]


def get_marked_years():
    return dict(bold=get_marked_years_bold(),
                right_align=get_marked_years_right_align(),
                left_align=get_marked_years_left_align())
