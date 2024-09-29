num = int(input("digite um numero: "))
c=0
v=1
a=0

if num !=2:

        if num%2 == 0:

            print("não é")

        else:

            for c in range (num):

                for v in range(num):

                    if c*v == num:

                        a = True;

else:

    print("é primo")


if a==True:

    print('não é primo')

else:

    print("é primo")