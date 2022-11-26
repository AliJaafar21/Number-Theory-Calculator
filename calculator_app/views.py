from django.shortcuts import render
from utilities.PrimeFactorization import PrimeFactorization


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
