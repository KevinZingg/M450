Grundlagen

Aufgabe 1:

Welche Formen von Tests kennen Sie aus der Informatik?
Arbeiten Sie zu zweit und erstellen Sie mind. drei Beispiele, die Sie aus der Praxis kennen.
Wie werden die Tests durchgeführt?


Unit Test (Einzelmodultest?):

Testet einzelne Komponenten oder Funktionen isoliert von anderen Teilen des Systems.
Beispiel aus der Praxis: Ein Entwickler schreibt eine Funktion, die zwei Zahlen addiert. Ein Unit Test könnte diese Funktion testen, indem er sicherstellt, dass die Summe korrekt berechnet wird.
Durchführung: Meistens mit speziellen Frameworks wie JUnit (für Java) oder NUnit (für .NET). Der Test wird automatisiert und regelmäßig durchgeführt, um sicherzustellen, dass Änderungen im Code die Funktionalität nicht beeinträchtigen.


Integrationstest:

Testet die Interaktion zwischen verschiedenen Komponenten oder Systemen.
Beispiel aus der Praxis: Ein Online-Shop hat eine Datenbank und ein Frontend. Ein Integrationstest könnte überprüfen, ob das Frontend korrekt mit der Datenbank kommuniziert, um Produktinformationen abzurufen.
Durchführung: Kann manuell oder automatisiert durchgeführt werden. Bei automatisierten Tests werden oft Mocks oder Stubs verwendet, um externe Systeme zu simulieren.


Systemtest:

Beschreibung: Testet das gesamte System als Ganzes, oft aus der Perspektive des Endbenutzers.
Beispiel aus der Praxis: Ein Benutzer möchte ein Produkt in einem Online-Shop kaufen. Ein Systemtest könnte den gesamten Prozess vom Hinzufügen des Produkts zum Warenkorb bis zum Abschluss des Kaufs testen.
Durchführung: Kann sowohl manuell (z.B. durch QA-Teams) als auch automatisiert (z.B. mit Selenium für Webanwendungen) durchgeführt werden.



Aufgabe 2:

Nennen Sie ein Beispiel eines SW-Fehlers und eines SW-Mangels.
Nennen Sie ein Beispiel für einen hohen Schaden bei einem SW-Fehler.

SW-Fehler (Bug):
Stell dir vor, du spielst ein Videospiel und jedes Mal, wenn du auf einen bestimmten Button klickst, stürzt das Spiel ab. Das wäre ein Bug, weil etwas im Code nicht richtig funktioniert und das Spiel abstürzen lässt.

SW-Mangel (Defekt):
Jetzt stell dir vor, du spielst dasselbe Spiel und es gibt eine Stelle, an der du erwartest, dass es Musik gibt, aber es ist einfach still. Es ist nicht unbedingt ein "Fehler" im Code, aber es fehlt etwas, was du erwartet hast. Das wäre ein Mangel.

Beispiel für hohen Schaden bei einem SW-Fehler:
Es gab einen Softwarefehler, bei dem Einheiten nicht richtig umgerechnet wurden (Pfund statt Newton). Das hat dazu geführt, dass die Sonde zu nah an den Mars geflogen ist und verloren ging. Das hat Millionen von Dollar gekostet. Ein ziemlich teurer Softwarefehler!

