# imports framework
import sys
sys.path.insert(0, 'evoman')
from environment import Environment
from controller import Controller
import os
import neat
import visualize

# Implementacao da estrutura de controle dos sprites do jogador
class player_controller(Controller):


        # params - a lista de sensores com os valores atuais dos mesmos
        # cont - o objeto do tipo net ou seja o objeto "rede neural"
        def control(self, params,cont):

            # recebe o objeto do tipo net para ser avaliado
            net = cont

            # retorna o resultado de saida da rede neural em forma de uma lista para a variavel output
            output = net.activate(params)

            # toma as decisoes de acao para o sprite do jogador
            if output[0] > 0.5:
                left = 1
            else:
                left = 0

            if output[1] > 0.5:
                right = 1
            else:
                right = 0

            if output[2] > 0.5:
                jump = 1
            else:
                jump = 0

            if output[3] > 0.5:
                shoot = 1
            else:
                shoot = 0

            if output[4] > 0.5:
                release = 1
            else:
                release = 0

            # dado como retorno uma lista de boleanos indicando as acoes para o sprite do jogador
            return [left, right, jump, shoot, release]

# configuracao do ambiente EvoMan
#
# esta configurado para o modo multi inimigos ja que o intuito do treino desta rede neural e que ele treine
# para conseguir derrotar todos os 8 tipos de inimigos
#
# enimies - a lista indicando quais inimigos serao enfrentados, existem 8 tipos de inimigos diferentes, cada
# fenotipo (rede neural) sera avaliada contra os 8 inimigos uma vez contra cada inimigo
#
# playermode - usado para indicar qual modo de controle para o jogador, no caso ai indica que sera uma inteligencia artificial
#
# passado a classe player_controller para indicar para o ambiente como o jogador sera controlado
#
# speed - utilizado para indicar a velocidade do jogo, fastest rodara o jogo sem limitacao de quadros por segundo
# acelerando o processo de treinamento, tambem pode ser configurado para normal
#
# randomini - o atributo utilizado para configurar a posicao de "spawn" (nascimento) do inimigo no mapa, esta
# configurado para nascer em partes aleatorias dos cenarios
env = Environment(multiplemode = 'no', enemies = [1], playermode="ai",
                  player_controller=player_controller(), speed = 'fastest',
                  randomini = 'yes')

# Executa a simulacao e retorna o valor do fitness deste fenotipo (rede neural) que esta sendo avaliada
def simula(env,x):
    # f = fitness result
    # p = player life result
    # e = enemy life result
    # t = time result
    f,p,e,t = env.play(pcont=x)
    return f

def eval_genomes(genomes, config):
    # for dedicado a percorrer toda a população de genomas
    for genome_id, genome in genomes:
        # transforma o genoma que está sendo avaliado
        # em fenotipo ou seja uma rede neural
        net = neat.nn.RecurrentNetwork.create(genome, config)
        # Metodo simula é executado e retorna o valor de fitness da rede neural
        # genome.fitness é um atributo do objeto genoma que tem a finalidade
        # de guardar o resultado do fitness deste genoma
        genome.fitness = simula(env, net)

def run(config_file):
    # carrega o arquivo de configuracao realizando os "parsers" necessarios para coletar as configuracoes.
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    # Cria uma populacao de genomas baseadas nas configuracoes setadas no arquivo
    p = neat.Population(config)

    # Adiciona algumas configuracoes de saidas no terminal para gerar pequenos relatorios durante a execucaoo.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    # informa no console e salva um arquivo com o estado atual da populacao de genotipos atual para evitar
    # perdas durante a execucao caso ocorra uma falha de energia por exemplo.
    p.add_reporter(neat.Checkpointer(5))

    # Executa N vezes o metodo de qualificacao de fitness para toda a populacao parametro 1 passa-se o metodo
    # e o segundo a quantidade de geracoes em que sera executada. Caso atinja-se o fitness antes do valor de
    # geracoes estimado a execucao e interrompida visto que o objetivo primario e sempre atingir o valor de fitness desejado
    winner = p.run(eval_genomes, 100)

    # Mostra qual o genoma obteve o maior fitness dentre as N execucoes de avaliacao e ou o melhor genoma que atingiu o valor
    # igual ou superior ou desejado e determinado no arquivo de configuracao.
    print('\nBest genome:\n{!s}'.format(winner))

    # Transforma o genoma e fenotipo para uma analise visual do resultado dele
    print('\nOutput:')
    winner_net = neat.nn.RecurrentNetwork.create(winner, config)

    # lista com os nomes das entradas da rede neural com os valores negativos
    # lista com os nomes das saidas da rede neural com os valores positivos
    node_names = {-1:'dintancia projetil 1', -2:'distancia projetil 2', -3:'distancia projetil 3', -4:'distancia projetil 4', -5:'distancia projetil 5', -6:'distancia projetil 6', -7:'distancia projetil 7', -8:'distancia projetil 8', -9:'distancia projetil 9', -10:'distancia projetil 10', -11:'distancia projetil 11', -12:'distancia projetil 12', -13:'distancia projetil 13', -14:'distancia projetil 14', -15:'distancia projetil 15', -16:'distancia projetil 16', -17:'distancia inimigo 1', -18:'distancia inimigo 2', -19:'direcao sprites 1', -20:'direcao sprites 2', 0:'esquerda', 1:'direita', 2:'pular', 3:'atirar', 4:'release'}

    # desenha uma representacao visual do fenotipo "campeao"
    visualize.draw_net(config, winner, True, node_names=node_names)

    # desenha um grafico de duas dimensoes com y sendo o fitness e x sendo as geracoes,
    # demonstrando assim a evolucao do nivel de fitness pelo passar das geracoes
    visualize.plot_stats(stats, ylog=False, view=True)

    # desenha visualmente a variacao e geracao de novas especies com o passar das geracoes
    visualize.plot_species(stats, view=True)

if __name__ == '__main__':
    # Aqui e onde toda a "acao" comeca. e determinado o caminho para o arquivo de configuracao.
    # Este arquivo de configuracao sera manipulado e se estiver com as configuracoes
    # sem conflitos ira executar normalmente.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-Neat-Evoman')
    run(config_path)
