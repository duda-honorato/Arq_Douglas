import random 
import time
import math
from mpi4py imoport MPI

def pi_paralelo(n_pontos):
  #Iniciliazar
  comm = MPI.COMM_WORLD
  rank = comm.Get_rank()
  size = comm.Get_size()
  #Divisao de Processos -- Pontos/Processo
  

