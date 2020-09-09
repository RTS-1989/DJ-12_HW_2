from collections import Counter

from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    from_landing_conversion = request.GET.get('from-landing')
    if from_landing_conversion == 'original':
        counter_click['original'] += 1
    elif from_landing_conversion == 'test':
        counter_click['test'] += 1
    return render_to_response('index.html')

def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    name = request.GET.get('ab-test-arg')
    if name == 'original':
        counter_show['original'] += 1
        return render_to_response('landing.html')
    elif name == 'test':
        counter_show['test'] += 1
        return render_to_response('landing_alternate.html')

def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:
    try:
        original_conversion = round((counter_click['original'] / counter_show['original']), 1)
    except ZeroDivisionError:
        original_conversion = 0
    try:
        test_conversion = round((counter_click['test'] / counter_show['test']), 1)
    except ZeroDivisionError:
        test_conversion = 0
    return render_to_response('stats.html', context={
        'test_conversion': test_conversion,
        'original_conversion': original_conversion,
    })

