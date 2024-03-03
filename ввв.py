def get_user_input(prompt):
    """
    Эта функция запрашивает ввод у пользователя и возвращает введенные данные.

    Args:
    prompt (str): Строка с вопросом или приглашением к вводу.

    Returns:
    str: Введенные пользователем данные.
    """
    user_input = input(prompt)
    return user_input

def greet_user():
    """
    Функция приветствует пользователя и использует имя, введенное им в качестве ввода.
    """
    name = get_user_input("Привет! Как тебя зовут? ")
    print(f"Привет, {name}! Рад видеть тебя здесь.")

if __name__ == "__main__":
    greet_user()