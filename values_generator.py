import random
from random import randrange

times, cc_list, amounts, cc_iterations, time_iterations, amounts_iterations = [], [], [], 0, 0, 0

# filling up the cc list
while cc_iterations < 10000:
    cc_list.append(randrange(1000000000000000, 10000000000000000))
    cc_iterations += 1

# filling up the times list
while time_iterations < 10000:
    times.append(f"{randrange(24):02}{randrange(60):02}{randrange(60):02}")
    time_iterations += 1

# filling the amounts list
while amounts_iterations < 10000:
    amounts.append(round(random.uniform(1.01, 9999.99), 2))
    amounts_iterations += 1

# filling up the times list
while time_iterations < 10000:
    times.append(f"{randrange(24):02}{randrange(60):02}{randrange(60):02}")
    time_iterations += 1
