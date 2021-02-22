
ZW_ONE = u"\u200b"
ZW_ZERO = u"\u200c"
ZW_SEP = u"\u200d"

class ZWStringConverter:
    def __init__(self, targetString):
        self.targetString = targetString
    
    def isZWS(self):
        """Determine whether the string is encoded with ZWS.

        Returns:
            bool: Whether the string is encoded with ZWS.
        """        
        for char in self.targetString:
            if char != ZW_ONE and char != ZW_ZERO and char != ZW_SEP:
                return False
        return True
    
    def convert(self):
        """Encrypt the string if it's a ZWS instance, or vice versa.

        Returns:
            str: Converted string.
        """        
        if self.isZWS():
            return self.unzerowidth()
        else:
            return self.zerowidth()

    def zerowidth(self):
        """Encrypt the string with ZWS.

        Returns:
            str: The encrypted string.
        """        
        origin = self.targetString
        bin_text = []
        for char in origin:
            bin_text.append(str(bin(ord(char))).lstrip('0b'))

        final_str = ""
        for item in bin_text:
            for binchar in item:
                final_str += ZW_ONE if binchar == "1" else ZW_ZERO
            final_str += ZW_SEP
        final_str.rstrip(ZW_SEP)
        return final_str

    def unzerowidth(self):
        """Decrypt the ZWS string to a normal string.

        Returns:
            str: The decrypted string.
        """        
        enc_str = self.targetString
        arr_oz = []
        for char in enc_str:
            if char == ZW_ONE: ZWStringConverter.apponlast(arr_oz, "1")
            elif char == ZW_ZERO: ZWStringConverter.apponlast(arr_oz, "0")
            elif char == ZW_SEP: arr_oz.append("")
            else: 
                # print("Input contains non-ZW string. Aborted.")
                return "Input contains non-ZW string."

        for idx in range(0, len(arr_oz)-1):
            arr_oz[idx] = chr(int(arr_oz[idx], 2))

        return "".join(arr_oz)

    @staticmethod
    def apponlast(arr, sth):
        """Append a string on the last element of the given array. If the array is empty, a new element will be created.

        Args:
            arr (list): The array object.
            sth (str): The string which is going to be appended.
        """        
        la = len(arr)
        if la: arr[la-1] += sth
        else: arr.append(sth)