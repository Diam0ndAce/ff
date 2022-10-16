from collections import Counter

def f(n_customers, n_first_id=0):
    id_sum = lambda x: sum([int(i) for i in str(x)])
    id_sum_arr = list(map(id_sum, [i for i in range(n_first_id, n_first_id+n_customers)]))
    
    groups = Counter(id_sum_arr)
        
    for group, num in groups.items():
        print(f'group_{group}: {num}')
    