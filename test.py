salario = float(input())

if 0 <= salario <= 400.00:
    reajuste = 15
    reajuste_ganho = ((reajuste * salario) / 100) 
    novo_salario = reajuste_ganho + salario
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste_ganho:.2f}")
    print(f"Em percentual: {reajuste} %")
elif 400.01 <= salario <= 800.00:
    reajuste = 12
    reajuste_ganho = ((reajuste * salario) / 100) 
    novo_salario = reajuste_ganho + salario
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste_ganho:.2f}")
    print(f"Em percentual: {reajuste} %")
elif 800.01 <= salario <= 1200.00:
    reajuste = 10
    reajuste_ganho = ((reajuste * salario) / 100) 
    novo_salario = reajuste_ganho + salario
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste_ganho:.2f}")
    print(f"Em percentual: {reajuste} %")
elif 1200.01 <= salario <= 2000.00:
    reajuste = 7
    reajuste_ganho = ((reajuste * salario) / 100) 
    novo_salario = reajuste_ganho + salario
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste_ganho:.2f}")
    print(f"Em percentual: {reajuste} %")
else:
    reajuste = 4
    reajuste_ganho = ((reajuste * salario) / 100) 
    novo_salario = reajuste_ganho + salario
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste_ganho:.2f}")
    print(f"Em percentual: {reajuste} %")