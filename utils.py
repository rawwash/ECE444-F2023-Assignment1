class Utils:
    @staticmethod
    def reversed_int(value):
        if type(value) != int:
            raise TypeError(f"Incorrect type: {type(value)}")
        
        str_equiv = str(value)
        reversed_string = ""
        is_negative = False
        if str_equiv[0] == "-":
            is_negative = True
            str_equiv = str_equiv[1:]
        
        for i in range(len(str_equiv)-1, -1, -1):
            reversed_string += str_equiv[i]
        
        final_int = 0
        if (is_negative):
            final_int = int(reversed_string) * -1
        else:
            final_int = int(reversed_string)
        return final_int
    
    @staticmethod   
    def formatter(value):
        if type(value) != int:
            raise TypeError(f"Incorrect type: {type(value)}")
        
        binary = bin(value)
        octal = oct(value)

        return binary, octal

