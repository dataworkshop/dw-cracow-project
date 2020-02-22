# Projekt przepisy -> lista zakupów

## notatki 2020-02-19

1. Pobieranie danych -> użytkownik może dodać przepisy chodząc po stronach internetowych i używając pluginu (plugin należy napisać)
   
   a. czy jest możliwość od razu w pluginie pokazać gdzie jest przepis na stronie?

   b. podawanie na ile osób chcemy gotować?

   c. podawanie na ile osób jest ten konkretny przepis?

   d. plugin komunikuje się z serwerem na którym następuje dalsza obróbka danych

   e. co ze stronami których nie obsługujemy? "Powiadom mnie kiedy będzie wsparcie dla tej strony"?

2. Scrapowanie składników z przepisów -> mamy niektóre strony z których możemy szybko pobrać składniki oraz sporo stron z których składniki jest trudniej pobrać (nie są jednoznacznie wydzielone). Potrzebujemy scrapery do różnych stron. 

   a. co otrzymujemy w wyniku scrapowania: lista składników, składnik i ilość

   b. Mamy gotowy scrapper do "przepisy.pl"

   c. Przydał by się silnik do entity recognition w przepisach w których nie mamy dostępu do listy składników

3. Grupowanie składników na listę zakupów -> rozpoznawanie podobnych składników, odrzucanie nieistotnych informacji
   
   a. potrzebujemy silnik do grupowania składników 

   b. w przyszłości, poza grupowaniem składników przydało by się jeszcze sumowanie ilości oraz przeliczanie ilości kiedy przepis jest na inną ilość osób a gotujemy na inną ilość.

4. Gotową listę przekazujemy do pluginu do wyświetlenia w przeglądarce

---

Podział pracy:

* Filip -> backend, plugin FF
* Mikołaj -> scraping Lidl
* Paweł -> plugin Chrome

## notatki 2020-01-22

* zobaczyć jakie mamy dane
* jakie mamy biblioteki do mierzenia podobieństwa ciągów znaków? Jak działają?
* czy możemy wyodrębnić grupy produktów?
* czy są słowa które można by usuwać z nazw produktów zanim je będziemy porównywać?
* czy warto grupować po informacji "w puszce" ze względu na lokalizację w sklepie?

## notatki 2020-01-08

* strona: przepisy.pl - przepisy w formie łatwiejszej do scrapowania

* Zbieranie danych
  * Scrapping danych
    * Gramatura w powiązaniu z produktem
      * różne sposoby podania gramatury, ilości
      * kiedy mamy podane produkty to nie zawsze wiadomo co jest gramaturą a co jest produktem, a co jest komentarzem do produktu
      * czasem jest podany składnik bez ilości (a w przepisie: możesz posypać ...)
    * Narządzia i naczynia które możemy potrzebować
    * Dla jakiej ilości osób jest przepis
    * Składniki czasem są wypisane osobno a czasem trzeba je wyciągnąć z przepisu jako takiego
      * można zacząć od stron na których dane są w odpowiedni sposób ustrukturyzowane
    * kwestia łączenia różnych opisów tych samych produktów
      * sztuki, gramy, szklanki, łyżki itd
    * produkt jeden albo drugi - limonki albo cytryny

* Konsolidacja produktów 
  * Jak wykrywamy że produkty to te same rzeczy?

* Inne pomysły 
  * dobieranie przepisów pod kątem tego co już posiadamy albo czego opakowanie napoczęliśmy i trzeba zużyć
  * czy możemy uzgodnić jeden format danych dla gramatury produktów?
  * Lista produktów -> dostępna na frisco.pl
  * Biblioteka do porównywania tekstów może pomóc w przypisaniu produktów z przepisów do produktów z listy frisco.pl
  * Czy możemy użyć word2vec? 
  * na repozytorium - scrapper do konkretnych stron -> linki wrzucić na slack


1) Jakikolwiek scrapper do przepisów -> konkretna lista produktów w formie jak jest na stronie z przepisem
2) Przeskalowanie ilości na ilość osób która nas interesuje
3) Konsolidacja produtków z różnych przepisów w jedną listę - wychwytywanie zależności między tym co wyciągnęliśmy z przepisów a tym co mamy w sklepie frisco.pl

## plan pracy do kolejnego spotkania:
- pobieranie produktów ze stron: przepisy.pl, kuchnialidla.pl, 
- zapisujemy do CSV - trzy kolumny - URL, produkt, gramatura (ilość)
