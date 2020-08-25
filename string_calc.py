import re

class StringCalc:

    def split_string(self, str_num):
        if str_num[:2] == '//':
            spl_pnt = str_num[2]
            lst = re.split(f"[{spl_pnt} \n]", str_num[3:])
        else:
            lst = re.split('[, \n]', str_num)
        return lst

    def to_int_list(self, str_num):
        lst = self.split_string(str_num)
        for i in range(len(lst)):
            if lst[i] == "":
                lst[i] = 0
            else:
                lst[i] = int(lst[i])
        return lst

    def check_negative(self, lst):
        negative_nums = []
        for item in lst:
            if item < 0:
                negative_nums.append(item)
        if negative_nums:
            raise ValueError(f'Negatives not allowed. {negative_nums} entered as argument')
                

    def add_num(self, str_num):
        lst = self.to_int_list(str_num)
        self.check_negative(lst)
        total = 0
        for x in lst:
            total += x
        return total