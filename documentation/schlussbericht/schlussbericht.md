### Schlussbericht

## Einführung

### Zweck

Dieses Dokument fasst unsere Erfahrungen und Ergebnisse des Projektes zusammen.

### Gültigkeitsbereich

Dieses Dokument ist gültig für das Engineering Projekt im Frühlingssemester 2021 an der Fachhochschule OST. Es ist für die Betreuer und Entwickler dieses Projektes ausgelegt.

## Zielerreichung

Wir konnten das Projekt erfolgreich abschliessen, da wir alle unsere MUSS-Ziele erreicht haben. Da unser Fokus auf Qualität gerichtet war, lag es nicht mehr drin, ein KANN-Ziel umzusetzen. Sofern man einen Laden findet, der Daten anliefert, kann man unsere Applikation einwandfrei verwenden. Das Design sieht ansprechend aus und sieht sowohl auf Mobile wie auch auf Desktopsystemen gut aus. Der Code und die ganze Architektur haben eine sehr hohe Qualität und es wurden auch viele Qualitätssichernde Massnahmen umgesetzt.

## Allgemeiner Erfahrungsbericht

### Projektmanagement

Unsere Zusammenarbeit mit SCRUM funktionierte ziemlich gut und es hat uns sehr gut unterstützt im Projekt. Unsere Schätzgenauigkeit war bei unseren zwei Wöchigen Sprints, schon von Beginn weg, erstaunlich genau. Wir haben jeweils pro Sprint ein Backlog Refinement, Sprint Planning, Sprint Review und als Abschluss eine Sprint Retrospektive gemacht. Auf die Daily Standup Meetings haben wir verzichtet, da es für uns nicht möglich war mit unserem Teilzeitpensum einen täglichen Termin einzuplanen. Bei den Retrospektiven haben wir verschiedene Formen ausprobiert. Diese haben uns geholfen die Problem in der Zusammenarbeit früh anzusprechen und so jeden Sprint besser zu werden. Da wir uns nicht physisch treffen konnten, haben wir uns auf einer virtuellen Kollaborationsplattform ausgetauscht. Nachfolgend zwei der verschiedenen Formen die wir ausprobiert haben:



#### Seestern

Zu Beginn der Retrospektive zeichnet der Scrum Master einen „Seestern“ an das Whiteboard oder auf den Flipchart.

Die Mitglieder des Scrum-Teams notieren auf Post-it’s eine Antwort zu jeder der folgenden Fragen:

- Was müssen wir fortsetzen?
- Was müssen wir intensivieren?
- Was müssen wir zurückfahren?
- Womit müssen wir beginnen?
- Womit müssen wir aufhören?

![Seestern](../../images/Seestern.png)



#### K.A.L.M.

K.A.L.M. steht für:

- Keep – Etwas, das vom Team gut gemacht wird und fortgesetzt werden muss

- Add – Eine neue Idee, die der Verbesserung dient

- Less – Etwas, das gegenwärtig gemacht wird, jedoch nicht zum Erreichen des Ziels beiträgt

- More – Etwas, das gegenwärtig gemacht wird und zum Erreichen des Ziels beitragen kann, wenn es intensiviert wird.

  ![KALM.png](../../images/KALM.png)

Wir hatten die Projektrollen Scrum Master und Product Owner. Unser Scrum Master hat ebenfalls die Rolle des Projektleiters wahrgenommen. Diese Zentrale Rolle war sehr wichtig, da sie einerseits die zentrale Ansprechstelle war für unser Team und andererseits den Fortschritt des Sprints genau verfolgte und auf einzelne Teammitglieder zuging, wenn noch nicht so viel umgesetzt worden ist. Zusätzlich hat er die Meetings moderiert und geschaut, dass wir keine Zeit verschwenden. Dadurch konnten wir den Umfang des Sprints bis auf kleine Ausnahmen jeweils Umsetzen. 

Unsere informelle zentrale Dokumentation wurde in OneNote geführt. Dort haben wir alle Meeting Protokolle mit Entscheidungen und Aufträgen dokumentiert, unsere Definition of Done definiert und andere Wichtige Punkte, welche wichtig waren für das Projekt, niedergeschrieben. Dies hat gut funktioniert und auch garantiert, dass alle Informationen nur an einem Ort gesammelt wurden. Und durch das führen von Protokollen konnte man immer nochmals nachlesen was besprochen worden ist.

Unsere Kommunikation wurde über die Kanäle Whatsapp, für Ankündigungen und Informationen, sowie MS Teams, für Meetings und bilaterale Besprechungen, geführt. Zu Beginn hat die Information von Teammitgliedern noch nicht so gut funktioniert. Dies hat sich im Verlauf des Projektes aber verbessert.

