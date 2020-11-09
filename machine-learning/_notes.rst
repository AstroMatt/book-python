*****
Notes
*****

Program
=======

Wprowadzenie do Machine Learning
--------------------------------
#. Czym jest uczenie maszynowe?
#. Typy problemów dla Machine Learning
#. Miary jakości modelu
#. Znajdowanie najlepszego modelu
#. Dokładność i precyzja
#. Bias

Biblioteki numeryczne
---------------------
#. Podstawy NumPy
#. Podstawy Scikit-learn

Tensorflow
----------
#. Budowa i podstawy

    * Core (Python)
    * Estimators
    * Experiments
    * Keras

#. Budowa modeli podstawy

    * Feature Engineering
    * Regularyzacja
    * Embeddings

#. Optymalizacje

    * Głębokie sieci neuronowe
    * Funkcje aktywacji
    * Learning Rate
    * Dropout
    * Overfitting

#. Convolutional Neural Networks
#. Recurrent Neural Networks
#. Image recognition

Program 2
=========

Cele zajęć
----------
1. Poznanie metod selekcji zmiennych
2. Ćwiczenie przeprowadzania analiz
3. Ćwiczenie obróbki danych
4. Zrozumienie problemu niezbalansowanych klas i podstawowych metod radzenia sobie z nim
5. Poznanie kolejnych klasyfikatorów
6. Omówienie jak mają wyglądać projekty

Dzień 1
-------
1. Selekcja: regularyzacja l1, wielkość współczynników, ważność cech (drzewa) , selekcja rekursywna, metoda losowych podzbiorów, filtrowanie zmiennych. Wszystko (oprócz metody losowych podzbiorów) przerobić w ``sklearn``
2. Kolejne miary oceny klasyfikatorów: krzywa ROC i AUC
3. Kolejne klasyfikatory: LDA, QDA oraz KNN
4. Problem niezbalansowanych klas. Podejście zwykłe jako do klasyfikacji (a nie detekcja obserwacji odstających czy cos innego) - omówienie zabiegów typu, over/undersampling i innych
5. Zarówno na selekcję zmiennych jaki i niezbalansowane klasy jakieś większe zadania. Podział czasowy: pierwsza połowa dnia selekcja, druga połowa dnia niezbalansowane klasy, reszta pomiędzy tymi dwoma tematami

Dzień 2
-------
1 Łączenie klasyfikatorów - pobieżna opowiastka o różnych sposobach. Pokazać w ``sklearn`` VotingClassifier i Bagging
1. XGBoost (przed zajęciami trzeba dać uczestnikom instrukcję instalacji!)
2. Problem optymalizacji bardzo wielu parametrów na przykładzie XGBoost: optymalizacja iteracyjna po parametrach /podzbiorach parametrów, randomizowany gridsearch, schematy kombinowane, ewentualnie optymalizacja bayesowska
3. Problem braków danych - jak obsługiwać braki.
4. Zarówno na optymalizację parametrów jak i braki danych większe zadania. Podział czasowy: pierwsza połowa dnia xgboost i optymalizacja parametrów, druga: braki danych
5. W obu zagadnieniach uwzględnić jako element zadania obróbkę danych
6. Na koniec dnia (ok 30 minut) trzeba opowiedzieć o tym jak mają wyglądać projekty


Notatki
=======
.. todo::
    * Luźne notatki
    * tensorFlow
    * pyTorch
    * Julia (język programowania)
    * funkcyjne: higher order function -> przekazywanie funkcji jako argument
    * ``nltk`` - natural language toolkit
    * dodać algorytmy genetyczne
    * sklearn ma wiele datasetów, a te które mają prefix ``fetch_`` zaciągają dane z internetu bo są większe

.. todo::
    * selekcja features
    * LDA, QDA, KNN. KNN akurat jest, i go wykorzystam
    * ROC, AUC
    * niezbalansowane klasy
    * Bagging, VotingClassifier
    * XGBoost
    * braki w danych

Data Science
============
* Scientific Computing (stara nazwa Data Science)
* analiza danych
* łączenie danych z różnych źródeł

Machine Learning - uczymy konkretne modele przewidywać
Budowa danych do uczenia modelu to jest zupełnie inna sprawa.

Eksploracja danych - poszukiwania trendów:

    * metody statystyczne
    * proste statystyki opisowe (kwantyle)
    * grupowania i opisowe statystyki
    * czy masz wartości wystające (nietypowe - outlayers)
    * odchylenia standardowe (czy obserwacje są 3 razy odchylenie)
    * czy to jest rozkład
    * można liczyć kurtozę
    * można liczyć średnie itp
    * rozkład Studenta-t stosujesz do 30 próbek, a w Machine Learning zwykle masz dużo więcej
    * czy rozkład jest gausem (czy jest wielomodalnym - złożeniem dwóch lub więcej rozkładów), np. wiek - gaus dla mężczyzn i dla kobiet, będzie inny
    * gaussian mixture models (model szuka ile modeli gaussowskich jest w danych)

Badacz Danych


Trzy dziedziny Data Science
---------------------------
* Data Science (wymaga trochę programowania, ale mniej niż Engineering)
* Data Engineering (przerzucanie danych z lewa na prawo - więcej programowania)
* Statystyk (budowanie rozbudowanych modelów danych)

Różne źródła danych:

    * rozmawianie po api
    * różne formaty
    * pochodzenie

Jupyter
=======
* średnik usuwa wyświetlanie linii
* zamykanie kerneli
* instalowanie pluginów - spellchecker
* list.pop? - znak zapytania wyświetla help do obiektu
* %%timeit
* % - globalne
* %% - dla komorki
* ! uruchamianie terminala pod spodem (interoperacyjne z pythonem)

Machine Learning
================
bez nadzoru:

    * Poszukiwanie wzorców
    * najczęściej to jakiś rodzaj klastrowania
    * zmniejsza wymiarowość danych
    * wykrywanie anomalii
    * klastrowanie hierarchiczne

z nadzorem:

    * Przewidujemy trend w danych, które otrzymujemy


