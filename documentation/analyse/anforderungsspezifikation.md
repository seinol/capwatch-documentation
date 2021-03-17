# Anforderungsspezifikationen

## Einführung

### Zweck

Dieses Dokument gibt einen groben Überblick über das Produkt CapWatch sowie die geplanten Anforderungen die es erfüllen muss und solche die optional noch umgesetzt werden können.

### Gültigkeitsbereich

Dieses Dokument ist gültig für das Engineering Projekt im Frühlingssemester 2021 an der Fachhochschule OST. Es ist für die Stakeholder dieses Projektes ausgelegt. Dazu gehören die Betreuer, sowie die Entwickler.

### Referenzen

**ISO/IEC 9126:** https://de.wikipedia.org/wiki/ISO/IEC_9126

**OWASP Threat Modeling:** https://owasp.org/www-community/Threat_Modeling

### Übersicht

Im Abschnitt "Allgemeine Beschreibung" werden allgemeine Informationen zum Produkt erläutert. Anschliessend werden im Abschnitt "Funktionale Anforderungen" die geplanten Funktionalitäten beschrieben. Im letzten Abschnitt werden die nicht Funktionalen Anforderungen genauer umschrieben und nicht kategorisierbare Themen zusammengefasst.

## Allgemeine Beschreibung

### Produkt Perspektive

Im Zuge der Corona Pandemie ist es plötzlich an sehr vielen Orten zu Einschränkungen der erlaubten Anzahl Personen innerhalb eines definierten Bereichs gekommen. Das führte dazu, dass man einkaufen gehen wollte und die Ampel auf Rot war und man somit gezwungen war zu warten. Dieses Problem kann gemindert werden, indem man sich zuhause im Voraus darüber informieren kann ob es ein guter Zeitpunkt ist, jetzt einkaufen zu gehen. Da die Systeme zur Personenzählung nun fest installiert sind, ist es gut möglich, dass sie auch in Zukunft bleiben werden.  Hier setzt unser Produkt an, indem es die ganzen gesammelten Daten konsolidiert und auf einer einfachen Benutzeroberfläche abrufbar macht. Dies hilft sowohl den Firmen wie auch den Kunden. 

### Produkt Funktion

CapWatch ist dazu da, um als Kunde einen einfach Überblick zu bekommen wie viele Personen aktuell in einem Laden/ Restaurant/ Sauna vorhanden sind. Da die Firmen aktuell gezwungen sind, das aktuelle Besucheraufkommen zu erfassen und zu steuern, wollen wir diese Daten bündeln und somit den Kunden die Möglichkeit geben das eigene Verhalten anzupassen und so unnötige Wartezeiten zu vermeiden.

### Benutzer Charakteristik

Jede Person die eine Einrichtung mit Personenbeschränkung besuchen möchte und sich im Voraus über das Besucheraufkommen informieren will.

### Einschränkungen

In der Grundausführung ist unser Produkt nur eine Zusammenfassung der vorhandenen Daten, welche in einer Übersicht angezeigt werden können. Es werden keine Informationen gesammelt und es sind jeweils nur die aktuellsten Daten verfügbar.

### Annahmen

Wir gehen davon aus, dass die Firmen die gesammelten Daten uns zur Verfügung stellen werden und dass sie die Daten in einer Art erfassen, die es uns erlaubt sie weiterzuverarbeiten. Im Rahmen des Projektes werden wir nur mit Testdaten arbeiten um externe Abhängigkeiten zu vermeiden.

### Abhängigkeiten

Wir sind von Firmen abhängig, die uns aktuelle Daten liefern wollen und können.

## Funktionale Anforderungen

Wir haben uns aufgrund des einfachen Geschäftsfalles dagegen entschieden Use Cases einzusetzen, da diese einen ziemlichen Mehraufwand mit sich bringen. Wir setzen dafür auf einen schlanken Mix aus User Story und MUSS/KANN Anforderungen.

### Anlieferer / Anbieter

***Als Anlieferer möchte ich mich registrieren können, damit ich den Kunden die aktuellen Besucherzahlen liefern kann.***

