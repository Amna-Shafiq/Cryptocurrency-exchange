from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Sum, Count, Q

class User(AbstractUser):
    country = models.CharField(max_length=50)
    def __str__(self):
        return self.username

class Transaction(models.Model):
    quote_currency = models.CharField(max_length=10)
    usd_amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quote_currency} {self.usd_amount} for user {self.user.username}"

def get_top_spending_customers(limit=3):
  results = Transaction.objects.values('user__email', 'user__country') \
                             .annotate(total_spent=Sum('usd_amount')) \
                             .order_by('-total_spent')[:limit]
  return list(results)

def get_user_count_by_spending_range(min_amount=1000, max_amount=2000):
    return Transaction.objects.filter(
        total_spent__gt=min_amount,
        total_spent__lt=max_amount
    ).values('user_id').distinct().count()

def get_countries_with_low_avg_spending(threshold=500):
  results = Transaction.objects.values('user__country') \
                             .annotate(avg_spent=Avg('usd_amount')) \
                             .filter(avg_spent__lt=threshold)
  return list(results.values_list('user__country', flat=True))