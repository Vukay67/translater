from django.shortcuts import render
from deep_translator import GoogleTranslator

def main_page(request):
    lan1 = request.GET.get('lan1')
    text = request.GET.get('tekt')
    lan2 = request.GET.get('lan2')

    result = ""

    if lan1 is not None and lan2 is not None:
        result = GoogleTranslator(source=f"{lan1}", target=f"{lan2}").translate(f"{text}")

    context = {
        "result": result
    }
    return render(request, "index.html", context)