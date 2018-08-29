# Text Filter (Incomplete)
These programs should allow us to find the average percentage of the most
popular words in the playbills, compare the sum of the average words to the
sum of the average words in any given playbill, and, if the sum is significantly
less than this average, mark that playbill for editing. These programs should
help us to figure out which playbill txt files desperately need our attention.
So far, these programs will find the 200 most popular words in the playbills,
obtain the average appearance of these words in a range of playbills - ignoring
words with under 0.01 percent appearance, and find the average sum of the most
popular words in any playbill or folder. Comparison functions still need to
be finished and tested.

## Word Counter
#### Running
In Terminal, cd into the folder where the download is desired. Enter ``python3
word_counter.py [folder pathname]`` Full pathname may be needed. Enter the folder
containing the playbill text files to be searched. Again, full pathname may be
needed. The program will search all txt files, including files found in subfolders,
for the 200 most common words. The program should ignore most incorrect words and
symbols (i.e. "U", "1fja", "I''", etc.) A csv containing the results will be created and
stored in the current directory.

## Stats Runner (Incomplete)
#### Running
In Terminal, cd into the folder where the download is desired. Enter ``python3
stats_runner.py [file] [folder]`` Full pathname may be needed. This program
will currently find the sum of the average appearances of each of the prevalent
most popular words, taken from the csv file created in Word Counter. Any word with
less than a 0.01 percent appearance will be ignored. This program currently Creates
a csv file with the average appearances of the most popular words, ignoring the
less prevalent words. An option to produce a csv with more detailed (but less
efficiently displayed) results is present, but not active.

#### To be done
When complete, this program will compare the sum of the word average percentages
with the sum of the word percentages in an individual playbill. If the difference
is over a certain threshold, (i.e. if the sum from the individual playbill is less
than half the sum of the average percentages), then the playbill will be renamed
or sorted to be edited.

## CSV Dictionary Writer
Contains the functions necessary to format a properly designed list of lists and convert it
into a csv file, which will be returned in the given path name. Useful and transferable
to other projects.

## Author
Anastasia Hutnick
