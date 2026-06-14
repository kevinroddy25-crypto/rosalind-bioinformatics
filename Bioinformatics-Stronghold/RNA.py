# Problem 2: Transcribe a given strand of DNA (t) into its RNA (u) equivalent.

t = input("Enter a DNA string: ")

# Return the transcribed RNA of string t.
u = t.replace('T', 'U')

print("The transcribed RNA string is:", u)
