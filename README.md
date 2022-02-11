# Shared Document Store

This document covers the basic design of the Shared Document Store. The features available with this repo are:
* Adding a Topic
* Adding a Folder
* Uploading a document
* Searching for a document by name
* Searching for documents by Topic
* Searching for documents by Folder

## Adding a Topic
We can add a topic to the Shared Document Storage system using the [Add Topic](https://frozen-lowlands-10236.herokuapp.com/createtopic) service. A sample curl request is given below: 
```
curl -d "{\"name\":\"Philosophy\"}" https://frozen-lowlands-10236.herokuapp.com/createtopic
```
The response will be as follows:
```
{"id": 3, "name": "Philosophy"}
```
## Adding a Folder
We can add a folder to the Shared Document Storage system to organize documents using the [Add Folder](https://frozen-lowlands-10236.herokuapp.com/createfolder) service. Folders can be assigned one or more topics. A sample curl request to add a folder is given below:
```
curl -d "{\"name\":\"Humor/Comedy\", \"topic\":[1,2]}" https://frozen-lowlands-10236.herokuapp.com/createfolder
```
The response will be as follows:
```
{"id": 1, "name": "Humor/Comedy", "topic": [2, 1]}
```
## Uploading a Document
We can upload a document from the [Upload Document screen](https://frozen-lowlands-10236.herokuapp.com/doc/upload). We can select the folder that the document should be placed under and assign all relevant topics to it on this screen. 
## List Topics
We can see a list of all topics in the Document Storage System using the [List Topics](https://frozen-lowlands-10236.herokuapp.com/topics) service. 
## List Folders
We can get a list of all folders in the Document Storage System with its associated topics using the [List Folders](https://frozen-lowlands-10236.herokuapp.com/folders) service. 
## Search Document by Name
We can search for all documents containing a specific set of characters or containing a name using the [Search Document](https://frozen-lowlands-10236.herokuapp.com/doc/<docname>) service. A sample url to get all documents containing the name **Flora** is as follows:
```
https://frozen-lowlands-10236.herokuapp.com/doc/Flora
```
## Search Document by Name/Folders/Topics
We can search for all documents by name, the names of the folders that the document may be in or the topics associated with the document search using the [Search Documents](https://frozen-lowlands-10236.herokuapp.com/docs/?name=temp&name=test&name=newname) service. The search keywords are:
* **name** for searching by document name
* **topic** for searching by topic
* **folder** for searching by folder

A sample url to get all documents containing:
* the name **Flora**, 
* in folders **Plants**, **Nature**, **Environment** 
* associated with topics **Earth**, **Nature**
is as follows:
```
https://frozen-lowlands-10236.herokuapp.com/docs/?name=Flora&folder=Plant&folder=Nature&folder=Environment&topic=Earth&topic=Nature
```
