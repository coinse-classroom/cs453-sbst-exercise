## Search Based Software Testing Hands-on

### [Randoop](https://randoop.github.io/randoop/)

1. Compule `Foo.java`
2. Invoke Randoop on class `Foo` to generate regression and error test cases (use the option to consider uncaught exceptions as errors)
3. Try to create another Java class `Bar` that contains an exception-raising branch that is very difficult for Randoop to execute

### [EvoSuite](https://www.evosuite.org)

1. Compile `Foo.java` and `Stack.java`
2. Use EvoSuite to generate branch-adequate JUnit test suites
3. Inspect the generated test cases

### Local Search
1. The given skeleton will generate a random Python list of length `LEN`, each element in the random range(`MAX`), called `hidden`.
2. A Euclidean distance based fitness function is provided.
3. Write a hillclimbing algorithm that uses the fitness function to retrieve contents of the hidden list, along with the number of spent fitness evaluation.
4. Write the AVM algorithm, and compare the number of fitness evaluation spent.

### Instrumentation for SBST
1. The template contains the example branches that we saw in the slides.
2. **Rewrite** the function `foo` so that, after each execution, the function updates `appr` and `bdist` with approach level and branch distance w.r.t. the target branch
(HINT: you can add support functions that implements the branch distance recipe)

### Combining Everything
1. Take the hill climbing algorithm from the Local Search task
2. Apply it to the manually instrumented function `foo`
3. See if we can generate the test data automatically
4. Consider what needs to be done if you want to do the instrumentation automatically (using Python `ast` module)