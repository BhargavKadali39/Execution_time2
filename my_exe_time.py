
import timeit

code_to_test = """
a = range(100000)
b = []
for i in a:
    b.append(i*2)
"""

elapsed_time = timeit.timeit(code_to_test, number=500)
print(elapsed_time)
# 10.159821493085474
