#!/usr/bin/python3                                                                    
"""This script is the base model"""                                                   
                                                                                      
import uuid                                                                           
from datetime import datetime                                                         
from models import storage                                                            
                                                                                      
                                                                                      
class BaseModel:                                                                      
                                                                                      
    """Class from which all other classes will inherit"""                             
                                                                                      
    def __init__(self, *args, **kwargs):                                              
        """Initializes instance attributes                                            
                                                                                      
        Args:                                                                         
            - *args: list of arguments                                                
            - **kwargs: dict of key-values arguments                                  
        """                                                                           
                                                                                      
        if kwargs is not None and kwargs != {}:                                       
            for key in kwargs:                                                        
                if key == "created_at":
