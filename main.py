import DrawingTools.Drawing  as DT
import Strategies.TestStrategy as TS



if __name__ == '__main__' :
  ts = TS.TestStrategy()
  d = DT.Drawing(ts)
  d.draw()
