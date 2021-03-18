# Projektplan

## Einführung

### Zweck

Dieses Dokument gibt eine Übersicht über die Art und Weise wie wir unser Projekt CapWatch durchführen werden.

### Gültigkeitsbereich

Dieses Dokument ist für die Stakeholder dieses Projektes. Dazu gehören die Betreuer, sowie die Entwickler. Es wurde im
Rahmen des Engineering Projekts der Fachhochschule Ost erstellt.

### Vorgehen zur Überarbeitung der Planung

Wenn wir die Planung nachträglich überarbeiten, wird diese Version von allen Zusammen in einem Meeting geprüft und abgenommen. 

### Referenzen

[Gitlab Dokumentation](https://docs.gitlab.com/ee/) \
[GitLab Time Tracker (gtt)](https://github.com/kriskbx/gitlab-time-tracker) \
[Youtrack](https://www.jetbrains.com/de-de/youtrack/)

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

Das Projekt unterliegt keinen speziellen Annahmen oder Einschränkungen. Die Dokumentation wird im Markdown-Format
erstellt und hat somit in der Erstellung einige Einschränkungen.

## Projektorganisation

Das Projekt wird durch fünf Software-Engineering Studenten der Ostschweizer Fachhochschule am Campus Rapperswil
durchgeführt. Alle Projektbeteiligten studieren im berufsbegleitenden Studienmodell und arbeiten nebenbei bis zu 70
Prozent für ihre Arbeitgeber. Einige Teammitglieder haben Spezialgebiete, nach welchen auch die Verantwortlichkeiten
verteilt werden. Betreut wird das Projekt durch den Advisor Herrn Thomas Kälin.

Wir im Team verwenden Microsoft Teams für die Meetings und die Dateiablage. Microsoft OneNote wird für diverse Notizen,
Meeting-Protokolle und weiteres genutzt, was nicht direkt in die offizielle Dokumentation muss. Zusätzlich verwenden wir
alle, für unser Projekt sinnvolle, Funktionen von GitLab. Die Nutzung von folgenden Funktionen ist geplant:

- Repositories in Subgruppen
- Analytics
- Integration von diversen Tools (SonarQube und Renovate)

Die Nutzung der folgenden Gitlab Funktionen wurden wegen diverser Probleme (siehe Abschnitt Arbeitspakete) verworfen:

- Issues mit Kanban Board
- Script für den Time Tracking Report (gtt)

Als Ersatz zu den oben erwähnten, gestrichenen Gitlab Funktionen verwenden wir [Youtrack](https://www.jetbrains.com/de-de/youtrack/) von Jetbrains mit den folgenden Funktionen:

- Issues mit Kanban Board
- Integriertes Timetracking


### Organisationsstruktur

```eval_rst
+-----------------------+---------------------------------------------+
| Name                  | Verantwortlichkeiten                        |
+=======================+=============================================+
| Jonas Hauser          | Projektleitung, Kommunikation,              |
|                       | Arbeitsorganisation, Qualitätssicherung und |
|                       | Meeting-Moderator                           |
+-----------------------+---------------------------------------------+
| Rafael Fuhrer         | Alles rund um Systemumgebungen wie z. B.    |
|                       | CI/CD, GitLab und Deploy-Server             |
+-----------------------+---------------------------------------------+
| Pascal Schneider      | Lead für Software-Architektur und -Design   |
|                       | und API-Design, GitLab Issue Time-Tracking  |
+-----------------------+---------------------------------------------+
| Christoph Scheiwiller | Allgemeine Codequalität (Guidelines und     |
|                       | Testing)                                    |
+-----------------------+---------------------------------------------+
| Pascal Schlumpf       | Daten- bzw. Datenbank-spezialist            |
+-----------------------+---------------------------------------------+
```

Alle beteiligten sind gleichberechtigte Teammitglieder und wir verfolgen eine komplett flache Hierarchie untereinander.
Der Projektleiter ist in keinem Fall ein Mitarbeiter mit höheren Befugnissen oder höherer Entscheidungsmacht.

Da wir Scrum als Projektmanagement Methode verwenden, haben wir ausserdem die folgenden Scrum Rollen besetzt.

```eval_rst
=============== =============
Name            Scrum Rolle
=============== =============
Jonas Hauser    Scrum Master
Pascal Schlumpf Product Owner
=============== =============
```

### Externe Schnittstellen

Wir werden unterstützt und betreut durch den Advisor Herrn Thomas Kälin. In einzelnen Fällen ziehen wir die Expertise
von anderen Studenten, anderen Betreuern und Modulverantwortlichen hinzu oder fragen bestimmte Zielgruppen für manuelle
Benutzertests an.

## Management Abläufe

### Kostenvoranschlag

Unser Projekt wird auf 15 Semesterwochen aufgeteilt, was dem Standard der Vorgaben für das Engineering Projekt
entspricht. Dies bedeutet ein durchschnittliches Arbeitspensum von ungefähr 8 Stunden pro Person pro Woche. Je nach
Arbeitsaufwand pro Woche kann dieser Wert stark variieren. Der Endwert von mindestens 120 Stunden pro Person nach 15
Wochen wird aber zwingend eingehalten.

### Zeitliche Planung

Die grobe Zeitplanung wurde nach den Vorgaben von RUP durchgeführt.

![rup-time-table](/images/rup-time-table.png)

#### Phasen / Iterationen

In der Entwicklung wird mit Sprints gearbeitet. Es gibt in jedem Sprint einen Meilenstein, welcher abgeschlossen werden
muss. Für die grobe Planung beziehungsweise für die Phasen gehen wir nach dem RUP-Modell vor.

##### *RUP-Phasen*

###### *Inception*

In der ersten einwöchigen Phase werden die Anwendungsfälle grob beschrieben, damit haben wir ein klares Ziel für die
Applikation CapWatch definiert.

###### *Elaboration*

In der Elaboration wird während vier Wochen ein Architekturprototyp erstellt. Die Anwendungsfälle werden detailliert
beschrieben. Projektplanung sowie Risikoanalyse werden durchgeführt.

###### *Construction*

In dieser Phase wird das Produkt CapWatch entwickelt und getestet. Während acht Wochen entsteht die Applikation auf
Grundlage der vorher definierten Anwendungsfälle.

###### *Transition*

Die Applikation CapWatch ist in der ersten Version zur Auslieferung bereit. Während zwei Wochen kann die Software
eingeführt und getestet werden.

##### *Scrum*

Nach dem Erreichen des ersten Meilensteins beginnen wir iterativ mit Scrum zu arbeiten. Es wurden sechs Sprints
definiert. Jeder Sprint dauert zwei Wochen, mit Ausnahme des fünften Sprints, welcher drei Wochen dauert. Am Ende jedes
Sprints ist der vorgegebene Meilenstein zu erreichen.

Für die Priorisierung der Tasks im Backlog verwenden wir die MoSCoW Methode.
Die Aufwandsschätzungen der Taks werden in absoluten Stunden vorgenommen. 

#### Meilensteine

**M1 Project Plan** (06.03.2021)

- Projektorganisation
- Arbeitspakete definiert
- Phasen und Meilensteine
- Qualitätsmassnahmen
- Richtlinien für Code und Dokumentation
- Build Server & Continuous Integration geplant
- Infrastruktur geplant
- Zeitplanung erstellt

**M2 Requirements** (20.03.2021)

- Use Cases erstellt
- Funktionale Anforderungen formuliert
- Nichtfunktionale Anforderungen formuliert
- Schnittstellen beschreiben
- Wireframes erstellt
- Domainmodell Diagramme gezeichnet

**M3 End of Elaboration / Prototyp** (03.04.2021)

- Architekturprototyp erstellt
- Architekturprototyp getestet
- Architekturprototyp Dokumentation vorbereitet
- Anforderungen vollständig definiert
- Test- und Reviewprozess definiert
- Risikoanalyse nachgeführt
- Entwicklungsumgebung komplett eingerichtet

**M4 Architecture** (17.04.2021)

- Physische und logische Architektur
- Persistenz
- User Interface
- Ausbau-Szenarien berücksichtigt
- Performance-Szenarien
- Verwendete Technologien
- Architektur Entscheidungen dokumentiert
- Besondere Merkmale der Architektur

**M5 Quality** (01.05.2021)

- Dokumentationsreview
- Testcases geplant, dokumentiert und umgesetzt
- Verwendung von Tools zur Sicherstellung der Codequalität (Bsp. Coderichtlinien)

**M6 Beta Version** (15.05.2021)

- Gesamter Funktionsumfang implementiert
- Funktionale Anforderungen getestet
- Manuelle Tests durchgeführt
- Vorhandene Bugs identifiziert

**M7 Final Submission** (29.05.2021)

- Code-Repositories in abgabefähigem Zustand
- Dokumentations-Repository in abgabefähigem Zustand
- Fehler aus Betaversion behoben
- Projekt- und Produktpräsentation vorbereitet

### Besprechungen

Hier sind alle fixierten Termine aufgeführt. Falls nötig können auch spontane Besprechungen dazukommen, wobei nicht alle
Gruppenmitglieder anwesend sein müssen. Diese spontanen Besprechungen können von jedem Gruppenmitglied einberufen werden und ersetzen bei uns das Daily Standup Meeting, da dieses bei uns keinen Sinn machen würde. 

**Ort:** Bis auf Weiteres finden alle Besprechungen digital in Microsoft Teams statt.

```eval_rst
+----------------------+----------------------+----------------------+
| Wann                 | Wer                  | Grund                |
+======================+======================+======================+
| Jeden Montag 16:00   | Team / Advisor bei   | Fragen zu            |
| Uhr                  | bedarf               | Projektablauf oder   |
|                      |                      | Vorgehen             |
+----------------------+----------------------+----------------------+
| Jeden Donnerstag     | Alle im Team         | Aktueller Stand,     |
| 16:00 Uhr            |                      | Offene Fragen        |
|                      |                      | besprechen, Weiteres |
|                      |                      | Vorgehen             |
+----------------------+----------------------+----------------------+
| Jeweils zu Beginn    | Alle im Team         | Sprint Planning      |
| des Sprints 10:00    |                      |                      |
| Uhr                  |                      |                      |
+----------------------+----------------------+----------------------+
| Jeweils am Ende des  | Alle im Team         | Sprint Review und    |
| Sprints 17:00 Uhr    |                      | anschliessend        |
|                      |                      | Retrospektive        |
+----------------------+----------------------+----------------------+
| 08.03.2021 16:00 Uhr | Team / Advisor       | Review 1             |
+----------------------+----------------------+----------------------+
| 22.03.2021 16:00 Uhr | Team / Advisor       | Review 2             |
+----------------------+----------------------+----------------------+
| 05.04.2021 16:00 Uhr | Team / Advisor       | Review 3             |
+----------------------+----------------------+----------------------+
| 19.04.2021 16:00 Uhr | Team / Advisor       | Review 4             |
+----------------------+----------------------+----------------------+
| 03.05.2021 16:00 Uhr | Team / Advisor       | Review 5             |
+----------------------+----------------------+----------------------+
| 31.05.2021 16:00 Uhr | Team / Advisor       | Review 6             |
+----------------------+----------------------+----------------------+
```

Um zu verhindern, dass unsere Scrum-Events zeitlich aus dem Ruder laufen, haben wir die folgenden Timeboxings für die Events definiert.

```eval_rst
+----------------------+----------------------+----------------------+
| Scrum Event          | Timeboxing           | Bemerkung            |
+======================+======================+======================+
| Sprint Planning      | 1 Stunde             | -                    |
+----------------------+----------------------+----------------------+
| Sprint Review        | 45 Minuten           | variabel, wird evtl. |
|                      |                      | nochmals angepasst   |
+----------------------+----------------------+----------------------+
| Sprint Retrospektive | 30 Minuten           | variabel, wird evtl. |
|                      |                      | nochmals angepasst   |
+----------------------+----------------------+----------------------+
```

## Risikomanagement

### Risiken

Die Risikoanalyse wurde im Dokument risikoanalyse.md detailliert beschreiben.

### Umgang mit Risiken

Die Risiken R1-R3 haben ein geringes Schadenspotenzial und werden deshalb nicht genauer angeschaut. Risiko R4
Zeitmanagement mit einem gewichteten Schaden von 6 macht fast die Hälfte des möglichen Schadenspotenzials aus, deshalb
wurde die Zeitplanung genau besprochen. Im weiteren Projektverlauf soll dem Risiko R4 Zeitmanagement bei der
Aufwandsschätzung der Stories Beachtung geschenkt und ausreichende Reserven in die Sprints eingeplant werden. Mit oben
genannten Massnahmen sind wir zuversichtlich das Risiko möglichst gut im Griff zu haben. Die Risiken werden nach jedem
Sprint ausgewertet, dabei können Risiken wegfallen und neue hinzukommen. Dadurch soll sichergestellt werden, dass
mögliche neue Risiken beachtet und eingeschätzt werden und nicht mehr relevante Risiken entfernt werden.

## Arbeitspakete

Zur Planung der Arbeit, sowie dem Tracking der aufgewendeten Arbeitszeit haben wir ursprünglich Gitlab angedacht. Für die Auswertung der Zeiterfassung hätte [gtt](https://github.com/kriskbx/gitlab-time-tracker) zum Einsatz kommen sollen. 

Leider hat sich in der ersten Projektwoche gezeigt, dass die uns von Gitlab zur Verfügung gestellten Tools nur unzureichend funktionieren. Nach einem nicht lösbaren Problem mit dem Timetracking, haben wir nach Absprache mit unserem Advisor den umstieg auf [Youtrack](https://www.jetbrains.com/de-de/youtrack/) beschlossen. 


## Infrastruktur

Für die Verwaltung des Quellcodes und der Projektdokumentation verwenden wir das von der OST bereitgestellte GitLab,
inklusive der zur Verfügung gestellten Continuous Integration Lösung. Für das Deployment verwenden wir eine einzelne
virtuelle Maschine, basierend auf Ubuntu, welche uns ebenfalls von der OST zur Verfügung gestellt wird. Über die CI
Lösung werden automatisch Docker Images generiert, welche dann auf der Deployment-VM ausgeführt werden können. \
Die Entwicklung erfolgt auf unseren persönlichen Notebooks oder Desktop-PCs. Weitere spezielle Geräte werden nicht
benötigt.\
Zur Unterstützung verwenden wir im CI-Prozess zusätzlich das Codequalitätstool [SonarQube](https://www.sonarqube.org/)
und das Tool [Renovate](https://github.com/renovatebot/renovate) für das automatisierte Updaten von Dependencies.

## Qualitätsmassnahmen

Erstens werden für den Umgang mit Git diverse Richtlinien definiert um eine professionelle und einfache Zusammenarbeit
im Softwareentwicklungsprozess mit dem ganzen Team zu erreichen. \
Zweitens wird nach einem Vorgehen gearbeitet, bei dem grundsätzlich keine Änderungen in den Git Repositories verwendet
werden, welche nicht mindestens von einem weiteren Teammitglied in einem Review validiert und bestätigt wurden. Ausnahmen dabei sind triviale Konfigurationsarbeiten und Fehlerbehebungen, die sofort eingebracht werden müssen. Drittens werden mit jedem Build und auch mit jedem Deployment der Applikationen Sicherheit- und Integrationchecks durchgeführt durch SonarQube und Renovate.

Um diese Massnahmen für die Verbesserung der Qualität umsetzen zu können, verwenden wir die folgenden Gitlab Features:

- Merge- bzw. Pull-Requests
- CI / CD

Jedes Product Backlog Item wird ausserdem mit einer Definition of Done versehen, welche dem Bearbeitenden und dem Reviewer dabei hilft, die Vollständigkeit dieses Product Backlog Items zu prüfen. 

Zusätzlich setzen wir die folgenden Techniken ein, um eine hohe Qualität innerhalb des Projekts zu gewährleisten:

- Spezifikation von funktionalen und nicht funktionalen Requirements
- Einsatz von Unit, Usability, Integrations und Performance Tests
- Nutzung der Report Funktion (Dashboards) von Youtrack zur Informationsgewinnung

Um den erfolgreichen Verlauf des Projekts zu garantieren, ist der Projektleiter dafür verantwortlich, wöchentlich die
Einhaltung der Qualitätsmassnahmen zu überprüfen und Abweichungen den Teammitgliedern mitzuteilen. Der Projektleiter
arbeitet nach einer wöchentlichen Checkliste, damit nichts vergessen wird.\
Das Team arbeitet nach dem Erreichen des ersten Meilensteins nach Scrum und garantiert somit pro Sprint fertige Teile des Produkts vorweisen zu können.

### Dokumentation

Die Dokumentation wird mit Markdown erstellt, basierend auf dem offiziellen Template der Ost. Der Produktionsbranch (
master) wird jeweils als Basis für den aktuellen Stand der Dokumentation verwendet. Neue Bereiche oder
Dokumentationsvorschläge werden über Supportbranches (feature und bugfix) erstellt, validiert und in den
Produktionsbranch zusammengeführt. Jeder neuer Teil der Dokumentation wird jeweils immer von mindestens einem
Teammitglied überprüft. Vor jedem Reviewtermin mit dem Advisor werden nochmals erneut alle geänderten Bereiche seit dem
letzten Review auf dem Produktionsbranch überprüft.

### Projektmanagement

Wir wollten ursprünglich die [Issues Integration](https://gitlab.ost.ch/groups/epj/2021-FS/g03_capwatch/-/issues) von GitLab selbst verwenden. Wegen den im Punkt Arbeitspakete beschriebenen Probleme kommt seit der zweiten Projektwoche aber Youtrack zum Einsatz. Die Issues durchlaufen einen klaren Workflow der
als [Kanban Board](https://capwatch.myjetbrains.com/youtrack/agiles/120-2/current) angezeigt wird. Jedes Issue
durchläuft folgende Schritte: open, planned, work in progress, review und closed. Die Issues werden am Anfang in einem
groben Format erstellt und warten dann im Status *open* auf deren Einplanung in einen Sprint, wodurch sie in den Status
*planned* wechseln. Das Arbeitspaket wird beim Start in den Status *work in progress* versetzt und vor Beendigung in den
Status *review*, um einen Review und je nachdem auch Testing durchzuführen. Im Status *closed* ist das Issue dann
komplett fertig und somit auch auf einem archivierten Stand.

### Entwicklung

Der Sourcecode vom Backend und Frontend befindet sich in einer
eigenen [Subgruppe](https://gitlab.ost.ch/epj/2021-FS/g03_capwatch/development)
in unserem GitLab Projekt als jeweils eigene Repositories.

Spezielle Qualitätsmassnahmen spezifisch für den Sourcecode wurden bereits durch die allgemeinen Qualitätsmassnahmen an
das ganze Projekt definiert.

#### Vorgehen

Wir entwickeln vollständig nach dem Prinzip der agilen Softwareentwicklung mit Scrum und entwickeln demnach in
Iterationen nach und nach Teile der Applikationen. Der Sourcecode wird klassisch und nach Features entwickelt, ohne dabei
zuerst Tests zu schreiben (kein Test Driven Development). Die Logik der Features wird zuerst implementiert und danach
werden die Unit Tests dazu geschrieben. Im Frontend verzichten wir auf automatisierte Tests, weil der Projektumfang zu
klein ist und der Aufwand dafür zu gross wäre. Das ganze Frontend wird manuell getestet.

#### Unit Testing

Automatisierte UnitTests werden ausschliesslich im Backend geschrieben. Der Grund hierfür ist, dass jegliche
Business-Logik, welche auf die Daten angewandt werden muss, bei der Aufbereitung der Daten vor dem Bereitstellen durch
die jeweiligen API's ausgeführt wird. Das FrontEnd wird lediglich die Rückgaben aus den API’s visuell zur Verfügung
stellen.

Die Tests im Backend werden technologisch mit [xUnit](https://www.nuget.org/packages/xunit/)
, [FluentAssertions](https://www.nuget.org/packages/FluentAssertions/6.0.0-alpha0002)
und [FakeItEasy](https://www.nuget.org/packages/FakeItEasy/7.0.0-beta.2) umgesetzt.

Um sicherzustellen, dass die Testabdeckung ausreichend ist, wird die in Visual Studio Enterprise verfügbare
Funktionalität "Analyze Code Coverage for All Tests" verwendet.

#### Code Reviews

Wie bereits im Kapitel zu den allgemeinen Qualitätsmassnahmen beschrieben, erstellen wir grundsätzlich immer Pull
Requests die von mindestens einem weiteren Teammitglied überprüft wird. Es wird immer mit Supportbranches gearbeitet und
nach dem Code Review erst die Zusammenführung auf einen Mainbranch gemacht.

#### Code Style Guidelines

Die folgenden Guidelines gelten als Ausgangspunkt, wie der Quellcode im Front- und Backend formatiert werden soll.
Etwaige Abweichungen, welche sich als sinnvoll herausstellen, müssen im Team besprochen und von diesem abgenommen
werden.

| Programmiersprache | Grundlage |
| ------------------ | --------- |
| .NET               | [C# Coding Conventions von Microsoft](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/inside-a-program/coding-conventions) |
| HTML / CSS         | [Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html) |
| TypeScript         | [Google TypeScript Style Guide](https://google.github.io/styleguide/tsguide.html) |
| React              | [React + Typescript Cheatsheets](https://github.com/typescript-cheatsheets/react) |
| JSX                | [React JSX](https://reactjs.org/docs/introducing-jsx.html)

##### Abweichungen von den Grundlagen

###### .Net

* Wir verwenden nicht die Standard IDE Einstellungen von Microsoft Visual Studio, sondern diejenigen aus dem Einstellungs-Backup *Exported-2021-02-04.vssettings*
* Wir verwenden LINQ ausschliesslich in der Methoden-Syntax

###### HTML / CSS

* Wir verwenden die Standard IDE Einstellungen von JetBrains Webstorm (auch die Standardformatierung)
* Bei HTML und CSS haben wir keine spezifischen Abweichungen von den Code Guidelines definiert

###### TypeScript

* Wir verwenden die Standard IDE Einstellungen von JetBrains Webstorm (auch die Standardformatierung)
* Bei der Aufsetzung vom Frontend-Repository wird TSLint installiert und konfiguriert

###### React + Typescript und JSX

* Wir verwenden die Standard IDE Einstellungen von JetBrains Webstorm (auch die Standardformatierung)
* Bei React, zusammen mit TypeScript, haben wir keine spezifischen Abweichungen von den Cheatsheets definiert
* Bei JSX haben wir keine spezifischen Abweichungen von der offiziellen React JSX Dokumentation vordefiniert

#### Software-Engineering Prinzipien

Um Maintainability und Qualität der Code Basis zu gewährleisten werden gängige Software-Engineering Prinzipien stets
berücksichtigt. Diese umfassen KISS, YAGNI, DRY, BDUF und S.O.L.I.D.

### Testen

#### Unit Tests

Siehe Kapitel *Unit Testing* unter *Entwicklung*.

#### Integrationstests

Integrationstests werden manuell nach Fertigstellung jedes Sprintumfangs durchgeführt. Hierfür wird beim Erstellen der
Detailspezifikationen eine Liste an benötigten Tests erstellt, welche in eine Gesamtliste an durchzuführenden
Integrationstests eingepflegt wird.

#### Performancetests

Da beim Backend über die Update API der Geschäfte theoretisch relativ viel Traffic eingehen kann, wird das Backend vor
jedem Release auf seine Performance getestet. Hierfür verwenden wir [Apache JMeter](https://jmeter.apache.org/).

#### Usability Tests

Um die Benutzerfreundlichkeit unseres Projekts sicherzustellen, werden wir auf manuell durchgeführte Usability Tests setzen, da diese mit vergleichsweise wenig Aufwand sehr viel wertvolles Feedback zur Qualität und zu möglichen Verbesserungen liefern.
