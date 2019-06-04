from machine import Timer


tim = Timer(0)
tim2 = Timer(1)
tim.init(period=5000, mode=Timer.ONE_SHOT, callback=lambda t: print(1))
tim2.init(period=2000, mode=Timer.PERIODIC, callback=lambda t: print(2))
