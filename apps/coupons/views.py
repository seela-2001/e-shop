# In your coupons/views.py
from django.shortcuts import redirect
from .forms import CouponApplyForm
from .models import Coupon
from django.utils import timezone

def coupon_apply(request):
    now = timezone.now()
    form = CouponApplyForm(request.POST)
    
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.filter(
                                        code__iexact=form.cleaned_data['code'],
                                        valid_from__lte=timezone.now(),
                                        valid_to__gte=timezone.now(),
                                        active=True  # Correct field
                                    ).first()

            request.session['coupon_id'] = coupon.id
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
    return redirect('cart:cart_detail')
