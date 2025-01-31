"""
I thought of a sorting algorithm that, for integers, takes O(n + r) time where n is the number of items to be sorted and r is the size of the range between min and max. The algorithm goes as follows: make one pass through the array of unsorted integers, counting the amount of times each one appears and strong that as the value in a has map, with the integer as the key, also keep track of the min and max integers. Then make one pass through the range from the min integer to the max inclusively and see if they appear as keys in the hash map. If they do, then append the value amount of that integer to a new array. For cases where n approaches or exceeds r, it would outperform all the O(n log n) sorting algorithms.
"""
def wise_counting_sort(arr):
    # Create a hash map to store the count of each integer
    count_map = {arr[0]: 1}
    # Make one pass through the array to count the occurrences of each integer and retrieve the min and max
    min_val = max_val = arr[0]
    for num in arr[1:]:
        if num in count_map:
            count_map[num] += 1
        else:
            count_map[num] = 1
        if num < min_val: 
          min_val = num
        if num > max_val:
          max_val = num
    # Make one pass through the range of values to construct the sorted array     
    sorted_arr = []
    for i in range(min_val, max_val + 1):
        if i in count_map:
            sorted_arr.extend([i] * count_map[i])

    return sorted_arr

def wise_counting_sort2(arr):
    # Create a hash map to store the count of each integer
    count_map = {arr[0]: 1}
    # Make one pass through the array to count the occurrences of each integer and retrieve the min and max
    min_val = max_val = arr[0]
    for num in arr[1:]:
        if num in count_map:
            count_map[num] += 1
        else:
            count_map[num] = 1
        if num < min_val: 
          min_val = num
        if num > max_val:
          max_val = num
    # Make one pass through the range of values to construct the sorted array
    sorted_arr = []
    curr_num = min_val
    while curr_num <= max_val:
        if curr_num in count_map:
            sorted_arr.extend([curr_num] * count_map[curr_num])
        curr_num += 1
    
    return sorted_arr
  
def wise_black_counting_sort(arr):
    # Create a hash map to store the count of each integer
    count_map = {}
    min_val = float('inf')
    max_val = float('-inf')

    # Make one pass through the array to count the occurrences of each integer
    for num in arr:
        if num in count_map:
            count_map[num] += 1
        else:
            count_map[num] = 1
        min_val = min(min_val, num)
        max_val = max(max_val, num)

    # Make one pass through the range of values to construct the sorted array
    sorted_arr = []
    for i in range(min_val, max_val + 1):
        if i in count_map:
            sorted_arr.extend([i] * count_map[i])

    return sorted_arr
  
import random
import time
def compare_wise_counting_sorts():
    n = 10000
    loops = 100
    times = [0, 0]
    for int_r in [100, 1000, 10000, 100000, 1000000, 10000000]:
      print(f"int_r = {int_r}")
      for _ in range(loops):
          arr = [random.randint(-int_r, int_r - 1) for _ in range(n)]
          
          methods = [wise_counting_sort, wise_counting_sort2]
          for i, method in enumerate(methods):
              start_time = time.time()
              method(arr)
              end_time = time.time()
              times[i] += end_time - start_time
            
      print(f"wise counting sort took {times[0]/loops} seconds")
      print(f"wise counting sort 2 took {times[1]/loops} seconds")

# compare_wise_counting_sorts()

# int_r = 10000000
# wise counting sort took 0.6986960196495056 seconds
# wise black counting sort took 0.6977080583572388 seconds

# int_r = 1000000
# wise counting sort took 0.06645619869232178 seconds
# wise black counting sort took 0.06959808588027955 seconds

# int_r = 100000
# wise counting sort took 0.06588746309280395 seconds
# wise black counting sort took 0.06761659383773803 seconds

# int_r = 10000
# wise counting sort took 0.0017896056175231933 seconds
# wise black counting sort took 0.002961125373840332 seconds

# int_r = 1000
# wise counting sort took 0.0009443855285644531 seconds
# wise black counting sort took 0.0022008752822875975 seconds

# int_r = 100
# wise counting sort took 0.0007310581207275391 seconds
# wise black counting sort took 0.0019195008277893067 seconds

