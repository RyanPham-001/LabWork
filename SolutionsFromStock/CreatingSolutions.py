from Solution import Solution

test = Solution(400,"NaCl")
print(test.get_concentration())
print(test)

test.set_compound_formula("KCl")
test.set_concentration(300)
print(test)
