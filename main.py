import pandas as pd

df = pd.read_csv('student_marks.csv', sep=';')
df.fillna({'Student': 'Name lacking', 'Discipline': 'Discipline lacking', 'Mark': 0}, inplace=True)
print(df.head(3))
df['Mark'] = pd.to_numeric(df['Mark'], errors='coerce')  # Приводим столбец 'Mark' к числовому типу данных
print(df.dtypes)  # Проверка типов данных

# Средняя оценка по каждому предмету
mean_marks = df.groupby('Discipline')['Mark'].mean()
print("Средняя оценка по каждому предмету:")
print(mean_marks)
print("\n----------------------------------------------------------------\n")

# Медианная оценка по каждому предмету
median_marks = df.groupby('Discipline')['Mark'].median()
print("Медианная оценка по каждому предмету:")
print(median_marks)
print("\n----------------------------------------------------------------\n")

# Q1 и Q3 для оценок по математике
Q1_math = df[df['Discipline'] == 'Math']['Mark'].quantile(0.25)
Q3_math = df[df['Discipline'] == 'Math']['Mark'].quantile(0.75)
print("Q1 для оценок по математике:", Q1_math)
print("Q3 для оценок по математике:", Q3_math)
print("\n----------------------------------------------------------------\n")

# IQR
IQR_math = Q3_math - Q1_math
print("IQR для оценок по математике:", IQR_math)
print("\n----------------------------------------------------------------\n")

# Стандартное отклонение
std_deviation = df['Mark'].std()
print("Стандартное отклонение:", std_deviation)
print("\n----------------------------------------------------------------\n")

print(df.info())  # Вывод сведений о массиве
print("\n----------------------------------------------------------------\n")
print(df.describe())  # Статистическое описание данных
