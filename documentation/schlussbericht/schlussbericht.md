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

Der Einsatz von Lintern, Formattern und Coding Conventions hat sich sehr bewährt und die Qualität des Codes massiv erhöht. Mit den Werkzeugen die Git zur Verfügung stellt haben wir regen gebrauch gemacht. Wir haben mit Git Flow, Branching, vordefinierten Commitmessagestrukturen und anschliessenden Merge Requests eine gute Struktur erstellt, welche es uns erlaubte Code Reviews einzubauen, die die Qualität ebenfalls gesteigert haben. Im Frontend wurden sogar die Branch Namen sowie die Commit Messages per Linter geprüft. Allgemein lief die Entwicklung im Backend recht flüssig, da schon viel Wissen vorhanden war. Mit Mongo DB und C# gab es zu beginn ein paar Hürden. Und später war es schwerer mit .NET SonarQube korrekt zu konfigurieren als mit Node.js. Im Frontend war es zu beginn sehr Zeitaufwendig, da vieles im Pairprogramming gemacht werden musste und auch sonst viel Wissen aufgebaut werden musste. Dies hat einige Issues weit über die geschätzte Zeit gebracht. Dies wurde mit der Zeit jedoch auch besser, nachdem wir uns mehr Wissen und Erfahrung angeeignet hatten.

### DevOps

### Pipeline und Infrastruktur

## Persönliche Erfahrungen

### Pascal Schlumpf

Für mich war das Projekt sehr lehrreich, da ich das erste Mal ein Projekt von Anfang bis Ende durchgeführt habe. Auch kam ich in Kontakt mit neuen Technologien, Methoden und Arbeitsweisen, die ich so in meinem Arbeitsalltag noch nie verwendet habe. Ich hatte am Anfang eine Weile gebraucht, bis ich die Mongo DB in C# integriert hatte. Als dies dann funktioniert hat, habe ich auch andere Bereiche im Backend umgesetzt. Am Ende konnte ich auch noch ein paar Aufträge im Frontend umsetzen, so dass ich alles einmal gesehen habe. Meine Rolle als Product Owner war für mich zu Beginn sehr ungewohnt und ich hatte auch nicht wirklich eine Wahl, was das Bestimmen der umzusetzenden Tasks anging. Es war auch schwierig alle nötigen Issues zu erfassen, da nicht alle Anforderungen über die Checkliste und die Vorlage abgedeckt waren. Für mich als Berufsbegleitender Student war die zusätzliche Belastung durch das EPJ Projekt sehr gross, so dass ich für viele Module nur das Nötigste tun konnte. Nichts desto trotz verlief das Projekt erfolgreich und es war eine grosse Teamleistung.

### Christoph Scheiwiller

Das EPJ war für mich eine super Erfahrung. Da das Projekt auf einer grünen Wiese startete, konnten wir interessante Technologien und moderne Tools einsetzen, welche uns ideal im Entwicklungsprozess unterstützten.
Da ich in meiner täglichen Arbeit SVN verwende, kämpfte ich am Anfang stark mit der Verwendung von GitLab, GitFlow und Conventional Commits. Auch wenn ich diese Tools und Prozesse noch nicht vollständig beherrsche sehe ich viele Vorteile und möchte Git weiterhin verwenden.
Gefordert war ich bei der Entwicklung des Frontends, da ich React noch nicht kannte. Das React Freamework ist sehr umfangreich und fordert deshalb eine längere Einarbeitungszeit.
Im Team hatten wir eine gute Zusammenarbeit, damit konnten wir jede Herausforderung gemeinsam meistern. Dabei halfen uns auch unsere Berufserfahrung und Interessen in verschiedenen Fachbereichen, mit welchen wir uns ideal ergänzten.
Insgesamt ziehe ich für mich ein positives Feedback und kann viele Erfahrungen für die Studienarbeit und die Bachelor-Arbeit mitnehmen.

### Rafael Fuhrer

