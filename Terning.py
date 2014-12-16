import random
import webbrowser

num = random.randrange(0, 6)

if num == 0:
    webbrowser.open('http://healthyfastfood.biz/wp-content/uploads/2014/10/dice-1.gif')
elif num == 1:
    webbrowser.open('http://i363.photobucket.com/albums/oo79/fizzgig2k4/dice%20face%20images/lego2dice-1-2.jpg')
elif num == 2:
    webbrowser.open('http://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Dice-3-b.svg/1024px-Dice-3-b.svg.png')

elif num == 3:
    webbrowser.open('http://dobbelsteen.virtuworld.net/img/4c.gif')
elif num == 4:
    webbrowser.open('http://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Dice-5-b.svg/557px-Dice-5-b.svg.png')
elif num == 5:
    webbrowser.open('http://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Dice-6-b.svg/557px-Dice-6-b.svg.png')
else:
    print "Noget gik galt"

