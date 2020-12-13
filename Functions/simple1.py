def func(message, name):
    result = f"{message}, {name}"
    print(result)

func('Hello', 'Reybey')
func('Reybey', 'Hello')
func(name='Reybey', message='Hello')