# CSV_Combiner

This Task takes several CSV files as arguments. Each CSV file (found in the fixtures directory of this repo) will have the same columns.Gives the Output containing new CSV file to stdout that contains the rows from each of the inputs along with an additional column that has the filename from which the row came (only the file's basename, not the entire path).

# Execution

    python csv_combiner.py ./fixtures/accessories.csv ./fixtures/clothing.csv > output.csv
    
# Unit test Execution

    python csv_combiner_test.py
    
# Example

 ## Given two input files named clothing.csv and accessories.csv.

![image](https://user-images.githubusercontent.com/43261364/161132051-d6661741-923d-4385-bcb5-0b3504e12418.png)

 ## Expected Output
 
![image](https://user-images.githubusercontent.com/43261364/161132537-ea43fd39-2ea4-4ad2-85d0-e90346cb3cf8.png)







