# Berkeley Deep Drive (BDD) dataset from json to xml.
The script provided will change the json formatted data to xml format (specifically Pascal Annotation format). The images and the output xml file will be renamed to an ascending order of number from 0 to the total number of data.

###Limitation
- The script cannot be used to convert the 'drivable area' and 'lane' categories. Hence, those will be skipped. However, more categories can be skipped by adding the category name to the ```unwanted_lists``` variable in line 71 in [convert.py](https://github.com/Ugenteraan/bdd_json_to_xml/blob/master/convert.py) or the same variable in the .ipynb file. 
