dividend = 1
divisor = 2

intdiv = dividend//divisor
float_div = dividend/divisor

if intdiv>float_div:
    diff = intdiv-float_div
else:
    diff = float_div-intdiv

if diff >= 0.5:
    intdiv += 1

print(intdiv)