Musimy mieć więcej niż 50 próbek. Poniżej tej ilości można bawić się w statystykę ale nie w machine learning:

    * czy idziemy w stronę regresji czy klasyfikacji
    * czy mamy oznaczone dane czy nie (idziemy w unsupervised learning)
    * czy mamy więcej czy mniej niż 100k próbek

Pierwszy wybór jeżeli chodzi o klasyfikator to Regresja Logistyczna.

// obrazek ze slajdów z wyborem algorytmu

Są metody które mają problemy gdy mają zbyt dużo próbek.
Sieci neuronowe lubią mieć więcej próbek (dobrze z nimi działaj)

W problemach tekstowych dane są rzadkie.
w problemach numerycznych możemy mieć więcej danych.


SGD - Stochastic Gradient Descent


Not working:

    * niestabilny algorytm (może nie zbiegać)
    * nie daje jakości klasyfikacji

Klastry
-------
Definiujemy K klastrów i dzielimy przez odległość od środka klastrów
PCA - znajdywanie wektorów własnych kowariancji (z wielowymiarowych przestrzeni możemy zbudować mniej wymiarowe)
Dużo algorytmów stosuje odwracanie macierzy, a komputery mają z tym problem, dlatego warto zmniejszyć jego poziom

PCA - Twój model będzie działał lepiej, ale nie wiesz który parametr ma większy wpływ na jakość, np:

    * długość, szerokość i położenie działki zamienia w jeden wektor
    * porównuje dane według tego wektora
    * ale nie wiadomo które z długość, szerokość i położenie działki ma największy wpływ

Sieci Neuronowe
---------------
GAN - General Adversarial Network  - używa się do obrazów, dźwięków - sieć jest dobrze nauczona, gdy nie potrafi rozróżnić danych wygenerowanych od prawidłowych. Analizując tekst, wylicza prawdopodobieństwo wystąpienia kolejnych słów po sobie

Deep Learning ma niski próg wejścia, trzeba tylko uważać na czystość danych. Karmimy model, a ktoś mądrzejszy wcześniej przygotował cały mechanizm. W klasycznym uczeniu maszynowym musimy sami tworzyć model.

Jak sieć neuronowa podejmuje na samym końcu decyzję (tzw. softmax) to stosuje regresję logistyczną.

Machine Learning
----------------
Klasyfikacja jest dyskretna (mamy skończoną listę klas)
Regresja jest liniowa (mamy nieskończoną listę klas)

Regresja liniowa
----------------
* Odczytywanie wartości z wykresu dla linii wykreślonej na podstawie danych.
* Minimalna funkcja, która daje nam poprawną predykcję.
* Mało podatna na overfitting
* Podatna na underfitting
* Dobra wartość dobroci w stosunku do trudności.
* Bardzo często wykorzystywana.
* Szczególnie często wykorzystywane w systemach RTB (Realtime Bidding) czyli system aukcji dla reklam na stronach, który musi wyrobić się w 100-200ms (trzeba uwzględnić narzut sieciowy). Dla takich przypadków stosuje się regresję liniową albo logistyczną, bo decyzja musi być podjęta bardzo szybko (wykorzystanie sieci neuronowych byłoby zbyt czasochłonne).

* Przykładowy dataset: Diabetes (http://www4.stat.ncsu.edu/~boos/var.select/diabetes.html)
* Sklearn wykorzystuje tablice numpy
* Target - zmienna opisywana (y)

.. code-block:: python

    diabetes_X = diabetes.data[:, np.newaxis, 2]  # wyciągamy jako wektor kolumnowy (nie trzeba tego robić jak mamy więcej niż jedną kolumnę)

* do cech (x) sklearn oczekuje wektora kolumnowego
* ilość wierszy w wektorze (y) musi być taka sama

* Zmienna opisująca
* Zmienna opisywana

* Im R2 jest bliżej 1 tym lepiej
* wykres dla danych trenowanych

.. code-block:: python

    plt.scatter(diabetes_X_train, diabetes_y_train,  color='red')
    plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)
    plt.show()

.. code-block:: python

    plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
    plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)
    plt.show()

* Zmienne lepiej opisujące (BMI) - mocny współczynnik mówiący o modelu
* Zmienne gorzej opisujące (sex) kiepsko determinuje czy ktoś ma cukrzycę
* W zależności od zmiennej regresja działa lepiej albo gorzej
* Funkcja kosztu to nie tylko błąd średniokwadratowy ale również współczynnik wag.

Zadanie
^^^^^^^
#. Użyj więcej zmiennych do uczenia modelu; porównaj wyniki pomiaru jakości regresji.
#. Narysuj linię regresji w stosunku do innych zmiennych.
#. ★ Jakie cechy wpływają na najbardziej na wynik? Jak to sprawdzić?

.. code-block:: python

    # np.newaxis - wyciągamy jako wektor kolumnowy (nie trzeba tego robić jak mamy więcej niż jedną kolumnę)
    diabetes_X = diabetes.data[:, np.newaxis, 2]

    # Dzielimy dane na zbiory treningowy i testowy
    diabetes_X_train = diabetes_X[:-20]
    diabetes_X_test = diabetes_X[-20:]

    diabetes_y_train = diabetes.target[:-20]
    diabetes_y_test = diabetes.target[-20:]

    # Tworzymy obiekt modelu i go uczymy
    regr = linear_model.LinearRegression()

    regr.fit(diabetes_X_train, diabetes_y_train)
    diabetes_y_pred = regr.predict(diabetes_X_test)


    print('Współczynniki: \n', regr.coef_)
    print("Błąd średniokwadratowy: %.2f"
          % mean_squared_error(diabetes_y_test, diabetes_y_pred))
    print('Metryka R2 (wariancji): %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))


    plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
    plt.scatter(diabetes_X_train, diabetes_y_train,  color='red')
    plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)
    plt.show()


