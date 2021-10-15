import DQN_Player
import random
from Environment import Game

def get_card():
    data = input().split()
    return data

# P1 : AI
# P2 : Human
# P0 : Human


print('starting game!\nP1 is AI Player.')

startingCards_num = 5

env = Game()


P1 = DQN_Player.Agent(env.state_size, env.action_size)

print('please take 5 cards each')
P1_cards = [get_card() for _ in range(startingCards_num)]
done = False
winner = False

env.top_card = get_card()

for t in range(300):
    turn, direction = env.find_turn()
    print(turn, direction)
    action = False
    if turn == 1:               # AI turn
        print("P{} turn".format(turn))
        print('top card : ', env.top_card)
        print('attack : ', env.attack)
        state = env.action_able(P1_cards, env.top_card)
        while True:
            if not state:
                action = 999
                break
            action = P1.get_action(state)
            if state[action] > 0:
                break
        able = list()
        if action != 999:
            if action == 0:
                for i in range(len(P1_cards)):
                    if P1_cards[i][0] == env.top_card[0]:
                        able.append(P1_cards[i])
            elif action == 1:
                for i in range(len(P1_cards)):
                    if P1_cards[i][1] == env.top_card[1]:
                        able.append(P1_cards[i])
            elif action == 2:
                for i in range(len(P1_cards)):
                    if P1_cards[i][1] == 'J':
                        able.append(P1_cards[i])
                env.turn += env.direction * 2
            elif action == 3:
                for i in range(len(P1_cards)):
                    if P1_cards[i][1] == 'Q':
                        able.append(P1_cards[i])
                env.direction *= -1
            elif action == 4:
                for i in range(len(P1_cards)):
                    if P1_cards[i][1] == 'K':
                        able.append(P1_cards[i])
                env.turn += 3
            elif action == 5:
                for i in range(len(P1_cards)):
                    if P1_cards[i][1] == '3':
                        able.append(P1_cards[i])
                env.attack = 0
            elif action == 6:
                for i in range(len(P1_cards)):
                    if P1_cards[i][1] == '2':
                        able.append(P1_cards[i])
                env.attack += 2
            elif action == 7:
                for i in range(len(P1_cards)):
                    if P1_cards[i][1] == 'A':
                        able.append(P1_cards[i])
                env.attack += 3
            elif action == 8:
                for i in range(len(P1_cards)):
                    if P1_cards[i][0] == 'J':
                        able.append(P1_cards[i])
                env.attack += 5
            print(able)
            final_action = random.choice(able)
            P1_cards.remove(final_action)
            print('final action : ', final_action)
            env.top_card = final_action[0]
        else:

            if env.attack:
                print('you can\'t avoid the attack. take {} cards'.format(env.attack))
                P1_cards.extend([get_card() for _ in range(env.attack)])
                env.attack = 0
                action = 999
            else:
                print('no possible action. take a card')
                P1_cards.append(get_card())
                action = 999
        if not P1_cards:
            break

    else:
        print("P{} turn".format(turn))
        action = get_card()
        print(env.top_card)
        if action == '0':
            print('passing')
            pass
        else:
            print('not passing')
            env.top_card = action

    env.turn += env.direction
    print('turn ended')

print('game ended!!!')


'''
< 작동 점검할 것들 >
- 공격 카드 작동 여부
- 방어 카드 작동 여부
- 특수카드(J, Q, K) 작동 여부
- 게임 끝나는가?
'''

