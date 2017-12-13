# Algoritmo neuro evolutivo aplicado a mecanica de um jogo 2D
A neuro-evolução é uma técnica de aprendizado de máquina que aplica algoritmos evolucionários para construir uma rede neural artificial, tendo como inspiração o processo biológico evolutivo do sistema nervoso na natureza.

A seguir um breve resumo e uma conclusão. Para mais detalhes a monografia completa está disponivel para download no próprio repositório.

# Resumo
Machine learning ou aprendizado de máquina em inteligência artificial é um tema relacionado à implementação de programas de computador capazes de realizar o processo de aprendizagem de forma autônoma.

Através da neuro-evolução é possível resolver não só problemas onde se tenham respostas conhecidas, como também desenvolver agentes inteligentes que aprendem a interagir com um determinado ambiente apropriadamente e encontrar soluções desconhecidas.

Jogos eletrônicos são cenários que na sua grande maioria possuem problemas abstratos e de soluções desconhecidas, tornando-se um bom cenário para aplicação e avaliação de um algoritmo neuro-evolutivo.

O objetivo desta monografia foi o estudo e desenvolvimento da aplicação de um algoritmo neuro-evolutivo a mecânica de um jogo eletrônico 2D, ou seja, um agente autônomo capaz de controlar a mecânica de um personagem e cumprir um devido objetivo. Obteve-se sucesso na implementação desse algoritmo.

# Conclusões e trabalhos futuros
A complexidade da mecânica de um jogo eletrônico 2D, juntamente com o desafio de dominar essa mecânica e derrotar um oponente torna o processo de aprendizagem de um agente autônomo com esse objetivo um cenário bom para a aplicação da neuro-evolução.

A técnica de neuro-evolução escolhida para o desenvolvimento da solução foi o NEAT (neuroevolution of augmenting topologies), por possibilitar a evolução da estrutura da rede neural como um todo. Para a mecânica de jogo eletrônico 2D foi escolhido o framework EvoMan, que fornece 8 jogos de presa-predador inspirados no jogo eletrônico MegaMan II, capaz de simular um ambiente dinâmico, ou seja, que não apresenta sempre o mesmo comportamento. O algoritmo implementado obteve sucesso no controle da mecânica do personagem, sendo apresentado os resultados para diferentes configurações de ambiente e parâmetros do algoritmo.

Pontos relevantes levantados durante o processo de estudo e desenvolvimento sugiram, como por exemplo a observação de que a diversificação de espécies aumentou somente quando a população era igual ou maior que 100 genomas. Um teste futuro interessante a ser realizado é colocar populações de tamanho ainda maiores que os testados.

Outro trabalho futuro relevante é o teste de um agente generalista como explicado no capítulo Framework EvoMan para observação do comportamento do algoritmo para a evolução de uma rede neural com multi-objetivos.

Um teste relevante para ser realizado é a alteração do atributo weight_max_value para o valor de 1 ao invés de 30 e o weight_min_value para 0 ao invés de -30. Essa distância grande nos pesos pode ter influenciado no crescimento baixo do fitness no decorrer das gerações. Alterando o valor desses atributos e refazendo todos os 40 testes comparando os resultados com os obtidos nesta monografia poderiam confirmar essa hipótese.
