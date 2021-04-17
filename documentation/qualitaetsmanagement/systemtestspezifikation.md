# Systemtest-Spezifikation

## Einführung

### Zweck

Dieses Dokument beschreibt in welcher Form Systemtests an der CapWatch Software durchgeführt werden sollen.

### Gültigkeitsbereich

Dieses Dokument ist für die Stakeholder dieses Projektes, sowie die Entwickler erstellt worden. Es wurde im Rahmen des Engineering Projekts der Fachhochschule Ost erarbeitet.

Die beschriebenen Systemtests reflektieren was auf dem aktuellen Entwicklungsstand der Software möglich ist.

### Referenzen

Die verwendeten Anforderungsbezeichnungen beziehen sich auf das Dokument [Anforderungsspezifikation](../analyse/anforderungsspezifikation.md).

## Voraussetzungen

Vollumfängliches Deployment der Software CapWatch muss vorhanden sein.

## Systemtest

Die folgende Liste von Tests bezieht sich vorerst auf die Funktionalität des Architekturprototypen und wird parallel zur Software entsprechend weiterentwickelt.

```eval_rst
+-------------+-------------------------------------------------------+
| Anforderung | Beschreibung                                          |
+=============+=======================================================+
| AL-1-1      | POST Request vorbereiten mit korrektem Body in JSON   |
|             | Format. Request an URL localhost:8080/Stores          |
|             | absenden. Antwort muss 200 sein und id und secret     |
|             | müssen in der Antwort zurückgesendet werden.          |
+-------------+-------------------------------------------------------+
| AL-1-2      | POST Request vorbereiten mit fehlendem Name im JSON.  |
|             | Request an URL localhost:8080/Stores absenden.        |
|             | Antwort muss 400 sein und es muss der Fehler "Name    |
|             | muss Vorhanden sein" als Antwort zurückkommen.        |
+-------------+-------------------------------------------------------+
| AL-1-3      | PATCH Request vorbereiten mit korrektem Body im JSON  |
|             | Format. Request an URL localhost:8080/Stores absenden.|
|             | Antwort muss 200 sein und es wird kein Body gesendet  |
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
| AW-3-3      | Aufbauen auf AW-3-2. In der Favoritenansicht das      |
|             | Geschäft wieder als Favorit entfernen durch           |
|             | nochmaliges klicken auf das Herzsymbol. Das Geschäft  |
|             | verschwindet aus der Ansicht und es wird die Meldung  |
|             | angezeigt, dass kein Geschäft gefunden worden ist.    |
+-------------+-------------------------------------------------------+
```