Das Engineering Projekt war für mich eine besondere Herausforderung. Ich habe bis zu diesem Projekt, trotz Berufstätigkeit neben dem Studium, nie an einem richtigen Softwareprojekt mitgearbeitet. Entsprechend gab es hier für mich viel zu lernen. Vor allem was die Themen Git, Git flow, Clean Code, Best Practices und Debugging angeht, habe ich in den letzten 3 Monaten sehr viel dazu gelernt. Ich durfte aber auch Aufgaben übernehmen, in denen ich um einiges routinierter bin, wie z.B. das Schreiben von Docker & Docker-Compose Files und das Setup der CI-Pipelines. Leider waren diese Tasks in diesem Projekt mit vielen Schwierigkeiten verbunden. Dies lag vor allem an der unzuverlässigen Infrastruktur und den Vorlagen, die uns die OST bereitstellte. Aber auch der Einsatz von C# im Zusammenhang mit Open Source Tools wie SonarQube und Renovate war am Ende eine grössere Herausforderung als ich ursprünglich gedacht hätte. Das Projekt hat mir aber trotzdem meistens viel Spass, da ich all diese interessanten neuen Dinge gelernt habe, die ich später sicher einmal gebrauchen kann. Alles in allem bin ich sehr froh, dass wir trotz all dieser Probleme unsere Projektziele erreicht und das Projekt erfolgreich abgeschlossen haben.

### Jonas Hauser

Ich habe mich persönlich sehr gefreut, dass ich bei der ersten grösseren Gruppenarbeit an der OST direkt die Funktion als Projektleiter und Scrum Master übernehmen durfte. Meine Passion ist es, Projekte zu organisieren und zu leiten und darum habe ich sehr viel Engagement und Erfahrungen in das Engineering Projekt gesteckt. Dies hat sich soweit wir als Team das beurteilen können, sehr gelohnt. Jeder Sprint ist nahezu problemlos von statten gegangen und die Resultate sind allesamt auf sehr hohem Niveau und im Vergleich zu Projekten auf dem Markt wahrscheinlich überdurchschnittlich.
 Dennoch gab es einige Schwierigkeiten zu meistern. Mitunter einer der grössten Dorne im Auge war der stetige Zeitdruck, ausgelöst durch die sehr kurze Zeitspanne, an dem am Projekt gearbeitet werden sollte. Viel Zeit wurde für die Dokumentation, dem allgemeinen Projektmanagement und der mangelnden Infrastruktur der OST aufgewendet, wodurch ich immer versucht habe, quantitativ voranzukommen, aber dennoch in möglichst hoher Qualität.
 Mir hat das Projekt viel Freude bereitet und ich habe persönlich viele praktische Erfahrungen dabei sammeln können.

### Pascal Schneider

Das Engineering Projekt war eine interessante Erfahrung. Neben Arbeit, restlichem Studium und sonstigen Verpflichtungen war es aber zeitweise auch sehr anstrengend.

Die Zusammenarbeit im Team hat zwischenmenschlich sehr gut funktioniert und die Sitzungen waren immer sehr positiv und motivierend.

Einen negativen Nachgeschmack hinterlassen hat hingegen die Infrastruktur der OST, welche uns des Öfteren Probleme bereitet hat. Die Unzulänglichkeiten von GitLab bezüglich Issue Tracking und Zeiterfassung konnten wir glücklicherweise früh mit YouTrack umgehen, die mangelnde Qualität / Anzahl GitLab Runner welche vor allem gegen Ende des Projekts bemerkbar wurde kostete hingegen sehr viel Zeit und Nerven.

Im Backend war für mich vor allem das Implementieren der hexagonalen Architektur spannend, auch wenn diese für unseren Projektumfang etwas übertrieben ist. Auf der negativen Seite ist das Zusammenspiel zwischen .NET und den open-source Werkzeugen, welche wir eingesetzt haben, aufgefallen. Da wir auf der Arbeit Team Foundation Server im Einsatz haben war mir nicht bewusst wie viele Stolpersteine hier existieren und wie oft .NET anders integriert werden muss als andere Technologien. Für zukünftige Projekte nehme ich definitive mit, dass ich bei der Auswahl von Tools besser recherchieren muss, wie gut sich diese mit .NET integrieren lassen.

Alles in Allem war das EPJ ein lehrreiches Projekt mit positiven und negativen Höhepunkten.

