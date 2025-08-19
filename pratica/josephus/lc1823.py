# Clássico
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = list(range(1,n+1))
        pos = 0
        while len(players) > 1:
            elim = (pos + k - 1) % len(players)
            players.pop(elim)
            pos = elim % len(players)
        return players[0]

# Binário (apenas para base 2)
class Solution:
    def findTheWinner(self, n: int) -> int:
        b = bin(n)[3:] + "1"
        return int(b, 2)

              

