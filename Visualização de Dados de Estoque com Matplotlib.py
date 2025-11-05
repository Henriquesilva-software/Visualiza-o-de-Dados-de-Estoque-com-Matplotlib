import matplotlib.pyplot as plt

dias = [1, 2, 3, 4, 5, 6, 7]
estoque = [100, 95, 110, 105, 120, 115, 130]

plt.figure(figsize=(10, 6))
plt.plot(dias, estoque, marker='o', color='blue', linestyle='-', linewidth=2, label='Produto A')
plt.title('Tendência de Estoque Diário')
plt.xlabel('Dia')
plt.ylabel('Quantidade em Estoque')
plt.legend()
plt.grid(True)
plt.show()

produtos = ['Teclado', 'Mouse', 'Monitor', 'Webcam']
quantidades = [50, 75, 30, 60]

plt.figure(figsize=(8, 5))
plt.bar(produtos, quantidades, color=['orange', 'green', 'purple', 'red'])
plt.title('Comparação de Quantidades em Estoque por Produto')
plt.xlabel('Produto')
plt.ylabel('Quantidade')
plt.show()

categorias = ['Eletrônicos', 'Vestuário', 'Alimentos']
valores = [15000, 8000, 5000]

plt.figure(figsize=(6, 6))
plt.pie(valores, labels=categorias, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightgreen', 'lightcoral'])
plt.title('Proporção do Valor Total de Estoque por Categoria')
plt.legend(categorias, loc='upper right')
plt.show()

precos = [50, 120, 300, 80, 20]
estoque_itens = [80, 25, 10, 70, 150]

plt.figure(figsize=(8, 6))
plt.scatter(precos, estoque_itens, color='darkred', marker='o')
plt.title('Relação entre Preço e Quantidade em Estoque')
plt.xlabel('Preço Unitário (R$)')
plt.ylabel('Quantidade em Estoque')
plt.grid(True)
plt.show()
