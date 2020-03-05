# Jak używać gita podczas pracy nad naszymi projektami

## Git to nie Github

Git to narzędzie - program do kontrolowania wersji kodu który piszemy. Git tworzy i zarządza repozytoriami kodu.
GitHub to miejsce gdzie możemy nasze repozytoria przechowywać, zarządzać nimi w bardziej ogólny sposób. 

## Pierwsze kroki

1. Załóż konto na GitHub jeśli jeszcze go nie posiadasz
2. Nasze projektowe repozytorium znajduje się na GitHub pod adresem:
https://github.com/dataworkshop/dw-cracow-project/
3. Będąc zalogowanym do GitHub możesz wejść na stronę naszego repozytorium i kliknąć `Fork` w prawym górnym rogu strony. Fork to Twoja prywatna kopia naszego repozytorium. Masz nad nim pełną władzę i możesz pracować w nim nie obawiając się że coś zepsujesz w naszym repozytorium projektowym.

## Mam już swój Fork i co dalej? (lokalne repozytorium Git)

Do pracy z narzędziem Git polecam linię poleceń (konsolę). Można używać także narzędzi wizualnych (Git GUI) czy obsługi Git wbudowanej w edytor programistyczny, ale wszystkie komendy w tym dokumencie będą się odnosić do konsoli z obsługą Git.

1. Zainstaluj Git na swoim komputerze. W Linux zazwyczaj wystarczy w konsoli wpisać: `sudo apt install git`, dla Windows można pobrać na przykład z https://git-scm.com/download/win
2. Załóż katalog w którym będziesz pracować, w tym miejscu utworzymy lokalną kopię Twojego repozytorium. Uruchom konsolę Git tak żeby pracowała w tym nowo utworzonym katalogu. 
3. Na stronie GitHub otwórz sobie swoje repozytorium, po prawej stronie ekranu znajdziesz przycisk "Clone or download". Po jego kliknięciu pojawi się małe okno z adresem repozytorium. Ten adres należy skopiować. Ważne żeby pobrać wersję HTTPS chyba że wiesz co robisz pobierając wersję SSH :) ![Clone in GitHub](images/clone-github.png)
4. W konsoli Git na swoim komputerze wykonaj komendę: `git clone [tutaj skopiowany adres]` czyli na przykład: `git clone https://github.com/kowalski/dw-cracow-project.git`. W ten sposób utworzyłeś lokalną kopię swojego repozytorium, na której będziesz pracować lokalnie.

## Codzienna praca z Git

Podczas swojej codziennej pracy z repozytorium staraj się utrzymywać swój kod w katalogu `/personal/[Twój Nick]` w ten sposób nie zrobisz bałaganu. Warto na poszczególne mniejsze projekty zakładać dodatkowe podkatalogi albo odpowiednio nazywać pliki. 

Git służy do kontroli wersji kodu który piszesz. Nie robi tego jednak automatycznie. Należy co jakiś czas wprowadzić swoje zmiany do repozytorium. Taką operację nazywa się `commit`. W jej wyniku Git zapamięta stan Twojego repozytorium, a właściwie tych plików które będziesz chciał zapamiętać. 

### Commit

Aby wykonać `commit` swoich zmian, należy najpierw wskazać Gitowi które pliki chcesz uwzględnić. Robi się to wykonując komendę: `git add [ścieżka i nazwa pliku]` czyli na przykład `git add personal/kowalski/test.py` W ten sposób przygotowaliśmy plik - nazywa się to `staging`. 

Możemy też dodawać pliki "hurtem" pisząc na przykład: `git add personal/kowalski/*.py` aby dodać wszystkie pliki z rozszerzeniem `.py`

Mając przygotowane wszystko co chcemy, wykonujemy komendę `git commit` która wprowadzi nasze zmiany do lokalnego repozytorium. Zostanie otworzony edytor w którym powinniśmy wpisać komentarz do naszych zmian. Jeśli chcemy wstawić komentarz od razu przy wykonywaniu komendy, można to zrobić pisząc: `git commit -m "Treść komentarza"`

### Ignorowanie plików

Jeśli czegoś nie chcemy zachowywać w naszym repozytorium (pliki z danymi, pliki tymczasowe, pliki z hasłami i tokenami), należy je wykluczyć za pomocą odpowiedniego wpisu w pliku `.gitignore`. Plik ten zakładamy w swoim katalogu `personal` i wpisujemy do niego nazwy plików lub katalogów które nie powinny być brane pod uwagę przez Git. Każdy wpis zajmuje osobną linijkę. Przykładowa treść pliku `.gitignore`:

```
*.tmp
tego-nie-commituj.txt
data/*
```

Powyższy plik `.gitignore` wskazuje że powinny być ignorowane wszystkie pliki z rozszerzeniem `.tmp`, plik o nazwie `tego-nie-commituj.txt` oraz cała zawartość katalogu `data`

### Wysyłanie zmian do GitHub

Warto aby Twoje zmiany do repozytorium nie pozostawały wyłącznie na Twoim komputerze. Aby wysłać je do Twojego repozytorium na GitHub, wykonaj polecenie `git push origin master` - spowoduje to "wypchnięcie" Twoich zmian do zdalnego repozytorium na GitHub.

## Wysyłanie moich zmian do głównego repozytorium projektu - Pull Request

## Pobieranie aktualnej wersji repozytorium projektu - fetch from upstream, merge

## Praca na branchach

## Materiały dodatkowe

* https://devstyle.pl/2018/10/26/5-sposobow-na-prace-z-gitem/

## Uwagi

### Instalacja Win: git-scm.com

Windows Explorer Integration -> Git Bash here
Default Text Editor -> VIM
Use Git From -> Windows Command Prompt
Terminal Emulator -> MinTTY

### Konfiguracja git

git config --global user.name "Jan Kowalski"
git config --global user.email "jan.kowalski@gmail.com"
