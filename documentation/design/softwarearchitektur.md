# Softwarearchitektur

## Einführung
    
### Zweck

*Zweck des Dokumentes*

### Gültigkeitsbereich

*Gültigkeitsbereich des Dokumentes*

### Referenzen

*Liste aller verwendeten und referenzierten Dokumente, Bücher, Links, usw.*

*Referenz auf ein Glossar Dokument, wo alle Abkürzungen und unklaren Begriffe erklärt werden*

*Die Quellen / Referenzen sollten (falls möglich) automatisch erstellt werden*

### Übersicht

*Übersicht über den restlichen Teil dieses Dokumentes geben und dessen Aufbau erläutern*

## Systemübersicht

*Beschreibt die Softwarearchitektur eines Systems und wie sie sich präsentiert (am besten mit einem Bild um eine Übersicht zu ermöglichen) und einzelne Beschreibungen zu den einzelnen Elementen des Systems*

## Architektonische Ziele & Einschränkungen

*Beschreibt die Softwareanforderungen und Objekte, welche einen Einfluss auf die Architektur haben (z.B. Safety, Security, Privacy, Distribution, usw.); Beinhaltet auch eine Beschreibung von Design und Implementationsstrategie, Entwicklungstools, usw. vor allem die Antworten auf ‚Warum‘-Fragen, z.B. „Warum haben wir eine Data Access Schicht hier eingezogen?“, oder „Warum kommunizieren wir mit eigenen Messages über Sockets, und nicht über eine REST-Schnittstelle?“*

*Anmerkung: Hier nicht noch einmal die Anforderungen wiederholen, sondern beschreiben, wie die Anforderungen in der Architektur umgesetzt wurden, um sie zu erreichen. Häufig sind es die nicht-funktionalen Anforderungen wie Security, Performance, Usability etc. welche einen Einfluss auf die Architektur haben. Also beschreiben Sie beispielsweise hier, wie sie die Architektur aufgebaut haben, um die Sicherheitsanforderungen zu erfüllen*

## Logische Architektur

*Beschreibung der logischen Struktur des Projekts. Pro Subsystem/Package ein einzelner Abschnitt und ein Übersichtsdiagramm über die einzelnen Subsysteme/Packages. Aufteilung in Subsysteme/Packages (zum Beispiel: 3-Layer-Architektur mit GUI, Problem Domain und Datenhaltung).*

### *Subsystem/Package Name*

*Beschreibung mit Text und Diagramm der Architektur des Subsystems/Packages.*

#### Klassenstruktur

*Klassendiagramm innerhalb des Packages und tabellarisch die wichtigsten Klassen beschreiben*

#### Schnittstellen

*Beschreibung der Schnittstellen*

#### Wichtige interne Abläufe

*Beschreibung von wichtigen internen Abläufen*

### Wichtige Abläufe

*Beschreibung von wichtigen Abläufen (packageübergreifend)*

## Prozesse und Threads

*Wenn mehrere Prozesse oder Threads eingesetzt werden wird hier beschrieben, wie diese ablaufen, miteinander funktionieren, Daten austauschen, sich synchronisieren, usw.*

## Deployment

*Beschreibung der einzelnen Komponenten und deren Aufteilung (auf welchen Umgebungen, Servern, usw. laufen die Komponenten)*

## Datenspeicherung

*Beschreibung mit Diagramm der Datenspeicherung (Datenmodell, z.B. Datenbank)*

## Grössen und Leistung

*Einschränkungen der Applikation bezüglich Speicher, Leistung, etc.… (zum Beispiel: Verwaltung unterstützt maximal 20'000 Einträge)*
