#!/usr/bin/python3
# 6.5 Write code using find() and string slicing (see section 6.10)
# to extract the number at the end of the line below.
# Convert the extracted value to a floating point number and print it out.


test = "X-DSPAM-Confidence:    0.8475";

wordc = test.find('0')

output_word = test[ wordc:]

output_word = float(output_word)

print(output_word)
