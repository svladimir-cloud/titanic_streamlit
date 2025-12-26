import pytest
import pandas as pd
from fare_byPclass_analyzer import (
    calculate_total_fare_by_class,
    check_required_columns
)


# --- Проверка корректного расчета для 'male' ---
def test_calculate_total_fare_male():
    df = pd.DataFrame({
        'Sex': ['male', 'male', 'female', 'male', 'female'],
        'Pclass': [1, 2, 1, 1, 3],
        'Fare': [100.0, 50.0, 200.0, 150.0, 75.0]
    })

    expected_result = pd.DataFrame({
        'Класс обслуживания': [1, 2],
        'Суммарная стоимость билетов': [250.0, 50.0]
    })

    result = calculate_total_fare_by_class(df, 'male')
    pd.testing.assert_frame_equal(
        result.sort_values('Класс обслуживания')
        .reset_index(drop=True),
        expected_result.sort_values('Класс обслуживания')
        .reset_index(drop=True))


# --- Проверка корректного расчета для 'female' ---
def test_calculate_total_fare_female():
    df = pd.DataFrame({
        'Sex': ['male', 'male', 'female', 'male', 'female', 'female'],
        'Pclass': [1, 2, 1, 1, 3, 3],
        'Fare': [100.0, 50.0, 200.0, 150.0, 75.0, 25.0]
    })

    expected_result = pd.DataFrame({
        'Класс обслуживания': [1, 3],
        'Суммарная стоимость билетов': [200.0, 100.0]
    })

    result = calculate_total_fare_by_class(df, 'female')
    pd.testing.assert_frame_equal(
        result.sort_values('Класс обслуживания')
        .reset_index(drop=True),
        expected_result
        .sort_values('Класс обслуживания').reset_index(drop=True))


# --- Проверка на отсутствие данных для выбранного пола ---
def test_calculate_total_fare_no_data():
    df = pd.DataFrame({
        'Sex': ['male', 'male', 'male'],
        'Pclass': [1, 2, 3],
        'Fare': [100.0, 50.0, 75.0]
    })

    # Ожидаем пустой DataFrame
    columns = ['Класс обслуживания', 'Суммарная стоимость билетов']
    expected_result = pd.DataFrame(columns=columns)
    column_types = {
        'Класс обслуживания': 'int64',
        'Суммарная стоимость билетов': 'float64'
        }
    expected_result = expected_result.astype(column_types)

    result = calculate_total_fare_by_class(df, 'female')
    pd.testing.assert_frame_equal(result, expected_result)


# --- Проверка на отсутствие необходимых колонок ---
def test_check_required_columns():
    df = pd.DataFrame({
        'Sex': ['male', 'female'],
        'Pclass': [1, 2]
        # 'Fare' отсутствует
    })

    # Проверяем, что функция выбрасывает ValueError
    with pytest.raises(ValueError, match="df должен содержать колонки:"):
        check_required_columns(df)
