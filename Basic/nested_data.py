"""program on nested data"""
import json

def process_json_results():

    data="""{
	"id": "0001",
	"type": "donut",
	"name": "Cake",
	"ppu": 0.55,
	"batters":
		{
			"batter":
				[
					{ "id": "1001", "type": "Regular" },
					{ "id": "1002", "type": "Chocolate" },
					{ "id": "1003", "type": "Blueberry" },
					{ "id": "1004", "type": "Devil's Food" }
				]
		},
	"topping":
		[
			{ "id": "5001", "type": "None" },
			{ "id": "5002", "type": "Glazed" },
			{ "id": "5005", "type": "Sugar" },
			{ "id": "5007", "type": "Powdered Sugar" },
			{ "id": "5006", "type": "Chocolate with Sprinkles" },
			{ "id": "5003", "type": "Chocolate" },
			{ "id": "5004", "type": "Maple" }
		]}"""
    d=json.loads(data)
    print(type(d)) 
    print(d.keys())  
    print(d["topping"][2]["id"]) 

def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)
        
 


    
#process_json_results()
d={"key1":{'c':5,'a':90,5:50},'key2':{'b':3,'c':'yes'}}
print(d)
print(pretty(d))    