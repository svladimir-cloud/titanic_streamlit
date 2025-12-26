
import fare_byPclass_analyzer as analyzer
from titanic_streamlit import start_app

if __name__ == "__main__":
    df = analyzer.read_csv('titanic_train.csv')
    start_app(df=df, analize_func=analyzer.calculate_total_fare_by_class)
