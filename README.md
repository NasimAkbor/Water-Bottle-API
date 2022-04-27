# Water Bottles API

An API made using Python, Flask, and SQL to display information about water bottles and the amount of mineral content within them. The API had full CRUD functionalities. 

### Description
Users will be able to access information about different Lego sets. 

## Instruction
1) Fork this repo
2) Clone it down
3) Create a virtual environment matching the folder name
4) Install the dependencies needed (found in requirements.txt)
5) Run the file using python3

NOTE** Only GET commands will work in browser. To do the rest you manipulate the API in an app like Postman.

## API Endpoints

| Method | Endpoint| Description |
|-|-|-|
| GET | /bottles | Retrieves all Bottles and thieir info |
| GET | /bottles/name | Retrieves a specific water bottle |
| POST | /bottles| Creates a bottles water based on JSON submitted |
| PUT | /bottles/Name | Update a bottle water file |
| DELETE | /bottles/name | Delete a Bottle Water object of the given name |