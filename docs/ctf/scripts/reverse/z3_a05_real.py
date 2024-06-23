from z3 import RealVal, RatVal

RealVal(1)
# 1
RealVal(1).sort()
# Real
RealVal("3/5")
# 3 / 5
RealVal("1.5")
# 3 / 2


RatVal(3, 5)
# 3 / 5
RatVal(3, 5).sort()
# Real
