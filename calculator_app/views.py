from django.shortcuts import render
from utilities.PrimeFactorization import PrimeFactorization
from utilities.ChineseRemainderTheorem import chineseRemainderTheoremScenario1, chineseRemainderTheoremScenario2
from utilities.FastExponentiation import FastExponentiation
from utilities.EulerTotientFunction import phi

def HomePageView(request):
    return render(request, 'index.html')


def PrimeFactorizationView(request):
    if request.method == 'POST':
        number = request.POST.get('number')

        if number == "":
            return render(request, 'PrimeFactorization.html')

        number = int(number)
        factors = PrimeFactorization(number)
        return render(request, 'PrimeFactorization.html', {'number': number, 'factors': factors})

    return render(request, 'PrimeFactorization.html')


def ChineseRemainderTheoremView(request):
    if request.method == 'POST':

        if (request.POST.get('btn1') is not None):
            A = request.POST.get('A')
            misList1 = request.POST.get('misList1')

            A = int(A)
            m = misList1.split(",")
            if (m[len(m)-1] == ""):
                m.pop()
            m = [int(e) for e in m]

            result = chineseRemainderTheoremScenario1(m,A)

            return render(request, 'ChineseRemainderTheorem.html',{'A': A, 'result1': result})
        
        if (request.POST.get('btn2') is not None):
            a = request.POST.get('aisList')
            misList2 = request.POST.get('misList2')

            a = a.split(",")
            if (a[len(a)-1] == ""):
                a.pop()
            a = [int(e) for e in a]
            
            m = misList2.split(",")
            if (m[len(m)-1] == ""):
                m.pop()
            m = [int(e) for e in m]

            result = chineseRemainderTheoremScenario2(m,a)
            
            if isinstance(result, str):
                return render(request, 'ChineseRemainderTheorem.html',{'error': result})       

            return render(request, 'ChineseRemainderTheorem.html',{'result2': result})

    return render(request, 'ChineseRemainderTheorem.html')


def FastExponentiationView(request):

    if request.method == 'POST':
        a = int(request.POST.get('a'))
        b = int(request.POST.get('b'))
        n = int(request.POST.get('n'))
        result = FastExponentiation(a, b, n)
        return render(request, 'FastExponentiation.html', {'a': a, 'b': b, 'n': n, 'result': result})

    return render(request, 'FastExponentiation.html')


def EulerTotientFunctionView(request):
    if request.method == 'POST':
        number = request.POST.get('number')

        number = int(number)
        result = phi(number)
        return render(request, 'EulerTotientFunction.html', {'number': number, 'phi': result})

    return render(request, 'EulerTotientFunction.html')