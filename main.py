from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from threading import Thread
import os
import time
import asyncio

router = Router()
promocode = ""





def open_session(session_id, url):
    """
    Открывает отдельную сессию с указанным ID и URL.
    """
    session_dir = os.path.join(os.getcwd(), f"session_{session_id}")
    if not os.path.exists(session_dir):
        os.makedirs(session_dir)

    # Настройки для отключения изображений и уникальной сессии
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options = Options()
    chrome_options.add_argument(f"--user-data-dir={session_dir}")
    chrome_options.add_argument(f"--remote-debugging-port={9222 + session_id}")
    chrome_options.add_argument("--no-sandbox")
    #chrome_options.add_argument("--disable-dev-shm-usage")
    #chrome_options.add_argument("--disable-extensions")
    #chrome_options.add_argument("--start-maximized")
    #chrome_options.add_argument("--headless")  # Убрать, если нужен видимый браузер
    #chrome_options.add_argument("--disable-gpu")
    #chrome_options.add_experimental_option("prefs", prefs)

    try:
        # Создаем драйвер и открываем URL
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.get(url)
        

    except Exception as e:
        print(f"[Сессия {session_id}] Ошибка при создании драйвера: {e}")
          # Ожидание загрузки страницы
        
    input("Нажмите энтер чтобы продолжить")


def thread_open_sessions(url="https://betboom.ru/actions#online", session_count=7):
    """
    Открывает указанный `session_count` сессий в многопоточном режиме.
    """
    threads = []
    for session_id in range(session_count):
        t = Thread(target=open_session, args=(session_id, url))
        threads.append(t)
        t.start()
        

    # Ждем завершения всех потоков
    for t in threads:
        t.join()

if __name__ == "__main__":
    thread_open_sessions()

      












    
    




    


