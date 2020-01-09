Scrapery do przepisy
=======================

Ze strony: https://github.com/dzieciou/shopping-lists

Setup
-----

.. code:: console

    conda env create --file environment.yml
    conda activate scrapers

Uruchamianie
-------------------------

.. code:: console

    cd scrapers/ingredients
    scrapy crawl kwestiasmaku -o kwestiasmaku.jl
    scrapy crawl jadlonomia -o jadlonomia.jl
    scrapy crawl kuchnialidla -o kuchnialidla.jl
