
<p align="center">
    <img src="assets/python.png" width="70">
</p>

<h1 align="center">Python Code Smells</h1>

```text
    .
    ├── shotgun_surgery   # folder with shotgun surgery code smell
    ├── assets
    ├── LICENSE
    └── README.md
```

## Shotgun Surgery
### What is it?
Shotgun surgery is a code smell that occurs when a single change to the source code requires changes to multiple classes. This is a problem because it means that the code is not cohesive and that the code is not encapsulated. This means that the code is not modular and that it is not easy to maintain.

<hr />

### Example

### Code example
Go to [shotgun surgery folder](https://github.com/Walikuperek/Python-code-smells/tree/master/shotgun_surgery) and check the code.

### How to fix it?
Proper models which encapsulates basic operations -> once done others don't have to remember :)

Check files in order:
1. problem.py
2. naive_solution.py 
3. smart_solution.py
4. ddd.py - this is the best solution

<hr />

Made with ♡ by [QUAK](https://quak.com.pl/)
