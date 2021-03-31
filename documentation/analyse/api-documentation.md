# API Dokumentation

## Anlieferer

### Als neuer Anlieferer registrieren

Über diese API können sich neue Anlieferer in CapWatch registrieren um bei Konsumenten in der Auflistung zu erscheinen.

```eval_rst
+--------------+----------------+
| HTTP Methode | URI            |
+==============+================+
| POST         | /stores        |
+--------------+----------------+
```

#### Body Parameter

Pflichtfelder: *name*, *street*, *zipCode*, *city*, *maxCapacity*

```json
{
	"name": "<Name>",
	"type": "<Typ>",
	"street": "<Strasse, Nr>"
	"zipCode": "<Postleitzahl>",
	"city": "<Ort>",
	"maxCapacity": <Maximale Anzahl Besucher>,
	"logo": "<Logo>"
}
```

#### Rückgabe

```json
{
	"data": {
		"id": <ID>,
		"secret": "<GUID>"
	},
	"links": {
		"update": "/stores/{id}"
	}
}
```

### Anlieferer aktualisieren und aktuelle Besucherzahlen melden

Diese API dient hauptsächlich dazu die aktuelle Anzahl Besucher zu melden, kann aber auch dazu verwendet werden um die Informationen über den Anlieferer zu aktualisieren.

```eval_rst
+--------------+----------------+
| HTTP Methode | URI            |
+==============+================+
| PUT          | /stores/{id}   |
+--------------+----------------+
```

#### Body Parameter

Pflichtfelder: *secret*, *currentCapacity*

```json
{
	"secret": "<GUID>",
	"name": "<Name>",
	"type": "<Typ>",
	"zipCode": "<Postleitzahl>",
	"city": "<Ort>"
	"maxCapacity": <Maximale Anzahl Besucher>,
	"logo": "<Logo>",
	"currentCapacity": <Aktuelle Anzahl Besucher>
}
```

#### Rückgabe

```
Status Code: 2xx
```

## Konsument

### Liste aller Anlieferer abrufen

Über diese API wird eine Liste aller Anlieferer geladen, für welche Auslastungsinformationen vorhanden sind.

```eval_rst
+--------------+----------------+
| HTTP Methode | URI            |
+==============+================+
| GET          | /stores        |
+--------------+----------------+
```

#### Rückgabe

```json
{
	"data": [
		{
			"id": <ID>,
			"name": "<Name>",
			"type": "<Typ>",
			"maxCapacity": <Maximale Anzahl Besucher>,
			"currentCapacity": <Aktuelle Anzahl Besucher>
		}
	],
	"links": {
		"refresh": "/stores",
		"details": "/stores/{id}"
	}
}
```

### Detailinformationen über einen Anlieferer laden

Lädt die Detailinformationen für einen Anlieferer, inklusive der aktuellen Auslastung.

```eval_rst
+--------------+----------------+
| HTTP Methode | URI            |
+==============+================+
| GET          | /stores/{id}   |
+--------------+----------------+
```

#### Rückgabe

```json
{
	"data": {
			"id": <ID>,
			"name": "<Name>",
			"type": "<Typ>",
			"zipCode": "<Postleitzahl>",
			"city": "<Ort>",
			"maxCapacity": <Maximale Anzahl Besucher>,
			"logo": "<Logo>",
			"currentCapacity": <Aktuelle Anzahl Besucher>
	},
	"links": {
		"refresh": "/stores/{id}"
	}
}
```
