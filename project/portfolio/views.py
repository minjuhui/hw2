from django.shortcuts import render
from .models import Portfolio

def portfolio(reqeust):
    portfolios=Portfolio.objects
    return render(reqeust, 'portfolio.html', {'portfolios':portfolios})