.. code-block:: python

    # 1, 2, 3 to są kolejne kolumny w których mamy cechy opisujące
    diabetes_X = diabetes.data[:, [1, 2, 3]]

    # Dzielimy dane na zbiory treningowy i testowy
    diabetes_X_train = diabetes_X[:-20]
    diabetes_X_test = diabetes_X[-20:]

    diabetes_y_train = diabetes.target[:-20]
    diabetes_y_test = diabetes.target[-20:]

    # Tworzymy obiekt modelu i go uczymy
    regr = linear_model.LinearRegression()

    regr.fit(diabetes_X_train, diabetes_y_train)
    diabetes_y_pred = regr.predict(diabetes_X_test)


    print('Współczynniki: \n', regr.coef_)
    print("Błąd średniokwadratowy: %.2f"
          % mean_squared_error(diabetes_y_test, diabetes_y_pred))
    print('Metryka R2 (wariancji): %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))


    # [:,2] wycinamy drugą kolumnę aby narysować wykres (bo matplotlib generuje wykresy dwuwymiarowe)
    # to spowoduje pozostawienie jedynie x i y i odrzucenie pozostałych kolumn
    plt.scatter(diabetes_X_test[:,2], diabetes_y_test,  color='black')
    plt.scatter(diabetes_X_train[:,2], diabetes_y_train,  color='red')
    plt.plot(diabetes_X_test[:,2], diabetes_y_pred, color='blue', linewidth=3)
    plt.show()
    # Wykres będzie chaotyczny,

Ciąg dalszy
^^^^^^^^^^^
* Regresję logistyczną można wykorzystać dla tzw. okien danych. Gdy wykres rośnie a później maleje, to regresja liniowa byłaby linią prostą, a tak gdy podzieli się wykres na połowę (rosnącą i malejącą) i stworzy się regresję dla przedziału.
* Można to łatwiej zrobić tworząc ``pandas.DataFrame`` i przekazując je do ``sklearn``
* Przypadek dla wielu zmiennych opisujących:

.. code-block:: python

    import pandas as pd

    dia_df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)\
        .assign(target=diabetes.target)

    # Podział zbioru na testowy i treningowy
    dia_train = dia_df.iloc[:-20, :]
    dia_test = dia_df.iloc[-20:, :]

    lr = linear_model.LinearRegression()
    lr.fit(dia_train[['age', 'sex', 'bmi']], dia_train['target'])

    dia_test = dia_test.assign(predict=lambda x: lr.predict(x[['age', 'sex', 'bmi']]))

    print('Współczynniki: \n', lr.coef_)
    print("Błąd średniokwadratowy: %.2f"
          % mean_squared_error(dia_test['target'], lr.predict(dia_test[['age', 'sex', 'bmi']])))
    print('Metryka R2 (wariancji): %.2f' % r2_score(dia_test['target'], dia_test['predict']))

* Przypadek dla jednej zmiennej opisującej:

.. code-block:: python

    import pandas as pd

    dia_df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)\
        .assign(target=diabetes.target)

    # Podział zbioru na testowy i treningowy
    dia_train = dia_df.iloc[:-20, :]
    dia_test = dia_df.iloc[-20:, :]

    lr = linear_model.LinearRegression()
    lr.fit(dia_train[['bmi']], dia_train['target'])

    dia_test = dia_test.assign(predict=lambda x: lr.predict(x[['bmi']]))

    print('Współczynniki: \n', lr.coef_)
    print("Błąd średniokwadratowy: %.2f"
          % mean_squared_error(dia_test['target'], lr.predict(dia_test[['bmi']])))
    print('Metryka R2 (wariancji): %.2f' % r2_score(dia_test['target'], dia_test['predict']))

Modele Chernove
---------------
* Czy klient przedłuży umowę mając jakieś dane (analityk Ci mówi, bo dzwonił do 1000 osób i wie, że najczęściej zmieniają umowę gdy...):

    * czy przedłużał wcześniej
    * od kiedy jest
    * czy zgłaszał jakieś problemy z umową
    * jaka jest wartość abonamentu
    * ile dzwoni
    * możesz mierzyć dobroć oferty 0-100 czy np. nowa oferta jest dla klienta

* Jak sprawdzić czy klient jest zadowolony? (np. śledzić trendy na FB, czy napisał, że jest niezadowolony):

    * Named Entity Recognition
    * Analiza Sentymentu (jak nacechowana jest wiadomość na social media)
    * Inżynieria cech z innych źródeł (typowy Data Science)

* Mogą wystąpić dyskretne eventy, które wpływają na ofertę. Np jakieś wydarzenia na świecie itp które wpływają na model. np. premier brał łapówki a to jest firma publiczna, jej akcje spadną, więc trzeba uwzględnić w modelu możliwość wprowadzenia dyskretnych eventów wraz z wagą wydarzenia i wpływem na model. Tu wchodzi teoria gier i Nash

* Ciężko jest przewidzieć wiek, ale łatwiej jest przewidzieć kubełki wieku (16-20, 20-25 itp). Zamieniasz problem ciągły na dyskretny. Przechodzisz z regresji na problem klasyfikacji. Nikogo nie obchodzi, że masz 26.5 roku, raczej, że jesteś w przedziale wiekowym 25-30 lat bo tak reklama jest targetowana.

* Błąd średniokwadratowy (jak daleko punkty są od linii - tylko liczymy kwadraty tych odległości).
* OLS - Ordinary Least Squares - można używać do czegokolwiek, trzeba mieć funkcję tylko trzeba napisać funkcję kosztu.

* W zależności od danych, linia może być nie tak nachylona. np. jeżeli mamy trochę ekstremalnych wyników - które nie są ważne, to jest overfitting.

Regularyzacja
-------------
* Regularyzacja - minimalizując funkcję kosztu, minimalizujesz wagi
* Lasso L1 - sprowadza wartości nieistotne do zera (sprawdzić czy to nie definicja Ridge)
* Ridge (dodaje regularyzację L2 wag) - sprowadza wartości nieistotne blisko do zera (sprawdzić czy to nie definicja Lasso)

* Regularyzację można stosować do każdego modelu, nie tylko dla Regresji Liniowej.

