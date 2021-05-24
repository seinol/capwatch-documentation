# Systemtest-Protokoll 2. April 2021

## Einführung

### Zweck

Dieses Dokument dient dazu, eine Übersicht zu geben welche Systemtests wann durchgeführt wurden und was das Resultat war.

### Gültigkeitsbereich

Dieses Dokument ist gültig für das Engineering Projekt CapWatch, welches im Frühlingssemester 2021 an der Fachhochschule OST Rapperswil-Jona durchgeführt wurde. Es ist für die Betreuer und Entwickler des Projekts ausgelegt.

### Referenzen

[Systemtestspezifikation](../systemtestspezifikation.md)

## Angaben zur Durchführung

**Testdatum:** 2021-04-02

Getestet wurde auf folgendem Stand der jeweiligen Git Repositories.

- **Frontend:** f04ca76a
- **Backend:** af817389

Um den Test durchzuführen wurde in beiden Repositories über Docker-Compose die Software gestartet.

## Protokoll

```eval_rst
+----------------+---------------+--------------------------------------------------------+----------------------------------+
| Anforderung    | Implementiert | Kommentare                                             | Status                           |
+================+===============+========================================================+==================================+
| AW-1-2         | ja            |                                                        | erfüllt                          |
+----------------+---------------+--------------------------------------------------------+----------------------------------+
```

## Verbesserungsmöglichkeiten

Da es sich aktuell noch um einen Architekturprototypen handelt wird nicht der bestehende Stand verbessert, sondern mit der Implementierung der effektiven Software fortgefahren.

### Bekannte Einschränkungen

Die meisten Funktionalitäten sind noch nicht implementiert, da es sich noch um einen Architekturprototypen handelt.
