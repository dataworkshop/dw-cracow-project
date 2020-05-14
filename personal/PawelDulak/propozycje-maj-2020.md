## Drzewostan
Autor: Rafał

Odczytywanie informacji na temat ilości wyciętych i nasadzonych drzew w Krakowie - gdzie, ile, dlaczego. Nanoszenie informacji na mapę? Przykładowy plik z informacją o zmianach w drzewostanie: https://www.bip.krakow.pl/?dok_id=69229.

Jest kilka możliwych kierunków i problemów do zaadresowania:

* jak odczytać dane z plików PDF które mają nie do końca ustaloną strukturę? Jest wiele podobnych ale zdarzają się trudne do doczytania. To zagadnienie z pogranicza NLP i algorytmiki
* jak zmiana w zadrzewieniu wpływa na temperatury? Tutaj problemem jest brak łatwo dostępnych danych. 

## Nauka prostej gry
Autor: Rafał

Nauczenie komputera gry w prostą grę (np. kółko i krzyżyk) w taki sposób że początkowo komputer __zupełnie nie zna zasad__. Dostaje tylko informację o ewentualnych błędach i wynikach jego działań (stan planszy, wygrana, przegrana, remis). Chodzi zatem o to żeby nasz program "sam" nauczył się zasad gry oraz optymalnej rozgrywki. Można zacząć od bardzo prostej gry typu "kółko i krzyżyk" tym bardziej że istnieją już gotowe rozwiązania które możemy podpatrzyć. W kolejnych krokach można wprowadzić bardziej skomplikowane wersje gry lub inną grę - kiedy już będziemy wiedzieć co robimy i jak :) 

To jest projekt który ma służyć głównie naszej nauce ML i rozwiązywania problemów.

## Rankingi
Autor: Vainamonen 

Ranking "cząsteczek" (uprzedzam abstrakcja):

* zrobienie lepszego rankingu FIFA, szachowego itp., 
* cząsteczki (drużyny, zawodnicy) mogą poruszać się dowolnie po osi liczbowej od 0 do 1 (umowne), na cząstkę poniżej 0  i powyżej 1 działa nieskończona siła spychająca z powrotem w dozwolony zakres, 
* jeśli 2 cząsteczki zremisowały ze sobą to przykładamy do nich siły przyciągające, 
* jeśli jedna cząstka wygrała to przykładamy siłę skierowaną ku 1, przegranemu taką samą w stronę 0, czym wyższy wynik tym większa siła, 
* można pomyśleć nad coraz mniejszą i zanikającą wagą dla starszych wydarzeń lub poprzednich dla danej pary, 
* po przyłożeniu wszystkich sił do wszystkich obiektów szukamy takiego rozmieszczenia układu, dla którego osiągniemy stan równowagi.

## Sondażowy podział administracyjny Polski
Autor: Vainamonen 

Na podstawie sond i ankiet pytamy mieszkańców wszystkich powiatów (może nawet gmin) o to pod jakie miasto wojewódzkie chcieliby podlegać - dla uproszczenia do wyboru na początek te powyżej 100k mieszkańców (w sumie 38, ewentualnie powyżej 50k dochodzi kolejne 46) ankietowani mogą głosować na podstawie dowolnych kryteriów - historycznie, biorąc pod uwagę sympatie i antypatie, łatwość dojazdu, dostępność pracy itd. każdy z listy sugerowanych (posortowane od najbliższych na podstawie kodu pocztowego zamieszkania) układa preferencje z np. 10 najbliższych, próbujemy podzielić Polskę na województwa tak, aby zadowolić jak najwięcej osób.

## Prognozy dla pszczelarzy
Autor: Ala S. 

Na podstawie historycznych prognoz dla alergików  stworzyć prognozowanie obszarów i czasu pylenia rożnych roślin dla.... pszczelarzy

## AI-driven regular expression
Autor: Albert 

Zrobienie AI regular expression - przyszedł na podstawie tego pytania https://dataworkshopclub.slack.com/archives/CCCTN4PV1/p1589279772066400
Potrzebuję z dosyć randomowych stringów wydobyć konkretne dane: Duża litera + dowolne znaki, ale jeżeli jest więcej takich kombinacji to chciałbym, żeby wszystkie zostały wychwycone np.
1. wejście: 'ACTHighline' ---> 'Highline'
2. wejście: 'CGIBlueEffClassic' ------> 'BlueEffClassic'
3. wejście: 'dAMGLineG' --------> 'Line'
4. wejście: 'MaticElegance' -----------> 'MaticElegance'

Możliwe co najmniej dwa podejścia: 

1. Budujemy system który będzie tworzył Regular Expression na podstawie podanych przykładów (czyli dostajemy regex który można użyć w jakimś programie)
2. Budujemy system który robi to, co robiłby regex w takim wypadku. Uczy się na przykładach, jaki wynik ma dawać i daje taki wynik dla kolejnych przykładów.

## Odczytywanie wyników strzelań z tarcz strzeleckich
Autor: Dulare 

Na podstawie zdjęcia tarczy, odczytywanie jaki jest wynik strzelania (ile punktów zdobył strzelec). Głównie chodzi zatem o analizę obrazu. Można zacząć od prostych tarcz (jeden typ tarczy, jeden kaliber) i stopniowo utrudniać zadanie. Chodzi tutaj nie tylko o wykrywanie gdzie strzelec trafił, ale też gdzie są poszczególne pierścienie (wartości punktowe) na tarczy - krzywo zrobione zdjęcie tarczy mogłoby być prostowane, dopiero wtedy poddawane analizie. 

## Kategoryzacja wydatków
Kategoryzacja wydatków w kategoriach zdefiniowanych przez użytkownika, na przykład: Spożywcze, Chemia, Opłaty, itd. coś co dałoby się podłączyć do zbioru danych o moich wydatkach. Wnioskowanie na podstawie na przykład opisu, kwoty, daty (okresu w miesiącu). Spodziewam się że nie jest to bardzo trudny temat, ale problem ze zdobyciem polskich danych - niewiele osób zechce ujawnić wydatki wraz z ich kategoryzacją :)
