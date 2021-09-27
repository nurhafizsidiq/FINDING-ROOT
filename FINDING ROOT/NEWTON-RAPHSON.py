import sympy as sp

x = sp.symbols('x')

def f(symx):
    tmp = sp.sympify(symx)
    return tmp

def fprime(symx):
    tmp = sp.diff(f(symx))
    return tmp


    

def newtons_method(): 
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
            print('Divide by zero error!')
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


 

def main():
    newtons_method()
if __name__ == "__main__":
    main()
  