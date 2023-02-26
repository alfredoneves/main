package me.dio.functions

fun print_message(message: String): Unit {	// defines a function that will receive a String and storage in the 
	println(message)			// variable "message" and will return a Unit (anything)
}

fun print_message_with_prefix(message: String, prefix: String = "Info:") {
	println("$prefix $message")
}

fun sum(a: Int, b: Int): Int {	// function with return specified as Int
	return a + b
}

fun multiply(x: Int, y: Int) = x * y		// inline function

fun main(){
    print_message("hello alfredo!")
    print_message_with_prefix("you need to swim")
    print_message_with_prefix(prefix = "[warning]", message = "You are in danger")
    println(sum(10, 20))
    println(multiply(10, 20))
}
