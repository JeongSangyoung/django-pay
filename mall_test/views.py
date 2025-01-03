from django.shortcuts import render, redirect, get_object_or_404
from mall_test.forms import PaymentForm
from mall_test.models import Payment

# Create your views here.
def payment_new(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save()
            return redirect("payment_pay", pk=payment.pk)
    else:
        form = PaymentForm()

    return render(request, 'mall_test/payment_form.html', {
        'form': form,
    })

def payment_pay(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    return render(request, 
        'mall_test/payment_pay.html',
        {
            'payment': payment,
        }    
    )