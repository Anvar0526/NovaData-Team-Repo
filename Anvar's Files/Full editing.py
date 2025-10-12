# Файл для правок, которые должны изменять исходный текст.

# scripts/generate_data.py
import pandas as pd
from datetime import datetime, timedelta
import random

# Генерируем простые данные
dates = [datetime.now() - timedelta(days=x) for x in range(10)]
sales = [random.randint(100, 1000) for _ in range(10)]

data = {
    'date': dates,
    'sales': sales,
    'product': ['A', 'B'] * 5
}

df = pd.DataFrame(data)
df.to_csv('data/sales_data.csv', index=False)
print("Сгенерированы тестовые данные!")