# Подключаем TestClient - клиент для тестирования API из FastAPI.
from fastapi.testclient import TestClient
from main import app

# Создается клиент для тестирования, которому при создании передается объект API app,
# тестирование которого необходимо выполнить.
client = TestClient(app)


# Тестирование кода ответа.
def test_status_code_question_answerer():
    response = client.get('/')
    assert response.status_code == 200


# Тестирование приветственного сообщения.
def test_welcome_question_answerer():
    response = client.get('/')
    assert response.json() == {'ПРИВЕТСТВИЕ': 'ПРАКТИЧЕСКОЕ ЗАДАНИЕ №3 ПО ДИСЦИПЛИНЕ \"ПРОГРАММНАЯ ИНЖЕНЕРИЯ\"'
                                              'УРАЛЬСКОГО ФЕДЕРАЛЬНОГО УНИВЕРСИТЕТА'}


# Тестирование работы модели.
def test_age_question_answerer1():
    '''
    Данное приложение осуществляет поиск ответа на вопрос в заданном тексте.
    В качестве тестового текста отправляем предложение "Мне 31 год.". Соответственно
    правильный ответ на вопрос "Сколько мне лет?" должен быть "31".
    '''
    response = client.post('/predict/',
                           json={"context_question": ["I am 31 years old.", "How old am I?"]})
    json_data = response.json()

    assert json_data['ANSWER'] == '31'

def test_age_question_answerer2():
    '''
    Данное приложение осуществляет поиск ответа на вопрос в заданном тексте.
    В качестве тестового текста отправляем предложение "Мне 31 год.". Соответственно
    правильный ответ на вопрос "Сколько мне лет?" должен быть "31".
    '''
    response = client.post('/predict/',
                           json={"context_question": ["My name is Maxim.", "What is my name?"]})
    json_data = response.json()

    assert json_data['ANSWER'] == 'Maxim'
    
