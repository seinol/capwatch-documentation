# Systemtest-Protokoll

## Einführung

### Zweck

Dieses Dokument dient dazu eine Übersicht zu geben welche Systemtests wann durchgeführt wurden und was das Resultat war.

### Gültigkeitsbereich

Dieses Dokument ist für die Stakeholder dieses Projektes, sowie die Entwickler erstellt worden. Es wurde im Rahmen des Engineering Projekts der Fachhochschule Ost erarbeitet.

### Referenzen

[Systemtestspezifikation](./systemtestspezifikation.md)

## Angaben zur Durchführung

Testdatum: 2021-04-02

Getestet wurde auf folgendem Stand der jeweiligen Git Repositories

- Frontend: f04ca76a
- Backend: af817389

Um den Test durchzuführen wurde in beiden Repositories über Docker-Compose die Software gestartet.

## Protokoll

```eval_rst
+----------------+---------------+--------------------------------------------------------+----------------------------------+
| Anforderung    | implementiert | Fehler/Unschönheit                                     | Status                           |
+================+===============+========================================================+==================================+
| AW-1-1         | nein          | Der Benutzer weiss nicht warum nichts angezeigt wird   | wird im folgenden Sprint behoben |
+----------------+---------------+--------------------------------------------------------+----------------------------------+
| AW-1-2         | ja            |                                                        | gut                              |
+----------------+---------------+--------------------------------------------------------+----------------------------------+
```

## Verbesserungsmöglichkeiten

Da es sich aktuell noch um einen Architekturprototypen handelt wird nicht der bestehende Stand verbessert, sondern mit der Implementierung der effektiven Software fortgefahren.

### Bekannte Einschränkungen

Die meisten Funktionalitäten sind noch nicht implementiert, da es sich noch um einen Architekturprototypen handelt.
