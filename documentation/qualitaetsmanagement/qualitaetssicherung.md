# Qualitätssicherung

## Einführung

### Zweck

Dieses Dokument ist eine Übersicht aller Massnahmen zur Qualitätssicherung im Projekt CapWatch.

### Gültigkeitsbereich

Dieses Dokument ist gültig für das Engineering Projekt CapWatch, welches im Frühlingssemester 2021 an der Fachhochschule OST Rapperswil-Jona durchgeführt wurde. Es ist für die Betreuer und Entwickler des Projekts ausgelegt.

### Referenzen

- [Git Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
- [Git Flow - GitHub](https://github.com/petervanderdoes/gitflow-avh)
- [Git Flow - Flow Graphs](https://git.logikum.hu/graph/feature)
- [Semantic Versioning](https://semver.org/lang/de/)

## Qualitätsmassnahmen

Die qualitätssichernden Massnahmen wurden bereits im Kapitel Qualitätsmassnahmen im [Projektplan](./../projektplan/projektplan.md) beschrieben. Nachfolgend werden einzelne wichtige Punkte noch genauer ergänzt.

### Git

#### Branching

Die Branches werden mit den Konzepten und dem Tooling von Git Flow (AVH Edition) erstellt und verwendet. Wir verwenden `feature`, `bugfix`, `release` und `hotfix` Branches mit den beiden Hauptbranches `develop` für die Entwicklungsumgebung und `master` für die Produktionsumgebung. \
Wir brauchen in diesem Projekt keine `support` Branches. Alle Branches werden in `kebab-case` benannt, ausser die `release` und `hotfix` Branches, welche in Semantischen Versionsnummern verfasst werden ohne Prefix.

#### Commits

Alle Commits müssen den Vorgaben zu Conventional Commits folgen. Dadurch wird sichergestellt, dass die Commit Messages einheitlich sind, die Erweiterungen und Anpassungen genau beschreiben und die Änderungsgeschichte schnell nachvollziehbar ist.

### Frontend Tests mit Lighthouse

Mit Lighthouse werden im Frontend die Kategorien Performance, Best Practices und Accessibility getestet. Die Tests haben mobile Endgeräte als primäre Zielplattform.

### Konfiguration Renovate

Renovate erkennt, wenn eingesetzte Bibliotheken nicht mehr aktuell sind und erstellt für die Aktualisierung automatisch einen Merge Request, welcher dann nur noch von einem Teammitglied begutachtet und zusammengeführt werden muss.

#### Renovate im Frontend

Renovate überprüft das Frontend einmal die Woche am Dienstag um 06:00.

#### Renovate im Backend

Renovate kann aktuell im Backend nicht eingesetzt werden, weil die verwendete NuGet-Version noch nicht unterstützt wird.

### SonarQube

Mit SonarQube wird für das Frontend und Backend eine Codeanalyse durchgeführt. Dabei werden folgende Kriterien ausgewertet:

- Bugs
- Vulnerabilities
- Security Hotspots
- Code Smells
- Code Coverage
- Duplication

#### SonarQube im Frontend

Da wir im Frontend keine automatisierten Tests schreiben, können wir die vorgegebene Code-Coverage von 80 Prozent nicht erreichen. Die Analyse schlägt deshalb in der Code Coverage fehl, da wir die verwendete [SonarQube Instanz](https://se1-sonarqube.dev.ifs.hsr.ch/dashboard?id=CapwatchFrontend) nicht auf unsere Bedürfnisse anpassen können. Aus diesem Grund läuft die Build-Pipeline auch erfolgreich durch, wenn SonarQube fehlschlägt. Jeder Entwickler ist selbst verantwortlich, die SonarQube checks in jedem Merge Request manuell zu analysieren.

#### SonarQube im Backend

In der Pipeline des Backends ist SonarQube in der Pipeline aktiv. Wenn ein SonarQube check fehlschlägt wird ein Merge Request automatisch abgelehnt.

### DoD - Definition of Done

Es gibt verschiedene DoD's. Zur Qualitätssicherung können die Tickets mit einer entsprechenden DoD versehen werden. Die DoD dient den Entwicklern als Leitfaden für die Umsetzung. Es gibt standardisierte DoD's für das Backend, Frontend und die Dokumentation. Diese können für jeden Auftrag individuell ergänzt werden.

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

- Renovate im Backend einsetzten, sobald dies unterstützt wird
- SonarQube für die Anforderungen durch CapWatch konfigurieren

## Sicherung der Geschichte

### Code und Dokumentation

Entwicklung und Dokumentation geschieht in je einem GitLab Projekt mit Repositories, welche auf dem OST GitLab gehostet werden. Somit ist eine Versionierung und Sicherung dieser Daten vorhanden. Durch die dezentrale Natur von Git ist sämtliche Arbeit auch bei allen Entwicklern lokal meistens fast vollständig vorhanden.

### Zeitauswertung / Tickets

Um die Arbeitszeit jederzeit nachweisen zu können, werden am Ende jedes Meilensteins die Auswertungen `Time Report per Milestone` und `Time Report per work item` erstellt und in der Dokumentation abgelegt. Die Zeitauflösung in den Auswertungen ist in Minuten angegeben.
