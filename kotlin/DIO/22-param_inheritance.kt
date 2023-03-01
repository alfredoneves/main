package me.dio.param_inheritance.kt 

open class Tiger(origin: String) {	// creates an open class (can be inherited) with a parameter
    fun roar(): String = "grhhh!"
}

class Siberian_tiger(): Tiger("Siberia")	// creates another class with the first open class

fun main() {
    val normal_tiger = Tiger("Africa")
    val siberian_tiger: Tiger = Siberian_tiger()
    
    println(normal_tiger.roar())
    println(siberian_tiger.roar())
}