* Regularyzacja Ridge lub Lasso:

    * parametr alfa to waga regularyzacji, jak bardzo wagi wpływają na funkcję kosztu
    * jak dochodzą nam parametry do modelu to trzeba zmieniać parametr alfa
    * regularyzacja L1 często wywala parametry nieistotne do zera
    * Czasami parametr alfa=1.0 to wyniki mogą być gorsze.
    * Samo użycie regularyzacji w regresji liniowej sprowadza się do użycia modelu o innej nazwie
    * Czasami dobierając parametr alfa np. 0.5 to może polepszyć wynik

Jest wersja modeli które mają CV w nazwie (Cross Validation):

    * LassoCV()
    * oprócz podziału na treningowy i testowy to dzielimy jeszcze na x małych części
    * trenujemy każdy przedział osobno i sprawdzamy jak błędy się rozkładają
    * domyślnie jest cv=3, cv=5 daje dobre wyniki
    * trzeba pamiętać, aby zbiór mógł się na tyle podzielić, aby nie było tam zerowych wartości
    * sam z siebie zmienia parametr alfa i próbuje znaleźć wartość dla której model będzie najlepszy na podstawie wyliczania Mean Square Errors
    * ``lasso.alpha_`` można zobaczyć jaki parametr jest najlepszy

* Elastic Net - ważona regularyzacja L1 i L2, i sprawdzanie która lepiej działa.
* Cechy binarne w modelach liniowych działają tak sobie, modele drzewiaste dobrze sobie z nią radzą.

.. code-block:: python

    # %matplotlib inline

    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    from sklearn import datasets
    from sklearn.metrics import mean_squared_error
    from sklearn.metrics import r2_score
    from sklearn.linear_model import LassoCV


    COLUMNS = ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']


    # Przygotowujemy zbiór danych
    diabetes = datasets.load_diabetes()
    dataframe = pd.DataFrame(diabetes.data, columns=diabetes.feature_names).assign(target=diabetes.target)

    # Dzielimy na zbiór danych treningowych i testowych
    dane_treningowe = dataframe.iloc[:-20, :]
    dane_testowe = dataframe.iloc[-20:, :]

    # Wybór modelu
    model = LassoCV(cv=5)

    # Nauka modelu
    model.fit(dane_treningowe[COLUMNS], dane_treningowe['target'])
    dane_testowe = dane_testowe.assign(predict=lambda df: model.predict(df[COLUMNS]))


    # Do wyświetlania
    wspolczynniki = model.coef_
    blad_sredniokwadratowy = mean_squared_error(dane_testowe['target'], model.predict(dane_testowe[COLUMNS]))
    metryka_r2_wariancji = r2_score(dane_testowe['target'], dane_testowe['predict'])

    print(f'Współczynniki: \n{wspolczynniki}')
    print(f'Błąd średniokwadratowy: {blad_sredniokwadratowy:.2f}')
    print(f'Metryka R2 (wariancji): {metryka_r2_wariancji:.2f}')


    # Wyświetlanie wykresu
    plt.plot(-pd.np.log10(model.alphas_), model.mse_path_, linestyle='--');
    plt.plot(-pd.np.log10(model.alphas_), model.mse_path_.mean(axis=1), 'k', linewidth=3);

    plt.xlabel('$-log_{10}(alpha)$');
    plt.ylabel('Mean Square Error (MSE)');


SVM
---
* Kiedyś bardziej rozpowszechnione obecnie trochę mniej
* Krenel Tricks (trik jądrowy)
* Jeżeli dane nie są liniowo separowalne (tzn można przeprowadzić linię, która rozdzieli zbiór na dwie części)
* Mapuje coś na jakąś funkcję np. koła i tak rozdziela punkty sprowadzając odległości od okręgu na płaszczyznę liniową (odległość punktu od okręgu)
* Funkcji się raczej nie pisze, używamy już istniejące.
* Stara się znaleźć taką linię, która nie tylko najlepiej aproksymuje punkty, ale także stara się by punkty graniczne były równoodległe od linii.
* Funkcja Sinus jest przedziałami liniowa. Model wielomianowy jest lepiej dopasowany.
* Lepiej jest zastosować OLS i dopasować sinusoidę (np. do sygnałów z szumem warto dopasować sinusoidę)
* Zwykle jednak nie znamy jaka to funkcja i trzeba szukać.
* Modele wielomianowe są dużo bardziej złożone obliczeniowo.
* SVM jest przydatny kiedy mamy ładne nieliniowe granice.

.. code-block:: python

    # %matplotlib inline

    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    from sklearn import datasets
    from sklearn.metrics import mean_squared_error
    from sklearn.metrics import r2_score
    from sklearn.svm import SVR


    COLUMNS = ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']


    # Przygotowujemy zbiór danych
    diabetes = datasets.load_diabetes()
    dataframe = pd.DataFrame(diabetes.data, columns=diabetes.feature_names).assign(target=diabetes.target)

    # Dzielimy na zbiór danych treningowych i testowych
    dane_treningowe = dataframe.iloc[:-20, :]
    dane_testowe = dataframe.iloc[-20:, :]

    # Wybór modelu
    model = SVR(kernel='linear', C=1e3)

    # Nauka modelu
    model.fit(dane_treningowe[COLUMNS], dane_treningowe['target'])
    dane_testowe = dane_testowe.assign(predict=lambda df: model.predict(df[COLUMNS]))


    # Do wyświetlania
    wspolczynniki = model.coef_
    blad_sredniokwadratowy = mean_squared_error(dane_testowe['target'], model.predict(dane_testowe[COLUMNS]))
    metryka_r2_wariancji = r2_score(dane_testowe['target'], dane_testowe['predict'])

    print(f'Współczynniki: \n{wspolczynniki}')
    print(f'Błąd średniokwadratowy: {blad_sredniokwadratowy:.2f}')
    print(f'Metryka R2 (wariancji): {metryka_r2_wariancji:.2f}')


Classification
--------------
.. code-block:: python

    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    from sklearn import linear_model, neighbors, svm, tree, datasets
    from sklearn.model_selection import train_test_split, GridSearchCV
    from sklearn.metrics import roc_curve, roc_auc_score, classification_report
    %matplotlib inline

    plt.rcParams['figure.figsize'] = (10, 8)

    iris_ds = datasets.load_iris()

    iris = pd.DataFrame(iris_ds.data, columns=iris_ds.feature_names).assign(target=iris_ds.target)
    iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'target']

    iris_train, iris_test = train_test_split(iris, test_size=0.2)


