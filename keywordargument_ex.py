"""
Defining the function with keyword Argument
"""
def add_suffix(suffix = '.com'):
    return 'google' + suffix
add_suffix()
add_suffix('.co.uk')


"""
Defining the function with positional and keyword Arguments
"""
def convert_usd_to_aus(amount, rate = 0.75):
    return amount/rate
convert_usd_to_aus(100)
#converting usd to aud with aspecific exchange rate argument
convert_usd_to_aus(500, 0.78)