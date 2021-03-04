# Projektplan

## Einführung

### Zweck

<!-- TODO TBD -->

*Zweck des Dokumentes*

### Gültigkeitsbereich

<!-- TODO TBD -->

*Gültigkeitsbereich des Dokumentes*

### Referenzen

<!-- TODO TBD -->

*Liste aller verwendeten und referenzierten Dokumente, Bücher, Links, usw.*

*Referenz auf ein Glossar Dokument, wo alle Abkürzungen und unklaren Begriffe erklärt werden*

*Die Quellen / Referenzen sollten (falls möglich) automatisch erstellt werden*

## Projekt Übersicht

Eine Webapplikation, in der man seine Lieblingsgeschäfte, Saunas, etc. abonnieren kann. Die Daten werden bei einem
Abonnement dann in Echtzeit aktualisiert. Die Daten werden von den Dienstleistern über eine API an das Backend geliefert
und in einer Datenbank abgelegt. Das Backend besteht aus insgesamt zwei zentralen API’s. Die zweite Schnittstelle ist
für die Datenauslieferung an das Frontend bzw. die Webseite, welche schlussendlich der Benutzer verwendet für die
Abonnements. Das Frontend ist ein reiner, einseitiger Empfänger ohne Authentifizierung in einer ersten Version.

### Zweck und Ziel

Real-time Daten zur Anzahl Personen in einem Raum oder Gebäude, welche eine Personenbeschränkung aufgrund einer Pandemie
oder einem sonstigen Grund haben, wie z. B. Geschäfte, Saunen, Bäder, Sportanlagen etc. um das persönliche Einkaufs- und
Konsumverhalten besser planen bzw. anpassen zu können. Es entstehen dabei sowohl Vorteile für die Anbieter und die
Konsumenten. Die Anbieter können Dienstleistungsendpässe vermeiden, welche zu einem Besucherverlust führen könnten. Die
Konsumenten profitieren von kurzen Wartezeiten und somit auch besseren Verkaufsdienstleistung wie z. B. Beratungen.

Die Ziele des Teams sind eine allgemein gut funktionierende, erweiterbare, performante und benutzerfreundliche Plattform
für die Endkunden, wie aber auch für die Datenlieferanten. Die Weblösung soll einfach zu bedien sein und das Leben
vereinfache, vor allem in der Zeit einer Pandemie wo Einschränkungen vom Konsumverhalten der Bevölkerung gefordert wird.

### Lieferumfang

- Offizielle Dokumentation des Projektes in Form des Templates der OST
- Frontend für den Endbenutzer
- Backend-API bestehend aus zwei logisch getrennten API’s

### Annahmen und Einschränkungen

Der Projektplan unterliegt keinen Annahmen oder Einschränkungen. Die Dokumentation wird im Readme-Format erstellt und
hat somit in der Erstellung einige Einschränkungen.

## Projektorganisation

Das Projekt wird durch fünf Software-Engineering Studenten der Ostschweizer Fachhochschule am Campus Rapperswil
durchgeführt. Alle Projektbeteiligten studieren im berufsbegleitenden Studiumsmodell und arbeiten nebenbei bis zu 70
Prozent für ihre Arbeitgeber. Einige Teammitglieder haben spezialgebiete, nach welchen auch die Verantwortlichkeiten
verteilt werden. Betreut wird das Projekt durch den Advisor Herrn Thomas Kälin.

Wir im Team verwenden Microsoft Teams für die Meetings und die Dateiablage. Microsoft OneNote wird für diverse Notizen,
Meeting-Protokolle und weiteres genutzt, was nicht direkt in die offizielle Dokumentation muss. Zusätzlich verwenden wir
alle, für unser Projekt sinnvolle, Funktionen von GitLab. Die Nutzung von folgenden Funktionen ist geplant:

- Repositories in Subgruppen
- Issues mit Kanban Board
- Merge- bzw. Pull-Requests
- CI / CD
- Analytics
- Integration von diversen Tools (genauere Beschreibung zu einem späteren Zeitpunkt)

<!-- TODO Liste oben überprüfen -->

### Organisationsstruktur

