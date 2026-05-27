
Nomes da Dupla:   
    Gabriel de Avelar Silva => Gadev122  
    Mateus Martins Machado  => MateusM-M  


Linguagem escolhida para o Trabalho: Python  



INSTRUÇÕES DE USO:
    -O programa pode ser executado utilizando "executar-windows.bat" ou "executar-linux.sh" na pasta principal do programa  
    -Quando o programa for executado, irá aparecer uma lista de 5 interações, você pode digitar o número correspondente à execução desejada.  
	-No modo normal você pode fazer as conversões (Ex: Binário <--> Decimal), basta digitar 1 para escolher esse modo e logo em seguida dar os valores de entrada (número a ser convertido, base desse número, nova base para que o número vai ser convertido  
	-No modo passo-a-passo, o programa irá fazer a mesma coisa que o modo normal só que mostrando cada processo da conversão  
	-No modo csv, o programa irá realizar as conversões desejadas a partir da leitura de um arquivo de entrada chamado "entrada.csv" que estará localizado na pasta raiz do programa. A ordem de leitura de cada linha do arquivo será: numero;base;nova_base  
	-No modo quiz será gerado 5 questões de conversão totalmente aleatórias que você deve responder de acordo com o que pede (Ex: Converta 11 de base 2 para a base 10). As questões vão ficando mais difíceis conforme você prossegue. No final do quiz, você receberá sua pontuação. Quanto mais difícil a questão que você acertar, mais pontos você ganha  
	-A opção de "calcular máximos" é para descobrir os valores máximos de cada base de acordo com a quantidade de bits inserida na entrada.  
    -Para executar o teste do conversor, utilize o comando: py -m Testes.conversor_test na pasta raiz do programa (.../Trabalho-Coversao/)  

EXEMPLOS DE USO: 
    -> Modo normal:
    
      	Entrada:
            Número: 1010
            Base de origem: 2
            Base de saída: 10
            
        Saída:
            Resultado: 10


    -> Modo passo-a-passo:
    
        Entrada:
            Número: 15
            Base de origem: 10
            Base de saída: 2
            
        Saída:
        
            [Passo a Passo] Parte Inteira (Divisões Sucessivas por 2):
            
              15 ÷ 2 = 7 | Resto: 1
               7 ÷ 2 = 3 | Resto: 1
               3 ÷ 2 = 1 | Resto: 1
               1 ÷ 2 = 0 | Resto: 1
               
            Resultado: 1111


    -> Modo CSV:
    
        Arquivo de entrada ("entrada.csv"):
        
            10;10;2
            1010;2;10
            FF;16;10
            
        Arquivo de saída ("saida.csv"):
        
            10;10;1010;2
            1010;2;10;10
            FF;16;255;10


    -> Modo quiz:
    
        Pergunta:
            Converta 1111 da base 2 para a base 10
            
        Resposta correta:
            15
            
        Resultado final:
            Pontuação: 35 pontos


    -> Calcular máximos:
    
        Entrada:
		Quantidade de Bits: 8

		Saída:
		O maior valor representável com 8 bits em cada base é:
		(255, '11111111', '377', 'FF')
    
LIMITAÇÕES CONHECIDAS:  
    - Se você executar o código direto no arquivo main.py sem usar o executável da pasta raiz do programa no modo CSV o programa não irá encontrar o arquivo "entrada.csv";
