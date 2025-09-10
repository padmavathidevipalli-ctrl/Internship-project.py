import numpy as np

def get_matrix():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    print("Enter the matrix row by row (space-separated):")
    
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != cols:
            print("Number of columns must match the input!")
            return None
        matrix.append(row)
    return np.array(matrix)

def operation():
    while True:
        print("\nChoose operation:")
        print("1: ADDITION")
        print("2: SUBTRACTION")
        print("3: MULTIPLICATION")
        print("4: TRANSPOSE")
        print("5: EXIT")
        
        choice = input("Enter your operation (1-5): ")
        
        if choice == "5":
            print("Exiting...")
            break
        
        if choice == "4":
            mat = get_matrix()
            if mat is not None:
                print("Result:\n", np.transpose(mat))
        else:
            print("Matrix 1:")
            mat1 = get_matrix()
            print("Matrix 2:")
            mat2 = get_matrix()
            
            if mat1 is None or mat2 is None:
                continue
            
            if choice == "1":
                if mat1.shape == mat2.shape:
                    print("Result:\n", mat1 + mat2)
                else:
                    print("Matrices must have the same dimensions for addition.")
            elif choice == "2":
                if mat1.shape == mat2.shape:
                    print("Result:\n", mat1 - mat2)
                else:
                    print("Matrices must have the same dimensions for subtraction.")
            elif choice == "3":
                if mat1.shape[1] == mat2.shape[0]:
                    print("Result:\n", np.dot(mat1, mat2))
                else:
                    print("Invalid dimensions for multiplication.")
            else:
                print("Invalid choice!")

# Run the program
operation()
