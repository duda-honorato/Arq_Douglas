import random 
import time
import math
from mpi4py imoport MPI

def pi_paralelo(n_pontos):
  #Iniciliazadores MPI
  comm = MPI.COMM_WORLD
  rank = comm.Get_rank()
  size = comm.Get_size()

  #Divisao de Processos -- Pontos/Processo
  n_pontos_local = n_pontos // size
  if rank == 0:
    n_pontos_local += n_pontos_total % size # Casos em que a divisao n for exata

  #Calculo do identificador para cada processo
  random.seed(rank + 42) #n precisa ser 42, so to c preguica de fazer o random 
  pontos_dentro_local = 0
  #Inicio - TIMER
  inicio = time.time()
  
  for i in range(n_pontos_local):
    pontos_dentro = 0
    pontos_fora = 0
    inicio = time.time()
    for i in range(n_pontos):
        x = 2*random.random()-1
        y = 2*random.random()-1
        z = x**2 + y**2
        if z <= 1.0:
            pontos_dentro += 1
          
  #Continuar.... 

def main():
  #Verificar se precisa inserie no MAIN
  comm = MPI.COMM_WORLD
  rank = comm.Get_rank()
  size = comm.Get_size()
  #Solicitar o n pontos -- Rank? 
  pi_aprox, pontos_dentro, pontos_fora, t_execucao = pi_paralelo(n_pontos)

  proporcao_dentro = pontos_dentro / n_pontos  
  proporcao_fora = pontos_fora / n_pontos  
  erro_absoluto = abs(math.pi - pi_aprox)  
  erro_percentual = erro_absoluto / math.pi * 100

  print("\n=== RESULTADOS ===")
  print(f"Pontos dentro do círculo: {pontos_dentro:,} ({proporcao_dentro:.4f} - {proporcao_dentro*100:.2f}%)")
  print(f"Pontos fora do círculo: {pontos_fora:,} ({proporcao_fora:.4f} - {proporcao_fora*100:.2f}%)")
  print(f"Pontos totais: {n_pontos:,}")  
  print(f"Razão (dentro/fora): {pontos_dentro/pontos_fora:.4f}")
  
  print(f"\nPi aproximado: {pi_aprox:.10f}")  
  print(f"Pi real: {math.pi:.10f}")
  print(f"Erro absoluto: {erro_absoluto:.10f}")
  print(f"Erro percentual: {erro_percentual:.6f}%")

  print(f"\nTempo de execução: {t_execucao:.4f} segundos")
  print(f"Número de processos: {size}")

  print(f"\n=== VERIFICAÇÃO ===")
    if erro_percentual < 0.1:
      print("✅ Aproximação EXCELENTE (erro < 0.1%)")
    elif erro_percentual < 1.0:
      print("✅ Aproximação BOA (erro < 1%)")
    else:
      print("⚠️  Aproximação pode ser melhorada (aumente o número de pontos)")

if __name__ == "__main__":
    main()


        