"""
int_r = 100
wise counting sort took 0.0007406640052795411 seconds
wise counting sort 2 took 0.000728142261505127 seconds !
int_r = 1000
wise counting sort took 0.0019952178001403807 seconds
wise counting sort 2 took 0.001905670166015625 seconds !
int_r = 10000
wise counting sort took 0.004052045345306396 seconds !
wise counting sort 2 took 0.004087138175964356 seconds
int_r = 100000
wise counting sort took 0.012195165157318116 seconds !
wise counting sort 2 took 0.014591860771179199 seconds
int_r = 1000000
wise counting sort took 0.08059471607208252 seconds !
wise counting sort 2 took 0.0996627140045166 seconds
int_r = 10000000
wise counting sort took 0.745500750541687 seconds !
wise counting sort 2 took 0.9280169749259949 seconds
"""

from binaryHashSort import binaryHashSort as binary_hash_sort
from decHashSort import decHashSort as dec_hash_sort
import heapq
import bisect
from collections import Counter
def test_wisecounting_sort():
    def count_sort(arr):
        count_map = Counter(arr)
        sorted_arr = []
        for num in range(min(arr), max(arr) + 1):
            sorted_arr.extend([num] * count_map[num])
        return sorted_arr

    def radix_sort(arr):
        RADIX = 10
        placement = 1
        max_digit = max(arr)

        while placement < max_digit:
            buckets = [list() for _ in range(RADIX)]
            for i in arr:
                tmp = int((i / placement) % RADIX)
                buckets[tmp].append(i)
            a = 0
            for b in range(RADIX):
                buck = buckets[b]
                for i in buck:
                    arr[a] = i
                    a += 1
            placement *= RADIX
        return arr
    
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)

    def merge(left, right):
        merged = []
        left_index = right_index = 0
        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1
        merged += left[left_index:] + right[right_index:]
        return merged

    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

    def heap_sort(arr):
        heap = []
        for num in arr:
            heapq.heappush(heap, num)
        sorted_arr = []
        while heap:
            sorted_arr.append(heapq.heappop(heap))
        return sorted_arr

    def bin_sort(arr):
        sorted_arr = []
        for num in arr:
            idx = bisect.bisect_left(sorted_arr, num)
            sorted_arr.insert(idx, num)
        return sorted_arr

    n = 100000
    loops = 100  
    for int_r in [150000, 200000, 250000, 300000]:
        times = [0, 0, 0, 0, 0, 0, 0, 0]
        print(f"int_r = {int_r}")
        for _ in range(loops):
            arr = [random.randint(-int_r, int_r - 1) for _ in range(n)]
            methods = [wise_counting_sort, count_sort, binary_hash_sort, dec_hash_sort, radix_sort, merge_sort, heap_sort, bin_sort]
            for i, method in enumerate(methods):
                start_time = time.time()
                method(arr)
                end_time = time.time()
                times[i] += end_time - start_time
            
        print(f"wise counting sort took {times[0]/loops} seconds")
        print(f"count sort took {times[1]/loops} seconds")
        print(f"binary hash sort took {times[2]/loops} seconds")
        print(f"dec hash sort took {times[3]/loops} seconds")
        print(f"radix sort took {times[4]/loops} seconds")
        print(f"merge sort took {times[5]/loops} seconds")
        # print(f"quick sort took {times[6]/loops} seconds")
        print(f"heap sort took {times[6]/loops} seconds")
        print(f"bin sort took {times[7]/loops} seconds")
        
test_wisecounting_sort()

# r/n
# For only positive ints:
# Repetitive numbers:

# For <= 11, quick sort reaches maximum recursion depth.
# Same for n = 500000 and int_r = 100.+-
# 12/10000
# wise counting sort took 0.0005418586730957031 seconds
# merge sort took 0.010829219818115235 seconds
# quick sort took 0.11957258939743041 seconds ?
# heap sort took 0.0018755578994750976 seconds
# bin sort took 0.01444303035736084 seconds
# count sort took 0.00040288925170898436 seconds !

# 20/10000
# wise counting sort took 0.0005224704742431641 seconds
# merge sort took 0.010850639343261718 seconds
# quick sort took 0.07898730039596558 seconds ?
# heap sort took 0.0019635605812072755 seconds
# bin sort took 0.017989039421081543 seconds
# count sort took 0.00038849353790283204 seconds !

# 50/10000
# wise counting sort took 0.0005512380599975586 seconds
# merge sort took 0.011283936500549317 seconds
# quick sort took 0.03670651912689209 seconds ?
# heap sort took 0.0020177412033081056 seconds
# bin sort took 0.01755707025527954 seconds
# count sort took 0.00034624338150024414 seconds !

