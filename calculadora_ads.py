def limpar_tela():
    print("\n" * 2)

def calcular_metricas():
    limpar_tela()
    print("=== 🚀 CALCULADORA DE TRÁFEGO PAGO (ADS) ===")
    print("Ferramenta do Robson - Engenharia de Software\n")

    # 1. Coletando dados do usuário
    nome_campanha = input("Nome da Campanha (ex: Landing Page Vendas): ")
    
    try:
        investimento = float(input("Valor Investido (R$): "))
        impressoes = int(input("Número de Impressões (Visualizações): "))
        cliques = int(input("Número de Cliques: "))
        conversoes = int(input("Número de Vendas/Leads: "))
        receita_total = float(input("Receita Total Gerada (R$): "))
    except ValueError:
        print("\n❌ Erro: Por favor, digite apenas números (use ponto para centavos).")
        return

    # 2. Cálculos de Engenharia de Tráfego
    # CTR (Taxa de Cliques)
    ctr = (cliques / impressoes) * 100 if impressoes > 0 else 0
    
    # CPC (Custo por Clique)
    cpc = investimento / cliques if cliques > 0 else 0
    
    # CPA (Custo por Aquisição/Venda)
    cpa = investimento / conversoes if conversoes > 0 else 0
    
    # ROAS (Retorno sobre Gasto em Anúncios) - Quantas vezes o dinheiro voltou
    roas = receita_total / investimento if investimento > 0 else 0

    # 3. Gerando o Relatório
    print("\n" + "="*40)
    print(f"📊 RELATÓRIO DE PERFORMANCE: {nome_campanha.upper()}")
    print("="*40)
    
    print(f"💰 Investimento: R$ {investimento:.2f}")
    print(f"💵 Receita:      R$ {receita_total:.2f}")
    print("-" * 20)
    print(f"📈 CTR (Interesse):   {ctr:.2f}%")
    print(f"🖱️ CPC (Custo Clique): R$ {cpc:.2f}")
    print(f"🤝 CPA (Custo Venda):  R$ {cpa:.2f}")
    print("-" * 20)
    print(f"🏆 ROAS: {roas:.2f}x")
    
    # Análise automática simples
    if roas > 1:
        print("\n✅ Conclusão: A campanha deu LUCRO!")
    elif roas == 1:
        print("\n⚠️ Conclusão: A campanha empatou (Break-even).")
    else:
        print("\n🔻 Conclusão: A campanha deu PREJUÍZO. Melhore a Landing Page!")
    
    print("="*40 + "\n")

# Executar a função
calcular_metricas()
