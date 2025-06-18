""""""
# 1
"""
print('''
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
How could he see where to go,
If you did not twinkle so?

In the dark blue sky you keep,
Often through my curtains peep
For you never shut your eye,
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.


''')
"""
# 3
"""
import statistics as sas
a = 5
b = 11
c = 8
l = (a,b,c)
print(sas.mean(l))
"""

# 4
"""
import os  # module

# Specify the directory path
path = '/python'

# List all entries in the specified directory
entries = os.listdir(path)

# Print the list of entries
print("Files and directories in '", path, "':")
# for loop because entries are in list
for entry in entries:
    print(entry)
"""