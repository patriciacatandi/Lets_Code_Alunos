import csv

f = open("C:\\Users\\Carol\\Desktop\\Lets_Code_Alunos\\02_Ferramentas_Programação\\03_Pandas\\alunos.csv", "r", encoding="utf-8")

leitor = csv.reader(f, delimiter=';', lineterminator='\n')



planilha = []

for linha in leitor:
    planilha.append(linha)
    
f.close()

print(planilha)