Normalizacja nazw kolumn:

.. code-block:: python

    name = iris_ds.feature_names[0]
    name.replace(' (cm)', '').replace(' ', '')

    cols = [name.replace(' (cm)', '').replace(' ', '') for name in iris_ds.feature_names]

Wyświetlanie nazw targetów:

.. code-block:: python

    >>> iris_ds.target_names
    array(['setosa', 'versicolor', 'virginica'], dtype='<U10')

    # to jest później wykorzystywane do podmiany jako
    # 0 - setosa
    # 1 - versicolor
    # 2 - virginica


Uwaga na ``train_test_split(iris, test_size=0.2)`` kiepsko działa, jeżeli jedna cecha jest słabo reprezentowana.
Np ilość osób które mają raka. Zdecydowana większość nie ma raka.

* Optymalizować nie tylko na Recall ale również F1
* Dzielisz próbki by ilość była równo reprezentowana (ale trzeba losować w zależności od wielu zmiennych opisujących)
* Szczególnie w tematach medycznych (neurologicznych) jest to często występujące: wtedy optymalizować Recall a nie precyzję.
* Trzeba losować próbki tak, by rozkład był jak najbardziej podobny do rozkładu zbioru oryginalnego
* Sprawdzasz jak bardzo zbiór oryginalny jest skrzywiony, a później coś robisz. zawsze popełniasz błąd, ale kwestia jak wielki
* Decydujesz się którą rzecz optymalizujesz, false positive czy false negative
* Recall = minimalizacja false negative (lepiej zrobić fałszywy alarm, niż nie wykryć)

Łańcuchy Markova
----------------
* konwersja z reklam
* totalnie nie interesuje Cię co nie konwertuje
* patrzysz na to na czym ludzie odpadają (np. układ strony, pozycja itp)

Regresja logistyczna
--------------------
* 1 / exp(...)
* klasyfikuje na dwie części
* Jeżeli mamy problem wieloklasowy, to możemy zastosować model (OVR) 1 vs rest.
* Mamy klasa numer jeden (pierwszy zbiór) i reszta.
* A reszta znów jest podzielona na jeden i reszta.

    * https://en.wikipedia.org/wiki/Precision_and_recall
    * https://en.wikipedia.org/wiki/Precision_and_recall#/media/File:Precisionrecall.svg

Recall
------
* Liczymy to ilościowo, tzn. czy zgadł czy nie
* Precision - ile zgadł poprawnie z wszystkich
* Recall - ile false positive wystąpiło
* F1 - średnia precyzji i recall
* ``F1 = 2 * (precision * recall) / (precision + recall)``

    * tp = true positives
    * fn = false negatives

* Recall = tp / tp + fn
* Type 1 i Type 2 error (częste pytanie na rozmowach kwalifikacyjnych):

    * Type 1 czyli tzw. false positive - powiedzieć mężczyźnie że jest w ciąży
    * Type 2 czyli tzw. false negative - ciężarnej kobiecie powiedzieć, że nie jest w ciąży

* False negative staramy się eliminować, szczególnie w systemach medycznych
* Support = ile mamy elementów w naszym zbiorze testowym

.. code-block:: python

    features = ['sepal_length', 'sepal_width']  # ['petal_width', 'petal_length'] daje lepsze wyniki
    logreg = linear_model.LogisticRegression(C=1e5)
    logreg.fit(iris_train[features], iris_train['target'])
    print(classification_report(iris_test['target'], logreg.predict(iris_test[features])))

* Jak użyjemy płatków, to nasz problem jest dużo lepiej liniowo separowalny.
* Jeżeli użyjemy kielichów, to cechy bardziej się se sobą mieszają.
* Dla problemów muiltiklasowych, można zamienić model na:

.. code-block:: python

    logreg = linear_model.LogisticRegression(C=1e5, multi_class='multinomial', solver='sag')

* Konwergencja = zbieżność
* Przy minimalizacji Epsilon określa zbieżność
* Jeżeli docierając do maksymalnej iteracji gradient będzie zbyt stromy, to wywali error konwergencji
* Wtedy trzeba zwiększyć ilość iteracji

.. code-block:: python

    logreg = linear_model.LogisticRegression(C=1e5, multi_class='multinomial', solver='sag', max_iter=1e6)

* Model ``sag`` dobrze działa dla dużych danych, i wtedy dobrze zbiega i nie trzeba zwiększać ``max_iter``

.. code-block:: python

    logreg = linear_model.LogisticRegression(C=1e5, multi_class='multinomial', solver='lbfgs')

* Jest szybszy, ale nie jest lepszy w optymalizacji globalnej. może błędnie wykryć minimum lokalne funkcji i błędnie pomyśleć, że jest to minimum globalne wielomianu.
* Zamiana petal z sepal w tym przypadku jest dużo ważniejsze niż zmiana solvera.

* SVC - modele support vector classifier
* SVR - support vector regression
* OVR - One vs Rest
* Przestrzeń decyzyjna = pole na wykresie

.. code-block:: python

    svc = svm.LinearSVC(multi_class='ovr')
    svc = svm.LinearSVC(multi_class='crammer_singer')

    # C - parametr nieliniowości
    # Podniesienie C daje model bardziej nieliniowy
    svc = svm.SVC(kernel='rbf', C=1e3)

    svc = svm.SVC(kernel='rbf', C=1)

* Mapuje funkcję nieliniową na płaszczyznę.
* Ten problem jest rozsądnie liniowo separowalny i nie warto używać bardziej skomplikowanych modelów, bo może skutkować to przeuczaniem.
* Teraz są popularne modele XGBoost (model drzewiasty)
* Modele drzewiaste dobrze sobie radzą z cechami dyskretnymi.
* Cecha dla zgadnięcia tego wyniku jest bardzo silna.

Ensemble
--------
* Ensemble to jest połączenie wielu modeli.
* Najczęściej się to stosuje w połączeniu Modeli drzewiastych.

