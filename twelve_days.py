def recite():
    day_num = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
    lyric = ['a Partridge in a Pear Tree.', 'two Turtle Doves,', 'three French Hens,', 'four Calling Birds,', 'five Gold Rings,', 'six Geese-a-Laying,', 'seven Swans-a-Swimming,', 'eight Maids-a-Milking,',\
            'nine Ladies Dancing,', 'ten Lords-a-Leaping,', 'eleven Pipers Piping,', 'twelve Drummers Drumming,']
    
    for i in range(len(day_num)):
        print(f"On the {day_num[i]} day of Christmas my true love gave to me:", end="")
        j = i
        while j >= 1:
            print(f" {lyric[j]}", end="")
            j -= 1
        if i != 0:
            print(f" and  {lyric[0]}")
        else:
            print(f"{lyric[0]}")

recite()