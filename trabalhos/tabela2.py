#CODIGO SEM ERRO
import random

# Definir uma semente fixa para garantir que o mapeamento seja o mesmo em cada execução
random.seed(42)

# Gerar uma tabela de mapeamento dos números para sequências de asteriscos
def generate_asterisk_mapping():
    asterisk_mapping = {}
    used_sequences = set()
    
    for i in range(1, 10):
        while True:
            # Gerar uma sequência de asteriscos de tamanho 1 a 10
            sequence_length = random.randint(1, 10)
            sequence = '*' * sequence_length
            if sequence not in used_sequences:
                used_sequences.add(sequence)
                asterisk_mapping[str(i)] = sequence
                break
                
    return asterisk_mapping

# Exibir a tabela de mapeamento
def display_mapping(mapping):
    print("Tabela de Mapeamento de Números para Asteriscos:")
    for k, v in sorted(mapping.items()):
        print(f"{k}: {v}")

# Função principal
def main():
    asterisk_mapping = generate_asterisk_mapping()
    
    # Mostrar a tabela de mapeamento
    display_mapping(asterisk_mapping)

if __name__ == "__main__":
    main()
