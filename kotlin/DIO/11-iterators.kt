package me.dio.iterators.kt

class Animal(val name: String)
class Zoo(val animals: List<Animal>){	// the class Zoo with a list of instances of the class "Animal"
	operator fun iterator(): Iterator<Animal> {	// creates the function to iterate with the class Animal
        return animals.iterator()	// returns the elements of the list
    }											
}

fun main(){
    val animals = listOf(Animal("zebra"), Animal("lion"), Animal("monkey"))	// creates a list of instances 
    val zoo = Zoo(animals)	// instances the class Zoo with a list of animals
    
    for (animal in zoo) {	// iterates 
        println("Watch out, it's a ${animal.name}")
    }
}
