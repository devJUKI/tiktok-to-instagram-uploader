## 📜 How to Use

**Request:**

`me/accounts`

**Response:**

```json
"data": [
    {
      "access_token": "YYYYYYYYYY",
      "category": "Prekyba ir pramonė",
      "category_list": [
        {
          "id": "YYYYYYYYYY",
          "name": "Prekyba ir pramonė"
        }
      ],
      "name": "YYYYYYYYYY",
      "id": "XXXXXXXXXXX",
      "tasks": [
        "ADVERTISE",
        "ANALYZE",
        "CREATE_CONTENT",
        "MESSAGING",
        "MODERATE",
        "MANAGE"
      ]
    }
  ]
```

1. Get the second id from the response:
    - "id": "XXXXXXXXXXX"
2. Use that id in this request:

**Request:**

`XXXXXXXXXXX?fields=instagram_business_account`

**Response:**
```json
{
  "instagram_business_account": {
    "id": "XXXXXXXXXXX"
  },
  "id": "YYYYYYYYYY"
}
```

3. Extract the Instagram account id from the nested response:
    - "id": "XXXXXXXXXXX" (This is the Instagram account ID).

Note:
- Accounts are limited to **25 API-published posts** within a **24-hour period**.
- **Carousels count as a single post**.
