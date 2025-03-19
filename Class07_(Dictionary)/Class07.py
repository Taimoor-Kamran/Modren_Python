from typing import Dict, Union, Optional
import pprint
# List     

key = Union[int, str] # create custom tyep
Value = Union[int, str, list, dict, tuple, set]


data: Dict[key,Value] = {"fname": "Kamran Sattar",
                        "name" : "Taimoor Kamran", 
                        "education" : "MSDS"
                        }

pprint.pprint(data)
