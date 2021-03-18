# Risikoanalyse

## Einführung

### Zweck

In diesem Dokument werden Risiken identifiziert und beurteilt. Aufgrund dieser Beurteilung wird definiert wie mit den Risiken zu verfahren ist.

### Gültigkeitsbereich

Dieses Dokument ist für das EPJ CapWatch gültig. Eine Überprüfung der Risiken ist während des Projektes mehrfach durchzuführen.

### Referenzen

Vorlesung SE1 FS2021: Woche 1 - W01 - Introduction and Project Planning

## Risikomanagement

- Projekt: CapWatch
- Erstellt am: 02.03.2021
- Autor: Christoph Scheiwiller
- Gewichteter Schaden Projekt: *31 Stunden*
- Durchschnitt Schadenspotenzial pro Strint: *4 Stunden** (gerundet)

```eval_rst
+-----+----------------------+-------------------------------------------+-------------------+----------------------+---------------+--------------------------+-------------------------------+
| Nr  | Titel                | Beschreibung                              | Schadenspotenzial | Eintrittswahrschein- | Gewichteter   | Vorbeugung               | Verhalten beim Eintreten      |
|     |                      |                                           |     [1-3] Stunden | lichkeit       [1-3] | Schaden**     |                          |                               |
|     |                      |                                           |                   |                      | [1-9] Stunden |                          |                               |
+=====+======================+===========================================+===================+======================+===============+==========================+===============================+
| Ri1 | Internetausfall      | Durch die Coronapandemie müssen alle      |                 1 |                    2 |             2 | Dokumentation relevanter | Meetingprotokoll lesen        |
|     |                      | Besprechungen online durchgeführt werden. |                   |                      |               | Inhalte während          |                               |
|     |                      | Dabei sind wir auf eine funktionierende   |                   |                      |               | Besprechungen            |                               |
|     |                      | Internetverbindung angewiesen.            |                   |                      |               |                          |                               |
+-----+----------------------+-------------------------------------------+-------------------+----------------------+---------------+--------------------------+-------------------------------+
| Ri2 | Softwarearchitektur  | Fehler im Designprozess werden erst       |                 1 |                    2 |             2 | Prototyp erstellen       | Fehleranalyse & Überarbeitung |
|     |                      | während der Umsetzung bemerkt.            |                   |                      |               |                          | der Softwarearchitektur       |
+-----+----------------------+-------------------------------------------+-------------------+----------------------+---------------+--------------------------+-------------------------------+
| Ri3 | Ungenügende          | Anforderungen wurden nicht klar definiert |                 2 |                    2 |             4 | Anforderung reviewen     | Anforderungsanalyse           |
|     | Spezifikation        | und müssen während der Implementierung    |                   |                      |               |                          | überarbeiten                  |
|     |                      | überarbeitet werden oder in den nächsten  |                   |                      |               |                          |                               |
|     |                      | Sprint verschoben werden.                 |                   |                      |               |                          |                               |
+-----+----------------------+-------------------------------------------+-------------------+----------------------+---------------+--------------------------+-------------------------------+
| Ri4 | Zeitmanagement       | Die Geplante Zeit für ein Feature wird    |                 3 |                    2 |             6 | Gemeinsames schätzen     | Verschiebung von Features     |
|     |                      | massiv überschritten.                     |                   |                      |               | der Aufwände             | in späteren Sprint            |
+-----+----------------------+-------------------------------------------+-------------------+----------------------+---------------+--------------------------+-------------------------------+
| Ri5 | Backend Technologie  | Das Backend wird in C# geschrieben,       |                 3 |                    1 |             3 | keine Massnahmen         |                               |
|     |                      | es kann auf viel bestehendes Wissen       |                   |                      |               |                          |                               |
|     |                      | zurückgegriffen werden.                   |                   |                      |               |                          |                               |
+-----+----------------------+-------------------------------------------+-------------------+----------------------+---------------+--------------------------+-------------------------------+
| Ri6 | Frontend Technologie | Das Frontend wird mit React implementiert,|                 3 |                    2 |             6 | Einlesen in React        | Erlernen der Technologie auch |
|     |                      | damit wurde bis anhin kaum Erfahrung      |                   |                      |               | Dokumentation            | auf private Zeit um den       |
|     |                      | gesammelt.                                |                   |                      |               |                          | Projektplan nicht zu gefährden|
+-----+----------------------+-------------------------------------------+-------------------+----------------------+---------------+--------------------------+-------------------------------+
| Ri7 | Organisation         | Termingerechte Abgabe wird nicht erreicht.|                 3 |                    1 |             3 | Alle grossen Tasks bis   | Abgabe ist zwingend           |
|     |                      |                                           |                   |                      |               | eine Woche vor Abgabe    | einzuhalten!                  |
|     |                      |                                           |                   |                      |               | bereit zur Besprechung   |                               |
|     |                      |                                           |                   |                      |               | im Team.                 |                               |
+-----+----------------------+-------------------------------------------+-------------------+----------------------+---------------+--------------------------+-------------------------------+
| Ri8 | Ausfall Teammitglied | Ein Teammitglied fällt für eine bestimme/ |                 3 |                    1 |             3 | keine Massnahmen         | Aufgaben auf andere           |
|     |                      | unbestimmte Zeit aus.                     |                   |                      |               |                          | Teammitglieder verteilen oder |    
|     |                      |                                           |                   |                      |               |                          | Sprint Umfang kürzen.         |
+-----+----------------------+-------------------------------------------+-------------------+----------------------+---------------+--------------------------+-------------------------------+
| Ri9 | Ausfall der von der  | Die durch die Ost bereitgestellte         |                 3 |                    1 |             3 | Spiegeln des Repository  | Wechsel auf das Github        |
|     | Ost bereitgestellten | Infrastruktur (z.B. Gitlab) fällt aus und |                   |                      |               | auf Github               | Repository                    |    
|     | Infrastruktur        | es kommt zu Datenverlust.                 |                   |                      |               |                          |                               |
+-----+----------------------+-------------------------------------------+-------------------+----------------------+---------------+--------------------------+-------------------------------+
|     |                      |                                           |                   |                Summe |            31 |                          |                               |
+-----+----------------------+-------------------------------------------+-------------------+----------------------+---------------+--------------------------+-------------------------------+
```
**Durchschnitt Schadenspotenzial (aufgerundet) = Gewichteter Schaden Projekt / Anzahl Risiken* \
***Gewichteter Schaden = Schadenspotenzial * Eintritts&shy;wahrscheinlichkeit*

## Risikoüberwachung

Die Risiken sollen nach jedem Sprint überprüft werden.

Risikoüberprüfung durchgeführt:
- 13.03.2021 (Christoph Scheiwiller)
