

def input_yes_no(text: str):
    question = input(text).strip().lower()

    return True if "y" in question else False


def ask_questions():
    poetry = input_yes_no('Do You want to use Poetry as dependency manager? [yN] ')

    postgres = input_yes_no('Do You want to use dockerized PostgreSQL as Your Database? [yN] ')

    celery = input_yes_no('Do You want to use dockerized Celery with Redis for Asynchronous tasks? [yN] ')

    jwt = input_yes_no('Do You want to use JWT Authentication provided by "dj_rest_auth" package? [yN] ')
    if jwt:
      registration = input_yes_no('Do You want to use registration provided by "dj_rest_auth" package? [yN] ')
    else:
      registration = False

    swagger = input_yes_no('Do You want to use swagger as API Documentation? [yN] ')

    backend_folder = input_yes_no('Do You want rename outer Django folder to "backend"?  [yN] ')

    project_name = input('How do You want to name the project? ').strip().lower()

    return dict(
        poetry=poetry,
        postgres=postgres,
        celery=celery,
        jwt=jwt,
        registration=registration,
        swagger=swagger,
        backend_folder=backend_folder,
        project_name=project_name
    )


def print_progress(iteration, total, current_task, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)

    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    #print(f'\rSetting up {current_task}...', end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


def insert_text_at_line(filename: str, line_number: int, text: str):
    with open(filename, 'r') as file:
        lines = file.readlines()

    lines.insert(line_number - 1, text + '\n')

    with open(filename, 'w') as file:
        file.writelines(lines)


def change_text_at_line(filename, line_number, text):
    with open(filename, 'r') as file:
        lines = file.readlines()

    lines[line_number - 1] = text + '\n'

    with open(filename, 'w') as file:
        file.writelines(lines)
