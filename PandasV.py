import pandas as pd

df = pd.read_csv(r"C:\Users\alejandro.nascimento\Downloads\funcionarios.csv")

print (df.loc[1:10, "nome":"departamento"])
