# CodeWars - Is he gonna survive?
# A hero is on his way to the castle to complete his mission. However, he's been
# told that the castle is surrounded with a couple of powerful dragons! each dragon
# takes 2 bullets to be defeated, our hero has no idea how many bullets he should
# carry.. Assuming he's gonna grab a specific given number of bullets and move
# forward to fight another specific given number of dragons, will he survive?

def hero(number_bullets, number_dragons):

    survive = bullets >= dragons * 2

    return survive


bullets = int(input('Enter number of bullets: '))
dragons = int(input('Enter number of dragons: '))

if hero(bullets, dragons):
    print('Hero survived the dragons. :)')
else:
    print('Hero did not survived the dragons. :(')