| Name                       | Verantwortlichkeiten      |
| -------------------------- | ------------------------- |
| Jonas Hauser               | Projektleitung, Kommunikation, Arbeitsorganisation, Qualitätssicherung und Meetingmoderator  |
| Rafael Fuhrer              | Alles rund um Systemumgebungen wie z. B. CI/CD, GitLab und Deploy-Server            |
| Pascal Schneider           | Lead für Software-Architektur und -Design und API-Design, GitLab Issue Time-Tracking            |
| Christoph Scheiwiller      | <!-- TODO --!>            |
| Pascal Schlumpf            | Daten- bzw. Datenbank-spezialist            |

Alle beteiligten sind gleichberechtigte Teammitglieder und wir verfolgen eine komplett flache Hierarchie untereinander.
Der Projektleiter ist in keinem Fall ein Mitarbeiter mit höheren Befugnissen oder höherer Entscheidungsmacht.

### Externe Schnittstellen

Wir werden unterstützt und betreut durch den Advisor Herrn Thomas Kälin. In einzelnen Fällen ziehen wir die Expertise
von anderen Studenten und oder anderen Advisoren und Modulverantwortlichen hinzu oder fragen bestimmte Zielgruppen als
Tester an.

## Management Abläufe

### Kostenvoranschlag

Unser Projekt wird auf 14 Studiumwochen aufgeteilt, was dem Standard der Vorgaben für das Engineer Projekt entspricht.
Dies bedeutet ein durchschnittliches Arbeitspensum von ungefähr 8.6 Stunden pro Person pro Woche. Je nach Arbeitsaufwand
pro Woche kann dieser Wert stark variieren. Der Endwert von mindestens 120 Stunden pro Person nach 14 Wochen wird aber
zwingend eingehalten.

### Zeitliche Planung

<!-- TODO Christoph, Rafael -->

*Kurze Beschreibung der zeitlichen Planung und mit einer Grafik einen Überblick über die Phasen, Iterationen und
Meilensteine geben.*
*Das Datum des Eintreffens der Meilensteine sollte in der Phasenübersicht ersichtlich sein.*

#### Phasen / Iterationen

##### *Bezeichnung der einzelnen Phasen*

*Kurze Beschreibung und Dauer der Phase angeben*

###### *Bezeichnung der einzelnen Iterationen*

*Kurze Beschreibung und Dauer der Iteration angeben*

*Vorgehen bei Iterationsplanung und Iterationsassessment*

#### Meilensteine

##### *Bezeichnung der einzelnen Meilensteine*

*Setzen Sie in Ihrem Projekt 6-8 Meilensteine. Kurze Beschreibung der Meilensteine mit genauem Datum.*

*In der Regel auf Ende jeder Iteration einen Meilenstein setzen (diese Faustregel gilt nur für die SE-2Projekte, in
realen Projekten haben Sie oft deutlich mehr Iterationen als Meilensteine, weil Meilensteine dort die nach aussen
kommunizierten Ereignisse sind).*

*Schreiben Sie zu jedem Meilenstein auf, welche Arbeitsprodukte (work products) Sie dann abliefern werden.*

*Spezifizieren Sie wenn nötig auch den Fertigstellungsgrad der Arbeitsprodukte, z.B. „Zentrale Use Cases ‚fully
dressed‘, restliche UCs im ‚brief‘ Format“, oder „Architekturskizze inkl. Definition der Interfaces zwischen
Sub-Systemen und Deployment Diagramm“*

### Besprechungen

Hier sind alle fixierten Termine aufgeführt. Falls nötig können auch spontane Besprechungen dazukommen, wobei nicht alle Gruppenmitglieder anwesend sein müssen. 

**Ort:** Bis auf weiteres finden alle Besprechungen in Microsoft Teams statt.

| Wann                       | Wer                       | Grund                                                        |
| -------------------------- | ------------------------- | ------------------------------------------------------------ |
| Jeden Montag 16:00 Uhr     | Team / Advisor bei bedarf | Fragen zu Projektablauf oder Vorgehen                        |
| Jeden Donnerstag 16:00 Uhr | Alle im Team              | Aktueller Stand, Offene Fragen besprechen, Weiteres Vorgehen |
| 08.03.2021 16:00 Uhr       | Team / Advisor            | Review 1                                                     |
| 22.03.2021 16:00 Uhr       | Team / Advisor            | Review 2                                                     |
| 05.04.2021 16:00 Uhr       | Team / Advisor            | Review 3                                                     |
| 19.04.2021 16:00 Uhr       | Team / Advisor            | Review 4                                                     |
| 03.05.2021 16:00 Uhr       | Team / Advisor            | Review 5                                                     |
| 31.05.2021 16:00 Uhr       | Team / Advisor            | Review 6                                                     |

