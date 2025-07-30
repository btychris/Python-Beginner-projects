# Endurance Expedition - www.101computing.net/endurance-shipwreck-search-expedition
import turtle
from submarine import Submarine

auv = Submarine()

# Starting scan of the search area...
auv.scan()
for i in range(5):
    auv.move(1)
    auv.scan()

auv.point("south")
auv.move(1)
auv.point("west")

# Complete the code here to cover the entire search area...
