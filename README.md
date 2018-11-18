# PySimplex

The simplex tree is an efficient data structure for representing simplicial complex of any dimension. All of face in simplicial complex store in a trie which nodes are bijection with the face of complex.
![alt text](https://raw.githubusercontent.com/Pakniat/PySimplex/master/images/sim1.png)

## Getting Started

Let's start simple example of PySimplex in 3 dimension:

```python
    def insert_childs(self, list_childs):
        if len(list_childs) > 0:
            if not (self.has_child(list_childs[self.HEAD])):
                self.set_childs(list_childs[self.HEAD])
                return
            if self.has_child(list_childs[self.HEAD]):
                list_recursion = []
                for i in range(len(list_childs)):
                    if i <> 0:
                        list_recursion.append(list_childs[i])
                self.get_child(list_childs[self.HEAD]).insert_childs(list_recursion)
        return
```
You can create complex with TkInter package(Graphical User Interface) as follow,

![alt text](https://raw.githubusercontent.com/Pakniat/PySimplex/master/images/te1.jpg)

You can import *.obj file with use read_simplex_obj class

![alt Text](https://github.com/Pakniat/PySimplex/tree/master/images/record.gif)

```
in the first textbox enter number of vertex of complex

either can you use the second textbox enter flag complex, or you can use the
third textbox for creation of your complexs

in the forth textbox you can delete face from complex
```
![alt text](https://raw.githubusercontent.com/Pakniat/PySimplex/master/images/te2.jpg)
## Requirements

* **Python >= 2.7**

PySimplex has no external dependencies outside of the Python standard library.

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore -->
| [<img src="https://avatars3.githubusercontent.com/u/41550630?s=400&v=4" width="100px;"/><br /><sub><b>Hossein Teimoori Faal</b></sub>](https://github.com/loveprog323)<br />
<!-- ALL-CONTRIBUTORS-LIST:END -->

## References

* [The Simplex Tree](https://hal.inria.fr/hal-01108441) - : An Efficient Data Structure for General Simplicial Complexes 
* [Combinatorial Topology](http://www.cis.upenn.edu/~cis610/convex67.pdf) - A Introduction

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

