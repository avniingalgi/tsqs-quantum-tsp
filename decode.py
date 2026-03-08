#this is the code which converts the measurement 000110 etc to city tours like 
 #0-1-2 the code converts the binary number in two blocks like 00 01 10 and then 
#compares it to the city representation --HOBO encoding


import math

def decode_tour(bitstring, n):

    k = math.ceil(math.log2(n))   # number of qubits per city

    tour = []

    for i in range(0, len(bitstring), k):
        city_bits = bitstring[i:i+k]
        city = int(city_bits, 2)
        tour.append(city)

    return tour