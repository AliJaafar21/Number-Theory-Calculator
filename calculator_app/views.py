from django.shortcuts import render
import func_timeout
from utilities.PrimeFactorization import PrimeFactorization
from utilities.ChineseRemainderTheorem import chineseRemainderTheoremScenario1, chineseRemainderTheoremScenario2
from utilities.FastExponentiation import FastExponentiation
from utilities.EulerTotientFunction import phi
from utilities.MillerRabinAlgorithm import MillerRabin

def HomePageView(request):
    return render(request, 'index.html')


def PrimeFactorizationView(request):
    if request.method == 'POST':
        number = int(request.POST.get('number'))

        try:
            result = func_timeout.func_timeout(2, PrimeFactorization, args=[number])
            return render(request, 'PrimeFactorization.html', {'number': number, 'factors': result})

        except func_timeout.FunctionTimedOut:
            return render(request, 'PrimeFactorization.html', {'error': 'Sorry, couldn\'t compute the result in time.'})
        
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

            try:
                result = func_timeout.func_timeout(2, chineseRemainderTheoremScenario1, args=[m, A])
                return render(request, 'ChineseRemainderTheorem.html',{'A': A, 'result1': result})

            except func_timeout.FunctionTimedOut:
                return render(request, 'ChineseRemainderTheorem.html', {'error': 'Sorry, couldn\'t compute the result in time.'})
        
        
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

            try:
                result = func_timeout.func_timeout(2, chineseRemainderTheoremScenario2, args=[m, a])
                if isinstance(result, str):
                    return render(request, 'ChineseRemainderTheorem.html',{'error': result})       
                return render(request, 'ChineseRemainderTheorem.html',{'result2': result})

            except func_timeout.FunctionTimedOut:
                return render(request, 'ChineseRemainderTheorem.html', {'error': 'Sorry, couldn\'t compute the result in time.'})

    return render(request, 'ChineseRemainderTheorem.html')


def FastExponentiationView(request):
    if request.method == 'POST':
        a = int(request.POST.get('a'))
        b = int(request.POST.get('b'))
        n = int(request.POST.get('n'))

        try:
            result = func_timeout.func_timeout(2, FastExponentiation, args=[a, b, n])
            return render(request, 'FastExponentiation.html', {'a': a, 'b': b, 'n': n, 'result': result})

        except func_timeout.FunctionTimedOut:
            return render(request, 'FastExponentiation.html', {'error': 'Sorry, couldn\'t compute the result in time.'})
        
    return render(request, 'FastExponentiation.html')


def MillerRabinView(request):
    if request.method == 'POST':
        n = int(request.POST.get('n'))

        try:
            result = func_timeout.func_timeout(2, MillerRabin, args=[n])
            return render(request, 'MillerRabin.html', {'n': n, 'result': result})

        except func_timeout.FunctionTimedOut:
            return render(request, 'MillerRabin.html', {'error': 'Sorry, couldn\'t compute the result in time.'})
    
    return render(request, 'MillerRabin.html')


def EulerTotientFunctionView(request):
    if request.method == 'POST':
        number = int(request.POST.get('number'))
        
        try:
            result = func_timeout.func_timeout(2, phi, args=[number])
            return render(request, 'EulerTotientFunction.html', {'number': number, 'phi': result})

        except func_timeout.FunctionTimedOut:
            return render(request, 'EulerTotientFunction.html', {'error': 'Sorry, couldn\'t compute the result in time.'})

    return render(request, 'EulerTotientFunction.html')
