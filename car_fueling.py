def compute_min_refills(distance, tank, stops):
    pre_stop = 0
    return_val = 0
    length = len(stops) 
    for i in range(length):
        if stops[i]>(tank+pre_stop):
            if (stops[i-1]-pre_stop)>tank:
                return -1
            pre_stop = stops[i-1]
            return_val += 1
    if distance>(tank+pre_stop):
        
        if (stops[length-1] - stops[length-2])>tank:
            return -1
        if distance>(tank+stops[length-1]):
            return -1
        return_val += 1
            
    return return_val

if __name__ == '__main__':
    d = int(input())
    m = int(input())
    n = int(input())
    stops = list(map(int, input().split()))
    print(compute_min_refills(d, m, stops))