K-Nearest Neighbors
-------------------
* To bardziej algorytm niż model. Programiści go lubią bo jest mniej matematyki.
* Jest bardzo prosty.
* Uczy się danych na pamięć.
* Jest parametr, ``weights='uniform'`` (niezależnie od tego jak są daleko)
* Ale możemy też ważyć ilu jest bliskich sąsiadów a ilu dalekich (``weights='distance'``).
* Można także użyć [callable] tj. przekazać funkcję, która liczy wagi

.. code-block:: python

    def my_function(*args):
        print(args)

    knn = neighbors.KNeighborsClassifier(n_neighbors=3, weights=my_function)

Zalety:

* Super prosta
* Dane reprezentują co dostaniemy (nie ma koncepcji funkcji)
* Jeżeli problem jest super nieliniowy, to będzie działało dobrze
* zapamiętuje dane, więc jak problem będzie duży to zapamięta dużo danych
* łatwo douczać
* jest bardzo szybki

Model najczęściej wykorzystuje się w analizie danych strumieniowych:

    * uczymy model, analizujemy
    * dostajemy nowe dane, uczymy model i znów analizujemy
    * model adaptacyjny

Modele strumieniowe:

    * uczone raz, tzw. offline'owe
    * douczane w trakcie, tzw. online (adaptują się do naszych danych) - ciężej nad nimi panować. Jeżeli się doucza sam, to ciężko panować nad jakością tego, więc trzeba monitorować.

.. note:: ``KNeighborsClassifier()`` i ``n_neighbors`` - pisownia amerykańska, bo angielska ma u w środku

Duży model SVM może być wolniejszy

Dobór parametru ``n_neighbors`` zwykle jest na czuja:

    * im więcej punktów tym więcej można sąsiadów dobrać
    * standardowo zaczyna się od 5 lub 3 ale częściej 5
    * różnica pomiędzy 5 a 10 mówi o gęstości punków
    * zbyt duże wartości parametrów niekoniecznie wpływa na jakość

Model bardzo szybko się uczy i klasyfikuje, więc można zmieniać parametry w trakcie i monitorować.

Drzewa decyzyjne
----------------
* Najczęściej w postaci drzewa binarnego - z dwoma opcjami:

    * znajdują nam formę klastrów związane z danymi
    * odwzorowują procesy biznesowe

* Entropia - uporządkowanie lub chaotyczność układu
* Gini Index - używa się jako index ekonomiczny w kontekście nierówności społecznych

* Criterion # Indeks informacyjności  # The function to measure the quality of a split:

    * criterion='gini'  # Gini impurity (nierówności)
    * criterion='entropy'  # for the information gain

* Albo chcesz dużą informacyjność albo dużą nierówność.
* Przestrzenie decyzyjne są w formie prostokątów ze względu na binarność decyzji:

    * inaczej rosną przyrosty wartości
    * może to powodować zmniejszanie dokładności

Zalety:

    * dobrze działają z wartościami kategorycznymi (lewo-prawo, mężczyzna-kobieta)
    * w miarę szybkie (tak naprawdę to wiele zagnieżdżonych ifów)
    * generują algorytm biznesowy pod spodem dla naszej logiki (bardzo często drzewa stosuje się tylko po to, aby odkryć klasę problemów)

Wady:

    * rzadziej używane jako klasyfikatory
    * przestrzenie klasyfikacyjne są prostokątne co kiepsko oddaje charakter liniowych danych
    * mają tendencję do przeuczania się (ma problemy z generalizacją)
    * zbyt dużo parametrów, którymi można sterować, co powoduje, że musimy sprawdzić bardzo dużo przypadków
    * best jest greedy algorytm, ale czasami ten podział późniejszy jest istotniejszy niż ten który dopasował na początku.

Zawsze bierze ten który ma największą wartość na wyższym stopniu.

CART - Classification and Regression Trees
------------------------------------------
W drzewach jest dużo parametrów:

    * ograniczanie rozbudowy drzewa
    * podejmowanie losowych decyzji
    * feature_importance
    * drzewa można nauczyć największej ilości feature'ów

Kalibracja parametrów modeli
----------------------------
Greed search CV:

    * przeszukiwanie przestrzeni hiperparametrów
    * cross validation

.. code-block:: python

    param_grid = [
      {'C': range(1, 1000, 10), 'kernel': ['linear']},
      {'C': [1, 10, 100, 1000, 1e4, 1e5], 'gamma': [0.001, 0.0001], 'kernel': ['rbf']},
    ]

    # Przejrzyj całą przestrzeń parametrów aby dobrać najlepszy model
    svc = GridSearchCV(svm.SVC(probability=True), param_grid, return_train_score=True)

    features = ['sepal_length', 'sepal_width']
    svc.fit(iris_train[features], iris_train['target'])
    print(classification_report(iris_test['target'], svc.predict(iris_test[features])))


.. code-block:: python

    >>> svc.best_estimator_
    SVC(C=100, cache_size=200, class_weight=None, coef0=0.0,
      decision_function_shape='ovr', degree=3, gamma=0.001, kernel='rbf',
      max_iter=-1, probability=True, random_state=None, shrinking=True,
      tol=0.001, verbose=False)

    >>> svc.best_params_
    {'C': 100, 'gamma': 0.001, 'kernel': 'rbf'}

    >>> svc.cv_results_
    # można przejrzeć wartości

Splity - podziały kroswalidacyjne


Ocena jakości modelu
--------------------
Aby ocenić jak dobrze model klasyfikuje, czy przeprowadza regresję, używamy wielu metryk, które mają za zadanie skupić się na poszczególnych parametrach modelu.

Dla regresji:

.. code-block:: python

    y_true = iris_test['iris_class']
    y_pred = svc.predict(iris_test[features])

    print(classification_report(y_true, y_pred))

Dla Klasyfikacji:

.. code-block:: python

    from sklearn.metrics import precision_score, recall_score, f1_score

    avg = 'macro'
    print('Precision: {:.4f}'.format(precision_score(y_true, y_pred, average=avg)))
    print('Recall: {:.4f}'.format(recall_score(y_true, y_pred, average=avg)))
    print('F1: {:.4f}'.format(f1_score(y_true, y_pred, average=avg)))


