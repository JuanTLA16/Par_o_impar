

print("----------------------------------------------------")
print("----------CUAL DE LOS 3 NUMEROS ES MAYOR------------")
print("----------------------------------------------------")



a = int(input(" Digite un valor: " ))
b = int(input(" Digite un valor: " ))
c = int(input(" Digite un valor: " ))


if(a>b):
    if(a>c):
        print("Mayor: " + str(a))
    else:
        print("Mayor: " + str(c))
else:
    if(b>c):
        print("Mayor: " + str(b))
    else:
        print("Mayor: " + str(c))


print("----------------------------------------------------")
print("--------------------RESULTADOS----------------------")
print("----------------------------------------------------")

