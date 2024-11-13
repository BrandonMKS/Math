def calculate(x1, x2, coefficients) :
    j = len(coefficients)
    sum1 = 0
    sum2 = 0
    for k in range(j) :
        sum1 += ((coefficients[k])/(j-k)) * (x1 ** (j-k))

        sum2 += ((coefficients[k])/(j-k)) * (x2 ** (j-k))
        print(sum2)
    final = sum2- sum1
    return final
def input_coefficients() :
    answer = int(input("What is the degree of the polynomial?: "))
    coefficients = []
    for k in range((answer+1)) :
        coefficient = int(input (f"what is coefficient for x^{answer-k}? "))
        coefficients.append(coefficient)
    return coefficients
def main():
    print('This program finds the definite integral of a given expression from x1 to x2')
    coefficients = input_coefficients()
    x1 = int(input('What is the starting x value for the integral? :'))
    x2 = int(input('What is the ending x value for the integral? :'))
    answer = calculate(x1, x2, coefficients)
    print (f"The definite value of the equation is {answer}")
    return 0
main()
