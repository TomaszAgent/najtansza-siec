# Najtańsza sieć
Twoim zadaniem jest napisanie programu, który obliczy, w jaki sposób należy połączyć miasta, aby zminimalizować koszt budowy sieci energetycznej.  
### Logika programu 
Załóżmy następującą sytuację: mamy dane miasta, które chcemy połączyć siecią energetyczną. 
Koszt budowy odcinka drogi między dwoma miastami jest proporcjonalny do odległości między nimi
oraz wymaganej mocy przesyłanej przez linię energetyczną.
Miasta dzielą się na dwie grupy: miasta, w których znajdują się elektrownie,
oraz miasta, które są odbiorcami energii.  

Dane o odległościach miast otrzymujemy w postaci pliku o następującej strukturze:  
A B 5  
A C 3  
B C 2  
B D 1  
C D 3  
D E 2  
A D 10  
F G 1  
F H 3  
G H 2  
D H 1   

Pierwsza kolumna to miasto A, druga kolumna to miasto B, a trzecia kolumna to odległość
między miastami A i B (na przykład w kilometrach czy setkach kilometrów).

W kolejnym pliku posiadamy bilansie energii w danym mieście:  
A 10  
B 5  
C -5  
D -10  
E -5  
F 10  
G -5  
H -5  

Liczba dodatnia oznacza, że miasto produkuje energię (ma elektrownię), a liczba ujemna, że
miasto zużywa energię (jest odbiorcą). Możemy przyjąć że na przykład 1 jednostka energii to 1
gigawat.  
Zadanie polega na znalezieniu takiego połączenia miast, aby zminimalizować koszt budowy sieci
energetycznej. Koszt budowy sieci energetycznej to suma kosztów budowy odcinków drogi między
miastami pomnożona przez sumę mocy przesyłanej przez linię energetyczną. Musimy więc ustalić,
pomiędzy którymi miastami zbudować linię energetyczną i jaką moc będziemy przesyłać tą linią.

Hinty  
• Nie wszystkie miasta muszą być połączone linią energetyczną. Jeśli miasto ma nadmiar energii,
możemy założyć, że wykorzysta ją sobie w jakiś sposób lokalnie.  
• Może się zdarzyć tak, że całkowita moc produkowana w systemie jest mniejsza niż całkowita
moc zużywana. W takim przypadku program powinien zwrócić taką informację.
