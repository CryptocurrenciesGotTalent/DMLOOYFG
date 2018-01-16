import DrawingTools.Drawing  as DT
import Strategies.TestStrategy as TS
import Strategies.GainsByMarketShareStrategy as GM



if __name__ == '__main__' :
  gm = GM.GainsByMarketShareStrategy("10/04/2017", 1)
  d = DT.Drawing(gm)
  d.draw()
