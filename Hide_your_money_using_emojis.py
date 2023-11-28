#Hide your money using emojis

row1=['😄','😄','😄']
row2=['😄','😄','😄']
row3=['😄','😄','😄']
matrix=[row1,row2,row3]


#Read position from the user
i,j=map(int,input("Enter position:").split())
matrix[i-1][j-1]='😚'
print(matrix)