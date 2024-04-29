# Design a distributed application using MapReduce under Hadoop for: a) Character
# counting in a given text file. b) Counting no. of occurrences of every word in a given text
# file

# python Char_Count_MR.py Text_File.txt
from mrjob.job import MRJob


class MRCharCount(MRJob):

    def mapper(self, _, line):
        for char in line.strip():
            yield char, 1

    def reducer(self, char, counts):
        yield char, sum(counts)


if __name__ == '__main__':
    MRCharCount.run()
