class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        l1=[0,0]
        m=[float('inf'),0]
        f1=True
        for i in range(len(grid)):
            if 1 in grid[i]:
                if f1:
                    l1[0]=i
                    f1=False
                l1[1]=i
            else:
                continue
            c=grid[i][::-1]
            m[0]=min(m[0],grid[i].index(1))
            m[1]=max(m[1],len(grid[i])-c.index(1))
        l1=l1[1]-l1[0]+1
        m=m[1]-m[0]
        return l1*m