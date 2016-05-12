# PythonTest
Programming test for an interview.

## Assignment:
* Write a program in python that gets all entries from a JSON source and store them in a database. Use http://jsonplaceholder.typicode.com/posts as a reference.
* Add a string to the body of all posts.
* Write all posts to JSON files. Use the user id as folder name, the post id as the filename.
* When the program has done its business, display the run time and the user that ran the program.

## Personal evaluation:
* This assignment has several clever things in my opinion, and I thank the guys that came up with it. See if you can spot them ;-)
* I spent the most time trying to get MySQL running on my macbook (osx 10.11.4) and finally gave up, writing a Vagrantfile instead...
* I had to think about connecting to the MySQL DB because I normally work with an ORM.
* Virtualenv was not used in this test because I did not need extra libraries that would mess up the system but I could have.
* To make it even more replicable I would add something to make MySQL accept connections for root from all hosts (`use mysql; GRANT ALL ON *.* TO 'root'@'% 'IDENTIFIED BY 'toor'; FLUSH PRIVILEGES;`)
