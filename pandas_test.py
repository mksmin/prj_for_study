import pandas as pd
import matplotlib.pyplot as plt


# Создаем пример DataFrame
data = {
    'Дата': pd.date_range(start='2023-01-01', periods=10, freq='D'),
    'Значение': [2, 5, 3, 8, 4, 9, 1, 6, 7, 10]
}
df = pd.DataFrame(data)
df.set_index('Дата', inplace=True)  # Устанавливаем дату в качестве индекса

# Строим график
df.plot(
    kind='line',        # Тип графика (линейный)
    title='Пример графика',
    ylabel='Значения',
    xlabel='Дата',
    grid=True,
    figsize=(10, 5)
)

plt.grid()
plt.show()  # Показываем график