# Projekt przepisy -> lista zakupów

## zadania na 2020-03-18

Tych którzy nie znają zbyt dobrze narzędzia Git i GitHub, zapraszam do przeglądnięcia dokumentu: https://github.com/dataworkshop/dw-cracow-project/blob/master/docs/git-notes.md

Nie jest to kompletna instrukcja, ale powinna wystarczyć na początek. **Proszę o zgłaszanie uwag do dokumentu, zauważonych niejasności, błędów.**

## Todo na 2020-03-18 i kolejne dni

1. Kto z Was jeszcze nie zainstalował rozszerzenia do Chrome, proszę zainstalować, przydaje się do dalszej pracy. Rozszerzenie jest tutaj: https://github.com/dataworkshop/dw-cracow-project/tree/master/personal/PawelDulak/recipes_shopping_list/chrome_extension Jeśli chcecie rozwijać własną wersję tego rozszerzenia, należy zrobić kopię do swojego katalgu personal, nie edytować w tym źródłowym :)
2. Kto jeszcze nie uruchomił swojego lokalnego serwera Flask, z którym "gada" rozszerzenie do Chrome, proszę uruchomić. Przykładowy serwer Flask, który potrafi scrapować z `przepisy.pl` jest tutaj: https://github.com/dataworkshop/dw-cracow-project/tree/master/personal/PawelDulak/recipes_shopping_list/recipes_server Podobnie jak z rozszerzeniem do Chrome, jeśli chcecie (a powinniście) edytować pliki serwera, zróbcie jego kopię do swojego katalogu personal.
3. Na koniec pracy zróbcie commit swoich zmian do swojego repozytorium, wypchnijcie (push) do swojego forka na GitHub, zróbcie Pull Request do głównego repozytorium projektu
   
To co powyżej to zupełne minimum żeby widzieć jaki jest stan projektu na dzisiaj. Teraz rzeczy które czekają na zrobienie:

4. Kiedy używamy pluginu co Chrome to zbieramy przepisy. Następnie serwer Flask robi scraping i wyciąga z nich składniki. Spróbujmy teraz zwrócić do pluginu listę składników. Kolejne kroki:
  * lista "jak leci" - wszystkie składniki jak zostały zescrapowane, bez podziału na przepisy z których pochodzą
  * lista "alfabetyczna" 
  * próba zgrupowania podobnych składników (np. pomidory z różnych przepisów) - można użyć jednej z funkcji badającej podobieństwa, przykład użycia w notebooku tutaj: https://github.com/dataworkshop/dw-cracow-project/blob/master/personal/PawelDulak/recipes_shopping_list/ingrediends_scraping/ingredients_analysis.ipynb
  * dane z 10 000 przepisów znajdziecie na drive: https://drive.google.com/drive/folders/1wy3yvAeSniZI8U6GZl-P_PLzVpNjyPrw?usp=sharing są tam wystawione tymczasowo, warto zatem mieć własną kopię. UWAGA - nie wrzucamy ich do repozytorium, ani własnego, ani na GitHub.
  * Każdy pomysł na lepsze zgrupowanie podobnych składników będzie cenny

5. Jeśli macie własny scrapper do którejś strony z przepisami, spróbujcie go napisać w formie "pluginu" do serwera Flask. Przykładem niech będzie prosty scraper do `przepisy.pl` tutaj: https://github.com/dataworkshop/dw-cracow-project/blob/master/personal/PawelDulak/recipes_shopping_list/recipes_server/przepisy_pl_scraping.py Przyjmuje on URL strony a zwraca listę składników. Chodzi o zbudowanie co najmniej kilku takich pluginów do różnych stron, tak żeby nasz serwer potrafił czytać przepisy z wielu źródeł.
6. Zachęcam też do poszukania tekstów na temat "entity recognition" czyli wyszukiwania w tekście encji - w naszym przypadku będą to składniki potraw oraz ich ilości. Przyda nam się to do przepisów w których składniki nie są podawane jako osobna lista. Dajcie znać co znaleźliście i jak możemy tego użyć w naszym projekcie.

Ponownie - jeśli będziecie mieli kod z nowymi rzeczami, pamiętajcie żeby zrobić commit do swojego repozytorium, wypchnąć do Git i wysłać Pull Request do głównego repozytorium projektu. W ten sposób wzbogacimy wspólne repozytorium i będziemy budować kolejne cegiełki do naszego projektu.