## Risikomanagement

### Risiken

*Verweis auf Dokument TechnischeRisiken.xlsx*

### Umgang mit Risiken

*Begründungen zur Tabelle. Weitere Beschreibungen zu Massnahmen und Vorbeugungen.*
*Werden Reserven /Rückstellungen eingeplant? Wieso und wie viele?*
*Wann werden Risiken qualitätssichernd überprüft (Vorgehen und Zeitpunkt(e) zur Neubeurteilung der Risiken)?*

## Arbeitspakete

Zur Planung der Arbeit, sowie dem Tracken der aufgewendeten Arbeitszeit verwenden wir GitLab. Für die Auswertung der
Zeiterfassung kommt [gtt](https://github.com/kriskbx/gitlab-time-tracker) zum Einsatz.

[Board der Arbeitspakete](https://gitlab.ost.ch/groups/epj/2021-FS/g03_capwatch/-/boards)

## Infrastruktur

*Benötigte Infrastruktur aufzählen. Spezielle Geräte, Laptop , Tools usw. und nötigenfalls aufzeigen für welche Bereiche
diese verwendet werden. Eventuell auch Verfahren beschreiben (auf Tools bezogen).*

## Qualitätsmassnahmen

Erstens werden für den Umgang mit Git diverse Richtlinien definiert um eine professionelle und einfache Zusammenarbeit
im Softwareentwicklungsprozess mit dem ganzen Team zu erreichen. \
Zweitens wird nach einem Vorgehen gearbeitet, bei dem grundsätzliche keine Änderungen in den Git Repositories verwendet
werden, welche nicht mindestens von einem weiteren Teammitglied validiert und bestätigt wurden. Ausnahmen dabei sind
triviale Konfigurationsarbeiten und Fehlerbehebungen, die sofort eingebracht werden müssen. Drittens werden mit jedem
Build und auch mit jedem Deployment der Applikationen Sicherheit- und Integration-checks durchgeführt durch SonarQube
und Renovate.

Um den erfolgreichen Verlauf des Projekts zu garantieren ist der Projektleiter dafür verantwortlich, wöchentlich die
Einhaltung der Qualitätsmassnahmen zu überprüfen und Abweichungen den Teammitgliedern mitzuteilen. Der Projektleiter
arbeitet nach einer wöchentlichen Checkliste, damit nichts vergessen wird.\
Das Team arbeitet nach dem Erreichen vom Meilenstein 1 nach Scrum und garantiert somit pro Sprint fertige Teile des
Produkts vorweisen zu können.

### Dokumentation

Die Dokumentation wird, basierend auf dem offiziellen Template der Ost, erstellt mit Markdown. Der Produktionsbranch (
master) wird jeweils als Basis für den aktuellen Stand der Dokumentation verwendet. Neue Bereiche oder
Dokumentationsvorschläge werden über Supportbranches (feature und bugfix) erstellt, validiert und in den
Produktionsbranch zusammengeführt. Jeder neuer Teil der Dokumentation wird jeweils immer von mindestens zwei
Teammitgliedern überprüft. Vor jedem Reviewtermin mit dem Advisor werden nochmals erneut alle geänderten Bereiche seit
dem letzten Review auf dem Produktionsbranch überprüft.

### Projektmanagement

Wir verwenden die [Issues Integration](https://gitlab.ost.ch/groups/epj/2021-FS/g03_capwatch/-/issues) von GitLab selbst
mit integriertem Time-Tracking. Die Issues durchlaufen einen klaren Workflow der
als [Kanban Board](https://gitlab.ost.ch/groups/epj/2021-FS/g03_capwatch/-/boards) angezeigt wird. Jedes Issue durch
läuft folgende Schritte: open, planned, work in progress, review und closed. Die Issues werden am Anfang in einem groben
Format erstellt und warten dann im Status *open* auf deren Einplanung in einen Sprint, wodurch sie den Status
*planned* wechseln. Das Arbeitspaket wird beim Start in den Status *work in progress* versetzt und vor Beendigung in
den Status *review*, um einen Review und je nachdem auch Testing durchzuführen. Im Status *closed* ist das Issue dann
komplett fertig und somit auch in einem archivierten Standpunkt.

### Entwicklung

Der Sourcecode vom Backend und Frontend befindet sich in einer
eigenen [Subgruppe](https://gitlab.ost.ch/epj/2021-FS/g03_capwatch/development)
in unserem GitLab Projekt als jeweils eigene Repositories.

Spezielle Qualitätsmassnhamen spezifischen für den Sourcecode wurden bereits durch die allgemeinen Qualitätsmassnahmen
an das ganze Projekt definiert.

#### Vorgehen

Wir entwickeln vollständige mit dem Prinzip der Agile Softwareentwicklung mit Scrum und entwickeln demnach in
Iterationen nach und nach teile der Applikationen. Der Sourcecode wird klassisch und nach Features entwickelt ohne dabei
zuerst Tests zu schreiben (kein Test Driven Development). Die Logik der Features wird zuerst implementiert und danach
werden die Unit Tests dazu geschrieben. Im Frontend verzichten wir auf automatisierte Tests, weil der Projektumfang zu
klein ist und der Aufwand dafür zu gross wäre. Das ganze Frontend wird manuell getestet.

#### Unit Testing

Automatisierte UnitTests werden ausschliesslich im Backend geschrieben. Der Grund hierfür ist, dass jegliche Business-Logik, welche auf die Daten angewandt werden muss, bei der Aufbereitung der Daten vor dem Bereitstellen durch die jeweiligen API's ausgeführt wird. Das FrontEnd wird lediglich die Rückgaben aus den API's visuell zur Verfügung stellen.

Die Tests im Backend werden technologisch mit [xUnit](https://www.nuget.org/packages/xunit/), [FluentAssertions](https://www.nuget.org/packages/FluentAssertions/6.0.0-alpha0002) und [FakeItEasy](https://www.nuget.org/packages/FakeItEasy/7.0.0-beta.2) umgesetzt.

Um sicherzustellen, dass die Testabdeckung ausreichend ist, wird die in Visual Studio Enterprise verfügbare Funktionalität "Analyze Code Coverage for All Tests" verwendet.

#### Code Reviews

Wie bereits im Kapitel zu den allgemeinen Qualitätsmassnahmen beschrieben, erstellen wir grundsätzlich immer Pull
Requests die von mindestens einem weiteren Mitarbeiter überprüft wird. Es wird immer mit Supportbranches gearbeitet und
nach dem Code Review erst die Zusammenführung auf einen Mainbranch gemacht.

#### Code Style Guidelines

Die folgenden Guidelines gelten als Ausgangspunkt, wie der Quellcode im Front- und Backend formatiert werden soll. Etwaige Abweichungen, welche sich als sinnvoll herausstellen, müssen im Team besprochen und von diesem abgenommen werden.

| Programmiersprache | Grundlage |
| ------------------ | --------- |
| .NET               | [C# Coding Conventions von Microsoft](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/inside-a-program/coding-conventions) |
| HTML / CSS         | [Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html) |
| TypeScript         | [Google TypeScript Style Guide](https://google.github.io/styleguide/tsguide.html) |

#### Software Engineering Prinzipien

Um Maintainability und Qualität der Code Basis zu gewährleisten werden gängige Software Engineering principles stets berücksichtigt. Diese umfassen KISS, YAGNI, DRY, BDUF und S.O.L.I.D.

### Testen

#### Unit tests

Siehe Kapitel *Unit Testing* unter *Entwicklung*

#### Integration tests

Integrationstests werden manuell nach Fertigstellung jedes Sprintumfangs durchgeführt. Hierfür wird beim Erstellen der Detailspezifikationen eine Liste an benötigten Tests erstellt, welche in eine Gesamtliste an durchzuführenden Integrationstests eingepflegt wird.

#### Performance tests

Da beim Backend über die Update API der Geschäfte theoretisch relativ viel Traffic eingehen kann, wird das Backend vor jedem Release auf seine Performance getestet. Hierfür verwenden wir [Apache JMeter](https://jmeter.apache.org/).