Lub dla każdej klasy jak w raporcie:

.. code-block:: python

    from sklearn.metrics import precision_recall_fscore_support

    precision, recall, f1, support = precision_recall_fscore_support(y_true, y_pred)
    precision, recall, f1, support

.. code-block:: python

    from sklearn.metrics import confusion_matrix

    cm = confusion_matrix(y_true, y_pred)

Confusion matrix:

    * pokazuje jak zgadywaliśmy
    * najlepiej jeżeli na diagonalach jest 0 (to znaczy, że nie popełniliśmy błędów)


Jacquard similarity score:

    * ile mamy elementów w części wspólnej (unii) zbirów

ROC (receiver operating characteristic):

    * stosuje się dla problemów dwuklasowych
    * dla wieloklasowych jest problematyczne bo trzeba podzielić na OVR
    * pokazuje jak bardzo klasy są od siebie oddalone

(linia konwolucji - splotu) czyli nachodzenie na siebie rozkładów na wykresie
miara AUC - Area under the curve - im bliżej 1.0 tym lepiej

Zgadywanie jak bardzo dobrze potrafimy klasyfikować poszczególne klasy

Jeżeli mamy wiele klas to najczęściej je uśredniamy

Najczęściej:
* confusion matrix
* zmieniamy miarę, którą optymalizujemy i wtedy dostajemy trochę inny model

Dane tekstowe
-------------
* Jak reprezentować tekst, aby można było coś na jego temat powiedzieć?
* Dane tekstowe zazwyczaj przychodzą w formie dokumentów
* Najczęściej klasyfikujemy dokumenty i przypisujemy im klasy (spam - nie spam, pozytywny tekst - negatywny)

MTD - Macierz TD (Term-Document):

    * budowanie macierzy z każdego słowa w zdaniu
    * bardzo dużo wierszy i kolumn
    * każde słowo to osobna kolumna, a wartość to ile razy w zdaniu
    * dużo rzadkich danych - słowa wspólne rzadko występują we wszystkich zdaniach
    * trzeba wszystkie dane sprowadzić do małych znaków (inaczej będziemy mieli dużo wersji)
    * odmiana wyrazów ma znaczenie (usuwanie liczb mnogich, fleksja - odmiana słów itp)
    * trzeba uwzględnić, że w danych mogą być literówki
    * stemer - odcinanie końcówek (databases utnie do database) - zależne od języka
    * lematyzator - hasłowanie
    * part of speech tagger - rozpoznawanie części mowy
    * używając stemerów i lemazytorów powoduje utratę informacji (np. zamieniając databases na database, gubimy info o liczbach mnogich)
    * wordnet - słowniki

W klasyfikacji spamu, wielkość liter ma znaczenie

CountVectorizer()
HashVectorizer() - częściej wykorzystywany przy dużych danych,

Dają nam sparse matrix czyli lista krotek, gdzie w naszej macierzy znajduje się nasz wyraz, jest dużo zer i dlatego nie warto zapamiętywać tych danych a jedynie miejsca gdzie występują unikalne wartości

Problemy tekstowe są generalnie rzadkie, więc często będzie wykorzystywało się sparse matrix

Nie będzie stop list (stop wordów), czyli wyrazów pojawiających się tak często, że nie ma sensu ich analizować (I, and, or, itp) - zależne od języka (trzeba przekazać własną listę stopwords).

Można ustawić CountVectorizer(analyzer='word') ale można również ustawić na podział na zdania.

Tokenizacja - podział na wyrazy

NLTK - standardowy do analizy mowy języka polskiego
Dużo narzędzi do języka polskiego jest w Javie:

    * np morfeusz (analizator morfologiczny) daje nam nie tylko części mowy ale również morfen - umie rozmawiać z pythonem

Słowosieć PLWORDNET

Tokenizator
Sentence splitter - (rozdzielanie po kropce, ale nie uwzględnianie skrótów, m.in., itp)
Apple może znaczyć jabłko ale również i firmę
bigram - czyli okolice wyrazu Apple computers wskazuje na firmę

Term Frequency–Inverse Document Frequency (TF-IDF)
--------------------------------------------------
ma w sobie countVectorizer() oraz TfidfTransformer():

    * liczy ile razy coś się pojawiło (dzieli przez ile wyrazów pojawiło się w danym dokumencie)
    * waży się jeszcze przez to ile razy to się pojawiło we wszystkich dokumentach
    * im częściej coś się pojawia we wszystkich dokumentach tym wyraz jest ważniejszy
    * im rzadziej w danym dokumencie coś się pojawiło tym ważniejsze

Nas interesuje jak często wyraz pojawia się w książce, ale nie ile razy:

    * książka 200 stron może mieć większą ilość wystąpień (proporcjonalnie) do książki 1000 stron

Zbiór jest zbalansowany do uczenia (wagi są od 0.0-1.0)

Cosine Similarity
^^^^^^^^^^^^^^^^^
* długie wektory wielowymiarowe
* Czy dokumenty są podobne do siebie? - liczymy cosinus konta wektorów
* Jeżeli naszymi cechami są słowa, to jeżeli w dokumentach są te same ilości słów - to dokumenty są takie same
* uwaga, bo słowa mogą mieć różną kolejność
* dostajemy macierz (nasze dokumenty) na diagonalach dostajemy podobieństwo dokumentów
* każdy wiersz tabelki TF-IDF to wektor (ilość słów to liczba wymiarów), wartości to częstości występowania
* często używana w modelach

Miara Levenshteina
^^^^^^^^^^^^^^^^^^
* jak bardzo jedna sekwencja jest podobna do drugiej
* nie obchodzi jej gdzie ta sekwencja występuje
* wykorzystanie difflib.SequenceMatcher(None, tekst_a, tekst_b).ratio()
* czy te literki występują na tych samych miejscach, kompletnie nie ma znaczenia znaczenie (cat i caterpillar)
* ile trzeba wprowadzić modyfikacji, aby stringi wyglądały tak samo
* często się stosuje do tekstów
* jest miarą pozycyjną

