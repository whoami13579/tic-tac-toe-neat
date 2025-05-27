import neat.genome
import pygame
from tic_tac_toe import Game
import neat
import os
import pickle
import time


WIDTH, HEIGHT = 600, 600

class TicTacToeGame:
    def __init__(self, width: int, height: int):
        self.__window = pygame.display.set_mode((width, height))
        self.__game = Game(self.__window, width, height)
    
    def testGame(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

                if event.type == pygame.MOUSEBUTTONDOWN and self.__game.getRun():
                    self.__game.addPiece()
                
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                self.__game.reset()
            
            self.__game.draw()

        pygame.quit()

    
    def train_ai(self, genome1, genome2, config):
        net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
        net2 = neat.nn.FeedForwardNetwork.create(genome2, config)

        while self.__game.getRun():
            result = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            output1 = net1.activate(self.__game.get_bitBoardList())
            tmp = sorted(output1, reverse=True)
            i = 0
            while True:
                try:
                    decision1 = output1.index(tmp[i])
                except:
                    print(f"i = {i}")
                    print(output1)
                    print(output1.index(tmp[i]))
                    print(decision1)
                    time.sleep(30)
                    return

                result = self.__game.addPieceByNumber(decision1)
                if result == 0:
                    output1[output1.index(tmp[i])] = None
                    i += 1
                else:
                    break

            self.__game.draw()
            if result == 2 or result == 4:
                self.calculate_fitness(genome1, genome2, result)
                self.__game.reset()
                self.__game.draw()
                return

            output2 = net2.activate(self.__game.get_bitBoardList())
            tmp2 = sorted(output2, reverse=True)
            i = 0
            while True:
                try:
                    decision2 = output2.index(tmp2[i])
                except:
                    print(f"i = {i}")
                    print(output2)
                    print(output2.index(tmp2[i]))
                    print(decision2)
                    time.sleep(30)
                    return

                result = self.__game.addPieceByNumber(decision2)
                if result == 0:
                    output2[output2.index(tmp2[i])] = None
                    i += 1
                else:
                    break

            self.__game.draw()
            if result == 3 or result == 4:
                self.calculate_fitness(genome1, genome2, result)
                self.__game.reset()
                self.__game.draw()
                return

            self.__game.draw()


    def calculate_fitness(self, genome1, genome2, result):
        genome1.fitness += 100 if result == 2 else 0
        genome2.fitness += 100 if result == 3 else 0

        genome1.fitness += 10 if result == 4 else 0
        genome2.fitness += 10 if result == 4 else 0

    def play_with_ai(self, genome, config):
        net = neat.nn.FeedForwardNetwork.create(genome, config)

        while self.__game.getRun():
            result = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                    break
                if event.type == pygame.MOUSEBUTTONDOWN and self.__game.getRun():
                    result = self.__game.addPiece()
                    self.__game.draw()

            if result == None:
                pass
            elif result == 2 or 4:
                continue

            if self.__game.getCircle() == False:
                output1 = net.activate(self.__game.get_bitBoardList())
                tmp = sorted(output1, reverse=True)
                i = 0
                while True:
                    try:
                        decision1 = output1.index(tmp[i])
                    except:
                        print(f"i = {i}")
                        print(output1)
                        print(output1.index(tmp[i]))
                        print(decision1)
                        time.sleep(30)
                        return

                    result = self.__game.addPieceByNumber(decision1)
                    if result == 0:
                        output1[output1.index(tmp[i])] = None
                        i += 1
                    else:
                        break

                self.__game.draw()
            self.__game.draw()
            pygame.display.update()

        pygame.quit()
    


def eval_genomes(genomes, config):
    for i, (genome_id1, genome1) in enumerate(genomes):
        if i == len(genomes) - 1:
            break
        genome1.fitness = 0
        for genome_id2, genome2 in genomes[i+1:]:
            genome2.fitness = 0 if genome2.fitness == None else genome2.fitness
            game = TicTacToeGame(WIDTH, HEIGHT)
            game.train_ai(genome1, genome2, config)
            del game

# def eval_genomes(genomes, config):
#     game = TicTacToeGame(WIDTH, HEIGHT)
#     for _ in range(2):
#         for i, (genome_id1, genome1) in enumerate(genomes):
#             if i == len(genomes) - 1:
#                 break
#             genome1.fitness = 0
#             genome_id2, genome2 = genomes[i+1]
#             genome2.fitness = 0 if genome2.fitness == None else genome2.fitness
#             game = TicTacToeGame(WIDTH, HEIGHT)
#             game.train_ai(genome1, genome2, config)


def run_neat(config: neat.Config):
    # p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-7')
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1))

    winner = p.run(eval_genomes, 1)
    with open("best.pickle", "wb") as f:
        pickle.dump(winner, f)


def play_with_ai(config):
    with open("best.pickle", "rb") as f:
        winner = pickle.load(f)

    game = TicTacToeGame(WIDTH, HEIGHT)
    game.play_with_ai(winner, config)


if __name__ == "__main__":
    # ticTacToeGame = TicTacToeGame(WIDTH, HEIGHT)
    # ticTacToeGame.testGame()

    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)
    # run_neat(config)
    play_with_ai(config)