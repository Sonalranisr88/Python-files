grid = [[1,2,6], [0,4,2], [3,1,5]] 
supply = [10,10,10] 
demand = [7,12,11] 
row = 0 
col = 0
ans = 0
while(row != len(grid) and col != len(grid[0])):
	if(supply[row] <= demand[col]):
		ans += supply[row] * grid[row][col]
		demand[col] -= supply[row]
		row += 1
	else:
		ans += demand[col] * grid[row][col]
		supply[row] -= demand[col]
		col += 1
print("The answer of this transportation problem using north west method is ", ans,)
