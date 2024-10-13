# TODO Найдите количество книг, которое можно разместить на дискете
DISK_VOL = 1.44
PAGE_NUM = 100
STR_NUM = 50
SYM_NUM = 25
VOL = 4

book_vol = PAGE_NUM * STR_NUM * SYM_NUM * VOL
book_num = int((DISK_VOL * 1024 * 1024) // book_vol)

print("Количество книг, помещающихся на дискету:", book_num)
