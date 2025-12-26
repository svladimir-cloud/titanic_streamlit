import pandas as pd

def read_csv(df_str):
    return pd.read_csv(df_str)

def check_required_columns(df):
    required_columns = ['Sex', 'Pclass', 'Fare']
    if not all(col in df.columns for col in required_columns):
        raise ValueError(f"DataFrame должен содержать колонки: {required_columns}")

def calculate_total_fare_by_class(df: pd.DataFrame, selected_sex: str) -> pd.DataFrame:
    """
    Фильтрует DataFrame по полу и возвращает суммарную стоимость билетов по классам.

    Args:
        df (pd.DataFrame): Исходный DataFrame с данными о пассажирах.
        selected_sex (str): Выбранный пол ('male' или 'female').

    Returns:
        pd.DataFrame: Таблица с колонками 'Класс обслуживания' и 'Суммарная стоимость билетов'.
    """
    # Проверяем, что необходимые колонки существуют
    check_required_columns(df)

    # Фильтрация по полу
    filtered_df = df[df['Sex'] == selected_sex]

    # Группировка по классу и суммирование стоимости билетов
    fare_summary = filtered_df.groupby('Pclass')['Fare'].sum().reset_index()
    fare_summary.columns = ['Класс обслуживания', 'Суммарная стоимость билетов']

    return fare_summary