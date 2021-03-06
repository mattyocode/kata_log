import re

class StringCalc:

    def add_num(self, str_num):
        lst = self.to_int_list(str_num)
        self.check_negative(lst)
        self.check_below_1000(lst)
        total = 0
        for x in lst:
            total += x
        return total

    def split_string(self, str_num):
        if str_num[:3] == '//[':
            lst = self.square_bracket_delimiter_split(str_num)
        elif str_num[:2] == '//':
            spl_pnt = str_num[2]
            lst = re.split(f"[{spl_pnt} \n]", str_num[3:])
        else:
            lst = re.split('[, \n]', str_num)
        return lst

    def square_bracket_delimiter_split(self, str_num):
        rules = re.compile(r"\[([^\[\]]+)\]")
        delimiters = rules.findall(str_num)
        delimiters_str = ' '.join(delimiters)
        defaults = r'\/ [ \]'
        pattern = f"[{delimiters_str} \n {defaults} ]"
        lst = re.split(f'{pattern}', str_num)
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
                
    def check_below_1000(self, lst):
        for item in lst:
            if item > 1000:
                lst.remove(item)
