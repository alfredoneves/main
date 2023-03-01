package me.dio.sealed_classes.kt

sealed class Mammal(val name: String)	// sealed class can be inherited inside the same package
class Cat(val cat_name: String): Mammal(cat_name)	// read : as "is" -> cat is mammal
class Human(val human_name: String, val job: String): Mammal(human_name)

fun greet_mammal(mammal: Mammal): String {
    when (mammal) {
        is Human -> return "hello ${mammal.name} , you work as a ${mammal.job}"
        is Cat -> return "Meow ${mammal.name}"
    }
}

fun main() {
    val cat: Mammal = Cat("snowball")
    val human: Mammal = Human("Alfredo", "student")
    
    println(greet_mammal(cat))
    println(greet_mammal(human))
}
