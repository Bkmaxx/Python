'''
1Tm : 1,000,000,000,000 meters
1Gm : 1,000,000,000 meters
1Mm : 1,000,000 meters
1Km : 1,000 meters
1hm : 100 meters
1dam : 10 meters
1m : 1 meter
1dm : 1/10 of a meter
1cm : 1/100 of a meter
1mm: 1/1,000 of a meter
1um: 1/1,000,000 of a meter
1nm: 1/1,000,000,000 of a meter
Write a Python function convert_units() that has a syntax:
convert_units(val, in_units, out_units)

Example:
convert_units(12.34, 'm', 'cm')           Output: 1234 cm
convert_units(12.34, 'm', 'Km')           Output: 0.01234 Km
convert_units(12.34, 'Km', 'um')         Output: 1.234e+10 um


Write a Python function nearest_units() that has syntax:
nearest_units(val, in_units)

Example:
nearest_units(0.012, 'm')                 Output: 1.2 cm
nearest_units(0.12, 'm')                   Output: 1.2 dm
nearest_units(0.00000147, 'mm')   Output: 1.47 nm
nearest_units(345345345, 'nm')     Output: 3.45345345 dm
nearest_units(12345, 'm')                Output: 12.345 Km
nearest_units(123456, 'm')              Output: 0.123456 Mm
nearest_units(1234567, 'm')            Output: 1.23456 Mm

'''
def convert_unit(num,in_type,out_type):
    output=num
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
    if(in_type !='m'):
            output=num*(scale[in_type])
    
    if(in_type != out_type):
            output=output/(scale[out_type])
    
    stri=str(output)+" "+out_type
    return stri

print(convert_unit(12.34, 'Km', 'um') )