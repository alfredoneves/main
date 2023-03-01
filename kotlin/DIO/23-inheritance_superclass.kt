package me.dio.inheritance_superclass.kt

open class Lion(val name: String, val origin: String) {
    fun say_hello(): String = "$name from $origin says GRAAOH!"
}

class African_lion(name: String): Lion(name = name, origin = "Madagascar")	// passes arguments to the supclass

fun main() {
    val lion: Lion = African_lion("Alex the lion")
    println(lion.say_hello())
}
