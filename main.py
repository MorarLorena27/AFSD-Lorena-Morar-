from pickletools import optimize

if __name__ == '__main__':
    numar1=7
    numar2=5
    if numar1>numar2:
        print("numarul unu este mai mare decat numarul2")
    elif numar1<numar2:
        print("numarul1 este mai mic decat numarul2")
    else:
        print("numarul1 este egal cu numarul2")
#verificam daca un nr este par sau impar
numar=10
if numar%2==0:
    print("nr este par")
else:
    print("nr este impar")

#verificam daca un sir de caractere este gol sau nu
sir=""
if len(sir)==0:
    print("sirul este gol")
else:
    print("sirul nu mai este glo")
#verificam daca sirul de caractere are @

#in un operator care verifica daca un element se afla intr-un sir

#"@" in sir

sir="testemail@.com"
if "@" in sir:
    print("sirul contine @")
else:
    print("sirul nu contine @")

#verificam daca sirul e palindrom
#inversul unui sir e sir[::-1]
sir="random"
if sir==sir[::-1]:
    print("sirul e palindrom")
else:
    print("sirul nu e palindrom")

#numaram daca litera a apare de nr par de ori intr-un sir

sir="AAAzi este o zi frumoasa"
numar_caractere_a=sir.count('a')
numar_caractere_A=sir.count('A')
if (numar_caractere_a+numar_caractere_A)%2==0:
    print("litera a apare de un nr par de ori")
else:
    print("litera a apare de nr impar de ori")

#structuri repetitive:for , while
#for - parcurgem un nr cunoscut de pasi
#range(start ,stop ,pas) -genereaza o secventa de nr
#start-de unde incepem
#stop-unde ne optimize
#pas-cu cat crestem

for i in range(0, 10, 1):
    print(i ,end=" ")

for i in range(0, 10, 2):
    print(i ,end=" ")

for i in range(10):
    print(i ,end=" ")

sir=" hello world"
#metoda 1

for caracter in sir:
    print(caracter)
    print("*")
print("----------")
#metoda2
#caracter=sir[0]
#caracter=sir[1]
#.....
#caracter=sir[len(sir)-1]
#0,1,2,3,.....,len(sir)-1=range(len(sir))
for i in range(len(sir)):
    print(i, sir[i])
#i e pozitia ,sir[i] e valoarea de la pozitia i
#numaram cate vocale sunt intr-un sir
sir="Azi este o zi frumoasa"
vocale="aeiouAEIOU"
numar_vocale=0
for caracter in sir:
    if caracter in vocale:
        numar_vocale=numar_vocale+1  #sau mai simplu numar_vocale+=1
print(numar_vocale)



#pe ce pozitii s afla spatiile intr-un sir de caractere
sir="Azi este o zi frumoasa"

for pozitie in range(len(sir)):
    if sir[pozitie]==" ":   #pozitie e indexul caracterului curent ,sir[pozitie].....
        print("spatiu gasit pe pozitia:",pozitie)



#afisam caracterele din sir pana intalnim un spatiu

sir="Azi e o zi frumoasa"
i=0
while sir[i] !=" ":  #cat timp valoarea de la pozitia i nu e spatiu
    print(sir[i])
    i+=1  #i=i+1