```eval_rst
+-----------------+-----------+--------------------------------------+
| Anforderungs-ID | Kategorie | Beschreibung                         |
+=================+===========+======================================+
| AL-1            | MUSS      | Der Anlieferer liefert regelmässig   |
|                 |           | die aktuelle Auslastung mit Token,   |
|                 |           | Timestamp und Maximal erlaubter      |
|                 |           | Auslastung an.                       |
+-----------------+-----------+--------------------------------------+
| AL-2            | KANN      | Der Anlieferer muss sich per Request |
|                 |           | registrieren können, indem er        |
|                 |           | Firmenname, Ortschaft und einem Logo |
|                 |           | als Attachment mit sendet. Er erhält |
|                 |           | als Antwort einen Token oder eine    |
|                 |           | Fehlermeldung.                       |
+-----------------+-----------+--------------------------------------+
```
### Konsument

***Als Konsument möchte ich mich über das aktuelle Besuchsaufkommen informieren können.***
```eval_rst
+-----------------+-----------+--------------------------------------+
| Anforderungs-ID | Kategorie | Beschreibung                         |
+=================+===========+======================================+
| AW-1            | MUSS      | Als Konsument kann ich eine Liste    |
|                 |           | aller verfügbaren Firmen anzeigen    |
|                 |           | lassen.                              |
+-----------------+-----------+--------------------------------------+
| AW-2            | MUSS      | Als Konsument kann ich nach einer    |
|                 |           | Firma suchen.                        |
+-----------------+-----------+--------------------------------------+
| AW-3            | MUSS      | Als Konsument kann ich eine Firma    |
|                 |           | als Favorit markieren. Favoriten     |
|                 |           | können in der Favoritenansicht       |
|                 |           | angezeigt werden.                    |
+-----------------+-----------+--------------------------------------+
| AW-4            | KANN      | Als Konsument kann ich mir eine      |
|                 |           | Liste der nächsten Läden in meiner   |
|                 |           | Umgebung nach Distanz sortiert       |
|                 |           | anzeigen lassen.                     |
+-----------------+-----------+--------------------------------------+
| AW-5            | KANN      | Ich kann mich als Konsument          |
|                 |           | registrieren und anschliessend nach  |
|                 |           | einem Login über mehrere Geräte      |
|                 |           | hinweg auf meine Favoriten           |
|                 |           | zugreifen.                           |
+-----------------+-----------+--------------------------------------+
| AW-6            | KANN      | Als Konsument kann ich meine         |
|                 |           | E-Mailadresse hinterlegen und mich   |
|                 |           | so über wichtige Ereignisse          |
|                 |           | informieren lassen.                  |
+-----------------+-----------+--------------------------------------+
| AW-7            | KANN      | Als Konsument kann ich über eine     |
|                 |           | Detailansicht einer Firma die        |
|                 |           | Prognosen und Verläufe des           |
|                 |           | Besucheraufkommens anzeigen lassen.  |
+-----------------+-----------+--------------------------------------+
| AW-8            | KANN      | Als Konsument kann ich mir bei einer |
|                 |           | Firma einen begrenzten Zeitraum      |
|                 |           | reservieren.                         |
+-----------------+-----------+--------------------------------------+
```

Für das Minimal Viable Product sind die MUSS-Anforderungen relevant. Falls Kapazität vorhanden ist, können aber auch schon KANN-Anforderungen umgesetzt werden.

## Weitere Anforderungen

### Threat Model nach OWASP

![threat_model_diagram](../../images/threat_model_diagram.png)



Um unser Produkt bestmöglich gegen die Gefahren von aussen abzusichern erstellen wir ein Threat Model. Dieses wird laufend aktualisiert. Hierzu machen wir uns Gedanken zu folgenden Punkten:

