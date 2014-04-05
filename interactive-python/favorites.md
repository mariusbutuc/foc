## Quiz 0

### mass_in_ounces

A gram is equal to 0.035274 ounces. Assume that the variable `mass_in_ounces` has a value representing a mass in ounces. Which arithmetic expressions below using the variable `mass_in_ounces` represent the equivalent mass in grams?

Think about it mathematically, but also test these expressions in [CodeSkulptor][cs]. If you are still confused, you might check out the student tutorial [video by Kelly on unit conversions][1] in the "Concepts and Examples" page.

  * `0.035274 * mass_in_ounces`
  * `0.035274 / mass_in_ounces`
  * `mass_in_ounces / 0.035274`
  * `mass_in_ounces * 0.035274`


## Quiz 1

### the ten's digit

Given a non-negative integer `n`, which of the following expressions computes the ten's digit of `n`? For example, if `n` is 123, then we want the expression to evaluate to 2.

Think about each expression mathematically, but also try each in [CodeSkulptor][cs].

  * `(n % 10) / 10`
  * `((n - n % 10) % 100) / 10`
  * `(n // 10) % 10`


### the compound interest

When investing money, an important concept to know is _compound interest_. The equation _FV = PV (1+rate)<sup>periods</sup>_ relates the following four quantities.

 * The _present value (PV)_ of your money is how much money you have now.
 * The _future value (FV)_ of your money is how much money you will have in the future.
 * The _nominal interest rate per period (rate)_ is how much interest you earn during a particular length of time, **before** accounting for compounding. This is  * typically expressed as a percentage.
 * The _number of periods (periods)_ is how many periods in the future this calculation is for.

Finish the following code, run it, and submit the printed number. Provide at least four digits of precision after the decimal point.

```python
def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years

    # Put your code here.

print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)
```

Before submitting your answer, test your function on the following example. `future_value(500, .04, 10, 10)` should return `745.317442824`.



  [cs]: http://www.codeskulptor.org/
  [1]: http://youtu.be/Qhwnq2S0cBE 'Unit Conversions Tutorial, by Kelly Vaughan'
