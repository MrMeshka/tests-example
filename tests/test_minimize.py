from minimize import minimize

assert minimize("HELLO") == "hello"
assert minimize("HeLlO") == "hello"
assert minimize("HELLO WORLD") == "hello world"
assert minimize("") == ""