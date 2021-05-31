# Projektantrag

```eval_rst
+---------------+------------+
| Projektkürzel | Datum      |
+===============+============+
| CAPWATCH      | 16.12.2020 |
+---------------+------------+
```

## Team

- Pascal Schlumpf
- Christoph Scheiwiller
- Jonas Hauser
- Rafael Fuhrer
- Pascal Schneider

## Beratungs- und Review-Zeitslots

*Beratungs- und Review-Zeitslots angeben, an denen **alle** Teammitglieder anwesend sein können:*

```generic
 X  = Slot ist dem Team möglich
(X) = Slot ist für das Team nicht optimal, wäre aber möglich
 O  = Treffen online möglich
 P  = Treffen physisch (Campus OST-RJ) möglich
 OP = Treffen online sowie physisch (Campus OST-RJ) möglich 
    = Slot ist nicht möglich
```

```eval_rst
+-----------------+--------+----------+----------+------------+---------+
| Zeitslot        | Montag | Dienstag | Mittwoch | Donnerstag | Freitag |
+=================+========+==========+==========+============+=========+
| 08:00-09:00     |        |          |          |            |         |
+-----------------+--------+----------+----------+------------+---------+
| 09:00-10:00     |        |          |          |            |         |
+-----------------+--------+----------+----------+------------+---------+
| 10:00-11:00     |        |          |          |            |         |
+-----------------+--------+----------+----------+------------+---------+
| 11:00-12:00     |        |          |          |            |         |
+-----------------+--------+----------+----------+------------+---------+
| 12:00-13:00     | (XO)   |          |          |            |         |
+-----------------+--------+----------+----------+------------+---------+
| 13:00-14:00     |  XO    |          |          |            |         |
+-----------------+--------+----------+----------+------------+---------+
| 14:00-15:00     |  XO    |          |          |            |         |
+-----------------+--------+----------+----------+------------+---------+
| 15:00-16:00     |  XO    |          |          |            |         |
+-----------------+--------+----------+----------+------------+---------+
| 16:00-17:00     |  XO    |          |          |            |         |
+-----------------+--------+----------+----------+------------+---------+
| 17:00-18:00     |        |          |          |            |         |
+-----------------+--------+----------+----------+------------+---------+
| 18:00-19:00     |        |          |          |            |         |
+-----------------+--------+----------+----------+------------+---------+
```

## Motivation

Real-time Daten zur Anzahl Personen in einem Raum oder Gebäude, welche eine Personenbeschränkung aufgrund einer Pandemie oder einem sonstigen Grund haben, wie z. B. Geschäfte, Saunen, Bäder, Sportanlagen etc. um das persönliche Einkaufs- und Konsumverhalten besser planen bzw. anpassen zu können.
Es entstehen dabei Vorteile für die Anbieter und die Konsumenten. Die Anbieter können Dienstleistungsengpässe vermeiden, welche zu einem Besucherverlust führen könnten. Die Konsumenten profitieren von kurzen Wartezeiten und somit auch besseren Verkaufsdienstleistung wie z. B. Beratungen.

## Projektidee

Eine Webapplikation, in der man seine Lieblingsgeschäfte, Saunas, etc. abonnieren kann. Die Daten werden bei einem Abonnement dann in Echtzeit aktualisiert.
Die Daten werden von den Dienstleistern über eine API an das Backend geliefert und in einer Datenbank abgelegt. Das Backend besteht aus insgesamt zwei zentralen APIs. Die zweite Schnittstelle ist für die Datenauslieferung an das Frontend bzw. die Webseite, welche schlussendlich der Benutzer für die Abonnements verwendet.
Das Frontend ist ein reiner, einseitiger Empfänger ohne Authentifizierung (Speicherung in einem lokalen Speicher beim Benutzer) in einer ersten Version.

Mögliche weitere Features:

- Automatische selektion von Abonnements (z. B. basierend auf dem Standort)
- Authentifizierung des Benutzers
- Benutzerprofile serverseitig speichern
- Vertikale Skalierung (mehr Workload verarbeiten können)
- Personalisierte Notifikationen an Benutzer (z. B. per E-Mail)
- Prognosen und Vorhersagen
- Möglichkeit zum Reservieren

Projektidee besprochen mit: Thomas Kälin

## Realisierung

Frontend: React oder Angular mit TypeScript (evtl. PWA)

Backend: Java oder Node.JS Framework für API-Entwicklung  

Datenbank: noch nicht festgelegt