# 100/10000
# wise counting sort took 0.000498652458190918 seconds
# merge sort took 0.01100391149520874 seconds
# quick sort took 0.021916418075561522 seconds ?
# heap sort took 0.0019571232795715333 seconds
# bin sort took 0.01765233516693115 seconds
# count sort took 0.00036852121353149415 seconds !

# 1000/10000
# wise counting sort took 0.0009856939315795899 seconds
# merge sort took 0.013814406394958496 seconds
# quick sort took 0.01052459716796875 seconds
# heap sort took 0.0022315335273742675 seconds
# bin sort took 0.015049152374267578 seconds ?
# count sort took 0.000734860897064209 seconds !

# 5000/10000
# wise counting sort took 0.001172647476196289 seconds
# merge sort took 0.011894769668579101 seconds
# quick sort took 0.008353056907653809 seconds
# heap sort took 0.0020627570152282715 seconds
# bin sort took 0.01394719123840332 seconds ?
# count sort took 0.0011092042922973633 seconds !

# Sparse numbers:

# 10000/10000
# wise counting sort took 0.001627962589263916 seconds !
# merge sort took 0.012948076725006103 seconds
# quick sort took 0.010056171417236328 seconds
# heap sort took 0.002205681800842285 seconds
# bin sort took 0.015487599372863769 seconds ?
# count sort took 0.002090315818786621 seconds

# 20000/10000
# wise counting sort took 0.0018767786026000976 seconds !
# merge sort took 0.012084972858428956 seconds
# quick sort took 0.008556709289550782 seconds
# heap sort took 0.0022025370597839357 seconds
# bin sort took 0.014102354049682617 seconds ?
# count sort took 0.0030411291122436524 seconds

# 100000/10000
# wise counting sort took 0.005392639636993408 seconds
# merge sort took 0.0135299015045166 seconds
# quick sort took 0.00941924810409546 seconds
# heap sort took 0.002330009937286377 seconds !
# bin sort took 0.01645859718322754 seconds
# count sort took 0.018167171478271484 seconds ?

# 1000000/10000
# wise counting sort took 0.03413230895996094 seconds
# merge sort took 0.01208749771118164 seconds
# quick sort took 0.008150663375854492 seconds
# heap sort took 0.0020015907287597658 seconds !
# bin sort took 0.013604795932769776 seconds ?
# count sort took 0.13560982227325438 seconds

# 10000000/10000
# wise counting sort took 0.3411851382255554 seconds
# merge sort took 0.011859211921691894 seconds
# quick sort took 0.008543050289154053 seconds
# heap sort took 0.0020445871353149416 seconds !
# bin sort took 0.013922586441040039 seconds
# count sort took 1.4269865536689759 seconds ?

# Using negative integers:
# -r to r for r/n
# 100/10000
# wise counting sort took 0.0007675385475158691 seconds
# merge sort took 0.012366304397583008 seconds
# quick sort took 0.015134358406066894 seconds ?
# heap sort took 0.002061450481414795 seconds 
# bin sort took 0.014753398895263671 seconds
# count sort took 0.0006062531471252441 seconds !

# 1000/10000
# wise counting sort took 0.0010204291343688964 seconds
# merge sort took 0.013471684455871581 seconds
# quick sort took 0.009627082347869874 seconds
# heap sort took 0.002224776744842529 seconds
# bin sort took 0.015552499294281007 seconds ?
# count sort took 0.0007968902587890625 seconds !

# 10000/10000
# wise counting sort took 0.0020115137100219726 seconds !
# merge sort took 0.012347335815429688 seconds
# quick sort took 0.009374113082885742 seconds
# heap sort took 0.002415900230407715 seconds
# bin sort took 0.014689507484436036 seconds
# count sort took 0.0035338664054870607 seconds ?

# 100000/10000
# wise counting sort took 0.007893228530883789 seconds
# merge sort took 0.011784965991973878 seconds
# quick sort took 0.008170180320739746 seconds
# heap sort took 0.0020566821098327638 seconds !
# bin sort took 0.013886399269104004 seconds
# count sort took 0.028082218170166016 seconds ?

# 1000000/10000
# wise counting sort took 0.07389483451843262 seconds
# merge sort took 0.012551662921905517 seconds
# quick sort took 0.008779318332672119 seconds
# heap sort took 0.0021179795265197756 seconds !
# bin sort took 0.014469921588897705 seconds
# count sort took 0.29775788068771364 seconds ?

