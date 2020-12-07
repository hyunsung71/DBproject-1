import datetime
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import render
from . import forms
from .models import BookedDay


# class ReservationView(FormView):
#     template_name = "reservations/reservation.html"
#     form_class = forms.ReservationForm


def search(request):
    form = forms.ReservationForm(request.GET)
    result = []
    if form.is_valid():
        start = form.cleaned_data.get("Start_Date")
        end = form.cleaned_data.get("End_Date")
        difference = end - start
        result = []
        for i in range(2):
            for date in range(difference.days + 1):
                obj = BookedDay.objects.all().filter(
                    day=start + datetime.timedelta(days=date), roomtype=i + 1
                )
                if obj.exists():
                    if obj.get().count >= 5:
                        break
                    if date == difference.days:
                        result.append(obj.get().roomtype)
                else:
                    if i == 0:
                        result.append("Deluxe")
                        result = list(set(result))
                    if i == 1:
                        result.append("Business")
                        result = list(set(result))
    else:
        form = forms.ReservationForm()

    return render(
        request, "reservations/reservation.html", {"form": form, "result": result}
    )


class Reservate(FormView):
    template_name = "reservations/reservate.html"
    form_class = forms.Reservate
    success_url = reverse_lazy("reservations:reservate")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)