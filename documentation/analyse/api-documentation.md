
<!-- Generator: Widdershins v4.0.1 -->

# CapWatchBackend.WebApi v1

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

## Stores

### get__Stores

> Code samples

```javascript

fetch('/Stores',
{
  method: 'GET'

})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```

`GET /Stores`

#### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|

This operation does not require authentication

### patch__Stores

> Code samples

```javascript
const inputBody = '{
"id": "string",
    "name": "string",
    "street": "string",
    "zipCode": "string",
    "city": "string",
    "maxCapacity": 1,
    "currentCapacity": 0,
    "logo": "string",
    "secret": "string",
    "storeType": {
    "id": "string",
        "description": "string"
  }
}';
const headers = {
  'Content-Type':'application/json'
};

fetch('/Stores',
{
  method: 'PATCH',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```

`PATCH /Stores`

> Body parameter

```json
{
  "id": "string",
  "name": "string",
  "street": "string",
  "zipCode": "string",
  "city": "string",
  "maxCapacity": 1,
  "currentCapacity": 0,
  "logo": "string",
  "secret": "string",
  "storeType": {
    "id": "string",
    "description": "string"
  }
}
```

#### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[StoreModel](#schemastoremodel)|false|none|

#### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|

This operation does not require authentication

### post__Stores

> Code samples

```javascript
const inputBody = '{
  "name": "string",
  "street": "string",
  "zipCode": "string",
  "city": "string",
  "maxCapacity": 1,
  "logo": "string",
    "storeType": {
    "id": "string",
        "description": "string"
    }
}';
const headers = {
  'Content-Type':'application/json'
};

fetch('/Stores',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```

`POST /Stores`

> Body parameter

```json
{
  "name": "string",
  "street": "string",
  "zipCode": "string",
  "city": "string",
  "maxCapacity": 1,
  "logo": "string",
  "storeType": {
    "id": "string",
    "description": "string"
  }
}
```

#### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[StoreNew](#schemastorenew)|false|none|

#### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|

This operation does not require authentication

### get__Stores_{id}

> Code samples

```javascript
fetch('/Stores/{id}',
{
  method: 'GET'

})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```

`GET /Stores/{id}`

#### Parameters

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer(int32)|true|none|

#### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|

This operation does not require authentication

## Schemas

### NewStoreModel

```json
{
  "id": "string",
  "name": "string",
  "street": "string",
  "zipCode": "string",
  "city": "string",
  "maxCapacity": 1,
  "currentCapacity": 0,
  "logo": "string",
  "storeType": {
    "id": "string",
    "description": "string"
  }
}
```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer(int32)|true|none|none|
|name|string|true|none|none|
|street|string|true|none|none|
|zipCode|string|true|none|none|
|city|string|true|none|none|
|maxCapacity|integer(int32)|true|none|none|
|currentCapacity|integer(int32)|true|none|none|
|logo|string(byte)¦null|false|none|none|
|secret|string|true|none|none|

### StoreModel

```json
{
  "id": "string",
  "name": "string",
  "street": "string",
  "zipCode": "string",
  "city": "string",
  "maxCapacity": 1,
  "currentCapacity": 0,
  "logo": "string",
  "secret": "string",
  "storeType": {
    "id": "string",
    "description": "string"
  }
}

```

#### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|none|
|street|string|true|none|none|
|zipCode|string|true|none|none|
|city|string|true|none|none|
|maxCapacity|integer(int32)¦null|false|none|none|
|logo|string(byte)¦null|false|none|none|
