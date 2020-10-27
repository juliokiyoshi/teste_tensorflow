import argparse
import os 
from csv import writer
parser = argparse.ArgumentParser()
parser.add_argument("pw", type=int,
                    help="Are you running in PW8 or PW9?")
parser.add_argument("csv", type = str,
                    help="Name of CSV File output")
parser.add_argument("name", type = str,
                    help="Name of TXT to convert in CSV")
args = parser.parse_args()
lista=[]
aux=[]
primeira_linha=['POWER'+str(args.pw)+'- arquivo_teste', 'cpu-cycles', 'instructions', 'cache-references','cache-misses', 'branches','branch-misses','time elapsed'] 


file_output=args.csv+'.csv'
#ira criar o arquivo csv que irá armazenar os dados dos teste
file_csv=open(file_output,'w+')

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

append_list_as_row(file_output, primeira_linha)

for j in range(0,9):
    file_name='N'+str(j)+args.name[2:] # POR EXEMPLO O NOME DO TXT ONDE ESTÁ OS DADOS É N7_PW8_vgg16.txt, então NOME_DO_ARQUIVO == _PW8_vgg16.txt
    f=open(file_name,'r')
    for lines in f:
        if str(lines) !='\n':
            lista.append(str(lines).split())

    for i in range(len(lista)):
        if i==0:
            aux.append('teste'+str(j))
        if i>=2 and i!= 8 and i<=9:
            aux.append(lista[i][0])
    append_list_as_row(file_output, aux)
    aux.clear()
    lista.clear()
    f.close()