- **Was sind unsere Assets:** In unserem MVP sind in unserem System nur Daten vorhanden die uneingeschränkt über unsere Webseite einsehbar sind. In der Datenbank sind nur regelmässigen Einträge mit Timestamp, Anzahl Personen  und maximal Erlaubter Anzahl Personen vorhanden. Diese Metriken sind völlig anonym und werden als Zahlen angeliefert, Rückschlüsse auf einzelne Personen sind unmöglich. Zusätzlich speichern wir noch die Token der Firmen, die uns Daten anliefern. Diese Daten sind schützenswert, da es als Angreifer mit dem Token möglich ist unser System zu überlasten. In der späteren Ausbaustufe, in der wir Kundendaten erfassen und speichern, ist die Datenbank mit Kundendaten ein wichtiges Asset.
- **Threat Agents und mögliche Angriffe:** Interne Angriffe können die Kundendaten abgreifen um die gespeicherten E-Mailadressen weiterzuverwenden. Dies ist möglich über einen Zugriff der Kundendatenbank, die nicht genügend gut per Zugriffsrechte abgesichert ist. Ein externer Angreifer, welcher eine Organisierte Verbrecherbande oder ein einzelner Hacker sein kann, müsste sich die Zugangsdaten der Datenbank beschaffen um direkt darauf zuzugreifen oder er schafft es über die API an mehr Daten als vorgesehen zu kommen.
- **Mögliche Schwachstellen:** Bei der Entwicklung unseres Produktes können mehrere Schwachstellen entstehen. Dazu gehören unsauber aufgesetzte Berechtigungen, fehlende Inputsäuberung und Inputvalidierung, überdimensionierte Schnittstellen mit zu vielen Feldern sowie schwache Passwörter und fehlende Passwortverwaltung.
- **Gegenmassnahmen:** Den internen Angriff kann man mit einem Berechtigungsmodell, welches nach dem Prinzip so wenig wie nötig aufgesetzt ist, mitigieren. Den Zugriff auf eine Kundendatenbank wird über einen Supportuser gelöst, welcher nur mit Begründung und Dokumentation der Tätigkeiten benutzt werden kann. Um die externen Angriffe zu erschweren kommen sichere Passwörter und klar definierte Schnittstellen zum Einsatz. Die Schnittstellen dürfen nur die klar definierten Felder verwenden und der Inhalt der Anfragen wird vor der Verarbeitung gesäubert um unerwünschte Effekte zu vermeiden.

### Qualitätsmerkmale

Da wir aktuell noch keine Anhaltspunkte haben, werden grobe Schätzungen gemacht. Wenn wir mehr Informationen haben, werden die Werte angepasst.

- **Änderbarkeit**

  - **Analysierbarkeit:** Ein mit dem Projekt nicht vertrauter Entwickler sollte bei einem einfach Problem innerhalb von 15min die betroffene Codestelle gefunden haben. 
  - **Modifizierbarkeit:** Der Aufwand für kleine Verbesserungen oder Anpassungen an Umgebungsänderungen sollte klein sein.
  - **Stabilität:** Unser Produkt ist unter einer Last von 100 Anfragen noch erreichbar.
  
- **Benutzbarkeit:**

  Die Benutzbarkeit messen wir mit Benutzerumfragen wobei wir eine Durchschnittliche Bewertung von 4 von 5 Sternen erreichen wollen. Gemessene Kriterien sind:

  - Attraktivität 
  - Bedienbarkeit
  - Erlernbarkeit
  - Verständlichkeit

- **Effizienz**

  - **Zeitverhalten:** Der Kunde soll innerhalb von einer Sekunde das Resultat einer Abfrage zur Verfügung haben.
  - **Verbrauchsverhalten:** Unser Produkt kann mit 100 Requests pro Sekunde umgehen.

- **Funktionalität**

  - **Richtigkeit:** Die Ergebnisse sollte nicht älter als 15min sein.
  - **Ordnungsmäßigkeit:** Wir stellen die Anforderungen des Datenschutzgesetzes (DSG) sicher.
  - **Sicherheit:** Die häufigsten Angriffspunkte und Schwachstellen nach OWASP sind berücksichtig worden.

- **Zuverlässigkeit**

  - **Reife:** Sofern die Infrastruktur funktioniert, soll unser Produkt nur kurzfristig nicht erreichbar sein. 
  - **Fehlertoleranz:** Antizipierbare Fehler dürfen die Leistung des Systems nicht vermindern.

### Schnittstellen

Gibt noch ein Dokument mit API-Beschreibung

- **Webapplikation**
  - Schnittstelle zu Backend um Besucherdaten abzufragen (1. Schritt)
  - Schnittstelle zu Backend für Authentifizierung und Autorisierung (2. Schritt)
- **Backend**
  - Schnittstelle zu Frontend um Besucherdaten zu liefern (1. Schritt)
  - Schnittstelle zu Frontend für Authentifizierung und Autorisierung (2. Schritt)
  - Schnittstelle zu Datenbank um Daten abzulegen und zu lesen (1. Schritt)
  - Schnittstelle um Daten von den Firmen anliefern zu lassen (1. Schritt)
  - Schnittstelle um Firmen Registrierung zu ermöglichen (2. Schritt)
- **Datenbank**
  - Schnittstelle zu Backend um Daten entgegenzunehmen oder zu liefern

### Randbedingungen

Wir sind abhängig von der Serverinfrastruktur der Ost. Wir haben keinen Einfluss darauf und vertrauen darauf, dass sie uns zur Verfügung steht.

Ansonsten gibt es keine Randbedingungen.