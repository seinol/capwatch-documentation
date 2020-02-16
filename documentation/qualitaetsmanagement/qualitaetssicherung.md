# Qualitätssicherung

## Einführung

### Zweck

*Zweck des Dokumentes*

### Gültigkeitsbereich

*Gültigkeitsbereich des Dokumentes*

### Referenzen

*Liste aller verwendeten und referenzierten Dokumente, Bücher, Links, usw.*

*Referenz auf ein Glossar Dokument, wo alle Abkürzungen und unklaren Begriffe erklärt werden*

*Die Quellen / Referenzen sollten (falls möglich) automatisch erstellt werden*

## Q-Massnahmen

*Auflisten, was alles geplant und durchgeführt wurde. Je nach Projekt und Teamgrösse/-fähigkeiten kann nicht alles abgehakt werden. Beschreiben Sie bitte genau, was Sie im Bereich Qualitätssicherung alles unternommen haben*

- Festlegen der Coding Guidelines

- Festlegen der Definition of Done

- Bugs immer in Redmine oder JIRA eingetragen

- Stunden-Erfassung auf den Arbeitspaketen (damit man besser Soll und Ist vergleichen kann)

- Code-Reviews geplant und durchgeführt? (am besten vor jedem grösseren Meilenstein)

- Unit Tests (Microtesting und Integration Tests) von guter Aussagekraft? mit guter Abdeckung?

- Metriken laufen bei jedem Build auf CI Server? (und natürlich vernünftige Grenzwerte definiert)

- Static Code Analysis Tools laufen immer auf CI Server? (findbugs, Lint, checkstyle, ReSharper, ...)

- github Workflow mit Feature Branches und Pull Requests als minimales Vier-Augen-Prinzip

- Usability Testing gemacht? (früh als Paper Prototype, später mit richtiger Software). Erkenntnisse daraus? Resultierende (Umbau-)Arbeiten?

- Händische Systemtests gemacht? (z.B. mit Umbau von Use Cases zu Test Cases) Testdurchführungen protokolliert?

- Tests möglichst automatisiert? (Android: Espresso, Web Browser: Selenium, cypress.io)

- Dashboard wie z.B. SonarQube eingesetzt?

## Sicherung der Geschichte

*Welche Daten wurden wann gesichert, um später die Projekt-Histoy nachvollziehen zu können*

- Kompletter Export der Arbeitspakete/Tickets aus Redmine oder JIRA bei jedem Meilenstein (als CSV Datei)

- Metrik- und Code Analysis-Auswertungen bei jedem Meilenstein sichern (z.B. als HTML oder PDF, auch CSV Datei)

- Stunden-Buchhaltung bei jedem Meilenstein sichern (z.B. als CSV Datei)

- Dokumente (auch Wiki) bei jedem Meilenstein sichern (z.B. als PDF Dateien)
