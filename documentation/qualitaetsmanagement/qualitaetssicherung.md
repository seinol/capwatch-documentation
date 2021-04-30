# Qualitätssicherung

## Einführung

### Zweck

Dieses Dokument ist eine Übersicht aller Massnahmen zur Qualitätssicherung im Projekt CapWatch.

### Gültigkeitsbereich

Dieses Dokument ist für die Stakeholder dieses Projektes, sowie die Entwickler erstellt worden. Es wurde im Rahmen des Engineering Projekts der Fachhochschule Ost erarbeitet.

### Referenzen

Git Conventional Commits: [https://www.conventionalcommits.org/en/v1.0.0/](https://www.conventionalcommits.org/en/v1.0.0/)

## Qualitätsmassnahmen

Die qualitätssichernden Massnahmen wurden bereits im Kapitel Qualitätsmassnahmen im [Projektplan](./../projektplan/projektplan.md) beschrieben. Nachfolgend werden einzelne wichtige Punkte noch genauer ergänzt.

### Conventional Commits

Alle Commits welche auf GitLab gemacht werden, müssen dem Pattern von Conventional Commits folgen. Dadurch wird sichergestellt, dass die Commit Messages einheitlich sind und die Erweiterungen und Anpassungen genau beschreiben.

### Frontend Tests mit Lighthouse

Mit Lighthouse werden im Frontend die Kategorien Performance, Best Practices und Accessibility getestet. Die Tests haben mobile Endgeräte als primäre Zielplattform.

### Konfiguration Renovate

Renovate erkennt, wenn eingesetzt Libraries nicht mehr aktuell sind und erstellt für die Aktualisierung automatisch einen Merge Request, welcher nur noch von einem Teammitglied begutachtet und bestätigt werden muss.

#### Renovate im Frontend

Renovate überprüft das Frontend einmal die Woche am Dienstag um 06:00.

#### Renovate Backend

Renovate kann aktuell im Backend nicht eingesetzt werden, da die verwendete NuGet Version noch nicht unterstützt wird.

### SonarQube

Mit SonarQube wird fürs Frontend und Backend eine Codeanalyse durchgeführt. Dabei werden folgende Kriterien ausgewertet:

* Bugs
* Vulnerabilities
* Security Hotspots
* Code Smells
* Code Coverage
* Duplications

Die Analysen schlagen in der Code Coverage fehl, da wir die verwendete [SonarQube Instanz](https://se1-sonarqube.dev.ifs.hsr.ch/dashboard?id=CapwatchBackend) nicht auf unsere Bedürfnisse anpassen können. Aus diesem Grund läuft die Build Pipeline auch erfolgreich durch, wenn SonarQube fehlschlägt.

#### SonarQube Frontend

Da wir im Frontend keine automatisierten Tests schreiben können wir die vorgegebene Codecoverage von 80% nicht erreichen.

#### SonarQube Backend

In der Pipeline des Backends können diejenigen Unittests, welche auf die Datenbank angewiesen sind, nicht ausgeführt werden. Es ist desshalb auch hier nicht möglich die vorgegebene Codecoverage von 80% zu erreichen.

### DoD - Definition of Done

Es gibt verschiedene DoDs. Zur Qualitätssicherung können die Tickets mit einer entsprechenden DoD versehen werden. Die DoD dient den Entwicklern als Leitfaden für die Umsetzung. Es gibt standardisierte DoDs für das Backend, Frontend und die Dokumentation. Diese können für jeden Auftrag individuell ergänzt werden.

#### Standard DoD

-[ ] Auftrag gelesen und verstanden
-[ ] Alle Teile des Auftrags umgesetzt
-[ ] Anforderungen mit Lösung verglichen
-[ ] Ergebnisse im Team besprochen oder alle informiert
-[ ] Review erstellt, umgesetzt und Merge durchgeführt (Merge Request)

#### Backend DoD

Die standard DoD wird für das Backend um folgende Punkte ergänzt.

-[ ] Coding Guidelines und Formatierung überprüft
-[ ] Unit Tests erstellt
-[ ] Code Review erstellt, umgesetzt und Merge durchgeführt (Merge Request)

#### Frontend DoD

Die standard DoD wird für das Frontend um folgende Punkte ergänzt.

-[ ] Coding Guidelines und Formatierung überprüft
-[ ] Code Review erstellt, umgesetzt und Merge durchgeführt (Merge Request)

### Technische Schulden in der Qualitätssicherung

* Renovate im Backend einsetzten, sobald dies unterstützt wird.
* SonarQube für Anforderungen durch CapWatch konfigurieren.
* Linter für Backend in Pipeline integrieren

## Sicherung der Geschichte

### Code und Dokumentation

Entwicklung und Dokumentation geschieht in einem Git Repository, welches auf dem OST GitLab gehostet wird. Somit ist eine Versionierung und Sicherung dieser Daten vorhanden. Durch die dezentrale Natur von Git ist sämtliche Arbeit auch bei allen Entwicklern lokal vollständig vorhanden.

### Zeitauswertung / Tickets

Um die Arbeitszeit jederzeit nachweisen zu können, werden am Ende jedes Sprints die Auswertungen `Time Report per Milestone` und `Time Report per work item` erstellt und in der Dokumentation abgelegt.
