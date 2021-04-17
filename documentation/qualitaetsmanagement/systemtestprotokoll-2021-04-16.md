# Systemtest-Protokoll 2. April 2021

## Einführung

### Zweck

Dieses Dokument dient dazu, eine Übersicht zu geben welche Systemtests wann durchgeführt wurden und was das Resultat war.

### Gültigkeitsbereich

Dieses Dokument ist für die Stakeholder dieses Projektes, sowie die Entwickler erstellt worden. Es wurde im Rahmen des Engineering Projekts der Fachhochschule Ost erarbeitet.

### Referenzen

[Systemtestspezifikation](./systemtestspezifikation.md)

## Angaben zur Durchführung

**Testdatum:** 2021-04-16

Getestet wurde auf folgendem Stand der jeweiligen Git Repositories.

- **Frontend:** d6063e72
- **Backend:** e0fcdadf

Um den Test durchzuführen wurde in beiden Repositories über Docker-Compose die Software gestartet.

## Protokoll

```eval_rst
+-----------+-------------+-----------------------------------------+-------------+
|Anforderung|Implementiert|Kommentare               				|	Status    |
+===========+=============+=========================================+=============+
|AL-1-1     |ja           |                         				|	erfüllt   |
+-----------+-------------+-----------------------------------------+-------------+
|AL-1-2     |ja           |                         				|	erfüllt   |
+-----------+-------------+-----------------------------------------+-------------+
|AL-1-3     |ja           |                         				|	erfüllt   |
+-----------+-------------+-----------------------------------------+-------------+
|AW-1-1     |ja           |                         				|	erfüllt   |
+-----------+-------------+-----------------------------------------+-------------+
|AW-1-2     |ja           |                         				|	erfüllt   |
+-----------+-------------+-----------------------------------------+-------------+
|AW-1-3     |ja           |                         				|	erfüllt   |
+-----------+-------------+-----------------------------------------+-------------+
|AW-2-1     |nein         |Wurde nicht umgesetzt da Umfang zu Gross |nicht erfüllt|
+-----------+-------------+-----------------------------------------+-------------+
|AW-3-1     |ja           |                         				|	erfüllt   |
+-----------+-------------+-----------------------------------------+-------------+
|AW-3-2     |ja           |                         				|	erfüllt   |
+-----------+-------------+-----------------------------------------+-------------+
|AW-3-3     |ja           |                         				|	erfüllt   |
+-----------+-------------+-----------------------------------------+-------------+
```

## Verbesserungsmöglichkeiten

 Der Umfang wurde unterschätzt und darum wurde auf eine Funktionalität verzichtet. Mit mehr Erfahrung werden hoffentlich die Schätzungen besser.

### Bekannte Einschränkungen

Eine MUSS Anforderung, die Suche, wurde aus Zeitgründen nicht umgesetzt und wird im nächsten Sprint implementiert.
