class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        s_len, t_len = len(stamp), len(target)
        s_list, t_list = list(stamp), list(target)
        result = []
        stamped = [False] * t_len
        total_stamped = 0
        
        def can_stamp(start):
            for i in range(s_len):
                if t_list[start + i] != '?' and t_list[start + i] != s_list[i]:
                    return False
            return True
        
        def do_stamp(start):
            nonlocal total_stamped
            for i in range(s_len):
                if t_list[start + i] != '?':
                    t_list[start + i] = '?'
                    total_stamped += 1
            result.append(start)
        
        changed = True
        while changed:
            changed = False
            for i in range(t_len - s_len + 1):
                if not stamped[i] and can_stamp(i):
                    do_stamp(i)
                    stamped[i] = True
                    changed = True
            if total_stamped == t_len:
                return result[::-1]
        
        return []
