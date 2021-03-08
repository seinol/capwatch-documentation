# Anforderungsspezifikationen

## Einführung

### Zweck

*Zweck des Dokumentes*

### Gültigkeitsbereich

*Gültigkeitsbereich des Dokumentes*

### Referenzen

*Liste aller verwendeten und referenzierten Dokumente, Bücher, Links, usw.*

*Referenz auf ein Glossar Dokument, wo alle Abkürzungen und unklaren Begriffe erklärt werden*

*Die Quellen / Referenzen sollten (falls möglich) automatisch erstellt werden*

### Übersicht

*Übersicht über den restlichen Teil dieses Dokumentes geben und dessen Aufbau erläutern*

## Allgemeine Beschreibung

### Produkt Perspektive

*Produkt Perspektive beschreiben*

### Produkt Funktion

*Allgemeine Beschreibung der Funktionen*

### Benutzer Charakteristik

*Zielgruppe des Produktes*

### Einschränkungen

*Wo sind die Grenzen des Produkts*

### Annahmen

*Was ist unklar und wird angenommen bezüglich des Projektes oder des Produktes*

### Abhängigkeiten

*Von welchen Faktoren hängt das Produkt ab*

## Funktionale Anforderungen

### Anlieferer

***Als Anlieferer möchte ich mich registrieren können, damit ich den Kunden die aktuellen Besucherzahlen liefern kann.***
```eval_rst
+-----------------+-----------+--------------------------------------+
| Anforderungs-ID | Kategorie | Beschreibung                         |
+=================+===========+======================================+
| AL-1            | MUSS      | Der Anlieferer muss sich per REST    |
|                 |           | Request registrieren können, indem   |
|                 |           | er Firmenname, Ortschaft und einem   |
|                 |           | Logo als Attachment mitsendet. Er    |
|                 |           | erhält als Antwort eine Bestätigung  |
|                 |           | oder Fehlermeldung.                  |
+-----------------+-----------+--------------------------------------+
| AL-2            | MUSS      | Der Anlieferer liefert per REST Call |
|                 |           | die aktuelle Auslastung mit          |
|                 |           | Timestamp und Maximal erlaubter      |
|                 |           | Auslastung an.                       |
+-----------------+-----------+--------------------------------------+
```
### Anwender

***Als Anwender möchte ich das aktuelle Besuchsaufkommen informieren können.***

```eval_rst
+-----------------+-----------+--------------------------------------+
| Anforderungs-ID | Kategorie | Beschreibung                         |
+=================+===========+======================================+
| AW-1            | MUSS      | Als Anwender kann ich eine Liste     |
|                 |           | aller verfügbaren Firmen anzeigen    |
|                 |           | lassen.                              |
+-----------------+-----------+--------------------------------------+
| AW-2            | MUSS      | Als Anwender kann ich nach einer     |
|                 |           | Firma suchen.                        |
+-----------------+-----------+--------------------------------------+
| AW-3            | KANN      | Als Anwender kann ich eine Firma als |
|                 |           | Favorit markieren. Favorit werden zu |
|                 |           | Beginn der Liste angezeigt.          |
+-----------------+-----------+--------------------------------------+
```
## Weitere Anforderungen

### Qualitätsmerkmale

*Beschreibung der Qualitätsmerkmale der Software (Verweis auf ISO 9126 als Checkliste)*

### Schnittstellen

*Beschreibung der Schnittstellen der Software*

### Randbedingungen

*Auflistung der wichtigsten Randbedingungen mit einer Beschreibung dazu*
