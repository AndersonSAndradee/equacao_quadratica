import math

def imcompletasC(ax, bx):#calcúla as imcopletas de C

    valor_x2 = -bx / ax
    
    print('A equação quadratica tendo o valor de C \nigual a 0, tem o valores respectivos para  \nprimeira ne segunda raiz de:', 0,"e","{:.2f}".format(valor_x2))




def imcompletasB(ax, c):#calcúla as imcopletas de B
    
    divisao_inicial = -c / ax #divisão antes de calcular raiz qudadrada
    
    '''calcula raiz quadrada das duas raízes'''
    raiz1 = + (math.sqrt(divisao_inicial))    
    raiz2 = - (math.sqrt(divisao_inicial))
    
    print('A equação quadratica tendo o valor de B \nigual a 0, tem o valores respectivos para \nprimeira ne segunda raiz de',"{:.2f}".format(raiz1),"e","{:.2f}".format(raiz2)) 
    #saída


    
def delta(ax, bx, c):#calcula o delta

    valor_delta = pow(bx, 2) - 4 * ax * c #calculo

    return valor_delta # saída



def baskhara(ax, bx, delta_calculado): #calcúla a func de 2° gráu

    raiz_quadrada = math.sqrt(delta_calculado) #chamada de valores para calcúlo do

    if delta_calculado == 0: #se o valor do delta for igual a 0
        print("a equação quadrática tem uma raiz real de: ",
              "{:.2f}".format((-bx + raiz_quadrada)  / (2*ax) ) )

    if delta_calculado > 0: #se o valor do delta for maior que 0
        print("O valor da primeira raíz é: ",
               "{:.2f}".format((-bx + raiz_quadrada)  / (2*ax) ) )
        print("O valor da segunda raíz é: ",
               "{:.2f}".format((-bx - raiz_quadrada) / (2*ax ) ) )
    else:
        print("A equação quadrática não possui raízes reais") #caso não possua raízes

def peso_letras():

    ax = 1
    '''peso de b = 2 e peso de c = 3'''
    
    valor_final = ax

    valadicao_de_b = input("Existe um valor para bX ? se sim digite (s), se não digite (n): ".lower())
    valadicao_de_c = input("Existe um valor para C ? se sim digite (s), se não digite (n): ".lower())

    if valadicao_de_b == 's':
        valor_final = valor_final + 2
    if valadicao_de_c == "s":
        valor_final = valor_final + 3

    return valor_final

def main(): #chamda de inicio
    '''entradas de valorres ax, bx, c'''
    
    peso = peso_letras()

    if peso == 4: #validação para imcompletas de c


        valor_ax = int(input("Digite o valor de aX²: "))
        valor_c = int(input("Digite o valor de C: "))

        imcompletasB(valor_ax, valor_c)

    if peso == 3: #validação para imcompletas de c


        valor_ax = int(input("Digite o valor de aX²: "))
        valor_bx = int(input("Digite o valor de bX: "))


        imcompletasC(valor_ax, valor_bx) #calculo das raizes sem C

    if peso == 6:

        valor_ax = int(input("Digite o valor de aX²: "))
        valor_bx = int(input("Digite o valor de bX: "))
        valor_c = int(input("Digite o valor de C: "))

        delta_calculado = delta(valor_ax, valor_bx, valor_c) #chamada de valores para calculo do delta
        baskhara(valor_ax, valor_bx, delta_calculado) #chamada de valores para calculo de raízes

if __name__ == "__main__":
    main()