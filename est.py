import csv
with open('exercicios.csv', 'r') as arquivo_csv:
    exercicios=[]
    leitor = csv.reader(arquivo_csv, delimiter=',')
    for linha in leitor:
        if(linha[1]=="abdominals"  or linha[1]=="lower back"):
            linha.append("abdomen")
        if(linha[1]=="adductors" or linha[1]=="quadriceps" or linha[1]=="hamstrings" or linha[1]=="calves" or linha[1]=="glutes" or linha[1]=="abductors"):
            linha.append("inferiores")
        if(linha[1]=="biceps" or linha[1]=="shoulders" or linha[1]=="chest" or linha[1]=="middle back" or linha[1]=="lats" or linha[1]=="triceps" or linha[1]=="traps" or linha[1]=="forearms" or linha[1]=="necks"):
            linha.append("superiores")
        exercicios.append(linha)
    print(exercicios)
with open('exercicios.csv', 'w') as arquivo_csv:
    escrever = csv.writer(arquivo_csv, delimiter= ',', lineterminator= '\n')
    for i in exercicios:
        escrever.writerow(i)
