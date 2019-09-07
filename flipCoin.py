import random
# x = 0
# y = 0
# Flip_list = []
# HNf = {}
# TNf = {}
# HNf = [0 for i in range(1, 51)]
# TNf = [0 for i in range(1, 51)]
# Hn = {}
# Tn = {}
# Hn = [0 for i in range(1, 51)]
# Tn = [0 for i in range(1, 51)]
# total_Heads = 0
# total_tails = 0
Tails_number = 0
Heads_number = 0
tries = 0
stake = 100
bet = 1
bet_amount = 1
winnings = 0

while bet_amount < stake:
    tries += 1
    coin = random.randint(1, 2)  # Flip coin

    bet = tries % 2 + 1
    stake -= bet_amount
    print('%-20s %-20s %-20s %-20s %-20s' % ("Tries  " + str(tries), "  coin  " + str(coin), "   bet  " + str(bet), "    bet amount   " + str(bet_amount) + "    stake   " +
                                                     str(stake), "    winnings   " + str(winnings)))
    if coin == 1:
        if bet == 1:
            stake += bet_amount
            winnings += bet_amount
            bet_amount = 10
#          print('%-20s %-20s %-20s %-20s %-20s' % ("Tries  " + str(tries), "  coin  " + str(coin), "   bet  " + str(bet), "    bet amount   " + str(bet_amount) + "    stake   " +
                                                    #  str(stake), "    winnings   " + str(winnings)))

        else:

            stake -= bet_amount
            bet_amount = bet_amount * 2 + 10
        #    print('%-20s %-20s %-20s %-20s %-20s' % ("Tries  " + str(tries), "  coin  " + str(coin), "   bet  " + str(bet), "    bet amount   " + str(bet_amount) + "    stake   " +
                                                    #  str(stake), "    winnings   " + str(winnings))) """
    if coin == 2:

        if bet == 2:
            stake += bet_amount
            winnings += bet_amount
            bet_amount = 10
            # print('%-20s %-20s %-20s %-20s %-20s' % ("Tries  " + str(tries), "  coin  " + str(coin), "   bet  " + str(bet), "    bet amount   " + str(bet_amount) + "    stake   " +
                                                    #  str(stake), "    winnings   " + str(winnings))) """
        else:

            stake -= bet_amount
            bet_amount = bet_amount * 2 + 10
            #  print('%-20s %-20s %-20s %-20s %-20s' % ("Tries  " + str(tries), "  coin  " + str(coin), "   bet  " + str(bet), "    bet amount   " + str(bet_amount) + "    stake   " +
                                                    #  str(stake), "    winnings   " + str(winnings)))"""


print(" ")
print(tries)
# print(total_tails, total_Heads)
print(("winnings   ") + str(winnings))
