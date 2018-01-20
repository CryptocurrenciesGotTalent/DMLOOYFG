import DrawingTools.Drawing  as DT
import Strategies.TestStrategy as TS
import Strategies.PriceGainsByMarketShareStrategy as GM


if __name__ == '__main__' :
  ts = TS.TestStrategy()
  # gm = GM.GainsByMarketShareStrategy("23/01/2017", "01/02/2017", 1, 1)
  gm = GM.PriceGainsByMarketShareStrategy("23/01/2017", "01/02/2017", 1, 1)
  d = DT.Drawing(gm)
  d.draw()