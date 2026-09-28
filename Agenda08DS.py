# Inicializando os contadores de respostas
qtd_excelente = 0
qtd_ruim = 0

# Definindo o número de entrevistados


total_entrevistados = 10

print(f"--- Início da Pesquisa de Opinião (Total: {total_entrevistados} entrevistados) ---")

# Estrutura de repetição para coletar os dados
for i in range(1, total_entrevistados + 1):
    print(f"\nEntrevistado(a) {i}:")
    
    # Coletando nome e idade
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    
    # Coletando a opinião com validação básica
    print("Avalie o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    opiniao = int(input("Digite o número correspondente à sua opinião: "))
    
    # Estrutura de decisão para contabilizar as respostas
    if opiniao == 1:
        qtd_excelente += 1
    elif opiniao == 3:
        qtd_ruim += 1
    elif opiniao == 2:
        # A opção 2 (BOM) não precisa de contador específico segundo o enunciado,
        # mas faz parte das opções válidas solicitadas.
        pass
    else:
        print("Opção inválida! Esta resposta não será contabilizada nas estatísticas principais.")

# Exibindo os resultados finais ao término da pesquisa
print("\n" + "="*30)
print("RESULTADO FINAL DA PESQUISA")
print("="*30)
print(f"a) Quantidade de respostas 'EXCELENTE': {qtd_excelente}")
print(f"b) Quantidade de respostas 'RUIM': {qtd_ruim}")
