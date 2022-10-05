def convert_unit(num,in_type,out_type):
    scale={ 'Tm' : 1000000000000,
            'Gm' : 1000000000, 
            'Mm' : 1000000, 
            'Km' : 1000, 
            'hm' : 100, 
            'dam': 10, 
            'm'  : 1, 
            'dm' : 1/10,  
            'cm' : 1/100,  
            'mm' : 1/1000,  
            'um' : 1/1000000,  
            'nm' : 1/1000000000}  
    output=num*(scale[in_type]/scale[out_type])
    stri=str(output)+" "+out_type
    
    return stri
print(convert_unit(15.6, 'm', 'cm') )
