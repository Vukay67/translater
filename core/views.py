from django.shortcuts import render
from deep_translator import GoogleTranslator

def main_page(request):
    lan1 = request.GET.get('lan1')
    text = request.GET.get('tekt')
    lan2 = request.GET.get('lan2')

    result = ""
    error = ""

    if text == "Мухаммед":
        result = "Красавчик"

    if lan1 is None or lan2 is None:
        error = "Ошибка: выберите исходный и целевой язык"
    elif text is None:
        error = "Ошибка: введите текст для перевода"
    else:
        try:
            result = GoogleTranslator(source=f"{lan1}", target=f"{lan2}").translate(f"{text}")
        except Exception as e:
            error = f"Ошибка перевода: {str(e)}"

    context = {
        "result": result,
        "error": error
    }
    return render(request, "index.html", context)