
<!-- Generator: Widdershins v4.0.1 -->

<h1 id="capwatchbackend-webapi">CapWatchBackend.WebApi v1</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

<h1 id="capwatchbackend-webapi-stores">Stores</h1>

## get__Stores

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

<h3 id="get__stores-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|

<aside class="success">
This operation does not require authentication
</aside>

## patch__Stores

> Code samples

```javascript
const inputBody = '{
  "id": 0,
  "name": "string",
  "street": "string",
  "zipCode": "string",
  "city": "string",
  "maxCapacity": 1,
  "currentCapacity": 0,
  "logo": "string",
  "secret": "string"
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
  "id": 0,
  "name": "string",
  "street": "string",
  "zipCode": "string",
  "city": "string",
  "maxCapacity": 1,
  "currentCapacity": 0,
  "logo": "string",
  "secret": "string"
}
```

<h3 id="patch__stores-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[StoreModel](#schemastoremodel)|false|none|

<h3 id="patch__stores-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|

<aside class="success">
This operation does not require authentication
</aside>

## post__Stores

> Code samples

```javascript
const inputBody = '{
  "name": "string",
  "street": "string",
  "zipCode": "string",
  "city": "string",
  "maxCapacity": 1,
  "logo": "string"
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
  "logo": "string"
}
```

<h3 id="post__stores-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[StoreNew](#schemastorenew)|false|none|

<h3 id="post__stores-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|

<aside class="success">
This operation does not require authentication
</aside>

## get__Stores_{id}

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

<h3 id="get__stores_{id}-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer(int32)|true|none|

<h3 id="get__stores_{id}-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|None|

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_StoreModel">StoreModel</h2>
<!-- backwards compatibility -->
<a id="schemastoremodel"></a>
<a id="schema_StoreModel"></a>
<a id="tocSstoremodel"></a>
<a id="tocsstoremodel"></a>

```json
{
  "id": 0,
  "name": "string",
  "street": "string",
  "zipCode": "string",
  "city": "string",
  "maxCapacity": 1,
  "currentCapacity": 0,
  "logo": "string",
  "secret": "string"
}

```

### Properties

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

<h2 id="tocS_StoreNew">StoreNew</h2>
<!-- backwards compatibility -->
<a id="schemastorenew"></a>
<a id="schema_StoreNew"></a>
<a id="tocSstorenew"></a>
<a id="tocsstorenew"></a>

```json
{
  "name": "string",
  "street": "string",
  "zipCode": "string",
  "city": "string",
  "maxCapacity": 1,
  "logo": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|none|
|street|string|true|none|none|
|zipCode|string|true|none|none|
|city|string|true|none|none|
|maxCapacity|integer(int32)¦null|false|none|none|
|logo|string(byte)¦null|false|none|none|

