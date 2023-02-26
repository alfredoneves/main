package me.dio.when_statement.kt

fun cases(obj: Any) {	// starts function receiving any object
    when(obj){	// starts when with the object received
        1 -> println("one")	// tests for condition and executes what is after ->
        "Hello" -> println("greeting")
        is Long -> println("long")
        !is String -> println("isn't string")
        else -> println("unkown")
    }
}

fun main(){
    class My_class
    val my_class = My_class()
    
    cases(1)
    cases("Hello")
    cases(1L)
    cases(my_class)
    cases("hello")
}