''' for n = 10000
int_r = 100
wise counting sort took 0.0007042813301086425 seconds
binary hash sort took 0.005941166877746582 seconds
merge sort took 0.011257791519165039 seconds
quick sort took 0.013363072872161865 seconds
heap sort took 0.0019229769706726075 seconds
bin sort took 0.012774558067321777 seconds
count sort took 0.0005388283729553223 seconds !
int_r = 1000
wise counting sort took 0.0008662080764770508 seconds
binary hash sort took 0.008102254867553711 seconds
merge sort took 0.011239135265350341 seconds
quick sort took 0.008320968151092529 seconds
heap sort took 0.0019750499725341795 seconds
bin sort took 0.012994909286499023 seconds
count sort took 0.0006951642036437988 seconds !
int_r = 10000
wise counting sort took 0.001980409622192383 seconds !
binary hash sort took 0.015090312957763672 seconds
merge sort took 0.011299314498901368 seconds
quick sort took 0.007863430976867676 seconds
heap sort took 0.0019601988792419434 seconds
bin sort took 0.013689231872558594 seconds
count sort took 0.003012070655822754 seconds
int_r = 100000
wise counting sort took 0.007757096290588379 seconds
binary hash sort took 0.024231560230255127 seconds
merge sort took 0.010945498943328857 seconds
quick sort took 0.007698311805725098 seconds
heap sort took 0.0019408917427062987 seconds !
bin sort took 0.012860796451568603 seconds
count sort took 0.026513612270355223 seconds
'''
''' for n = 20000
int_r = 100
wise counting sort took 0.0015740060806274413 seconds
binary hash sort took 0.012539381980895997 seconds
merge sort took 0.025387215614318847 seconds
quick sort took 0.0443075966835022 seconds
heap sort took 0.004265105724334717 seconds
bin sort took 0.056472482681274416 seconds
count sort took 0.001125931739807129 seconds !
int_r = 1000
wise counting sort took 0.0015490460395812988 seconds
binary hash sort took 0.0159861159324646 seconds
merge sort took 0.023717548847198486 seconds
quick sort took 0.018580822944641112 seconds
heap sort took 0.004344978332519531 seconds
bin sort took 0.052063822746276855 seconds
count sort took 0.0011673521995544433 seconds !
int_r = 10000
wise counting sort took 0.0027036666870117188 seconds !
binary hash sort took 0.025541517734527588 seconds
merge sort took 0.02343769311904907 seconds
quick sort took 0.01639326333999634 seconds
heap sort took 0.004292595386505127 seconds
bin sort took 0.05133686065673828 seconds
count sort took 0.003203420639038086 seconds
int_r = 100000
wise counting sort took 0.008708395957946778 seconds
binary hash sort took 0.041840274333953854 seconds
merge sort took 0.02313981294631958 seconds
quick sort took 0.01626720428466797 seconds
heap sort took 0.004250237941741944 seconds !
bin sort took 0.05117754220962525 seconds
count sort took 0.02625779390335083 seconds
int_r = 1000000
wise counting sort took 0.06643813610076904 seconds
binary hash sort took 0.06573899269104004 seconds
merge sort took 0.024065773487091064 seconds
quick sort took 0.01676027774810791 seconds
heap sort took 0.004326937198638916 seconds !
bin sort took 0.05256741762161255 seconds
count sort took 0.27237414836883544 seconds
'''
''' for n = 50000
int_r = 100
wise counting sort took 0.0037116360664367675 seconds
binary hash sort took 0.031575131416320804 seconds
merge sort took 0.07008803129196167 seconds
quick sort took 0.21400234699249268 seconds
heap sort took 0.011624016761779786 seconds
bin sort took 0.33268226861953737 seconds ?
count sort took 0.0028172969818115235 seconds !
int_r = 1000
wise counting sort took 0.003755679130554199 seconds
binary hash sort took 0.03982186555862427 seconds
merge sort took 0.06560032606124878 seconds
quick sort took 0.059156455993652345 seconds
heap sort took 0.01274606704711914 seconds
bin sort took 0.32696469068527223 seconds ?
count sort took 0.002795729637145996 seconds !
int_r = 10000
wise counting sort took 0.005949909687042236 seconds
binary hash sort took 0.06058638095855713 seconds
merge sort took 0.06575311660766602 seconds
quick sort took 0.046639549732208255 seconds
heap sort took 0.012821528911590576 seconds
bin sort took 0.3168133115768433 seconds ?
count sort took 0.004765777587890625 seconds !
int_r = 20000
wise counting sort took 0.007752704620361328 seconds !
binary hash sort took 0.07832008361816406 seconds
merge sort took 0.07087446212768554 seconds
quick sort took 0.05021707773208618 seconds
heap sort took 0.014279437065124512 seconds
bin sort took 0.33230202198028563 seconds ?
count sort took 0.007863104343414307 seconds
int_r = 100000
wise counting sort took 0.012138931751251221 seconds !
binary hash sort took 0.10216902494430542 seconds
merge sort took 0.06469780921936036 seconds
quick sort took 0.0452589750289917 seconds
heap sort took 0.012852234840393066 seconds
bin sort took 0.31387016296386716 seconds ?
count sort took 0.027507736682891845 seconds
'''
''' 
for n = 100000
int_r = 100
wise counting sort took 0.007589132785797119 seconds
binary hash sort took 0.06214733839035034 seconds
dec hash sort took 0.028156325817108155 seconds
merge sort took 0.14259565353393555 seconds
quick sort took 0.7983507609367371 seconds
heap sort took 0.02364750385284424 seconds
count sort took 0.0056849527359008785 seconds
int_r = 1000
wise counting sort took 0.007257547378540039 seconds
binary hash sort took 0.07748674392700196 seconds
dec hash sort took 0.0357969880104065 seconds
merge sort took 0.142030029296875 seconds
quick sort took 0.15669968366622924 seconds
heap sort took 0.028242263793945312 seconds
count sort took 0.005272176265716553 seconds
int_r = 10000
wise counting sort took 0.00913733959197998 seconds
binary hash sort took 0.11342888355255126 seconds
dec hash sort took 0.04522015810012817 seconds
merge sort took 0.13917894124984742 seconds
quick sort took 0.10239872455596924 seconds
heap sort took 0.02806950092315674 seconds
count sort took 0.007026398181915283 seconds
int_r = 100000
wise counting sort took 0.019667155742645263 seconds
binary hash sort took 0.18414395809173584 seconds
dec hash sort took 0.08656525611877441 seconds
merge sort took 0.13729483604431153 seconds
quick sort took 0.09556241512298584 seconds
heap sort took 0.027419207096099855 seconds
count sort took 0.029933125972747804 seconds
int_r = 1000000
wise counting sort took 0.06746742486953736 seconds
binary hash sort took 0.34703328609466555 seconds
dec hash sort took 0.21001242399215697 seconds
merge sort took 0.1338896131515503 seconds
quick sort took 0.09361958503723145 seconds
heap sort took 0.02716545104980469 seconds
count sort took 0.25783729553222656 seconds
'''
'''for n=100000
int_r = 150000
wise counting sort took 0.026001784801483154 seconds
count sort took 0.04669290781021118 seconds
binary hash sort took 0.22776042699813842 seconds
dec hash sort took 0.10844118356704711 seconds
radix sort took 0.06329371213912964 seconds
merge sort took 0.09022497177124024 seconds
heap sort took 0.02040376663208008 seconds
bin sort took 1.1894132995605469 seconds
int_r = 200000
wise counting sort took 0.02539945363998413 seconds
count sort took 0.05574319362640381 seconds
binary hash sort took 0.23342375040054322 seconds
dec hash sort took 0.11827208518981934 seconds
radix sort took 0.06512683153152465 seconds
merge sort took 0.08950021505355835 seconds
heap sort took 0.0201138973236084 seconds
bin sort took 1.1490886092185975 seconds
int_r = 250000
wise counting sort took 0.029422826766967773 seconds
count sort took 0.06845591306686401 seconds
binary hash sort took 0.2594465684890747 seconds
dec hash sort took 0.13001112937927245 seconds
radix sort took 0.0627887201309204 seconds
merge sort took 0.09124549865722656 seconds
heap sort took 0.02189523935317993 seconds
bin sort took 1.1610770845413207 seconds
int_r = 300000
wise counting sort took 0.03213505268096924 seconds
count sort took 0.08123610734939575 seconds
binary hash sort took 0.2540627193450928 seconds
dec hash sort took 0.13851625442504883 seconds
radix sort took 0.06436794996261597 seconds
merge sort took 0.09122348308563233 seconds
heap sort took 0.020716807842254638 seconds
bin sort took 1.1510496473312377 seconds
'''