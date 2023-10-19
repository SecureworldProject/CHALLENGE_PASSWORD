# CHALLENGE_PASSWORD
This is a basic challenge that asks the pc user for a password to generate the challenge key. Note this means that it is focused in providing conventional security against the external threat.

It allows two modes of execution:
* Parental: checks the user input against the configured `parental_key`.
* Non-parental: the user input is the challenge key result.




## Requisites

##### Python and the Challenge loader
This challenge is written in python and therefore it requires Python version 3.10 or later and the challenge loader (`challenge_loader_python.dll`) to be able to execute inside securemirror.




## Configuration
The value of the `"FileName"` field must be `"challenge_loader_python.dll"`.
Inside `"Props"` field there must be several key-value pairs:
* `"module_python"`: must contain the python module file name (without including ".py"). In this case: `"chpass"`.
* `"validity_time"`: the validity time of the challenge in secconds (integer).
* `"refresh_time"`: the time in secconds (integer) between automatic executions of the challenge.
* `"mode"`: determines the mode of execution. The parental mode is selected if its value is `"parental"`. The non-parental mode is used otherwise.
* `"parental_key"`: the key (string) with which the user input will be checked against to allow or not access if the parental mode is active. Not used in non-parental mode.

Other fields like `"Description"` and `"Requirements"` are optional and merely informative.


##### Example
This is an example of the configuration of the challenge. This code would be inserted as a value in the array `"ChallengeList"` inside a challenge equivalence group.
In parental mode the key typed by user is compared with the right one: the "parental key" parameter
```json
{
	"FileName": "challenge_loader_python.dll",
	"Description": "Loads a python challenge.",
	"Props": {
		"module_python": "chpass",
		"validity_time": 3600,
		"refresh_time": 3000,
		"mode": "parental",
		"parental_key": "1234"
	},
	"Requirements": "none"
}
```

and this is another example for normal use (NOT parental). 
In normal mode the key typed by user is the returned value. there is nothing to compare
```json
{
	"FileName": "challenge_loader_python.dll",
	"Description": "Loads a python challenge.",
	"Props": {
		"module_python": "chpass",
		"validity_time": 3600,
		"refresh_time": 3000,
		"mode": "normal",
		"parental_key": "1234"
	},
	"Requirements": "none"
}
```




## How to use
Copy `chpass.py` into the execution folder.
Ensure that the loader (`challenge_loader_python.dll`) is there also.
Finally, add the challenge configuration in the `config.json`.
