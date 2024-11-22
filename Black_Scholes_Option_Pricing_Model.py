import math
from scipy.stats import norm

def Black_Scholes_Formula():
    #VARIABLES
    print("BLACK-SCHOLES OPTION PRICING MODEL CALCULATION")
    print("Input only valid numbers as values for variables. ")
    S = float(input("What is the underlying price?: ")) # underlying price
    T = float(input("What is the time to experiation?: ")) # time to experiation
    K = float(input("What is the strike price?: "))  # strike price
    R = float(input("What is the risk-free rate?: ")) # risk-free rate
    sigma = float(input("What is the volatility?: ")) # volatility (σ)

    #MAIN FORMULA CALCULATIONS
    d1 = (math.log(S/K) + (R + 0.5 * sigma**2)*T ) / (sigma * math.sqrt(T))
    d2 = d1 - (sigma * math.sqrt(T))
    call_option = S * norm.cdf(d1) - K * math.exp(-R * T) * norm.cdf(d2)
    put_option = K * math.exp(-R * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

    #FORMULA OUTPUT
    print("The price of the call option is: $", round(call_option, 2))
    print("The price of the put option is: $", round(put_option, 2))
    redo = input("Redo: Yes or No ").lower()

    #REDO LOGIC
    if redo == "yes":
        Black_Scholes_Formula()

Black_Scholes_Formula()