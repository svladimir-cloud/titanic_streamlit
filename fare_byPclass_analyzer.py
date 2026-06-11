import pandas as pd


def read_csv(df_str):
    return pd.read_csv(df_str)


def check_required_columns(df):
    required_columns = ['Sex', 'Pclass', 'Fare']
    if not all(col in df.columns for col in required_columns):
        raise ValueError(f"df должен содержать колонки: {required_columns}")


def calculate_total_fare_by_class(df: pd.DataFrame, selected_sex: str):
    # Проверяем, что необходимые колонки существуют
    check_required_columns(df)

    # Фильтрация по полу
    filtered_df = df[df['Sex'] == selected_sex]

    # Группировка по классу и суммирование стоимости билетов
    fare_summary = filtered_df.groupby('Pclass')['Fare'].sum().reset_index()
    columns = ['Класс обслуживания', 'Суммарная стоимость билетов']
    fare_summary.columns = columns

    return fare_summary

def calculate_survival_rate(df: pd.DataFrame, selected_sex: str):
    """Рассчитывает процент выживших по классу обслуживания."""
    check_required_columns(df)
    
    required = ['Sex', 'Pclass', 'Survived']
    if not all(col in df.columns for col in required):
        raise ValueError(f"df должен содержать колонки: {required}")
    
    filtered_df = df[df['Sex'] == selected_sex]
    
    survival_summary = (
        filtered_df
        .groupby('Pclass')['Survived']
        .agg(['count', 'sum'])
        .reset_index()
    )
    survival_summary['survival_rate'] = (
        survival_summary['sum'] / survival_summary['count'] * 100
    ).round(2)
    
    survival_summary.columns = [
        'Класс обслуживания',
        'Всего пассажиров',
        'Выжило',
        'Процент выживших'
    ]
    return survival_summary.drop(columns=['Всего пассажиров', 'Выжило'])