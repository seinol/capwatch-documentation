# Systemtest-Spezifikation

## Einführung

### Zweck

Dieses Dokument beschreibt in welcher Form Systemtests an der CapWatch Software durchgeführt werden sollen.

### Gültigkeitsbereich

Dieses Dokument ist gültig für das Engineering Projekt CapWatch, welches im Frühlingssemester 2021 an der Fachhochschule OST Rapperswil-Jona durchgeführt wurde. Es ist für die Betreuer und Entwickler des Projekts ausgelegt.

### Referenzen

Die verwendeten Anforderungsbezeichnungen beziehen sich auf das Dokument [Anforderungsspezifikation](../analyse/anforderungsspezifikation.md).

## Voraussetzungen

Vollumfängliches Deployment der Software CapWatch muss vorhanden sein.

## Systemtest

Die folgende Liste von Tests deckt alle Funktionalitäten der Beta Version von CapWatch ab.

```eval_rst
+-------------+-------------------------------------------------------+
| Anforderung | Beschreibung                                          |
+=============+=======================================================+
| AL-1-1      | PATCH Request vorbereiten mit korrektem Body im JSON  |
|             | Format. Request an URL localhost:8080/stores senden.  |
|             | Antwort muss 200 sein ohne Rückgabe.                  |
+-------------+-------------------------------------------------------+
| AL-2-1      | POST Request vorbereiten mit korrektem Body im JSON   |
|             | Format. Request an URL localhost:8080/stores senden.  |
|             | Antwort muss 200 sein und die id und das secret       |
|             | müssen in der Antwort zurückgesendet werden.          |
+-------------+-------------------------------------------------------+
| AL-2-2      | POST Request vorbereiten mit fehlendem Namen im JSON  |
|             | Format. Request an URL localhost:8080/stores senden.  |
|             | Antwort muss 400 sein und es muss der Fehler "Name    |
|             | muss Vorhanden sein" als Antwort zurückkommen.        |
+-------------+-------------------------------------------------------+
| AW-1-1      | Datenbank nicht anbinden. URL des CapWatch Frontend   |
|             | aufrufen. Es wird eine Meldung angezeigt, dass ein    |
|             | Fehler aufgetreten ist.                               |
+-------------+-------------------------------------------------------+
| AW-1-2      | Datenbank anbinden aber keine Einträge erfassen. URL  |
|             | des CapWatch Frontend aufrufen. Es wird eine Meldung  |
|             | angezeigt, dass keine Geschäfte gefunden worden sind. |
+-------------+-------------------------------------------------------+
| AW-1-3      | Auf Datenbank manuell Geschäfte hinzufügen. URL des   |
|             | CapWatch Frontend aufrufen. Es wird eine Liste von    |
|             | Geschäften mit Informationen zur Auslastung           |
|             | angezeigt.                                            |
+-------------+-------------------------------------------------------+
| AW-2-1      | Aufbauend auf AW-1-3. Wenn die Liste angezeigt wird,  |
|             | auf die Lupe klicken und im Suchfeld nach einem       |
|             | Geschäft suchen. Es wird eine nach dem Suchbegriff    |
|             | gefilterte Liste angezeigt.                           |
+-------------+-------------------------------------------------------+
| AW-3-1      | Aufbauend auf AW-1-3. Wenn die Liste angezeigt wird,  |
|             | noch kein Geschäft als Favorit markieren und in die   |
|             | Favoritenansicht wechseln. Es dürfen keine Geschäfte  |
|             | angezeigt werden sondern die Meldung aus AW-1-2.      |
+-------------+-------------------------------------------------------+
| AW-3-2      | Aufbauend auf AW-1-3. Wenn die Liste angezeigt wird,  |
|             | auf einem Geschäft das Herzsymbol anklicken und es so |
|             | als Favorit markieren. In die Favoritenansicht        |
|             | wechseln. Das ausgewählte Geschäft wird nun           |
|             | angezeigt.                                            |
+-------------+-------------------------------------------------------+
| AW-3-3      | Aufbauend auf AW-3-2. In der Favoritenansicht das     |
|             | Geschäft wieder als Favorit entfernen durch           |
|             | nochmaliges klicken auf das Herzsymbol. Das Geschäft  |
|             | verschwindet aus der Ansicht und es wird die Meldung  |
|             | angezeigt, dass kein Geschäft gefunden worden ist.    |
+-------------+-------------------------------------------------------+
```
