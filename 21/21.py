from functools import lru_cache
from time import time

def deterministic_die():
    while True:
        for i in range(1, 101):
            yield i

def play_one(p1, p2, s1, s2, goal):
    d = deterministic_die()
    game = True
    rolls = 0
    
    while game:
        roll = [next(d),next(d),next(d),]
        rolls += 3
        p1 += sum(roll) % 10
        p1 = p1 if p1 <= 10 else p1 % 10
        s1 += p1
        if s1 >= goal:
            break
        
        roll = [next(d),next(d),next(d),]
        rolls += 3
        p2 += sum(roll) % 10
        p2 = p2 if p2 <= 10 else p2 % 10
        s2 += p2
        if s2 >= goal:
            break
            
    return min(s1, s2) * rolls
        

@lru_cache
def play_two(p1, p2, s1, s2):
    
    p1_wins = 0
    p2_wins = 0
    
    for roll_sum, times in {6: 7, 5: 6, 7: 6, 4: 3, 8: 3, 3: 1, 9: 1}.items(): # 4 is more often achieved than 3...
        np1 = p1 + roll_sum
        np1 = np1 if np1 <= 10 else np1%10
        ns1 = s1 + np1
        if ns1 >= 21:
            p1_wins += times
        else:
            for roll_sum, times2 in {6: 7, 5: 6, 7: 6, 4: 3, 8: 3, 3: 1, 9: 1}.items():
                np2 = p2 + roll_sum
                np2 = np2 if np2 <= 10 else np2%10
                ns2 = s2 + np2
                if ns2 >= 21:
                    p2_wins += times * times2
                else:
                    p1w, p2w = play_two(np1, np2, ns1, ns2)
                    p1_wins += p1w * times * times2
                    p2_wins += p2w * times * times2
                    
    
    return p1_wins, p2_wins


if __name__ == "__main__":
    st = time()
    print("Test One:", play_one(4,8,0,0,1000), " == 739785?")
    print("Part One:", play_one(3,5,0,0,1000), f" == 720750? -> {time()-st:.4f} s")
    st = time()
    print("Test Two:", play_two(4,8,0,0), f"== 444356092776315? -> {time()-st:.4f} s")
    st = time()
    print("Part Two:", play_two(3,5,0,0), f"-> {time()-st:.4f} s")
    