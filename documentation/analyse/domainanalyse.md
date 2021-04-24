# Domainanalyse

## Einführung

### Zweck

Dieses Projekt gibt eine Übersicht über die Domain des Projektes CapWatch.

### Gültigkeitsbereich

Dieses Dokument ist für die Stakeholder dieses Projektes, sowie die Entwickler erstellt worden. Es wurde im Rahmen des
Engineering Projekts der Fachhochschule Ost im Frühlingssemester 2021 erarbeitet.

## Domain Modell

### Strukturdiagramm

![domain-model](../../images/domain-model.png)

Da C# bereits als Backendtechnologie festgelegt wurde, werden im Domain Model Technologiespezifische Datentypen
verwendet.

### Wichtige Konzepte

#### Store

Store ist die einzige Klasse, welche für den MVP relevant ist. In dieser Klasse sind Name, Adresse und Logo enthalten,
sowie die aktuelle/maximale Auslastung. Die Applikation unterstützt nur Stores in der Schweiz.

#### Consumer

Die Klasse Consumer wird für den Login und das Speichern von Favoriten des Konsumenten verwendet.

#### CapacityHistory

Um die erwartete und durchschnittliche Auslastung zu berechnen, wird die Auslastung mit einem Zeitstempel als History
abgelegt.

#### Reservation

Der Konsument kann sich bei einem Store einen Timeslot reservieren und erhält dafür eine Reservations-ID.

## Systemsequenzdiagramme

Die aktuell geplanten Funktionalitäten sind einfach im Aufbau, Systemsequenzdiagramme bringen daher keinen Mehrwert. Aus
diesem Grund werden sie in dieser Dokumentation bewusst weggelassen.

