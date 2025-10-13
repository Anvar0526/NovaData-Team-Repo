# Файл для правок, которые должны изменять исходный текст.

# scripts/generate_data.py
import pandas as pd
from datetime import datetime, timedelta
import random

# Генерируем простые данные
ids   = [i for i in range(15)]
dates = [datetime.now() - timedelta(days=x) for x in range(15)]
sales = [random.randint(100, 1000) for _ in range(15)]

data = {
    'id': ids,
    'date': dates,
    'sales': sales,
    'product': ['A', 'B'] * 255
}

df = pd.DataFrame(data)
df.to_csv('data/sales_data.csv', index=False)
print("Сгенерированы тестовые данные!")
print("Сгенерированы новые тестовые данные!")
