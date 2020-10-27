import os 
from csv import writer
lista=[]
aux=[]
primeira_linha=['POWER X - arquivo_teste', 'cpu-cycles', 'instructions', 'cache-references','cache-misses', 'branches','branch-misses','time elapsed'] 

#ira criar o arquivo csv que irá armazenar os dados dos teste
file_csv=open("resultado.csv",'w+')

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

append_list_as_row('resultado.csv', primeira_linha)


for j in range(0,9):
    file_name='N'+str(j)+'NOME_DO_ARQUIVO' # POR EXEMPLO O NOME DO TXT ONDE ESTÁ OS DADOS É N7_PW8_vgg16.txt, então NOME_DO_ARQUIVO == _PW8_vgg16.txt
    f=open(file_name,'r')
    for lines in f:
        if str(lines) !='\n':
            lista.append(str(lines).split())

    for i in range(len(lista)):
        if i==0:
            aux.append('teste'+str(j))
        if i>=2 and i!= 8 and i<=9:
            aux.append(lista[i][0])
    append_list_as_row('resultado.csv', aux)
    aux.clear()
    lista.clear()
    f.close()
