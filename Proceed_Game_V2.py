import DQN_Player
import random
from Environment import Game

def get_card():
    while True:
        data = input().split()
        if data[0] != '0' and len(data) != 2:
            print('wrong input. try again')
        else:
            break
    return data

# P1 : Human
# P2 : Human
# P0 : AI


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
    if turn == 0:               # AI turn
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
                env.turn += env.direction
            elif action == 3:
                for i in range(len(P1_cards)):
                    if P1_cards[i][1] == 'Q':
                        able.append(P1_cards[i])
                env.direction *= -1
            elif action == 4:
                for i in range(len(P1_cards)):
                    if P1_cards[i][1] == 'K':
                        able.append(P1_cards[i])
                env.turn += 2 * env.direction
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
            final_action = random.choice(able)
            P1_cards.remove(final_action)
            print('final action : ', final_action)
            env.top_card = final_action
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
        print(env.top_card)
        action = get_card()
        print(action)
        if action[0] == '0':
            print('attack : ', env.attack)
            env.attack = 0
        elif action[0] == '999':
            break
        else:
            env.top_card = action
            if action[0] == 'J':
                env.attack += 5
            elif action[1] == '2':
                env.attack += 2
            elif action[1] == 'A':
                env.attack += 3
            elif action[1] == '3':
                env.attack = 0
            elif action[1] == 'J':
                env.turn += env.direction
            elif action[1] == 'Q':
                env.direction *= -1
            elif action[1] == 'K':
                env.turn += 2 * env.direction

    env.turn += env.direction
    print('\n')

print('game ended!!!')


'''
< 작동 점검할 것들 >
- 공격 카드 작동 여부
- 방어 카드 작동 여부
- 특수카드(J, Q, K) 작동 여부
- 게임 끝나는가?

< 나중에 보완할 것들 >
- 불가능한 카드를 냈을 경우 오류 메세지
- 잘못 입력했을 경우 오류 메세지
'''


