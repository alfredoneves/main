package me.dio.also.kt 

data class Person(var name: String, var age: Int, var desc: String) {
    constructor(): this("", 0, "")	// when the instance is create this values are the default
}

fun write_creation_log(p: Person) {
    println("person ${p.name} was created !")
}

fun main() {
    val jake: Person = Person("jake", 20, "studdent").also {
        write_creation_log(it)	// executes the function with the instance created "it"
    }
}
