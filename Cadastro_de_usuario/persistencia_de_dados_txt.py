from rich.console import Console
from time import sleep
 
lista = []
 
def ler():
    try:
        with open("rich.txt", "r", encoding="utf-8") as texto:
            for c in texto:
                if ";" in c:
                    c = c.strip().split(";")
                    lista.append(c)
    except:
                pass
    else:
            console.print("-"*30)
            for c in lista:
                    print(f"{c[0]:<10}{c[1]} anos")
            console.print("-"*30)
                
                
def save(lista1):
            with open("rich.txt", "a", encoding="utf-8") as texto:
                texto.write(f"{lista1[0]};{lista1[1]};\n")
   

          
                              
nome = str(input("Nome: ")).upper()
idade = int(input("Idade: "))

console = Console()

with console.status("[bold green]Processando salvamento dos dados...[/]"):
    sleep(4)
    console.print("[bold green]Etapa 1 concluída[/]")
    sleep(3)
    console.print("[bold green]Etapa 2 concluída[/]")
    sleep(2)
    console.print("[bold yellow]Salvamento concluído com êxito[/]")

lista2 = [nome, idade]
save(lista2)

with console.status("[bold green]Mostrar dados...[/]"):
    sleep(4)
    console.print("[bold green]Aguarde um momento...[/]")
    sleep(3)

ler()