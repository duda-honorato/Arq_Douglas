import random 
import time 
import math

def pi_sequencial(n_pontos):
    pontos_dentro = 0
    pontos_fora = 0
    inicio = time.time()
    for i in range(n_pontos):
        x = random.random()
        y = random.random()
        z = x*x + y*y
        if z <= 1.0:
            pontos_dentro += 1
        else
            pontos_fora += 1
    pi_aprox = 4.0 * pontos_dentro/n_pontos
    fim = time.time()
    t_execucao = fim - inicio

    return pi_aprox, pontos_dentro, pontos_fora, t_execucao
    
def main():
     while True:
        try:
            n_pontos = int(input("Digite o número de pontos a serem gerados: "))
            if n_pontos > 0:
                break
            else:
                print("Por favor, digite um número positivo.")
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

    print("=== Cálculo de Pi via Método de Monte Carlo (Sequencial) ===")
    print(f"Número de pontos: {n_pontos:,}")

    proporcao_dentro = pontos_dentro / num_pontos
    proporcao_fora = pontos_fora / num_pontos
    erro_absoluto = abs(math.pi - pi_aproximado)
    erro_percentual = erro_absoluto / math.pi * 100

    print("\n=== RESULTADOS ===")
    print(f"Pontos dentro do círculo: {pontos_dentro:,} ({proporcao_dentro:.4f} - {proporcao_dentro*100:.2f}%)")
    print(f"Pontos fora do círculo:   {pontos_fora:,} ({proporcao_fora:.4f} - {proporcao_fora*100:.2f}%)")
    print(f"Pontos totais:           {num_pontos:,}")
    print(f"Razão (dentro/fora):     {pontos_dentro/pontos_fora:.4f}")
       
    print(f"\nPi aproximado:  {pi_aproximado:.10f}")
    print(f"Pi real:        {math.pi:.10f}")
    print(f"Erro absoluto:  {erro_absoluto:.10f}")
    print(f"Erro percentual: {erro_percentual:.6f}%")
    
    print(f"\nTempo de execução: {tempo_execucao:.4f} segundos")
]
    print(f"\n=== VERIFICAÇÃO ===")
    if erro_percentual < 0.1:
        print("✅ Aproximação EXCELENTE (erro < 0.1%)")
    elif erro_percentual < 1.0:
        print("✅ Aproximação BOA (erro < 1%)")
    else:
        print("⚠️  Aproximação pode ser melhorada (aumente o número de pontos)")

if __name__ == "__main__":
    main()



        
