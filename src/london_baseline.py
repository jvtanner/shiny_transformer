# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

from tqdm import tqdm

counter_london = 0
counter_full = 0

for line in tqdm(open("birth_dev.tsv")):
    x = line.split('\t')[1]
    counter_full += 1

    if x == "London\n":
        counter_london += 1

print(counter_london / counter_full)