Wir haben am Anfang Gitlab benutzt als Tracking System, dieses aber aufgrund verschiedenen Gründen, welches wir im Dokument Projektplan genauer beschrieben haben, durch YouTrack ersetzt. Gitlab verwendeten wir nur noch für die Sourcen Verwaltung und Generierung der Dokumente und  Container über die Pipeline. Die Verfügbarkeit von Gitlab und der Pipeline liess sehr zu wünschen übrig und war Zeitweise sehr Frustrierend, so dass wir sogar hier überlegt haben, die Plattform zu wechseln.

### Dokumentation

Die Dokumentationsvorlage war für uns zuerst sehr Verwirrend, da wir es so verstanden haben, dass man alle Punkte, welche aufgeführt sind, auch dokumentieren muss. Da aber viele Punkte keinen Sinn machten für unsere Grösse des Projektes, haben wir am Anfang einige Zeit aufgewendet für Punkte, welche wir nicht in die Dokumentation genommen haben. Ein weiterer Punkt, welcher sehr mühsam war, war der Workaround mit den Markdown-Tabellen, welche alle in Restructured Text-Tabellen umgewandelt werden mussten. Dies machte das Bearbeiten von Tabellen aufwendiger. Es war auch nicht immer klar, was nun wirklich erwartet wurde basierend auf den Checklisten. Dazu kam, dass in der Anleitung wichtige Details nicht korrekt waren, was uns mehrere Stunden an Aufwand beschert hat mit Nutzlosen Fehlersuchen, welche mit einer korrekten Anleitung nicht angefallen wären.

Es war vor allem zu beginn schwierig, die Arbeit aufzuteilen, da alle auf den gleichen zwei Dokumenten gearbeitet haben. Dieses Problem hat sich später gemindert, da wir mehr unterschiedliche Arbeiten hatten.

### Entwicklung

Der Einsatz von Lintern, Formattern und Coding Conventions hat sich sehr bewährt und die Qualität des Codes massiv erhöht. Mit den Werkzeugen die Git zur Verfügung stellt haben wir regen gebrauch gemacht. Wir haben mit Git Flow, Branching, vordefinierten Commitmessagestrukturen und anschliessenden Merge Requests eine gute Struktur erstellt, welche es uns erlaubte Code Reviews einzubauen, die die Qualität ebenfalls gesteigert haben. Im Frontend wurden sogar die Branch Namen sowie die Commit Messages per Linter geprüft.



### DevOps

Der Einsatz der Gitlab Pipelines für das CI hat sich gut bewährt und die Produktivität des Teams spürbar erhöht, da sich die einzelnen Teammitglieder ganz auf das schreiben von Code konzentrieren konnten und sich nicht um das bauen und integrieren des neuen Codes sorgen mussten. Der Einsatz von SonarQube in der Pipeline hat uns ausserdem stets mit aktuellen Codequalitäts-Metriken versorgt und die Qualitäät des Codes insgesamt nochmals weiter verbessert. Im Backend wurden die geschriebenen Unittests durch die Pipelinies ausgeführt und ein Merge eines Feature Branches in den develop Branch konnte nur vorgenommen werden, wenn die Unittests erfolgreich ausgeführt werden konnten. 

Es gab aber auch Probleme im DevOps Bereich vor allem mit der Infrastruktur (siehe unten) und dem CD Teil. Das Thema CD konnten wir am Ende leider gar nicht mehr umsetzen, da die Infrastruktur in der letzten Projektphase oft nicht erreichbar und generell sehr langsam war. Da die OST IT uns ausserdem von den Gitlab Runners her keinen Zugriff via SSH (Port 22) auf unseren Deploymentserver geben wollte, hätten wir aber ohnehin kein richtiges CD implementieren können. 

### Pipeline und Infrastruktur

Die von der OST zur Verfügung gestellte Infrastruktur war oft von Problemen und Ausfällen betroffen. Dies war vor allem in den letzten Wochen des Projekts immer häufiger das Problem. Diese Probleme haben zum Teil zu starken Verzögerungen geführt und am Ende haben sie dann auch dazu geführt, dass wir das Deployment auf unseren Server nicht korrekt fertigstellen konnten. Wir mussten schliesslich ein manuelles lokales Deployment vornehmen, um das Projektdeployment demonstrieren zu können.

Die Pipeline selber war generell langsam und eher schwerfällig. Vermutlich lag das daran, dass allen Projekten zusammen nur ein einzelner Gitlab Runner zugeteilt war. Leider konnten wir das nicht weiter beeinflussen. Es hat aber dazu geführt, dass wir bei der Arbeit oft unnötig ausgebremst wurden, weil unnötig lange Wartezeiten entstanden sind. 

## Persönliche Erfahrungen

*Pro Teammitglied ein Kapitel*

### *Name des Teammitgliedes*

*Die Erfahrungen eines Teammitgliedes während der gesamten Projektdauer*

