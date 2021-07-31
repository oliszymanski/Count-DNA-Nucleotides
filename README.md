# Count-DNA-Nucleotides
Used for counting the number of all four nucleotides and finding the percentage number of each of them



<br>

## About the project

This program made are specifically for studies made with genetics and organisms in microbiology such 
as viruses or bacterias. There are a few features here:

1. Counting the amount of nucleotides (in a specific sequence)
2. counting the percentage of each nucleotide


You can count all nucleotides in DNA and RNA.




<br>

## How does this work

Genetic sequence should be written in a .txt file. In the example with DNA, every sequence should have
symbols A, C, G and T; with RNA without T. Then you need to specify files path (if its in a local 
directory, just specify the name) in `count_nucleotides()`. 

All the characters in the file need to be type string. You need to go through the file and change every
single character to string. This can be done by using:
```python
    ls = [ str(element) for element in ls ]
```



<br>


### Counting nucleotides

When every element is string type, we can go through every element and with if statements, that way each
element will be automatically assigned to its list:

**note:** There is a list made for every nucleotide.

```python
    for element in line:

        if (element == 'A'): ls_a_amount.append(element)       # find adenine

        elif (element == 'C'): ls_c_amount.append(element)     # find cytosine

        elif (element == 'G'): ls_g_amount.append(element)     # find guanine

        elif (element == 'T'): ls_t_amount.append(element)     # find thymine
```


<br>

Length of each list will be saved in a dictionary.

The `count_nucleotides()` returns the amount of every nucleotide which is stored in a dictionary (key
is the nucleotide and value length of each list):

```python
    dict_nucleotides = { 'A' : len(ls_s_a) ,'C' : len(ls_s_c), 'G' : len(ls_s_g), 'T' : len(ls_s_t) }
```



<br>

### Counting percentage of each nucleotide

The length of lists will be added to one "main" list of data. We need to have the number of all nucleotides
and that's why the `sum()` needs to be used on the main list. 

We loop through that same list and divide every element by the sum of main list, and multiply the value by 100
to get the percentage. Add that value to `ls_percentage` list:

```python
    for element in ls_main:
        
        val = ( element / sum(ls_main) ) * 100

        ls_percentage.append( val )
```

<br>


When that is done, elements from `ls_percentage` will be added into a dictionary which can be returned by the
function.



<br>

### Note
I will be adding more features in the future