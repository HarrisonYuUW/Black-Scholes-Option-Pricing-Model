# Black-Scholes-Option-Pricing-Model
A simple Black-Scholes option price model calculator. A prerequisite project for my ongoing Monte Carlo simulation.

What is an option?
Options are hard to explain in just a paragraph. To put simply, an option is a contract that gives you the right, but not the obligation, to buy or sell a stock at a specific price (strike price) on or before a certain date (expiration date). For example, a stock currently costs 100 dollars. I am willing to pay $250 for a contract that states I can buy 10 units for $100 each in 6 months. Consider these two scenarios after 6 months:

The stock now sits at $200:
I can now buy 10 units for $100 as opposed to the current $200. Effectively saving me $1000-$250.

The stock now sits at $50: 
Instead of losing $500 I only have to pay the initial costs of the contract. I am not obligated to execute the contract; I am only obligated to have paid the agreed price for the contract.

This is where Black-Scholes comes into play. It creates a theoretically fair price for the cost of the option contract based on given values to variables. Black-Scholes does not work with the American market. It also is not a primary formula used by any traders today. It is a revolutionary formula often overshadowed by more sophisticated ones today.

The variables at play:
The underlying stock (S) is the price at which one can buy the stock as of this moment. 

Time (T) is the amount of time you wish to have before the option expires. This variable is to be submitted in units of years. Ex. 6 months = 0.5

A strike price (K) is the price at which you can buy the current underlying stock at only when the option expires. 

The risk-free rate (R) represents the annualized return of an investment with zero risk over the option's time to maturity. It is typically the interest rate of a government bond, as bonds are often safe bets with a consistent return rate.

The general formula for the risk-free rate in any scenario is calculated as R option = R annual ​⋅ T.

Volatility (sigma) represents the uncertainty of the asset's price. Higher uncertainty (volatility) means a greater chance of large price swings, which makes options more valuable.

Disclaimer: I am not the maker of this formula, nor do I claim to be. 
