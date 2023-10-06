# 函数的定义和使用
def is_float(sInput):
    sInput = str(sInput)
    if sInput.count('.') == 1:
        sLeft = sInput.split('.')[0]  # 小数左边
        sRight = sInput.split('.')[1]  # 小数右边
        if sLeft.isdigit() and sRight.isdigit():
            return True  # 正小数
        elif sLeft.startswith('-') and sLeft.count('-') == 1 and \
                sLeft.split('-')[1].isdigit() and sRight.isdigit():
            return True  # 负小数
        else:
            return False
    else:
        return False
