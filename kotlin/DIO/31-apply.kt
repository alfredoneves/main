package me.dio.apply.kt 

data class Person(var name: String, var age: Int, var desc: String) {
    constructor(): this("", 0, "")	// when the instance is create this values are the default
}

fun main() {
    val jake: Person = Person()
    val string_jake = jake.apply {	// can be used to modify the object
        name = "Jake"
        age = 20
        desc = "studdent"
    }.toString()
    
    println(string_jake)
}
