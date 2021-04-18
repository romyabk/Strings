# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player_0 = 'Ruud Gullit' 
player_1 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = str(player_0) +' ' + str (goal_0) + ', ' + str(player_1) + ' ' + str (goal_1)
print(scorers)
report = str(player_0) + ' ' + f"scored in the {goal_0}nd minute\n" + str(player_1) + ' ' + f"scored in the {goal_1}th minute"
print(report)

player = 'Hans van Breukelen'
print(player.find(' '))
first_name = player[0:4]
print(first_name)
print(player.find(' '))
print('len(player) = ', len(player))
last_name_len = len(player[5:18])
print(last_name_len)
name_short = player[0] + '.' + player [4:18]
print(name_short)
cheer = first_name + '!' +' '
chant = cheer +  cheer + cheer + cheer [:5]
print(chant)
good_chant = chant[:23] != ' ' 
print (good_chant)