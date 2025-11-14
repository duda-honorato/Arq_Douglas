#cdg em andamento, nada disso foi testado
#Ref https://materials.jeremybejarano.com/MPIwithPython/introMPI.html -https://fbpic.github.io/_modules/fbpic/utils/random_seed.html

import MPI #verificar se eh assim msm
import random
import time
import math

def pi_parcial(n_pontos):
  pontos_dentro = 0
  pontos_fora = 0
  #Incluir Seed para meio que separar os processos, sem isso tera processos duplicados - DIVISAO DE PROCESSOS
  random.seed(MPI.COMM_WORLD.Get_rank() + int(time.time()))
  for i in range(n_pontos):
        x = random.random()
        y = random.random()
        z = x*x + y*y
        if z <= 1.0:
            pontos_dentro += 1
        else
            pontos_fora += 1
  return pontos_dentro, pontos_fora
def main():

