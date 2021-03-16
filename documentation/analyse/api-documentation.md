# API Dokumentation

## Geschäfte

### Als neues Geschäft registrieren

Über diese API können sich neue Geschäfte in CapWatch registrieren um bei Konsumenten in der Auflistung zu erscheinen.

```eval_rst
+--------------+----------------+
| HTTP Methode | URI            |
+==============+================+
| POST         | /shops         |
+--------------+----------------+
```

#### Body Parameter

Pflichtfelder: *name*, *street*, *zipCode*, *city*, *maxCapacity*

```json
{
	"name": "<Name>",
	"street": "<Strasse, Nr>"
	"zipCode": "<Postleitzahl>",
	"city": "<Ort>",
	"maxCapacity": "<Maximale Anzahl Besucher>"
}
```

#### Rückgabe

```json
{
	"data": {
		"shopId": <Shop ID>,
		"shopSecret": "<GUID>"
	},
	"links": {
		"update": "/shops/{id}"
	}
}
```

### Geschäft aktualisieren und aktuelle Besucherzahlen melden

Diese API dient hauptsächlich dazu die aktuelle Anzahl Besucher zu melden, kann aber auch dazu verwendet werden um die Informationen über das Geschäft zu aktualisieren.

```eval_rst
+--------------+----------------+
| HTTP Methode | URI            |
+==============+================+
| PUT          | /shops/{id}    |
+--------------+----------------+
```

#### Header Parameter

```eval_rst
+--------------+-------------------------+
| Parameter    | Beschreibung            |
+==============+=========================+
| shop_secret  | GUID zur Authorisierung |
+--------------+-------------------------+
```

#### Body Parameter

Pflicht-Felder: *currentCapacity*

```json
{
	"name": "<Name>",
	"zipCode": "<Postleitzahl>",
	"city": "<Ort>"
	"maxCapacity": "<Maximale Anzahl Besucher>",
	"currentCapacity": "<Aktuelle Anzahl Besucher>"
}
```

#### Rückgabe

```
Status Code: 200
```

## Konsument

### Liste aller Geschäfte abrufen

Über diese API wird eine Liste aller Geschäfte geladen, für welche Auslastungsinformationen vorhanden sind.

```eval_rst
+--------------+----------------+
| HTTP Methode | URI            |
+==============+================+
| GET          | /shops         |
+--------------+----------------+
```

#### Rückgabe

```json
{
	"data": [
		{
			"shopId": <Shop ID>,
			"name": "<Name>"
		}
	],
	"links": {
		"refresh": "/shops",
		"details": "/shops/{id}"
	}
}
```

### Detailinformationen über ein Geschäft laden

Lädt die Detailinformationen, inklusive aktueller Auslastung, für ein Geschäft.

```eval_rst
+--------------+----------------+
| HTTP Methode | URI            |
+==============+================+
| GET          | /shops/{id}    |
+--------------+----------------+
```

#### Rückgabe

```json
{
	"data": {
			"shopId": <Shop ID>,
			"name": "<Name>",
			"zipCode": "<Postleitzahl>",
			"city": "<Ort>",
			"maxCapacity": "<Maximale Anzahl Besucher>",
			"currentCapacity": "<Aktuelle Anzahl Besucher>"
	},
	"links": {
		"refresh": "/shops/{id}"
	}
}
```
