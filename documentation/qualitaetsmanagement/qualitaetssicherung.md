# Qualitätssicherung

## Einführung

### Zweck

Dieses Dokument ist eine Übersicht, welche alle Massnahmen zur Qualitätssicherung im Projekt CapWatch auflistet.

### Gültigkeitsbereich

Dieses Dokument ist für die Stakeholder dieses Projektes, sowie die Entwickler erstellt worden. Es wurde im Rahmen des Engineering Projekts der Fachhochschule Ost erarbeitet.

### Referenzen

Git Conventional Commits: https://www.conventionalcommits.org/en/v1.0.0/

## Q-Massnahmen

Die Qualitätssichernden Massnahmen wurden bereits im Kapitel Qualitätsmassnahmen in [Projektplan](./../projektplan/projektplan.md) beschrieben. Nachfolgend werden einzelne wichtige Punkte noch genauer ergänzt.

### Conventional Commits

Alle Commits welche auf GitLab gemacht werden müssen dem Pattern von Conventional Commits folgen, dadurch wird sichergestellt, dass die Commit Messages einheitlich sind und die Erweiterungen und Anpassungen genau beschreiben.

### Frontend Tests mit Lighthouse

Mit Lighthouse werden im Frontend die Kategorien Performance, Best practices und Accessibility getestet. Die Tests haben als primäre Zielplattform Mobile Endgeräte.

### Konfiguration Renovate

Renovate erkennt, wenn eingesetzt Libraries nicht mehr aktuell sind und erstellt für die Aktualisierung automatisch einen Merge Request, welcher nur noch von einem Teammitglied bestätigt werden muss.

#### Renovate im Frontend

Renovate überprüft das Frontend einmal in der Woche am Dienstag um 06:00.

#### Renovate Backend

Renovate kann aktuell im Backend nicht eingesetzt werden da die verwendete DotNet Nuget Version, welche wir verwenden, noch nicht unterstützt wird.

### SonarQube

Mit SonarQube wird fürs Frontend und Backend eine Codeanalyse durchgeführt, dabei werden folgende Kriterien ausgewertet:
* Bugs
* Vulnerabilities
* Security Hotspots
* Code Smells
* Code Coverage
* Duplications

Die Analysen schlagen in der Code Coverage fehl, da wir die verwendete [SonarQuebe Instanz](https://se1-sonarqube.dev.ifs.hsr.ch/dashboard?id=CapwatchBackend) nicht für unsere Bedürfnisse anpassen können. Aus diesem Grund läuft die Build Pipeline auch erfolgreich, wenn SonarQube fehlschlägt.

#### SonarQube Frontend

Da wir im Frontend keine Tests schreiben können wir die vorgegebene Codecoverage von 80% nicht erreichen.

#### SonarQube Backend

In der Pipeline des Backends können die Unittests, welche auf die Datenbank angewiesen sind, nicht ausgeführt werden. Es ist desshalb auch hier nicht möglich die vorgegebene Codecoverage von 80% nicht erreichen.

### DoD - Definition of Done

Est gibt verschiedene DoDs. Zur Qualitätssicherung können die Tickets mit einer Entsprechender DoD versehenen werden. Die DoD dient den Entwicklern auch als Leitfaden für die Umsetzung. Es gibt Standard DoDs für das Backend, Frontend und die Dokumentation, diese können für jeden Auftrag individuell ergänzt werden.

#### Standard DoD

-[ ] Auftrag gelesen und verstanden
-[ ] Alle teile des Auftrags umgesetzt
-[ ] Anforderungen mit Lösung vergleichen
-[ ] Ergebnisse im Team besprochen oder alle informiert
-[ ] Review erstellen, Review umsetzen und Merge durchgeführt (Merge Request)

#### Backend DoD

-[ ] Auftrag gelesen und verstanden
-[ ] Alle teile des Auftrags umgesetzt
-[ ] Coding Guidelines und Formatierung überprüfen
-[ ] Unit Tests erstellt
-[ ] Anforderungen mit Lösung vergleichen
-[ ] Ergebnisse im Team besprochen oder alle informiert
-[ ] Code Review erstellen, Review umsetzen und Merge durchgeführt (Merge Request)

#### Frontend DoD

-[ ] Auftrag gelesen und verstanden
-[ ] Alle teile des Auftrags umgesetzt
-[ ] Coding Guidelines und Formatierung überprüfen
-[ ] Anforderungen mit Lösung vergleichen
-[ ] Ergebnisse im Team besprochen oder alle informiert
-[ ] Code Review erstellen, Review umsetzen und Merge durchgeführt (Merge Request)

### Technische Schulen in der Qualitätssicherung

* Renovate im Backend einsetzten, sobald dies unterstützt wird.
* SonarQube für Anforderungen durch CapWatch konfigurieren.
* Linter für Backend in Pipeline integrieren

## Sicherung der Geschichte

### Code und Dokumentation

Entwicklung und Dokumentation werden in einem GitLab Repository welches von der HSR zur verfügung gestellt wird bearbeitet, somit eine Versionierung und Sicherung dieser Daten vorhanden. Eine weitere Sicherung ist hier nicht notwendig.

### Zeitauswertung / Tickets

Um die Arbeitszeit jederzeit nachweisen zu können wird am Ende jedes Sprints die Auswertungen `Time Report per Milestone` und `Time Report per work item` erstellt und in der Dokumentation abgelegt.