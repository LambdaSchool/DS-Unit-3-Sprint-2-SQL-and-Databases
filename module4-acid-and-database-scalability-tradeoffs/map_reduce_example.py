from functools import reduce

my_list = [1, 2, 3, 4]

# We want the sum of squared values
# (A fairly real statistical task)

# Traditional (non-mapreduce approach)
ssv_trad = sum([i**2 for i in my_list])

# That works fine - but what it ew had 40 billion numbers?
# We could use a mapreduce approach

# To be clear - this code still runs on one computer
# But mapreduce paradigm *could* be distributerd more directly

squared_values = map(lambda i: i**2, my_list)

def add_numbers(x1, x2):
    return x1 + x2

ssv_mapreduce = reduce(add_numbers, squared_values)

print('Sum of squared values (traditional): '+ str(ssv_trad))
print('Sum of squared values (map-reduce): ' + str(ssv_mapreduce))
