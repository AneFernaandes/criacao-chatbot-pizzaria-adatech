# # Projeto de Chatbot para Anotação de Pedidos da Pizzaria Delícia 🍕😋

import random #biblioteca para geração de numeros aleatorios. Utilizaremos para gerar horario e tempo de entrega aleatórios.

#lista para armazenar o pedido 
pedido = []
#variavel para o total do pedido
total = 0
#dicionario com os sabores e preços das pizzas. usaremos ele no loop e para calcular e informar o preço do pedido
menu = {
    "calabresa": 70.00,
    "queijo": 50.00,
    "pepperoni": 80.00,
    "margherita": 80.00,
    "vegetariana": 80.00
}

# Geração de um horário aleatório entre 1 e 24
hora = random.randint(1, 24)

# Geração de um tempo de entrega aleatório entre 10 e 60 minutos
tempo_de_entrega = random.randint(30, 60)

# Link fictício para rastreio
link = "https://maps.app.goo.gl/wvnzfpeDNMMWfmR36"

#logica de saudação com base no horário de funcionamento entre 17 às 03h
if hora > 3 and hora < 18: 
    saudacao = "Boa tarde"
elif hora >= 18 and hora <= 23:
    saudacao = "Boa noite"
else:
    saudacao = "Bom dia"

if hora <= 3 or hora >= 17:
    funcionamento = "Olá, estamos abertos. Como posso ajudar você hoje?"
    opcao = 1
else:
    funcionamento = "Estamos fechados no momento, nosso horário de funcionamento é das 17 às 3"
    opcao = 3

#saudação de boas vindas
print(f"""
           
            {saudacao}! Bem-vindo à Pizzaria Delícia 🍕😋
            {funcionamento} {hora}:00

            ===============================

            """)

#variaveis para armazenar conteudo input
opcao1 = ""
sabor = ""
#loop do menu e pedido
while True:
    opcao1 = input("""
            
            
            Escolha uma opção:

            1 - VISUALIZAR MENU 🍕
            2 - FAZER PEDIDO 😁            

            ================================             
            Digite o número da opção desejada:    """

)

    if opcao1 == '1':
        print("""
              

            🧾 Conheça os sabores disponíveis:
            =================================
                     
            - CALABRESA
            molho especial, queijo mussarela, calabresa fatiada, cebola

            - QUEIJO
            molho especial, queijo mussarela, queijo parmesao, queijo provolone, catupiry

            - PEPPERONI
            mussarela, pepperoni, catupiry

            - MARGHERITA
            tomate, manjericão e mussarela
                 
            - VEGETARIANA
            molho especial, queijo mussarela,palmito, tomate, tomate,cebola,pimentao
            
            =================================
              
           😊 Nosso atendimento é totalmente automático para agilizar o seu pedido.
              
            """) #menu com descrição do cardápio
        opcao = input("""
                      
😋 Já sabe o que quer? Digite:
*2* para FAZER O PEDIDO,
*3* para SAIR:
------------                   
""") #menu para cliente seguir com o pedido ou sair da aplicação

    if opcao1 == '3' or opcao == '3':
        break

    if opcao1 == '2' or opcao == '2':
        nome = input("""
Qual seu nome?
------------
""")

#loop para o sistema solicitar sabor da pizza, acrescentar ao pedido e só parar quando o cliente digitar sair
    while sabor != "sair":
        sabor = input("""
                      
            😋 Por favor, digite o sabor da pizza que deseja. 
            Exemplo: Se quer QUEIJO digite *queijo*. (ou 'sair' para encerrar o pedido):
                      
            =============== MENU ===============
            
            CALABRESA 
            QUEIJO 
            PEPPERONI 
            MARGHERITA 
            VEGETARIANA 
            - SAIR - para fechar o pedido
            =================================
            """).lower()
        if sabor == 'sair':
            break
        if sabor in menu:
            preco = menu[sabor]
            print(f"""

{nome}, você escolheu uma pizza de {sabor}. Preço: R${preco}""")
            confirmacao = input("""                                
Confirmar pedido, está certo? Sim ou Não:  """).lower()
            if confirmacao == "sim" or confirmacao == "s":
                total += preco
                pedido.append(f"{sabor}")
                print("""
                      
            ✔️ Pedido computado. Deseja adicionar outra pizza? """)
            else:
                print("""
                      
            ❌ Pedido cancelado.""")
        else:
            print("""
                  
            ❌ Sabor de pizza não encontrado no menu. Por favor, escolha um sabor válido.""")

#solicitação de dados do cliente
    endereco = input(f"""

{nome}, qual é o seu endereço ?
------------
""")

    forma_pagamento = input("""
                            
💰 Por favor, qual é a forma de pagamento? 
Obs: aceitamos todos os cartões com acréscimo de 5%, pix ou à vista sem acréscimo.
------------
""")
    
#resumo com as pizzas pedidas e o valor total do pedido. Incluimos o tempo para entrega e link para rastreio do pedido.

    print("""
          

        Seu pedido:""")
    for item in pedido:
        print(f"""
😁🎉 Pedido confirmado!
Pizza de: {item}""")

    print(f"""
Total a pagar: R${total} | Forma de pagamento: {forma_pagamento}
⏰ Tempo de entrega: {tempo_de_entrega} minutos, para o seu endereço:  {endereco}.
{nome} , acompanhe seu pedido no link {link}
""")

    opcao = input("""
                  
            Deseja fazer outro pedido? Digite:
            *1* para VISUALIZAR O MENU,
            *2* para FAZER OUTRO PEDIDO,
            *3* para SAIR:
            """)

#loop para cliente ter opção de fazer um novo pedido apos finalizar a compra
    if opcao == '1':
        continue
    elif opcao == '3':
        break

print("Atendimento encerrado!! Volte sempre :)")


# VARIAS PARTES NESSE CÓDIO HÁ POSSIBILIDADE DO USO DE FUNÇOES. 
# Exemplo : no menu inicial {opcao} poderia ser usado funcção para tornar o codigo mais limpo e não precisar repetir, toda a caixa e sim apenas chamar a função.


# *Este projeto em equipe foi desenvolvido durante o Módulo 1 da Formação em Dados da ADA Tech, em parceria com o Ifood, sob a orientação do professor Diego Lacerda.*

