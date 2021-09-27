import sympy as sp

x = sp.symbols('x')

def f(symx):
    tmp = sp.sympify(symx)
    return tmp

def fprime(symx):
    tmp = sp.diff(f(symx))
    return tmp


    

def newtons_method(): 
    print("-----USING NEWTON-RAPHSON METHOD-----")
    guess = sp.sympify(float(input("Enter an initial guess: "))) # Convert to an int immediately.
    symx = input("Input your function here: ") 
    e = float(input('Tolerable Error: '))
    N = int(input('Maximum Step: '))
    div = f(symx)/fprime(symx) 
    print('turunannya adalah')
    print(fprime(symx))
    g = sp.lambdify(x, fprime(symx))
    

    step = 1
    condition = True
    while condition:
        if g(guess) == 0.0:
            print('ERROR, Divide by zero error!  Use secant instead')
            break

        print("iterasi ke-", step, guess.evalf())
        nextGuess = guess - div.subs(x, guess)
        ea = abs((nextGuess-guess)/nextGuess)
        guess = nextGuess
        step = step + 1

        if (ea < e):
            print('\nakarnya adalah ')
            print(guess.evalf())
            break

        if (step > N):
            print('iterasi maksimum dan x terakhir adalah ')
            print(guess.evalf())    
    
    else:
        print('\nNot Convergent.')


def secant_method(): 
    x0 = sp.sympify(float(input("Enter an initial guess: ")))   # Convert to an int immediately.
    x1 = sp.sympify(float(input("Enter an initial guess: ")))
    symx = input("Input your function here: ") 
    e = float(input('Tolerable Error: '))
    N = int(input('Maximum Step: '))
    div1 = f(symx) #saat x0
    div2 = f(symx) #saat x1
    step = 1
    condition = True
    while condition:
        if f(x0) == f(x1):
            print('Divide by zero error!')
            break

        print("iterasi ke-", step, x1.evalf())
        x2 = x0 - (x1-x0)*div1.subs(x, x0)/( div2.subs(x, x1) - div1.subs(x, x0) ) 
        ea = abs((x2-x1)/x2)
        x0 = x1
        x1 = x2
        step = step + 1

        if (ea < e):
            print('\nakarnya adalah ')
            print(x2.evalf())
            break

        if (step > N):
            print('iterasi maksimum dan x terakhir adalah ')
            print(x2.evalf())   
             
    
    else:
        print('\nNot Convergent.')


 

def main():
    newtons_method()
    print("----------------------------------------------------")
    print("-----NOW USING SECANT METHOD-----")
    secant_method()
if __name__ == "__main__":
    main()
  