#!/usr/bin/env python3

"""
__author__ = 'Norman Cheng'
__pkuid__  = '1700011727'
__email__  = '1700011727@pku.edu.cn'
"""

def get_information(currency_from, currency_to, amount_from):
    """get necessary information according to given instructions"""
    from urllib.request import urlopen
    url='http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+currency_from+'&to='+currency_to+'&amt='+amount_from
    doc = urlopen(url)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return url

def simplify(jstr):
    """simplify the string received"""
    for ch in jstr:
        if ch in ',:"{}':
            jstr = jstr.replace(ch,'')
        else:
            pass
    jstr = jstr.split()
    return jstr

def extract(jstr):
    """locate and extract the informatin needed"""
    for i in range(len(jstr)):
        if jstr[i] == 'to':
            position = i+1
        else:
            pass
    currency_get = jstr[position]
    return currency_get

def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""

    from urllib.request import urlopen
    url='http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+currency_from+'&to='+currency_to+'&amt='+amount_from
    doc = urlopen(url)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii') #get necessary information
    
    for ch in jstr:
        if ch in ',:"{}':
            jstr = jstr.replace(ch,'')
        else:
            pass
    jstr = jstr.split() #make the information easy to handle
    
    for i in range(len(jstr)):
        if jstr[i] == 'to':
            position = i+1
        else:
            pass
    currency_get = jstr[position] #locate and extract the informatin needed
    
    return currency_get #return the information needed
    
def main():
    """This is the main module"""
    a = input('Currency from?')
    b = input('Currency to?')
    c = input('the amount of currency from?')
    print(exchange(a,b,c))
    
def test_get_information():
    """Test the information asking function"""
    a = get_information('USD','EUR','2.5')
    assert(a == 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=EUR&amt=2.5')

def test_simplify():
    """Test the simplify procedure"""
    a = simplify('{ "from" : "2.5 United States Dollars", "to" : "2.24075 Euros", "success" : true, "error" : "" }')
    assert(a == ['from','2.5','United','States','Dollars','to','2.24075','Euros','success','true','error'])

def test_extract():
    """Test the information extraction function"""
    a = extract(['from','2.5','United','States','Dollars','to','2.24075','Euros','success','true','error'])
    assert(a == '2.24075')
    
def testAll():
    """Test all cases"""
    test_get_information()
    test_simplify()
    test_extract()
    print("All tests passed")
    
if __name__ == '__main__':
    testAll()
    main()
