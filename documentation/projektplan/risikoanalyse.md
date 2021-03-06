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
- Gewichteter Schaden Projekt gesamt: _20 Stunden_
- Durchschnitt Schadenspotenzial pro Sprint (gerundet): \*6 Stunden\*\*

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
| Ri2 | Ausfall Teammitglied | Ein Teammitglied fällt für eine bestimme/ |                 3 |                    1 |             3 | keine Massnahmen         | Aufgaben auf andere           |
|     |                      | unbestimmte Zeit aus.                     |                   |                      |               |                          | Teammitglieder verteilen oder |
|     |                      |                                           |                   |                      |               |                          | Sprint Umfang kürzen.         |
+-----+----------------------+-------------------------------------------+-------------------+----------------------+---------------+--------------------------+-------------------------------+
| Ri3 | Ausfall der von der  | Die durch die Ost bereitgestellte         |                 3 |                    1 |             3 | Spiegeln des Repository  | Wechsel auf das Github        |
|     | Ost bereitgestellten | Infrastruktur (z.B. Gitlab) fällt aus und |                   |                      |               | auf Github               | Repository                    |
|     | Infrastruktur        | es kommt zu Datenverlust.                 |                   |                      |               |                          |                               |
+-----+----------------------+-------------------------------------------+-------------------+----------------------+---------------+--------------------------+-------------------------------+
| Ri4 | Ungenügende          | Anforderungen wurden nicht klar definiert |                 0 |                    0 |             0 | Anforderung reviewen     | Anforderungsanalyse           |
|     | Spezifikation        | und müssen während der Implementierung    |                   |                      |               |                          | überarbeiten                  |
|     |                      | überarbeitet werden oder in den nächsten  |                   |                      |               |                          |                               |
|     |                      | Sprint verschoben werden.                 |                   |                      |               |                          |                               |
+-----+----------------------+-------------------------------------------+-------------------+----------------------+---------------+--------------------------+-------------------------------+
| Ri5 | Zeitmanagement       | Die Geplante Zeit für ein Feature wird    |                 3 |                    1 |             3 | Gemeinsames schätzen     | Verschiebung von Features     |
|     |                      | massiv überschritten.                     |                   |                      |               | der Aufwände             | in späteren Sprint            |
+-----+----------------------+-------------------------------------------+-------------------+----------------------+---------------+--------------------------+-------------------------------+
| Ri6 | Softwarearchitektur  | Fehler im Designprozess werden erst       |                 0 |                    0 |             0 | Prototyp erstellen       | Fehleranalyse & Überarbeitung |
|     |                      | während der Umsetzung bemerkt.            |                   |                      |               |                          | der Softwarearchitektur       |
+-----+----------------------+-------------------------------------------+-------------------+----------------------+---------------+--------------------------+-------------------------------+
| Ri7 | Backend Technologie  | Das Backend wird in C# geschrieben,       |                 0 |                    0 |             0 | keine Massnahmen         |                               |
|     |                      | es kann auf viel bestehendes Wissen       |                   |                      |               |                          |                               |
|     |                      | zurückgegriffen werden.                   |                   |                      |               |                          |                               |
+-----+----------------------+-------------------------------------------+-------------------+----------------------+---------------+--------------------------+-------------------------------+
| Ri8 | Frontend Technologie | Das Frontend wird mit React implementiert,|                 0 |                    0 |             0 | Einlesen in React        | Erlernen der Technologie auch |
|     |                      | damit wurde bis anhin kaum Erfahrung      |                   |                      |               | Dokumentation            | auf private Zeit um den       |
|     |                      | gesammelt.                                |                   |                      |               |                          | Projektplan nicht zu gefährden|
+-----+----------------------+-------------------------------------------+-------------------+----------------------+---------------+--------------------------+-------------------------------+
| Ri9 | Organisation         | Termingerechte Abgabe wird nicht erreicht.|                 3 |                    1 |             3 | Alle grossen Tasks bis   | Abgabe ist zwingend           |
|     |                      |                                           |                   |                      |               | eine Woche vor Abgabe    | einzuhalten!                  |
|     |                      |                                           |                   |                      |               | bereit zur Besprechung   |                               |
|     |                      |                                           |                   |                      |               | im Team.                 |                               |
+-----+----------------------+-------------------------------------------+-------------------+----------------------+---------------+--------------------------+-------------------------------+
| Ri10| Pipeline             | Die Pipline funktioniert nicht und ver-   |                 3 |                    2 |             6 | Solange es läuft wenn    | Höchste Prio um es wieder zum |
|     |                      | zögert die Umsetzung.                     |                   |                      |               | möglich nicht verändern. | laufen zu bringen.            |
+-----+----------------------+-------------------------------------------+-------------------+----------------------+---------------+--------------------------+-------------------------------+
|     |                      |                                           |                   |                Summe |            20 |                          |                               |
+-----+----------------------+-------------------------------------------+-------------------+----------------------+---------------+--------------------------+-------------------------------+
```

\* _Durchschnitt Schadenspotenzial (aufgerundet) = Gewichteter Schaden Projekt / Anzahl Sprints_

\*\* _Gewichteter Schaden = Schadenspotenzial _ Eintrittswahrscheinlichkeit\*

## Risikoüberwachung

Die Risiken sollen nach jedem Sprint überprüft werden.

Risikoüberprüfung durchgeführt:

- 13.03.2021 (Christoph Scheiwiller): Risiken ergänzt / Neuberechnung Schadenspotenzial
- 02.04.2021 (Pascal Schlumpf): Risiken neu beurteilt
  - Ri4 bleibt gleich da im Prototyp die MUSS-Anforderungen nicht vollständig umgesetzt worden sind.
  - Ri5 bleibt trotz ersten Erfahrungen gleich. Wir müssen unsere Erkenntnisse in den nächsten Sprint einfliessen lassen und schauen ob wir uns verbessert haben. Erst dann können wir die Eintrittswahrscheinlichkeit reduzieren.
  - Bei Ri6 reduziert sich die Eintrittswahrscheinlichkeit, da wir den Grundstein der Architektur im Prototyp schon umgesetzt haben und es sich bewährt hat.
  - Bei Ri8 reduziert sich die Eintrittswahrscheinlichkeit, da im Prototyp schon viel neues Wissen erlangt worden ist.
- 15.04.2021 (Pascal Schlumpf): Risiken neu beurteilt.
  - Bei Ri4 reduziert sich die Eintrittswahrscheinlichkeit, da wir nun fast alle MUSS Anforderungen umgesetzt haben. Eine Anforderung mussten wir auf den nächsten Sprint verschieben, da der Umfang zu gross wurde. Bis jetzt wurde noch keine Kritik an den Anforderungen ausgesprochen.
  - Bei Ri5 reduziert sich die Eintrittswahrscheinlichkeit. Wir haben auch in diesem Sprint die Tasks für Entwicklung zu tief geschätzt. In diesem Punkt müssen wir uns noch verbessern. Die Abweichungen bei der Gesamtzeit sind aber soweit im Rahmen, dass wir das Risiko als kleiner einstufen.
- 29.04.2021 (Pascal Schlumpf): Risiken neu beurteilt.
  - Bei Ri7 reduziert sich das Schadenspotential um 2 auf 1, da alle wichtigen Komponenten in einer guten Qualität umgesetzt worden sind und das Team eingespielt ist. Alle KANN Anforderungen können nun mit tieferem Druck umgesetzt werden.
  - Es wurde das Risiko Ri10 erfasst. Aufgrund der Erfahrungen der letzten Wochen hat sich dieses Risiko aufgedrängt. Es hat sich herausgestellt, dass die Pipeline sehr diffizil und gleichwohl für die Erfüllung unseres Auftrags zentral ist.
- 18.05.2021 (Pascal Schlumpf): Risiken neu beurteilt.
  - Ri4, Ri6, Ri7, Ri8 wurden auf 0h gesetzt, da die Entwicklungsarbeiten abgeschlossen sind und nur noch Dokumentation ansteht.
