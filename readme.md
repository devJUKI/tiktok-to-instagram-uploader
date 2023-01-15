Request:
me/accounts

Response:
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
      "name": "ComfyHousing",
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

Get second id ("id": "XXXXXXXXXXX")

Use that id in this request:
XXXXXXXXXXX?fields=instagram_business_account

Response:
{
  "instagram_business_account": {
    "id": "XXXXXXXXXXX"
  },
  "id": "YYYYYYYYYY"
}

We get first (nested) id ("id": "XXXXXXXXXXX")

Accounts are limited to 25 API-published posts within a 24 hour period. Carousels count as a single post.
