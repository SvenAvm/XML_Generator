The script (**xml_generator.py**) will create a logs.xml file with randomly generated transaction logs.
values_generator.py generates the values to be used in the xml log.
splunk_script_py does the same job as XML_Generator, but does it without the need for values_generator, at the expense of code readability

# Template:

		
			    	<LOG>  
    			<DATE>DDMMYYYY</DATE>  
    			<TIME>HHMMSS</TIME>  
    			<CC>\d{16}</CC>  
    			<AMOUNT>\d+\.\d{2}</AMOUNT>  
    			</LOG>

## Date: 
8 character long integer, in the format DDMMYYYY
		   date used will be today

## Time: 
Randomly generated 6 character long integer, in the format HHMMSS

## CC:	
Randomly generated 16 character long integer, representing a credit card number

## Amount: 
Randomly generated float representing a transaction amount, limited to 2 numbers after the decimal point

