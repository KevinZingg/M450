## Sixt Autovermietung Testfälle

### Testfall 1: Verfügbarkeit von Fahrzeugen
- **Beschreibung**: Überprüfung, ob die Website korrekt anzeigt, welche Fahrzeuge an einem bestimmten Ort und Datum verfügbar sind.
- **Erwartetes Ergebnis**: Korrekte Anzeige verfügbarer Fahrzeuge.

### Testfall 2: Buchungsprozess
- **Beschreibung**: Überprüfung des gesamten Buchungsprozesses von der Fahrzeugauswahl bis zur Bestätigung.
- **Erwartetes Ergebnis**: Erfolgreiche Buchungsbestätigung.

### Testfall 3: Preisberechnung
- **Beschreibung**: Sicherstellen, dass die Website den Preis korrekt berechnet, einschliesslich aller Rabatte, Steuern und Gebühren.
- **Erwartetes Ergebnis**: Korrekter Gesamtpreis.

### Testfall 4: Benutzerkonto
- **Beschreibung**: Überprüfung der Funktionen im Benutzerkonto, z.B. Anmeldung, Registrierung, Passwortzurücksetzung.
- **Erwartetes Ergebnis**: Erfolgreiche Anmeldung/Registrierung.

### Testfall 5: Zahlungsprozess
- **Beschreibung**: Überprüfung der Zahlungsoptionen und des Zahlungsprozesses.
- **Erwartetes Ergebnis**: Erfolgreiche Zahlungsbestätigung.

### Testfall 6: Stornierung
- **Beschreibung**: Überprüfung des Stornierungsprozesses und ob eventuell anfallende Gebühren korrekt berechnet werden.
- **Erwartetes Ergebnis**: Erfolgreiche Stornierungsbestätigung.

### Testfall 7: Feedback und Bewertungen
- **Beschreibung**: Überprüfung, ob Kunden Feedback hinterlassen können und ob dieses Feedback korrekt angezeigt wird.
- **Erwartetes Ergebnis**: Korrekte Anzeige von Kundenbewertungen.

### Testfall 8: Mehrsprachigkeit
- **Beschreibung**: Überprüfung, ob die Website korrekt in verschiedene Sprachen übersetzt wird.
- **Erwartetes Ergebnis**: Korrekte Übersetzung der Website.

### Testfall 9: Kundenservice-Kontakt
- **Beschreibung**: Überprüfung der Kontaktmöglichkeiten zum Kundenservice, z.B. Kontaktformular, Live-Chat.
- **Erwartetes Ergebnis**: Erfolgreiche Kontaktaufnahme zum Kundenservice.

### Testfall 10: Mobile Responsiveness
- **Beschreibung**: Überprüfung, ob die Website auf verschiedenen Geräten und Bildschirmgrössen korrekt angezeigt wird.
- **Erwartetes Ergebnis**: Korrekte Darstellung auf verschiedenen Geräten.


### Aufgabe 3

- ### Blackbox ###

1. Kann Konto erstellen
2. Kann wechselkurs abfragen
3. Kann ID von Konto angeben und bekommt angaben der Person
4. Kann 2 Mal Konto mit gleichen Namen erstellen
5. Kann Programm beenden


- ### Whitebox ###

1. In der Klasse Account auf der Zeile 53 wird Geld subtrahiert wenn User dies auswählt.

2. In der Klasse Bank auf Zeile 25 wird der ausgewählte account gelöscht

3. In der Klasse Bank auf der Zeile 14-15 wird ein Account mit den benötigten Feldern / Werten erstellt

4. In der Klasse Counter auf der Zeile 43 kommt eine Error-meldung wenn der User etwas ungültiges bei der Eingabe eingibt. (Funktioniert nicht immer... wenn am Anfang ein Gültiger Buchstabe ist aber trotzdem ungültig ist z.B. "aqwertzuio" dann kommt die Meldung nicht.)

5. In der Klasse ExchangeRateOkhttp wird in den Zeilen 26 - 30 der aktuelle Kurs geholt sofern er aufgerufen wird.

- ### Verbesserungen ###

1. API Key könnte man in einem seperatem File speichern für extra Sicherheit

2. Das Programm ist zwar simple, könnte aber trotzdem mehr kommentare benötigen.

3. Eine Anleitung um das Programm zu starten wäre schön gewesen.
