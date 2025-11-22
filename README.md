# Descricao
Este projeto implementa o calculo de π (PI) utilizando o Metodo do Monte Carlo com a paralelizacao atraves do MPI com o objetivo de demonstrar os ganhos de desempenho obtidos atraves da programacao paralela em comparacao com a abordagem sequencial

# 🎯 Objetivos
1 - Implementar o algoritmo de Monte Carlo para cálculo de π				

2 - Desenvolver uma versao sequencial e outra paralela do algoritmo 

3 - Analisar o speedup e eficiência do paralelismo com MPI

# Fundamentação Teórica
Método de Monte Carlo
O método baseia-se na geração de pontos aleatórios dentro de um quadrado unitário e na verificação de quantos pontos caem dentro de um quarto de círculo inscrito. A aproximação de π é dada por: π ≈ 4 × (Número de pontos dentro do círculo) / (Total de pontos)

MPI (Message Passing Interface)
MPI é um padrão para comunicação entre processos em computação paralela, permitindo que múltiplos processos trabalhem cooperativamente na resolução de um problema.

# 🔗 Sobre a libguagem
Linguagem: Python

Biblioteca de Paralelismo: mpi4py

Biblioteca Auxiliares: random, time e math

Ferramentas: MPI (Message Passing Interface)

# Links Ref:
https://rabernat.github.io/research_computing/parallel-programming-with-mpi-for-python.html; https://stackoverflow.com/questions/21088420/mpi4py-send-recv-with-tag
