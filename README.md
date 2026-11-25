# Contoso Travel API

Proste API z danymi pogodowymi dla miast. Projekt szkoleniowy do kursu GitHub Foundations.

## Po co ten projekt

Na tym repozytorium ćwiczymy pracę z GitHub Copilot, skanowanie kodu i automatyczne sprawdzanie zależności. Kod jest celowo krótki, żeby dało się go objąć wzrokiem.

## Jak zacząć

1. Kliknij zielony przycisk Code, kartę Codespaces, potem Create codespace on main.
2. Poczekaj, aż środowisko się zbuduje. Biblioteki instalują się same.
3. W terminalu uruchom serwer: `uvicorn main:app --reload`
4. Otwórz kartę Ports, port 8000, ikonę globusa, a na końcu adresu dopisz `/docs`.

## Co jest w środku

| Plik | Co zawiera |
| --- | --- |
| `main.py` | cztery adresy API: lista krajów, lista miast, temperatury, przekierowanie na dokumentację |
| `cities.json` | zmyślone dane dla czterech miast w trzech krajach |
| `test_main.py` | dwa testy uruchamiane komendą `pytest -q` |

## Zespół

| Imię | Rola |
| --- | --- |
| Adele Vance | opiekun projektu |
| Megan Bowen | przeglądy kodu |

---

Firmy, osoby i dane w tym projekcie są fikcyjne. Podobieństwo do rzeczywistych jest przypadkowe.
