import pandas as pd

df = pd.read_csv(r"C:\Users\alejandro.nascimento\Downloads\funcionarios.csv")

#print (df.loc[1:10, "nome":"departamento"])

salario = df.query("salario > 3000 and ativo == True") 

SalarioNome = df[["nome", "salario"]]
