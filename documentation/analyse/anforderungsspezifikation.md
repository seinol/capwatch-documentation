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

Wir haben uns aufgrund des einfachen Geschäftsfalles dagegen entschieden Use Cases einzusetzen, da diese einen ziemlichen Overhead mit sich bringen. Wir setzen dafür auf einen schlanken Mix aus User Story und MUSS/KANN Anforderungen.

### Anlieferer / Anbieter

***Als Anlieferer möchte ich mich registrieren können, damit ich den Kunden die aktuellen Besucherzahlen liefern kann.***
```eval_rst
+-----------------+-----------+--------------------------------------+
| Anforderungs-ID | Kategorie | Beschreibung                         |
+=================+===========+======================================+
| AL-1            | MUSS      | Der Anlieferer liefert regelmässig   |
|                 |           | die aktuelle Auslastung mit Token,   |
|                 |           | Timestamp und Maximal erlaubter      |
|                 |           | Auslastung an.                       |
+-----------------+-----------+--------------------------------------+
| AL-2            | KANN      | Der Anlieferer muss sich per Request |
|                 |           | registrieren können, indem er        |
|                 |           | Firmenname, Ortschaft und einem Logo |
|                 |           | als Attachment mit sendet. Er erhält |
|                 |           | als Antwort einen Token oder eine    |
|                 |           | Fehlermeldung.                       |
+-----------------+-----------+--------------------------------------+
```
### Konsument

***Als Konsument möchte ich mich über das aktuelle Besuchsaufkommen informieren können.***
```eval_rst
+-----------------+-----------+--------------------------------------+
| Anforderungs-ID | Kategorie | Beschreibung                         |
+=================+===========+======================================+
| AW-1            | MUSS      | Als Konsument kann ich eine Liste    |
|                 |           | aller verfügbaren Firmen anzeigen    |
|                 |           | lassen.                              |
+-----------------+-----------+--------------------------------------+
| AW-2            | MUSS      | Als Konsument kann ich nach einer    |
|                 |           | Firma suchen.                        |
+-----------------+-----------+--------------------------------------+
| AW-3            | MUSS      | Als Konsument kann ich eine Firma    |
|                 |           | als Favorit markieren. Favoriten     |
|                 |           | können in der Favoritenansicht       |
|                 |           | angezeigt werden.                    |
+-----------------+-----------+--------------------------------------+
| AW-4            | KANN      | Als Konsument werden mir automatisch |
|                 |           | die nächsten Läden in meiner         |
|                 |           | Umgebung zuoberst in der Auflistung  |
|                 |           | angezeigt.                           |
+-----------------+-----------+--------------------------------------+
| AW-5            | KANN      | Ich kann mich als Konsument          |
|                 |           | registrieren und anschliessend nach  |
|                 |           | einem Login über mehrere Geräte      |
|                 |           | hinweg auf meine Favoriten           |
|                 |           | zugreifen.                           |
+-----------------+-----------+--------------------------------------+
| AW-6            | KANN      | Als Konsument kann ich meine         |
|                 |           | E-Mailadresse hinterlegen und mich   |
|                 |           | so über wichtige Ereignisse          |
|                 |           | informieren lassen.                  |
+-----------------+-----------+--------------------------------------+
| AW-7            | KANN      | Als Konsument kann ich über eine     |
|                 |           | Detailansicht einer Firma die        |
|                 |           | Prognosen und Verläufe des           |
|                 |           | Besucheraufkommens anzeigen lassen.  |
+-----------------+-----------+--------------------------------------+
| AW-8            | KANN      | Als Konsument kann ich mir bei einer |
|                 |           | Firma einen begrenzten Zeitraum      |
|                 |           | reservieren.                         |
+-----------------+-----------+--------------------------------------+
```
Für das Minimal Viable Product sind die MUSS-Anforderungen relevant. Falls Kapazität vorhanden ist, können aber auch schon KANN-Anforderungen umgesetzt werden.

## Weitere Anforderungen

### Qualitätsmerkmale

*Beschreibung der Qualitätsmerkmale der Software (Verweis auf ISO 9126 als Checkliste)*

### Schnittstellen

*Beschreibung der Schnittstellen der Software*

### Randbedingungen

*Auflistung der wichtigsten Randbedingungen mit einer Beschreibung dazu*
