import streamlit as st


def start_app(df, analize_func, analize_func_survival):
    st.title("Анализ стоимости билетов пассажиров Титаника")

    # Выбор пола пользователем
    selected_sex = st.selectbox(
        "Выберите пол пассажиров:",
        ('male', 'female')
    )

    fare_summary = analize_func(df, selected_sex)

    # Отображение результата в таблице
    st.subheader(f"Суммарная стоимость билетов для\
                 пассажиров пола '{selected_sex.capitalize()}' по классам:")
    st.dataframe(fare_summary)

    survival_summary = analize_func_survival(df, selected_sex)
    st.subheader(f"Процент выживших для '{selected_sex.capitalize()}' по классам:")
    st.dataframe(survival_summary)