Miara Jacquarda
^^^^^^^^^^^^^^^
* można liczyć na wiele sposobów
* ile mamy elementów na przecięciu zbioru

Transformatory i pipeline
-------------------------
* Transformer - jak transformujemy dane
* Pipeline - łączy transformatory
* Estimator - model

Sposób na rozszerzanie sklearn
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* kolejność elementów w pipeline jest ważna
* składa się ze steps
* na każdym obiekcie wykona pipeline.fit_transform()
* można nazywać kolejne elementy pipeline
* można je podawać jako słownik (uwaga na zmieniającą się kolejność, lepiej użyć OrderedDict)
* aby uciszyć error ``sklearn.preprocessing.FunctionTransformer()`` trzeba dać ``validate=False``, ma to związek z tym, że oczekuje wartości ``float``. Transformer jest w pełni gotowy do przetwarzania danych tekstowych

Pipeline
^^^^^^^^
* stosowane do oczyszczania danych, np. usuwania liczb mnogich, usuwania ul. os. pl. itp z nazw ulic
* jeżeli jest coś bardziej skomplikowanego, to lepiej użyć klasy dziedziczącej po BaseEstimator i FunctionTransformer

Klasyfikacja danych tekstowych
------------------------------
* SMS Spam Collection (https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip)
* Dane są jako TSV (Tab Separated Values)

Naive Bayes
-----------
* Naive dlatego, że uznaje wszystkie cechy za liniowo niezależne
* dla dokumentów tekstowych jest to bardzo poprawne
* prawdopodobieństwo jest nie tylko zależne od tego ile razy wystąpiło, ale również z naszą wiedzą ekspercką

.. code-block:: python

    from sklearn.metrics import classification_report, confusion_matrix
    from sklearn.naive_bayes import MultinomialNB
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.model_selection import train_test_split
    import pandas as pd

    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip'
    # z pliku SMSSpamCollection odczytaj plik i wczytaj
    sms = pd.read_csv(plik_danych, sep='\t', names=['is_spam', 'text'])
    train_sms, test_sms = train_test_split(sms, test_size=0.2)

    steps = [('tfidf', TfidfVectorizer()), ('cls', MultinomialNB())]
    nb_pipe = Pipeline(steps=steps)
    nb_pipe.fit(train_sms['text'], train_sms['is_spam'])

    y_pred = nb_pipe.predict(test_sms['text'])
    y_true = test_sms['is_spam']

    print(confusion_matrix(y_true, y_pred))
    print(classification_report(y_true, y_pred))


Modelowanie tematów
-------------------
* uczenie bez nadzoru
* gensim i model LDA (Latent Dirichlet Allocation)
* pakiet nie usuwa stopwords

Metody bez nadzoru
==================
* Klastrowanie - Minus: musimy powiedzieć ile chcemy mieć klastrów
* Algorytm K-Means bardzo często wykorzystywany (liczą gdzie jest środek geometryczny punktów, a później klasyfikuje
* Batch k-means - nie bierze wszystkich danych na raz, tylko dane po kawałku
* K-Means można użyć do danych dużych (batch) oraz dla danych strumieniowych (przychodzących)
* K-Means z pamięcią i z zapominaniem
* W k-means nie przywiązywać się do nazwy klastrów (mogą być przydzielane losowo) ale zawsze ilość klastrów będzie się zgadzała
* ``MiniBatchKMeans()``
* K-Means nie bardzo sobie radzi z tym jak klastry są podzielone
* Jeżeli odległość między dwoma centroidami jest niewielka to opisują ten sam klaster
* K-Means jest prosty obliczeniowo

* Dendrogramy - drzewa - przy klastrowaniu hierarchicznym możemy odcinać drzewa klastrów w hierarchii na interesującym nas poziomie zagnieżdżenia
* Dendrogram - rysunek hierarchiczności klastrów w postaci drzewa

* Jeżeli nie wiemy ile klastrów, to lepiej zacząć od budowania dendrogramów i zobaczenie jak dane są połączone

* K-Means nie bierze geometrii - tylko odległość
* Klastry Aglomeracyjne

Dryft - zmiana w danych (np. przy mierzeniu ilości ruchu (w ciągu dnia możemy mieć mniej wrażliwy system, a w nocy bardziej wrażliwy na pojedyncze alarmy)

* Stabilizacja klastrów
* Adaptowanie modelu

PCA
---
* Analiza wektorów własnych macierzy kowariancji, które rozpinają system bazowy
* gdy mamy dużo zmiennych które są skorelowane (np. Naive Bayes nie lubi tego)
* często stosuje się do rysowania wielowymiarowych danych
* Word to weg generuje 100-300 stopni swobody i można zastosować PCA aby sprowadzić do 2 lub 3 wymiarów
* PCA jest transformatorem a nie modelem

.. code-block:: python

    # Jak dobrze wektor tłumaczy wariancję
    pca.explained_variance_ratio_

* System jest odwrócony względem wektorów
* Składa ze sobą wartości skorelowane, np. jeżeli długość działki rośnie to prawdopodobnie i szerokość również, PCA złączy je ze sobą

Sieci neuronowe
---------------
* Detekcja sentymentów na podstawie wyrazu twarzy która patrzy na reklamę
* SKLearn nie jest narzędziem deeplearningowym, ale ma w sobie zaimplementowane sieci neuronowe
* Sieci neuronowe są dość trudne w porównaniu z innymi rodzajami
* Przy analizie obrazu na wejściu są piksele w skali szarości.
* ``matshow`` (część ``plt.subplot`` pokazuje macierz jako obrazek
* Sieć neuronowa uczy się backpropagation w każdym przejściu sieci
* Większość sieci bazuje na obrazkach 300x300 px
* Preprocessing:

    * usuwanie kolorów
    * zmniejszanie do wspólnych rozmiarów

* TensorFlow
* PyTorch
* Caffe

Pojęcia
^^^^^^^
* warstwa wejściowa
* warstwy ukryte
* warstwa wyjściowa
* Przestrzeń wag
* SGD - Stochastic Gradient Descent
* Backpropagation
* Epoki (kolejne przejścia dla propagacji)
* Label detection - wykrywanie cech z obrazka
