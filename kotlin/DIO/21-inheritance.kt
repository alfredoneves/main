package me.dio.inheritance.kt 

// the pattern in kotlin is that all classes and functions are final (closed)
open class Dog() {	// creates an open class (can be inherited)
    open fun say_hello(): String = "woof woof"	// creates an open function
}

class Yorkshire: Dog() {	// creates the class Yorkishire that inherits the class Dog
    override fun say_hello(): String = "wif wif"	// overrides the function
}

fun main() {
    val my_pet0: Dog = Dog()
    val my_pet: Dog = Yorkshire()	// instances object Yorkshire inheriting Dog
    
    println(my_pet0.say_hello())
    println(my_pet.say_hello())
}
