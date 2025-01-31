# Now, you will use the same strategy to assess two different methods for solving a similar problem: calculate the sum of squares of all the positive integers from 1 to 1 million (1,000,000). Similar to what you saw in the video, you will compare two methods; one that uses brute force and one more mathematically sophisticated. In the function formula, we use the standard formula N∗(N+1)(2N+1)/6 where N=1,000,000. In the function brute_force we loop over each number from 1 to 1 million and add it to the result.

# Calculate the result of the problem using formula() and print the time required
N = 1000000
fm_start_time = time.time()
first_method = formula(N)
print("Time using formula: {} sec".format(time.time() - fm_start_time))

# Calculate the result of the problem using brute_force() and print the time required
sm_start_time = time.time()
second_method = brute_force(N)
print("Time using the brute force: {} sec".format(time.time() - sm_start_time))

# <script.py> output:
    # Time using formula: 0.0001823902130126953 sec
    # Time using the brute force: 0.2707936763763428 sec
