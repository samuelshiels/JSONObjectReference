```json
{
  "properties": [
    {
      "name": "errorCode",
      "description": "A short string code description of an error, can be an HTTP response code, Exception name or a custom crafted code",
      "examples": [
        "404",
        "json.decoder.JSONDecodeError"
      ]
    },
    {
      "name": "errorDescription",
      "description": "Long error message relating to the code, can be the text representation of a number code, code stack or log dump",
      "examples": [
        "File not found",
        "Unterminated string starting at: line 1 column 14 (char 13)"
      ]
    }
  ]
}
```

Example

```json
{"errorCode":"404","errorDescription":"Resource not found"}

{"errorCode":"json.decoder.JSONDecodeError","errorDescription":"Unterminated string starting at: line 1 column 14 (char 13)"}
```
