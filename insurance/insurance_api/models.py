from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    dob = models.DateField(blank=False, null=False)

    def __str__(self):
        return '{} {} {}'.format(self.first_name, self.last_name, self.dob)

    def __repr__(self):
        return self.__str__()


class Policy(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='policies',
    )
    type = models.CharField(max_length=255, null=False, blank=False)
    premium = models.DecimalField(
        null=False, blank=False, max_digits=10, decimal_places=2
    )
    cover = models.DecimalField(
        null=False, blank=False, max_digits=10, decimal_places=2
    )

    def __str__(self):
        return '{} {} {}'.format(self.customer_id, self.type, self.premium, self.cover)
