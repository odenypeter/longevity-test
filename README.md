# Test API
To run this application locally:
- Set up python virtual environment
- run `pip install -r reuirements.txt`
- run `python manage.py migrate`
- serve the app by running `python manage.py runserver`

# Execute Test
- run `pythonmanage.py test`

## To test the merge data functionality
Make a POST request to the endpoint:
`http://localhost:8000/api/sample-model/merge_data/`
Sample Payload:
```python
[
    {
        "column_maps":[
                { "incoming_column": "username", "app_column": "field1" },
                { "incoming_column": "email", "app_column": "field2" },
                { "incoming_column": "name", "app_column": "field3" }
        ],
        "data_url": "https://jsonplaceholder.typicode.com/users"
    },
    {
        "column_maps":[
                { "incoming_column": "title", "app_column": "field1" },
                { "incoming_column": "userId", "app_column": "field2" },
                { "incoming_column": "completed", "app_column": "field3" }
        ],
        "data_url": "https://jsonplaceholder.typicode.com/todos"
    }
]
```
Explanation: 
Above request will merge the data from the 2 open endpoints based on the specifications, store the merged data to the DB and return the same as response