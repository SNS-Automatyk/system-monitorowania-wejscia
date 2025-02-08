# System Monitorowania Wejścia
System monitorowania wejść do warsztatu

## Wymagania
- Python 3.x
- Django 3.x
- Django-Tailwind

## Instalacja
1. Sklonuj repozytorium:
    ```bash
    git clone https://github.com/twoje-repozytorium/system-monitorowania-wejscia.git
    cd system-monitorowania-wejscia
    ```

2. Utwórz i aktywuj wirtualne środowisko:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Na Windows: venv\Scripts\activate
    ```

3. Zainstaluj wymagane pakiety:
    ```bash
    pip install -r requirements.txt
    ```

4. Skonfiguruj Django-Tailwind:
    ```bash
    python manage.py tailwind install
    ```

5. Wykonaj migracje bazy danych:
    ```bash
    python manage.py migrate
    ```

6. Uruchom serwer deweloperski:
    ```bash
    python manage.py runserver
    ```

## Użycie
Aby uzyskać dostęp do aplikacji, otwórz przeglądarkę i przejdź do `http://127.0.0.1:8000`.
