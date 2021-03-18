# Domainanalyse

## Einführung
    
### Zweck

Dieses Projekt gibt eine Übersicht über die Domain des Projektes CapWatch.

### Gültigkeitsbereich

Dieses Dokument ist für die Stakeholder dieses Projektes, sowie die Entwickler erstellt worden. Es wurde im Rahmen des Engineering Projekts der Fachhochschule Ost erarbeitet.

### Übersicht

- Domain Modell
- Systemsequenzdiagramme

## Domain Modell

### Strukturdiagramm

![domain-model](/images/domain-model.png)

Da C# bereits als Backendtechnologie festgelegt wurde, werden im Domain Model bereits Technologie spezifische Datentypen verwendet.

### Wichtige Konzepte

####Shop
Shop ist die einzige Klasse, welche für den MVP relevant ist. In dieser Klasse sind Name, Adresse und Logo enthalten, sowie die aktuelle/maximale Auslastung. Die Applikation unterstützt nur Shops in der Schweiz.

#### Consumer
Die Klasse Consumer wird für den Login und das Speichern von Favoriten des Konsumenten verwendet.

#### CapacityHistory
Um die erwartete Auslastung zu berechnen, wird die Auslastung mit einem Zeitstempel als History abgelegt, um damit die durchschnittliche Auslastung zu berechnen.  

####Reservation
Der Konsument kann sich bei einem Shop einen Timeslot reservieren und erhält dafür eine Reservations-ID.

## Systemsequenzdiagramme

Es wurden nur die Sequenzdiagramme für den MVP erstellt, wenn notwendig werden weitere vor der Umsetzung eines Features designt.

### Datenalieferung Shop
Der Shop liefert Daten zur aktuellen Auslastung an CapWatch.\
![systemsequenzdiagramm-capacity-delivery-service.png](/images/systemsequenzdiagramm-capacity-delivery-service.png)

### 
Konsumenten können die aktuelle Auslastung der Shops abrufen.\
![systemsequenzdiagramm-capacity-consumer-service.png](/images/systemsequenzdiagramm-capacity-consumer-service.png)

