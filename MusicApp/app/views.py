from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from .models import Musician, Album, AlbumStatistic


class MusicianForm(ModelForm):
    class Meta:
        model = Musician
        fields = ["first_name", "last_name", "instrument"]


def musician_list(request, template_name="app/musicianList.html"):
    musician = Musician.objects.all()
    data = {}
    data["musicianList"] = musician
    return render(request, template_name, data)


def musician_view(request, pk, template_name="app/musicianDetail.html"):
    musician = get_object_or_404(Musician, pk=pk)
    return render(request, template_name, {"object": musician})


def musician_create(request, template_name="app/musicianForm.html"):
    form = MusicianForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("musicianList")
    return render(request, template_name, {"form": form})


def musician_update(request, pk, template_name="app/musicianForm.html"):
    musician = get_object_or_404(Musician, pk=pk)
    form = MusicianForm(request.POST or None, instance=musician)
    if form.is_valid():
        form.save()
        return redirect("musicianList")
    return render(request, template_name, {"form": form})


def musician_delete(request, pk, template_name="app/musicianDelete.html"):
    musician = get_object_or_404(Musician, pk=pk)
    if request.method == "POST":
        musician.delete()
        return redirect("musicianList")
    return render(request, template_name, {"object": musician})
