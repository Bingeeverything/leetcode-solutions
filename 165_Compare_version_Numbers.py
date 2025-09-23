class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split(".")
        ver2 = version2.split(".")
        
        max_len = max(len(ver1), len(ver2))
        
        for i in range(max_len):
            rev1 = int(ver1[i]) if i < len(ver1) else 0
            rev2 = int(ver2[i]) if i < len(ver2) else 0
            
            if rev1 < rev2:
                return -1
            elif rev1 > rev2:
                return 1
        return 0