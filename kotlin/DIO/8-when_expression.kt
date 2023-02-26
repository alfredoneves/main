package me.dio.when_expression.kt 

fun when_assign(obj: Any): Any {	// receives Any value and returns Any value
    val result = when(obj) {	// storages the result of the when
        1 -> "one"
        "Hello" -> "greeting"
        is Long -> false
        else -> "other"
    }
    return result	// returns Any result
}

fun main(){
    class My_class
    val my_class = My_class()
    
    println(when_assign(1))
    println(when_assign("Hello"))
    println(when_assign(0L))	// capital L
    println(when_assign(my_class))
}
