# Projekt przepisy -> lista zakupów

## notatki

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
