# P4 Demo
This repo contains two highly simplified demo directories: mapreduce and threads_and_sockets

We hope that these demos provide a foundation for you to get started on Project 4. You will have to build on the concepts presented in this demo, the spec, and the lecture slides in order to build a fully functional MapReduce server like the one necessary for P4
<br><br>

## mapreduce
The intent of this directory is to provide a Python (AKA human-readable) solution to the simple word count job illustrated in Bash in the project spec [here](https://eecs485staff.github.io/p4-mapreduce/#walk-through-example).

This solution is highly simplified with the intent to give you an idea of how to write MapReduce jobs. This is not a memory-efficient implementation, due to the use of a dictionary in our reducer, but it's necessary in order to keep the simplicity for this demo.

The main purpose of the mapper is identify key-value pairs that will allow us to accomplish the computation we desire in a parallel manner. We do this by associating keys to values, **knowing that each reducer is going to receive every key for a each given value**.

In this case, we want to map each word to a value of 1, `<word, 1>`, so that the reducer will receive a count value each individual occurrence of the word.
