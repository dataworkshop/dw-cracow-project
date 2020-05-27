- nauka o algorytmach
- rywalizacja algorytmów
- granie w inną prostą grę (flappy birds)


## Możliwe podejścia do grania (wybór)

- strategia ruchów niezależna lub słabo zależna od stanu planszy - można rozwiązywać algorytmem genetycznym - najlepsze pokolenia krzyżujemy, dodajemy mutacje i badamy "dzieci"
- ponieważ mamy skończoną liczbę dostępnych ruchów (max 9 możliwości) - można rozpatrywać jako klasyfikację o dziewięciu klasach. Problem w tym że do nauczenia klasyfikatora, potrzebujemy danych uczących (zbioru treningowego) którego zbudowanie może być czasochłonne
- przy prostych grach o małej ilości stanów, można zbudować drzewo stanów i iść drogą która jest najbardziej obiecująca w danej sytuacji - to podejście które nie jest ML i działa bardzo dobrze, ale powoduje problemy przy większych planszach
- uczenie ze wzmocnieniem - algorytm "wzmacnia" ścieżki które prowadzą do sukcesu i "osłabia" te które prowadzą do porażki (rozrysować?)

- Kółko i krzyżyk wymagają dwóch graczy - ponieważ zatem trzeba odpowiadać na ruchy, dlaczego nie zaprząc do tego dwóch algorytmów 


## jak działa uczenie ze wzmocnieniem?

- początkowe ruchy losujemy (później odbywa się to z pewnym prawdopodobieństwem)
- przebieg gry tworzy "ścieżkę" po kolejnych stanach gry
- gra kończy się wygraną, remisem lub przegraną - gracz otrzymuje nagrodę (kiedy wygra) lub karę (większą kiedy przegra, mniejszą kiedy zremisuje)
- teraz trzeba tą nagrodę lub karę rozłożyć na kroki które zostały wybrane podczas gry (back propagation) Chodzi o to żeby każdemu odkrytemu stanowi gry przypisać "prawdopodobieństwo" z jakim prowadzi do wygrania lub przegrania gry - im wyższa wartość, tym wyższe prawdopodobieństwo wygranej. 

V(s) <-- V(s) + learning_rate * (reward - V(s))

W naszym przypadku dokładniej:

V(s) <-- V(s) + learning_rate * (decay_gamma * reward - V(s))

- Każdy z graczy nauczy sie taktyki dla swojej pozycji - inaczej gra gracz rozpoczynający, inaczej gracz który startuje jako drugi. Rozpoczynający ma większe szanse na zwycięstwo, aczkolwiek przy dwóch graczach idealnych zawsze dostajemy remis.

--------

Wykresy nauki?
Czy decay gamma wpływa?
jakie mamy parametry:
- learning rate
- exploration rate (jak dużo losować)
- decay gamma
- ilość rund

W sieciach neuronowych często kumulujemy nagrodę zanim zrobimy backpropagation

------------

Propozycje:
- każdy szuka swojego rozwiązania TicTacToe, stara się go zrozumieć i wytłumaczyć innym jak działa
- konstruujemy gry które można "rozgrywać" za pomocą algorytmu (ekipa konstruktorów) i gramy w nie (ekipa trenująca)

