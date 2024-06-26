import numpy
numpy.random.seed(0)
data = numpy.random.randint(100, 1000, 50)
print(data)

mean=numpy.mean(data)
weighted_mean=numpy.average(data, weights=numpy.arange(1, 51))
max=numpy.max(data)
min=numpy.min(data)
median=numpy.median(data)
std_dev=numpy.std(data)
print(f"Средние продажи: {mean}")
print(f"Средние взвешенные продажи: {weighted_mean}")
print(f"Максимальные продажи: {max}")
print(f"Минимальные продажи: {min}")
print(f"Медиана продаж: {median}")
print(f"Стандартное отклонение продаж: {std_dev}")